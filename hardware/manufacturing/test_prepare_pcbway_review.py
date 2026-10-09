"""Placement guards against independent saved IPC fixture expectations."""
import copy
import csv
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET

import prepare_pcbway_review as prepare

EVIDENCE = Path(__file__).resolve().parents[1] / 'review/integration-20261009'


def fixture():
    live = prepare.response(EVIDENCE / 'live-board.json')['inventory']['components']
    xml = ET.parse(EVIDENCE / 'netlist.xml').getroot()
    refs = {c.attrib['ref'] for c in xml.findall('components/comp')} - {'TP1'}
    rows = []
    for fp in live:
        if fp['reference'] in refs:
            rows.append({'Ref': fp['reference'], 'Val': fp['value'],
                         'Package': fp['footprint'].split(':')[-1],
                         'PosX': f"{fp['x']:.6f}", 'PosY': f"{-fp['y']:.6f}",
                         'Rot': f"{fp['rotation']:.6f}",
                         'Side': 'top' if fp['layer'] == 'F.Cu' else 'bottom'})
    return rows, refs, live


class PlacementTests(unittest.TestCase):
    def setUp(self):
        self.rows, self.refs, self.live = fixture()

    def row(self, ref):
        return next(p for p in self.rows if p['Ref'] == ref)

    def check(self):
        prepare.verify_placements(self.rows, self.refs, self.live)

    def test_actual_inventory_and_native_y(self):
        self.assertEqual(len(self.rows), 47)
        # Independent checkpoint anchors include the bottom connector and
        # new bulk parts, plus U2's critical orientation.
        self.assertEqual((self.row('H1')['PosX'], self.row('H1')['PosY'], self.row('H1')['Side']),
                         ('289.000000', '-40.000000', 'bottom'))
        self.assertEqual((self.row('C17')['PosX'], self.row('C17')['PosY']),
                         ('87.460000', '-65.500000'))
        self.assertEqual(self.row('U2')['Rot'], '0.000000')
        self.check()

    def test_u2_rotation_rejected(self):
        self.row('U2')['Rot'] = '180'
        with self.assertRaisesRegex(AssertionError, 'rotation differs: U2'):
            self.check()

    def test_non_anchor_displacement_rejected(self):
        self.row('C17')['PosX'] = '88.46'
        with self.assertRaisesRegex(AssertionError, 'X differs: C17'):
            self.check()

    def test_native_y_sign_rejected(self):
        self.row('C18')['PosY'] = '65.5'
        with self.assertRaisesRegex(AssertionError, 'Y differs: C18'):
            self.check()

    def test_side_flip_rejected(self):
        self.row('H1')['Side'] = 'top'
        with self.assertRaisesRegex(AssertionError, 'side differs: H1'):
            self.check()

    def test_omission_rejected(self):
        self.rows = [p for p in self.rows if p['Ref'] != 'C18']
        with self.assertRaisesRegex(AssertionError, 'coverage disagreement'):
            self.check()

    def test_extra_duplicate_rejected(self):
        self.rows.append(copy.deepcopy(self.row('U2')))
        with self.assertRaisesRegex(AssertionError, 'Duplicate placement reference'):
            self.check()

    def test_wrong_reference_with_same_count_rejected(self):
        self.row('C18')['Ref'] = 'C99'
        with self.assertRaisesRegex(AssertionError, 'coverage disagreement'):
            self.check()

    def test_identity_and_nonfinite_values_rejected(self):
        cases = [('Val', 'wrong', 'value differs'), ('Package', 'wrong', 'footprint differs'),
                 ('PosX', 'nan', 'Nonfinite'), ('PosY', 'inf', 'Nonfinite'),
                 ('Rot', '-inf', 'Nonfinite'), ('PosX', 'wrong', 'Invalid')]
        original = copy.deepcopy(self.rows)
        for field, value, message in cases:
            with self.subTest(field=field, value=value):
                self.rows = copy.deepcopy(original)
                self.row('U2')[field] = value
                with self.assertRaisesRegex(AssertionError, message):
                    self.check()

    def test_rotation_wrap_and_export_rounding(self):
        self.row('U2')['Rot'] = '360'
        self.row('C17')['Rot'] = '-360'
        self.row('C17')['PosX'] = '87.4600005'
        self.check()

    def test_guard_runs_before_output_creation(self):
        # Stub only unrelated source/electrical checks. The actual prepare()
        # path must reject a reversed U2 before any package is created.
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            native = directory / 'native'
            native.mkdir()
            self.row('U2')['Rot'] = '180'
            with (native / 'positions.csv').open('w', newline='') as stream:
                writer = csv.DictWriter(stream, fieldnames=list(self.rows[0]))
                writer.writeheader()
                writer.writerows(self.rows)
            destination = directory / 'output'
            snapshot = EVIDENCE / 'source-checkpoint.json'
            hashes = json.loads(snapshot.read_text())['design_sha256']
            with patch.object(prepare, 'design_hashes', return_value=hashes), \
                 patch.object(prepare.verify_board, 'verify', return_value=(166, 4)):
                with self.assertRaisesRegex(AssertionError, 'rotation differs: U2'):
                    prepare.prepare(native, EVIDENCE / 'netlist.xml',
                                    EVIDENCE / 'erc-mcp.json', EVIDENCE / 'drc-mcp.json',
                                    destination, snapshot, EVIDENCE)
            self.assertFalse(destination.exists())

    def test_rotation_guard_negative_control(self):
        # Neutralize only rotation comparison in an isolated ordinary-Python
        # function; the U2 regression must then fail to reject.
        source = Path(prepare.__file__).read_text().replace(
            "assert abs(difference) <= tolerance, 'Live placement rotation differs: ' + ref",
            'pass  # rotation guard intentionally neutralized')
        isolated = {'__file__': prepare.__file__, '__name__': 'negative_control'}
        exec(compile(source, prepare.__file__, 'exec'), isolated)
        with patch.object(prepare, 'verify_placements', isolated['verify_placements']):
            with self.assertRaisesRegex(AssertionError, 'AssertionError not raised'):
                self.test_u2_rotation_rejected()


class ExportOriginTests(unittest.TestCase):
    def check_origin(self, rear_y):
        with tempfile.TemporaryDirectory() as tmp:
            native = Path(tmp)
            gerbers = native / 'gerbers'
            gerbers.mkdir()
            rear = round(rear_y * 1_000_000)
            (gerbers / 'make_music-Edge_Cuts.gm1').write_text(
                f'X20000000Y-{rear}D02*\nX350000000Y-{rear}D01*\n'
                'X350000000Y-140000000D01*\nX20000000Y-140000000D01*\n')
            (gerbers / 'make_music-NPTH.drl').write_text('METRIC\nX26.0Y-26.0\n')
            prepare.verify_native_origin(native)

    def test_final_y18_5_and_unchanged_drill_datum(self):
        self.check_origin(18.5)

    def test_superseded_y20_rejected(self):
        with self.assertRaisesRegex(AssertionError, 'Unexpected outline or Gerber origin'):
            self.check_origin(20)

    def test_interim_y19_rejected(self):
        with self.assertRaisesRegex(AssertionError, 'Unexpected outline or Gerber origin'):
            self.check_origin(19)


if __name__ == '__main__':
    unittest.main()
