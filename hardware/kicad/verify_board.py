#!/usr/bin/env python3
"""Verify PCB/schematic identity and every pad net from a fresh KiCad XML netlist.

Run with KiCad's pcbnew-enabled Python. This supplements native ERC/DRC;
physical fit, component ratings and built hardware are separate validations.
"""
import argparse
import re
import sys
from pathlib import Path
import xml.etree.ElementTree as ET
try:
    import pcbnew as pcb
except ImportError:
    sys.exit('Use the Python shipped with KiCad; pcbnew is required.')

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('netlist', type=Path)
parser.add_argument('--board', type=Path, default=Path(__file__).with_name('make_music.kicad_pcb'))
args = parser.parse_args()
xml = ET.parse(args.netlist).getroot()
board = pcb.LoadBoard(str(args.board))
components = {c.attrib['ref']: c for c in xml.findall('components/comp')}
footprints = {}
errors = []
for fp in board.GetFootprints():
    ref = fp.GetReference()
    if ref in footprints:
        errors.append('Duplicate footprint ' + ref)
    footprints[ref] = fp
    if fp.GetAttributes() & pcb.FP_BOARD_ONLY:
        if ref in components:
            errors.append('Schematic part incorrectly marked board-only: ' + ref)
    elif ref not in components:
        errors.append('PCB-only electrical part: ' + ref)
expected = {}
for net in xml.findall('nets/net'):
    for node in net.findall('node'):
        key = (node.attrib['ref'], node.attrib['pin'])
        if key in expected:
            errors.append('Repeated schematic endpoint: ' + str(key))
        expected[key] = net.attrib['name']
actual = {}
for ref, comp in components.items():
    fp = footprints.get(ref)
    if fp is None:
        errors.append('Missing PCB part: ' + ref)
        continue
    if fp.GetFPIDAsString() != comp.findtext('footprint', ''):
        errors.append('Footprint assignment differs: ' + ref)
    if fp.GetValue() != comp.findtext('value', ''):
        errors.append('Value differs: ' + ref)
    path = fp.GetPath().AsString().rstrip('/').split('/')[-1]
    if path != comp.findtext('tstamps'):
        errors.append('Schematic UUID differs: ' + ref)
    for pad in fp.Pads():
        key = (ref, pad.GetNumber())
        # Repeated numbered pads are legal (e.g. power packages), but must agree.
        name = pad.GetNetname()
        if key in actual and actual[key] != name:
            errors.append('Split net across duplicate-number pads: ' + str(key))
        actual[key] = name
for key in sorted(set(expected) | set(actual)):
    if actual.get(key) != expected.get(key):
        errors.append(f'{key}: PCB={actual.get(key)!r}, schematic={expected.get(key)!r}')
if board.GetCopperLayerCount() != 2:
    errors.append('Expected two copper layers')
tracks = [t for t in board.GetTracks() if not isinstance(t, pcb.PCB_VIA)]
vias = [t for t in board.GetTracks() if isinstance(t, pcb.PCB_VIA)]
if not tracks:
    errors.append('Board has no routed copper tracks')
if not any(not z.GetIsRuleArea() for z in board.Zones()):
    errors.append('Board has no copper zones')
if errors:
    print('\n'.join('FAIL: ' + e for e in errors))
    sys.exit(1)
print(f'PASS: {len(components)} schematic parts and {len(actual)} pad endpoints agree by reference, footprint, value, UUID and net.')
print(f'PASS: two-layer board; {len(tracks)} tracks, {len(vias)} vias, {len(list(board.Zones()))} copper zones/rule areas.')
print('Native ERC/DRC and physical component/assembly validation remain required.')
