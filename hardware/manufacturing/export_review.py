#!/usr/bin/env python3
"""Check the native project and regenerate held review outputs, never a release.

Requires KiCad 10 CLI and ordinary Python 3. Diagnostics go to a temporary
directory. Existing managed output filenames are regenerated after checks pass.
"""
import csv
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
HW = HERE.parent
KD = HW / 'kicad'
OUT = HERE / 'REVIEW_ONLY_DO_NOT_ORDER'
CLI = os.environ.get('MAKE_MUSIC_KICAD_CLI') or shutil.which('kicad-cli')
if not CLI:
    candidate = Path('/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli')
    CLI = str(candidate) if candidate.exists() else None
if not CLI:
    sys.exit('KiCad 10 kicad-cli is required.')
SCH = KD / 'make_music.kicad_sch'
PCB = KD / 'make_music.kicad_pcb'


def cli(*args):
    result = subprocess.run([CLI, *map(str, args)], check=True, capture_output=True, text=True)
    return result.stdout.strip()


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def natural(ref):
    return [int(t) if t.isdigit() else t for t in re.split(r'(\d+)', ref)]


with tempfile.TemporaryDirectory(prefix='make-music-review-') as temp:
    temp = Path(temp)
    net = temp / 'netlist.xml'
    print(cli('sch', 'erc', '--severity-all', '--exit-code-violations', '--format', 'json', '-o', temp / 'erc.json', SCH))
    cli('sch', 'export', 'netlist', '--format', 'kicadxml', '-o', net, SCH)
    subprocess.run([sys.executable, str(KD / 'verify_connectivity.py'), str(net)], check=True)
    print(cli('pcb', 'drc', '--schematic-parity', '--severity-all', '--exit-code-violations', '--format', 'json', '-o', temp / 'drc.json', PCB))
    erc = json.loads((temp / 'erc.json').read_text())
    drc = json.loads((temp / 'drc.json').read_text())
    assert not any(s.get('violations') for s in erc.get('sheets', [])), 'ERC violations must be zero'
    assert not any(drc.get(k) for k in ['violations', 'unconnected_items', 'schematic_parity']), 'DRC must be zero'
    parts = []
    for comp in ET.parse(net).getroot().findall('components/comp'):
        ref = comp.attrib['ref']
        if ref == 'TP1':
            continue  # Bare PCB copper, no purchased component.
        fields = {f.attrib['name']: f.text or '' for f in comp.findall('fields/field')}
        mpn = fields.get('MPN', '')
        if ref in ['J1', 'J2']:
            mpn = 'SSQ-120-01-G-S'
        assert mpn, (ref, 'missing MPN')
        if ref.startswith('C'):
            maker = 'KEMET' if int(ref[1:]) <= 12 else 'TDK'
        else:
            maker = {'J': 'Harwin', 'H': 'JST', 'S': 'NKK', 'R': 'Yageo', 'F': 'SCHURTER',
                     'U': 'Texas Instruments', 'D': 'Vishay' if ref == 'D2' else 'Littelfuse'}[ref[0]]
        if ref in ['J1', 'J2']:
            maker = 'Samtec'
        datasheet = comp.findtext('datasheet', '')
        if ref in ['J1', 'J2']:
            datasheet = 'https://suddendocs.samtec.com/prints/ssq-1xx-xx-xxx-x-xx-xxx-xx-x-mkt.pdf'
        parts.append({'Reference': ref, 'Quantity': 1, 'Manufacturer': maker, 'MPN': mpn,
                      'Value': comp.findtext('value'), 'Footprint': comp.findtext('footprint'),
                      'Assembly': 'THT' if ref[0] in ['J', 'H', 'S'] else 'SMT',
                      'Side': 'Bottom' if ref == 'H1' else 'Top',
                      'Datasheet': datasheet})
    parts.sort(key=lambda row: natural(row['Reference']))
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / 'carrier-bom.csv').open('w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=list(parts[0]))
        writer.writeheader()
        writer.writerows(parts)
    shutil.copyfile(HW / 'assembly/instrument-parts.csv', OUT / 'instrument-parts.csv')
    cli('pcb', 'export', 'gerbers', '--layers', 'F.Cu,B.Cu,F.Paste,F.Mask,B.Mask,F.Silkscreen,B.Silkscreen,Edge.Cuts',
        '--use-drill-file-origin', '--subtract-soldermask', '--output', OUT / 'gerbers', PCB)
    cli('pcb', 'export', 'drill', '--format', 'excellon', '--drill-origin', 'plot', '--excellon-separate-th',
        '--excellon-units', 'mm', '--excellon-zeros-format', 'decimal', '--output', OUT / 'gerbers', PCB)
    cli('pcb', 'export', 'pos', '--side', 'both', '--format', 'csv', '--units', 'mm', '--use-drill-file-origin',
        '--output', OUT / 'carrier-positions.csv', PCB)
    for side, layers in [('top', 'F.Fab,F.Silkscreen,Dwgs.User,Edge.Cuts'), ('bottom', 'B.Fab,B.Silkscreen,Dwgs.User,Edge.Cuts')]:
        args = ['pcb', 'export', 'pdf', '--mode-single', '--black-and-white', '--layers', layers,
                '--sketch-pads-on-fab-layers', '--output', OUT / ('assembly-' + side + '-review.pdf'), PCB]
        if side == 'bottom':
            args.insert(3, '--mirror')
        cli(*args)
    cli('pcb', 'export', 'pdf', '--mode-multipage', '--black-and-white', '--layers', 'F.Cu,B.Cu',
        '--common-layers', 'Edge.Cuts', '--output', OUT / 'copper-review.pdf', PCB)
    cli('sch', 'export', 'pdf', '-o', OUT / 'schematic-review.pdf', SCH)
    (OUT / 'validation-summary.json').write_text(json.dumps({
        'status': 'REVIEW ONLY - DO NOT ORDER', 'kicad_version': cli('version'),
        'erc_violations': 0, 'drc_violations': 0, 'unconnected_items': 0, 'schematic_parity_issues': 0,
        'purchased_carrier_parts': len(parts), 'physical_fit_verified': False,
        'bench_validation_complete': False, 'fabrication_release': False
    }, indent=2) + '\n')
    inputs = [SCH, KD / 'battery_power.kicad_sch', PCB, KD / 'make_music.kicad_pro', KD / 'make_music.kicad_dru',
              KD / 'MakeMusic.kicad_sym', KD / 'sym-lib-table', KD / 'fp-lib-table',
              HW / 'assembly/instrument-parts.csv', HW / 'assembly/MODULE_HARNESSES.md',
              HW / 'assembly/FIT_CHECKLIST.md', HERE / 'export_review.py']
    inputs += list(KD.glob('*.pretty/*.kicad_mod')) + list((HW / 'libraries').glob('*.pretty/*.kicad_mod'))
    outputs = {str(p.relative_to(OUT)): digest(p) for p in sorted(OUT.rglob('*')) if p.is_file() and p.name != 'manifest.json'}
    (OUT / 'manifest.json').write_text(json.dumps({
        'status': 'REVIEW ONLY - DO NOT ORDER', 'generator': cli('version'),
        'input_sha256': {str(p.relative_to(HW)): digest(p) for p in inputs}, 'output_sha256': outputs
    }, indent=2) + '\n')
    print('Held review outputs generated:', len(parts), 'purchased carrier parts;', len(outputs), 'files')
