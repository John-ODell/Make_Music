#!/usr/bin/env python3
"""Check an exported KiCad XML netlist against the reviewed carrier contract."""
import argparse
import csv
import xml.etree.ElementTree as ET
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('netlist', type=Path)
args = parser.parse_args()
root = ET.parse(args.netlist).getroot()
actual = {}
pin_functions = {}
for net in root.findall('./nets/net'):
    name = net.attrib['name'].removeprefix('/')
    for node in net.findall('node'):
        key = (node.attrib['ref'], node.attrib['pin'])
        assert key not in actual, f'Duplicate node {key}'
        pin_functions[key] = node.attrib.get('pinfunction', '')
        actual[key] = 'NC' if node.attrib['pintype'].endswith('+no_connect') else name

expected = {}
with Path(__file__).with_name('pico-socket-map.csv').open() as stream:
    rows = list(csv.DictReader(stream))
assert len(rows) == 40
assert {int(row['pico_physical_pin']) for row in rows} == set(range(1, 41))
for row in rows:
    expected[(row['socket'], row['socket_pin'])] = row['carrier_net']

# Assignment follows octave_half_8_key.py: buzzer1 GP13, buzzer2 GP12.
for ref, gpio in zip(range(3, 15), [16, 17, 18, 19, 20, 21, 22, 26, 27, 28, 13, 12]):
    expected[(f'J{ref}', '1')] = f'GP{gpio}'
    expected[(f'J{ref}', '2')] = '3V3_OUT'
    expected[(f'J{ref}', '3')] = 'GND'
for pin, net in enumerate([f'GP{i}' for i in range(12)] + ['GP14', 'GP15', '3V3_OUT', 'GND'], 1):
    expected[('J15', str(pin))] = net
# Holder +/- identifiers are provisional logical terminals, not mechanical pad numbers.
expected.update({
    ('H1', '+'): 'BAT_PROT_PLUS', ('H1', '-'): 'GND',
    ('S1', '2'): 'BAT_PROT_PLUS', ('S1', '3'): 'BAT_SW_PLUS', ('S1', '1'): 'NC',
    ('D1', '2'): 'BAT_SW_PLUS', ('D1', '1'): 'VSYS',
    ('TP1', '1'): 'VBUS_USB',
})
# Preserve electrical polarity as well as endpoint numbers.
for key, role in {('D1', '1'): 'K', ('D1', '2'): 'A', ('S1', '2'): 'COM', ('S1', '3'): 'BAT_ON', ('S1', '1'): 'BAT_OFF'}.items():
    assert pin_functions[key] == f'{role}_{key[1]}', f'Incorrect power terminal role: {key} {pin_functions[key]}'
assert actual == expected, f'Connectivity mismatch: {[(k, expected.get(k), actual.get(k)) for k in expected.keys() | actual.keys() if expected.get(k) != actual.get(k)]}'
components = {comp.attrib['ref']: comp for comp in root.findall('./components/comp')}
assert set(components) == {f'J{i}' for i in range(1, 16)} | {'H1', 'S1', 'D1', 'TP1'}
socket_footprint = 'MakeMusic:Samtec_SSQ-120-01-G-S_1x20_P2.54mm'
for ref, comp in components.items():
    expected_footprint = socket_footprint if ref in {'J1', 'J2'} else ''
    assert (comp.findtext('footprint') or '') == expected_footprint, f'Unexpected footprint assignment on {ref}: {comp.findtext("footprint")}'
footprint_path = Path(__file__).resolve().parent.parent / 'libraries' / 'MakeMusic.pretty' / (socket_footprint.split(':', 1)[1] + '.kicad_mod')
assert footprint_path.is_file(), f'Assigned socket footprint missing: {footprint_path}'
assert len(root.findall('./nets/net')) == 36
assert components['S1'].findtext('value') == 'MN12SS1W03'
assert components['D1'].findtext('value') == 'SS14-E3/61T'
print('PASS: 40 socket contacts, 12 module interfaces, 16 expansion pins and 8 actual power/test contacts.')
print('PASS: all 100 endpoints match; 32 connected nets and 4 intentional NC nets.')
print('PASS: switch common2/ON3/OFF1, diode K1/A2, and VBUS/battery/VSYS/3V3 source separation.')
print('PASS: only J1/J2 carry the expected local SSQ candidate footprint; all other footprints unset.')
