#!/usr/bin/env python3
"""Prepare held assembly tables from fresh Konnect-native exported artifacts.

Does not change CAD, export CAD, contact a supplier or grant release. Run only
after fresh saved-board ERC/DRC/parity and native XML/position exports. Output
is a NEW directory so previous evidence is not silently overwritten.
"""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import re
import shutil
import sys
import xml.etree.ElementTree as ET

HW = Path(__file__).resolve().parents[1]
KD = HW / 'kicad'
sys.path.insert(0, str(KD))
import verify_board


def natural(ref):
    return [int(t) if t.isdigit() else t for t in re.split(r'(\d+)', ref)]


def table(path, rows):
    assert rows, f'Empty table: {path}'
    with path.open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def design_inputs():
    paths = [KD / p for p in ('make_music.kicad_sch', 'battery_power.kicad_sch',
        'make_music.kicad_pcb', 'make_music.kicad_pro', 'make_music.kicad_dru',
        'MakeMusic.kicad_sym', 'sym-lib-table', 'fp-lib-table')]
    paths += list(KD.glob('*.pretty/*.kicad_mod'))
    paths += list((HW / 'libraries').glob('*.pretty/*.kicad_mod'))
    return sorted(paths)


def design_hashes():
    return {str(p.relative_to(HW)): digest(p) for p in design_inputs()}


def response(path):
    raw = json.loads(path.read_text())
    if 'content' not in raw:
        return raw
    assert not raw.get('isError'), raw
    return json.loads(''.join(p['text'] for p in raw['content'] if p['type'] == 'text'))


def verify_placements(positions, purchased_refs, live_components):
    """Bind every native (0,0), x-right/y-up placement to verified IPC data."""
    refs = [p['Ref'] for p in positions]
    assert len(refs) == len(set(refs)), 'Duplicate placement reference'
    assert set(refs) == set(purchased_refs), 'BOM/placement coverage disagreement'
    live = {p['reference']: p for p in live_components}
    assert len(live) == len(live_components), 'Duplicate live reference'
    assert set(purchased_refs) <= set(live), 'Purchased part missing from live inventory'

    def number(value, label):
        try:
            result = float(value)
        except (TypeError, ValueError):
            raise AssertionError('Invalid placement number: ' + label) from None
        assert math.isfinite(result), 'Nonfinite placement number: ' + label
        return result

    # Native exports print six decimal places; allow one nanometre/one
    # microdegree for rounding, not a board or rotation adjustment.
    tolerance = 1e-6
    for p in positions:
        ref = p['Ref']
        fp = live[ref]
        assert fp['layer'] in ('F.Cu', 'B.Cu'), 'Invalid live side: ' + ref
        side = 'top' if fp['layer'] == 'F.Cu' else 'bottom'
        assert p['Side'].lower() == side, 'Live placement side differs: ' + ref
        assert p['Val'] == fp['value'], 'Live placement value differs: ' + ref
        assert p['Package'] == fp['footprint'].split(':')[-1], 'Live placement footprint differs: ' + ref
        x, y = number(p['PosX'], ref + ' X'), number(p['PosY'], ref + ' Y')
        native_x, native_y = number(fp['x'], ref + ' live X'), number(fp['y'], ref + ' live Y')
        assert abs(x - native_x) <= tolerance, 'Live placement X differs: ' + ref
        assert abs(y + native_y) <= tolerance, 'Live placement Y differs: ' + ref
        angle = number(p['Rot'], ref + ' rotation')
        native_angle = number(fp['rotation'], ref + ' live rotation')
        difference = (angle - native_angle + 180) % 360 - 180
        assert abs(difference) <= tolerance, 'Live placement rotation differs: ' + ref


def prepare(native_dir, netlist, erc_path, drc_path, destination, snapshot, electrical_evidence):
    assert not destination.exists(), 'Output must be a fresh directory'
    before = json.loads(snapshot.read_text())
    assert before['design_sha256'] == design_hashes(), 'Native sources changed since export checkpoint'
    erc, drc = response(erc_path), response(drc_path)
    # Exact source-bound live pad/identity checks adjudicate only the four
    # documented connector metadata warnings. No DRC category is suppressed.
    _, metadata_warnings = verify_board.verify(electrical_evidence)
    for source, name in ((netlist, 'netlist.xml'), (erc_path, 'erc-mcp.json'), (drc_path, 'drc-mcp.json')):
        assert digest(source) == digest(electrical_evidence / name), 'Electrical evidence differs: ' + name
    assert response(electrical_evidence / 'source-checkpoint.json')['design_sha256'] == before['design_sha256']
    assert erc['total'] == 0, erc
    assert drc['total_violations'] == metadata_warnings and not drc['categories_not_reported'], drc
    assert drc['schematic_parity'] == metadata_warnings and drc['unconnected_items'] == 0, drc
    assert drc['design_rule_violations'] == 0, drc
    assert drc['source'] == 'saved_file' and drc['live_board_synced'], drc
    assert drc['zones_refilled'] and drc['zone_refill_source'] == 'ipc', drc
    assert not drc['truncated'] and drc['severity_filter'] == 'info', drc
    xml = ET.parse(netlist).getroot()
    parts = []
    for comp in xml.findall('components/comp'):
        ref = comp.attrib['ref']
        if ref == 'TP1':
            continue  # Bare copper, not a purchased part.
        fields = {p.attrib['name']: p.text or '' for p in comp.findall('fields/field')}
        mpn = fields.get('MPN', '')
        assert mpn, (ref, 'Missing native MPN; no hidden substitution is permitted')
        if ref.startswith('C'):
            maker = 'KEMET' if int(ref[1:]) <= 12 else 'TDK'
        else:
            maker = {'J': 'Harwin', 'H': 'JST', 'S': 'NKK', 'R': 'Yageo',
                     'F': 'SCHURTER', 'U': 'Texas Instruments',
                     'D': 'Vishay' if ref == 'D2' else 'Littelfuse'}[ref[0]]
        if ref in ('J1', 'J2'):
            assert mpn == 'SSQ-120-01-G-S'
            maker = 'Samtec'
        parts.append({'Reference': ref, 'Quantity': 1, 'Manufacturer': maker,
            'MPN': mpn, 'Value': comp.findtext('value'),
            'Footprint': comp.findtext('footprint'),
            'Assembly': 'THT' if ref[0] in ('J', 'H', 'S') else 'SMT',
            'Side': 'Bottom' if ref == 'H1' else 'Top',
            'Datasheet': comp.findtext('datasheet', '')})
    parts.sort(key=lambda p: natural(p['Reference']))
    assert len(parts) == 47, 'Current revision expects 47 purchased parts'
    by_ref = {p['Reference']: p for p in parts}
    with (native_dir / 'positions.csv').open(newline='') as stream:
        positions = list(csv.DictReader(stream))
    live_components = response(electrical_evidence / 'live-board.json')['inventory']['components']
    verify_placements(positions, by_ref, live_components)
    smt, tht = [], []
    for p in positions:
        part = by_ref[p['Ref']]
        assert p['Side'].lower() == part['Side'].lower(), p
        assert p['Val'] == part['Value'], p
        assert p['Package'] == part['Footprint'].split(':')[-1], p
        row = {'Designator': p['Ref'], 'X': p['PosX'], 'Y': p['PosY'],
               'Rotation': p['Rot'], 'Side': p['Side']}
        (smt if part['Assembly'] == 'SMT' else tht).append(row)
    assert len(smt) == 30 and len(tht) == 17
    assert all(p['Side'] == 'top' for p in smt)
    pos = {p['Ref']: p for p in positions}
    assert (float(pos['J3']['PosX']), float(pos['J3']['PosY'])) == (87.46, -98)
    assert (float(pos['J4']['PosX']), float(pos['J4']['PosY'])) == (121.46, -98)
    assert (float(pos['H1']['PosX']), float(pos['H1']['PosY'])) == (289, -40)
    # All geometry uses the served native export origin, NOT the old held
    # package's auxiliary origin. No Gerber/drill coordinates are rewritten.
    edge = (native_dir / 'gerbers/make_music-Edge_Cuts.gm1').read_text()
    for point in ('X20000000Y-20000000', 'X350000000Y-20000000',
                  'X20000000Y-140000000', 'X350000000Y-140000000'):
        assert point in edge, 'Unexpected outline or Gerber origin'
    drill = (native_dir / 'gerbers/make_music-NPTH.drl').read_text()
    assert 'METRIC' in drill and 'X26.0Y-26.0' in drill, 'Drill/placement origin disagreement'
    shutil.copytree(native_dir, destination)
    table(destination / 'carrier-bom.csv', parts)
    table(destination / 'pcbway-centroid-smt.csv', smt)
    table(destination / 'manual-tht-positions.csv', tht)
    grouped = {}
    for p in parts:
        key = (p['Manufacturer'], p['MPN'], p['Footprint'], p['Assembly'], p['Side'])
        if key not in grouped:
            grouped[key] = {'Reference Designator': p['Reference'], 'Quantity Per Board': 1,
                'Quantity For Five': 5, 'Manufacturer': p['Manufacturer'],
                'Manufacturer Part Number': p['MPN'], 'Description': p['Value'],
                'Package/Footprint': p['Footprint'], 'Type': p['Assembly'], 'Side': p['Side']}
        else:
            grouped[key]['Reference Designator'] += ',' + p['Reference']
            grouped[key]['Quantity Per Board'] += 1
            grouped[key]['Quantity For Five'] += 5
    table(destination / 'pcbway-bom-five.csv', list(grouped.values()))
    (destination / 'positions.csv').rename(destination / 'carrier-positions.csv')
    (destination / 'bom.csv').unlink()  # Generic export replaced by exact BOM.
    for source, name in [(HW / 'assembly/instrument-parts.csv', 'instrument-parts.csv'),
                         (HW / 'assembly/PCBWAY_HANDOFF.md', 'PCBWAY_HANDOFF.md'),
                         (HW / 'manufacturing/REVIEW_PACKAGE_README.md', 'README.md')]:
        shutil.copyfile(source, destination / name)
    (destination / 'validation-summary.json').write_text(json.dumps({
        'status': 'REVIEW ONLY - DO NOT ORDER', 'kicad_version': '10.0.6',
        'export_transport': 'Konnect MCP; native saved-file evidence',
        'erc_violations': 0, 'drc_violations': drc['total_violations'], 'unconnected_items': 0,
        'copper_layout_drc_violations': 0, 'reviewed_metadata_warnings': metadata_warnings,
        'schematic_parity_issues': drc['schematic_parity'], 'purchased_carrier_parts': len(parts),
        'smt_centroid_parts': len(smt), 'manual_tht_parts': len(tht),
        'assembled_instruments_requested': 5, 'optional_additional_bare_carriers': 1,
        'machine_origin': 'native (0,0); x right/y up; board (20,-20)..(350,-140) mm',
        'physical_fit_verified': False, 'bench_validation_complete': False,
        'supplier_acceptance_complete': False, 'fabrication_release': False
    }, indent=2) + '\n')
    inputs = design_inputs()
    inputs += [HW / p for p in ('assembly/instrument-parts.csv',
        'assembly/MODULE_HARNESSES.md', 'assembly/FIT_CHECKLIST.md',
        'assembly/PCBWAY_HANDOFF.md', 'manufacturing/prepare_pcbway_review.py',
        'manufacturing/REVIEW_PACKAGE_README.md', 'kicad/verify_board.py')]
    inputs += [netlist, erc_path, drc_path]
    evidence = destination / 'verification'
    evidence.mkdir()
    shutil.copytree(electrical_evidence, evidence / 'electrical-integration')
    for source, name in ((netlist, 'netlist.xml'), (erc_path, 'erc-mcp.json'), (drc_path, 'drc-mcp.json')):
        shutil.copyfile(source, evidence / name)
    shutil.copyfile(snapshot, evidence / 'source-checkpoint.json')
    for p in destination.rglob('*'):
        if p.is_file():
            assert p.stat().st_size, f'Empty output: {p}'
    outputs = {str(p.relative_to(destination)): digest(p) for p in sorted(destination.rglob('*')) if p.is_file()}
    assert before['design_sha256'] == design_hashes(), 'Native sources changed during packaging'
    # External temporary evidence is copied into verification/; its hashes
    # are recorded there. Only durable project inputs enter input_sha256.
    (destination / 'manifest.json').write_text(json.dumps({
        'status': 'REVIEW ONLY - DO NOT ORDER', 'generator': 'Konnect MCP / KiCad 10.0.6',
        'input_sha256': {str(p.relative_to(HW)): digest(p) for p in inputs if p.is_relative_to(HW)},
        'output_sha256': outputs
    }, indent=2) + '\n')
    print(f'Prepared {len(parts)} carrier parts, {len(smt)} SMT, {len(tht)} THT; {len(outputs)} held files.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('native_dir', 'netlist', 'erc', 'drc', 'output_dir'):
        parser.add_argument(name, type=Path)
    parser.add_argument('--source-snapshot', required=True, type=Path,
        help='Hash checkpoint taken after saved/refilled checks and before native exports')
    parser.add_argument('--electrical-evidence', required=True, type=Path,
        help='Source-bound XML/live IPC/ERC/DRC evidence checked by verify_board.py')
    args = parser.parse_args()
    prepare(args.native_dir, args.netlist, args.erc, args.drc, args.output_dir,
            args.source_snapshot, args.electrical_evidence)
