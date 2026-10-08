#!/usr/bin/env python3
"""Check an exported KiCad XML netlist against the reviewed carrier contract."""
import argparse
import csv
import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('netlist', type=Path)
parser.add_argument('--kicad-footprint-dir', type=Path, help='Installed KiCad 10 footprint root; otherwise use KICAD10_FOOTPRINT_DIR or common install paths')
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
# Physical JST harness circuits; polarity is our carrier convention.
expected.update({
    ('H1', '1'): 'BAT_PROT_PLUS', ('H1', '2'): 'GND',
    ('S1', '2'): 'BAT_PROT_PLUS', ('S1', '3'): 'BAT_SW_PLUS', ('S1', '1'): 'NC',
    ('D1', '2'): 'BAT_SW_PLUS', ('D1', '1'): 'VSYS',
    ('TP1', '1'): 'VBUS_USB',
})
for ref, net in [('R1', 'GP13'), ('R2', 'GP12')]:
    expected[(ref, '1')] = '3V3_OUT'
    expected[(ref, '2')] = net
for n in range(1, 13):
    expected[(f'C{n}', '1')] = '3V3_OUT'
    expected[(f'C{n}', '2')] = 'GND'
# Preserve electrical polarity as well as endpoint numbers.
for key, role in {('D1', '1'): 'K', ('D1', '2'): 'A', ('S1', '2'): 'COM', ('S1', '3'): 'BAT_ON', ('S1', '1'): 'BAT_OFF'}.items():
    assert pin_functions[key] == f'{role}_{key[1]}', f'Incorrect power terminal role: {key} {pin_functions[key]}'
assert actual == expected, f'Connectivity mismatch: {[(k, expected.get(k), actual.get(k)) for k in expected.keys() | actual.keys() if expected.get(k) != actual.get(k)]}'
components = {comp.attrib['ref']: comp for comp in root.findall('./components/comp')}
assert set(components) == {f'J{i}' for i in range(1, 16)} | {'H1', 'S1', 'D1', 'TP1', 'R1', 'R2'} | {f'C{i}' for i in range(1, 13)}
socket_footprint = 'MakeMusic:Samtec_SSQ-120-01-G-S_1x20_P2.54mm'
footprints = {
    'J1': socket_footprint, 'J2': socket_footprint,
    **{f'J{i}': 'MakeMusicCarrier:Harwin_M20-9990346_1x3_P2.54mm' for i in range(3, 15)},
    'J15': 'MakeMusicCarrier:Harwin_M20-9991646_1x16_P2.54mm',
    'H1': 'Connector_JST:JST_PH_B2B-PH-K_1x02_P2.00mm_Vertical',
    'S1': 'MakeMusicCarrier:NKK_MN12SS1W03_TerminalPattern_Candidate',
    'D1': 'MakeMusicCarrier:Vishay_SS14_SMA_K1_A2',
    'TP1': '',
    'R1': 'Resistor_SMD:R_0603_1608Metric', 'R2': 'Resistor_SMD:R_0603_1608Metric',
    **{f'C{i}': 'MakeMusicCarrier:KEMET_C0603_1608_LevelB' for i in range(1, 13)},
}
mpns = {**{f'J{i}': 'M20-9990346' for i in range(3, 15)}, 'J15': 'M20-9991646',
        'H1': 'B2B-PH-K-S(LF)(SN)', 'R1': 'RC0603FR-0710KL', 'R2': 'RC0603FR-0710KL',
        **{f'C{i}': 'C0603C104K5RACTU' for i in range(1, 13)}}
base = Path(__file__).resolve().parent
install_candidates = [args.kicad_footprint_dir, os.environ.get('KICAD10_FOOTPRINT_DIR'),
                      '/Applications/KiCad/KiCad.app/Contents/SharedSupport/footprints',
                      '/usr/share/kicad/footprints']
installed = next((Path(p) for p in install_candidates if p and Path(p).is_dir()), None)
assert installed is not None, 'Set --kicad-footprint-dir or KICAD10_FOOTPRINT_DIR to the installed KiCad 10 footprint root'
library_paths = {'MakeMusic': base.parent / 'libraries' / 'MakeMusic.pretty',
                 'MakeMusicCarrier': base / 'MakeMusicCarrier.pretty',
                 'Connector_JST': installed / 'Connector_JST.pretty',
                 'Resistor_SMD': installed / 'Resistor_SMD.pretty'}
for ref, comp in components.items():
    expected_footprint = footprints[ref]
    assert (comp.findtext('footprint') or '') == expected_footprint, f'Unexpected footprint assignment on {ref}: {comp.findtext("footprint")}'
    if ref in mpns:
        assert comp.findtext('./fields/field[@name="MPN"]') == mpns[ref], f'Unexpected MPN on {ref}'
    if expected_footprint:
        library, name = expected_footprint.split(':', 1)
        footprint_path = library_paths[library] / (name + '.kicad_mod')
        assert footprint_path.is_file(), f'Assigned footprint missing: {footprint_path}'
        pads = re.findall(r'\(pad\s+"([^"]+)"', footprint_path.read_text())
        assert len(pads) == len(set(pads)), f'Duplicate footprint pad numbers: {footprint_path}'
        assert set(pads) == {pin for component, pin in expected if component == ref}, f'Footprint pads do not match {ref} contacts'
for ref in ['R1', 'R2']:
    assert components[ref].findtext('value') == '10k', f'Unexpected reset bias value on {ref}'
for n in range(1, 13):
    comp = components[f'C{n}']
    assert comp.findtext('value') == '100n', f'Unexpected bypass value on C{n}'
    assert comp.findtext('./fields/field[@name="Header"]') == f'J{n+2}', f'Incorrect header association on C{n}'
assert len(root.findall('./nets/net')) == 36
assert components['S1'].findtext('value') == 'MN12SS1W03'
assert components['D1'].findtext('value') == 'SS14-E3/61T'
print('PASS: 40 socket contacts, 12 cable interfaces, 16 expansion pins, 8 power/test contacts and 28 R/C contacts.')
print('PASS: all 128 endpoints match; 32 connected nets and 4 intentional NC nets.')
print('PASS: switch common2/ON3/OFF1, diode K1/A2, and VBUS/battery/VSYS/3V3 source separation.')
print('PASS: physical JST H1 polarity, GP13/12 reset pull-ups and twelve 3V3/GND bypass capacitors.')
print('PASS: exact assigned footprints, existing files and pad numbers; exact carrier-header/R/C/H1 MPNs. TP1 remains unset.')
