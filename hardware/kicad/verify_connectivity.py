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
for net in root.findall('./nets/net'):
    name = net.attrib['name'].removeprefix('/')
    for node in net.findall('node'):
        key = (node.attrib['ref'], node.attrib['pin'])
        assert key not in actual, f'Duplicate node {key}'
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
expected.update({('X1', '1'): 'VSYS', ('X1', '2'): 'GND', ('X1', '3'): 'VBUS_USB'})
assert actual == expected, f'Connectivity mismatch: {[(k, expected.get(k), actual.get(k)) for k in expected.keys() | actual.keys() if expected.get(k) != actual.get(k)]}'
components = {comp.attrib['ref']: comp for comp in root.findall('./components/comp')}
assert set(components) == {f'J{i}' for i in range(1, 16)} | {'X1'}
assert all(not comp.findtext('footprint') for comp in components.values()), 'Unexpected footprint assignment'
assert len(root.findall('./nets/net')) == 33
print('PASS: 40 socket contacts, 12 module interfaces, 16 expansion pins and 3 logical power points.')
print('PASS: all 95 endpoints match; 30 connected nets and 3 intentional NC nets; no assigned footprints.')
