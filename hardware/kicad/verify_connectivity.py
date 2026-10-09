#!/usr/bin/env python3
"""Check an exported KiCad XML netlist against the reviewed carrier contract."""
import argparse
import csv
import os
import xml.etree.ElementTree as ET
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('netlist', type=Path)
parser.add_argument('--kicad-footprint-dir', type=Path, help='Installed KiCad 10 footprint root; otherwise use KICAD10_FOOTPRINT_DIR or common install paths')
args = parser.parse_args()
root = ET.parse(args.netlist).getroot()
actual = {}
pin_functions = {}
pin_types = {}
connected_names = set()
for net in root.findall('./nets/net'):
    name = net.attrib['name'].rsplit('/', 1)[-1]
    if not name.startswith('unconnected-'):
        assert name not in connected_names, f'Disjoint hierarchical nets share a contract name: {name}'
        connected_names.add(name)
    for node in net.findall('node'):
        key = (node.attrib['ref'], node.attrib['pin'])
        assert key not in actual, f'Duplicate node {key}'
        pin_functions[key] = node.attrib.get('pinfunction', '')
        pin_types[key] = node.attrib['pintype'].split('+', 1)[0]
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
expected[('TP1', '1')] = 'VBUS_USB'
# Power PR #18 uses role references; preserve the existing buzzer/header parts.
power_ref_map = {**{f'R{i}': f'R{i+2}' for i in range(1, 7)},
                 **{f'C{i}': f'C{i+12}' for i in range(1, 5)}}
with (Path(__file__).resolve().parent.parent / 'power' / 'branch-endpoints.csv').open() as stream:
    power_rows = list(csv.DictReader(stream))
assert len(power_rows) == 41
assert len({(row['reference'], row['pin']) for row in power_rows}) == 41
for row in power_rows:
    ref = power_ref_map.get(row['reference'], row['reference'])
    key = (ref, row['pin'])
    assert key not in expected, f'Power reference overwrites an existing interface: {key}'
    expected[key] = row['carrier_net']
for ref, net in [('R1', 'GP13'), ('R2', 'GP12')]:
    expected[(ref, '1')] = '3V3_OUT'
    expected[(ref, '2')] = net
for n in range(1, 13):
    expected[(f'C{n}', '1')] = '3V3_OUT'
    expected[(f'C{n}', '2')] = 'GND'
for ref in ['C17', 'C18']:
    expected[(ref, '1')] = '3V3_OUT'
    expected[(ref, '2')] = 'GND'
# Preserve electrical polarity as well as endpoint numbers.
roles = {('D2', '1'): 'K', ('D2', '2'): 'A', ('S1', '2'): 'COM', ('S1', '3'): 'BAT_ON', ('S1', '1'): 'BAT_OFF',
         **{('U2', str(n)): role for n, role in enumerate(['EN/UVLO', 'OVLO', 'PG', 'PGTH', 'IN', 'OUT', 'DVDT', 'GND', 'ILM', 'ITIMER'], 1)}}
for key, role in roles.items():
    assert pin_functions[key] == f'{role}_{key[1]}', f'Incorrect power terminal role: {key} {pin_functions[key]}'
assert actual == expected, f'Connectivity mismatch: {[(k, expected.get(k), actual.get(k)) for k in expected.keys() | actual.keys() if expected.get(k) != actual.get(k)]}'
for n, kind in enumerate(['input', 'input', 'open_collector', 'input', 'power_in', 'power_out', 'output', 'power_in', 'output', 'output'], 1):
    assert pin_types[('U2', str(n))] == kind, f'Incorrect TI electrical pin type on U2.{n}'
components = {comp.attrib['ref']: comp for comp in root.findall('./components/comp')}
assert set(components) == {ref for ref, pin in expected}
socket_footprint = 'MakeMusic:Samtec_SSQ-120-01-G-S_1x20_P2.54mm'
footprints = {
    'J1': socket_footprint, 'J2': socket_footprint,
    **{f'J{i}': 'MakeMusicCarrier:Harwin_M20-9990346_1x3_P2.54mm' for i in range(3, 15)},
    'J15': 'MakeMusicCarrier:Harwin_M20-9991646_1x16_P2.54mm',
    'H1': 'Connector_JST:JST_PH_B2B-PH-K_1x02_P2.00mm_Vertical',
    'S1': 'MakeMusicCarrier:NKK_MN12SS1W03_TerminalPattern_Candidate',
    'F1': 'MakeMusicPower:Schurter_UMT-H_3403-0275-23',
    'U2': 'MakeMusicPower:TI_RPW0010A_TPS259474_2x2mm',
    'D2': 'MakeMusicCarrier:Vishay_SS14_SMA_K1_A2',
    'D3': 'MakeMusicPower:Littelfuse_SMAJ5-0CA_DO-214AC',
    'TP1': 'TestPoint:TestPoint_Pad_D2.0mm',
    'R1': 'Resistor_SMD:R_0603_1608Metric', 'R2': 'Resistor_SMD:R_0603_1608Metric',
    **{f'C{i}': 'MakeMusicCarrier:KEMET_C0603_1608_LevelB' for i in range(1, 13)},
    **{f'R{i}': 'Resistor_SMD:R_0603_1608Metric' for i in range(3, 9)},
    **{f'C{i}': 'Capacitor_SMD:C_0805_2012Metric' for i in [13, 14, 16, 17, 18]},
    'C15': 'Capacitor_SMD:C_0603_1608Metric',
}
mpns = {'J1': 'SSQ-120-01-G-S', 'J2': 'SSQ-120-01-G-S',
        **{f'J{i}': 'M20-9990346' for i in range(3, 15)}, 'J15': 'M20-9991646',
        'H1': 'B2B-PH-K-S(LF)(SN)', 'R1': 'RC0603FR-0710KL', 'R2': 'RC0603FR-0710KL',
        'C17': 'C2012X7R1A106K125AC', 'C18': 'C2012X7R1A106K125AC',
        **{f'C{i}': 'C0603C104K5RACTU' for i in range(1, 13)}}
power_parts = {
    'F1': ('1.25A T', '3403.0275.23'), 'U2': ('TPS259474LRPWR', 'TPS259474LRPWR'),
    'S1': ('MN12SS1W03', 'MN12SS1W03'), 'D2': ('SS14-E3/61T', 'SS14-E3/61T'), 'D3': ('SMAJ5.0CA', 'SMAJ5.0CA'),
    'R3': ('649k', 'RC0603FR-07649KL'), 'R4': ('332k', 'RC0603FR-07332KL'),
    'R5': ('1.05M', 'RC0603FR-071M05L'), 'R6': ('332k', 'RC0603FR-07332KL'),
    'R7': ('3.32k', 'RC0603FR-073K32L'), 'R8': ('100', 'RC0603FR-07100RL'),
    **{f'C{i}': ('4u7 / 25V', 'C2012X7R1E475K125AB') for i in [13, 14, 16]},
    'C15': ('10n / 50V', 'C1608C0G1H103J080AA'),
}
mpns.update({ref: mpn for ref, (value, mpn) in power_parts.items()})
base = Path(__file__).resolve().parent
install_candidates = [args.kicad_footprint_dir, os.environ.get('KICAD10_FOOTPRINT_DIR'),
                      '/Applications/KiCad/KiCad.app/Contents/SharedSupport/footprints',
                      '/usr/share/kicad/footprints']
installed = next((Path(p) for p in install_candidates if p and Path(p).is_dir()), None)
assert installed is not None, 'Set --kicad-footprint-dir or KICAD10_FOOTPRINT_DIR to the installed KiCad 10 footprint root'
library_paths = {'MakeMusic': base.parent / 'libraries' / 'MakeMusic.pretty',
                 'MakeMusicCarrier': base / 'MakeMusicCarrier.pretty',
                 'MakeMusicPower': base / 'MakeMusicPower.pretty',
                 'Connector_JST': installed / 'Connector_JST.pretty',
                 'Resistor_SMD': installed / 'Resistor_SMD.pretty',
                 'Capacitor_SMD': installed / 'Capacitor_SMD.pretty',
                 'TestPoint': installed / 'TestPoint.pretty'}
for ref, comp in components.items():
    expected_footprint = footprints[ref]
    assert (comp.findtext('footprint') or '') == expected_footprint, f'Unexpected footprint assignment on {ref}: {comp.findtext("footprint")}'
    if ref in mpns:
        assert comp.findtext('./fields/field[@name="MPN"]') == mpns[ref], f'Unexpected MPN on {ref}'
    if expected_footprint:
        library, name = expected_footprint.split(':', 1)
        footprint_path = library_paths[library] / (name + '.kicad_mod')
        assert footprint_path.is_file(), f'Assigned footprint missing: {footprint_path}'
        # Physical pad coverage is checked from Konnect live readback by
        # verify_board.py, rather than parsing protected footprint sources.
for ref in ['R1', 'R2']:
    assert components[ref].findtext('value') == '10k', f'Unexpected reset bias value on {ref}'
for n in range(1, 13):
    comp = components[f'C{n}']
    assert comp.findtext('value') == '100n', f'Unexpected bypass value on C{n}'
    assert comp.findtext('./fields/field[@name="Header"]') == f'J{n+2}', f'Incorrect header association on C{n}'
for ref, header in [('C17', 'J13'), ('C18', 'J14')]:
    comp = components[ref]
    assert comp.findtext('value') == '10u / 10V', f'Unexpected buzzer bulk value on {ref}'
    assert comp.findtext('./fields/field[@name="Header"]') == header, f'Incorrect header association on {ref}'
    assert comp.findtext('datasheet') == 'https://product.tdk.com/info/en/documents/chara_sheet/C2012X7R1A106K125AC.pdf', f'Incorrect TDK datasheet on {ref}'
for ref in ['J1', 'J2']:
    assert components[ref].findtext('datasheet') == 'https://suddendocs.samtec.com/prints/ssq-1xx-xx-xxx-x-xx-xxx-xx-x-mkt.pdf', f'Incorrect socket datasheet on {ref}'
for ref, (value, mpn) in power_parts.items():
    assert components[ref].findtext('value') == value, f'Unexpected power component value on {ref}'
assert len(actual) == 166
assert len(components) == 48
excluded = {ref for ref, comp in components.items() if comp.find('./property[@name="exclude_from_bom"]') is not None}
assert excluded == {'TP1'}, f'Unexpected BOM exclusions: {excluded}'
assert not any(comp.find('./property[@name="dnp"]') is not None for comp in components.values()), 'Unexpected DNP population flag'
assert len(components) - len(excluded) == 47
assert len(root.findall('./nets/net')) == 44
assert len(connected_names) == 38
print('PASS: all 166 physical endpoints and 48 components match; 38 connected nets and 6 intentional NC nets.')
print('PASS: all 41 power-contract endpoints with R3-R8/C13-C16 mapping; U2 ten pin roles/types; no pad11 or carrier D1.')
print('PASS: upstream fuse, switch common2/ON3/OFF1, shunt D2 K1/A2 and bidirectional D3; VBUS/battery/VSYS/3V3 separation.')
print('PASS: physical JST H1 polarity, GP13/12 reset pull-ups, twelve 100nF bypass capacitors and C17/C18 10uF buzzer bulk.')
print('PASS: all 48 components have exact assigned footprint files; 47 purchased parts with native MPNs; TP1 2mm pad excluded.')
