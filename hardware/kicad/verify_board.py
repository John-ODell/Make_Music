#!/usr/bin/env python3
"""Verify exported XML against Konnect live readback, without pcbnew/SWIG.

All evidence must be regenerated after CAD changes. This verifies electrical
integration only; physical fit and manufacturing release remain pending.
"""
import argparse
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

HW = Path(__file__).resolve().parents[1]
BOARD = HW / 'kicad/make_music.kicad_pcb'
METADATA = {
    ('C17', "Missing symbol field 'Header' in footprint"): '803cbb59-146e-48b1-aeda-4595b89d458a',
    ('C18', "Missing symbol field 'Header' in footprint"): '17f86661-a1a8-44cc-a63e-d7c0643710a5',
    ('J1', "Missing symbol field 'MPN' in footprint"): '4402266d-929c-484b-8b94-d96b7d71e403',
    ('J2', "Missing symbol field 'MPN' in footprint"): 'c78dc07c-3fca-42d6-80f0-9c8ed7f1fb4d',
}


def response(path):
    raw = json.loads(path.read_text())
    if 'content' not in raw:
        return raw
    assert not raw.get('isError'), 'MCP error'
    return json.loads(''.join(c['text'] for c in raw['content'] if c['type'] == 'text'))


def verify(evidence):
    source = response(evidence / 'source-checkpoint.json')['design_sha256']
    assert source and 'kicad/make_music.kicad_pcb' in source
    for name, expected_hash in source.items():
        assert hashlib.sha256((HW / name).read_bytes()).hexdigest() == expected_hash, 'Stale source: ' + name
    live = response(evidence / 'live-board.json')
    info = live['board_info']
    assert info['source'] == 'ipc' and Path(info['file']).resolve() == BOARD.resolve()
    assert info['copper_layer_count'] == 2
    sync = live['identity_sync']
    assert sync['status'] == 'noop' and not sync['changes'] and not sync['diagnostics']
    assert not sync['unassigned_footprints']
    assert sync['coverage']['transport'] == 'live_kicad_ipc'
    assert sync['coverage']['hierarchy_files'] == 2
    xml = ET.parse(evidence / 'netlist.xml').getroot()
    components = {c.attrib['ref']: c for c in xml.findall('./components/comp')}
    assert len(components) == 48
    inventory = live['inventory']['components']
    by_ref = {c['reference']: c for c in inventory}
    assert len(by_ref) == len(inventory) == 65
    assert set(by_ref) - set(components) == {f'MH{i}' for i in range(1, 18)}
    assert set(live['pads']) == set(components)
    expected, actual = {}, {}
    for net in xml.findall('./nets/net'):
        for node in net.findall('node'):
            key = (node.attrib['ref'], node.attrib['pin'])
            assert key not in expected
            expected[key] = net.attrib['name']
    for ref, comp in components.items():
        fp = by_ref[ref]
        assert fp['value'] == comp.findtext('value'), 'Value differs: ' + ref
        assert fp['footprint'] == comp.findtext('footprint'), 'Footprint differs: ' + ref
        pads = live['pads'][ref]
        assert pads['source'] == 'ipc' and pads['reference'] == ref
        assert pads['pad_count'] == len(pads['pads'])
        for pad in pads['pads']:
            key = (ref, pad['number'])
            assert key not in actual and pad['net'] is not None
            actual[key] = pad['net']
    assert actual == expected and len(actual) == 166, 'PCB/XML pad-net mismatch'
    assert live['traces']['count'] == len(live['traces']['traces']) > 0
    erc = response(evidence / 'erc-mcp.json')
    assert erc['total'] == 0 and not erc['violations']
    drc = response(evidence / 'drc-mcp.json')
    assert not drc['categories_not_reported'] and not drc['truncated']
    assert drc['severity_filter'] == 'info'
    assert drc['source'] == 'saved_file' and drc['live_board_synced']
    assert drc['zones_refilled'] and drc['zone_refill_source'] == 'ipc'
    assert drc['design_rule_violations'] == drc['unconnected_items'] == drc['errors'] == 0
    assert drc['schematic_parity'] == drc['total_violations'] == len(drc['violations'])
    seen = set()
    for item in drc['violations']:
        assert item['rule'] == 'footprint_symbol_field_mismatch' and item['severity'] == 'warning'
        assert len(item['items']) == 1
        fp = item['items'][0]
        ref = fp['description'].removeprefix('Footprint ')
        key = (ref, item['description'])
        assert key in METADATA and key not in seen and fp['uuid'] == METADATA[key], 'Unreviewed DRC finding'
        seen.add(key)
    return len(actual), len(drc['violations'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('evidence', type=Path)
    args = parser.parse_args()
    endpoints, metadata = verify(args.evidence)
    print(f'PASS electrical integration: {endpoints} live pad nets; 48 values/footprints; identity sync noop.')
    print(f'ERC 0; copper/layout DRC 0; unconnected 0; {metadata} reviewed metadata warnings retained.')
    print('Physical fit, bench qualification and manufacturing release remain pending.')
