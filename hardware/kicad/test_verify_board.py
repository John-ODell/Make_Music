"""Negative controls for the live-evidence electrical verifier."""
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch
import verify_board

EVIDENCE = Path(__file__).resolve().parents[1] / 'review/rear-edge-20261009'


class EvidenceTests(unittest.TestCase):
    def reject(self, filename, mutation):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / 'evidence'
            shutil.copytree(EVIDENCE, target)
            data = verify_board.response(target / filename)
            mutation(data)
            (target / filename).write_text(json.dumps(data))
            with self.assertRaises(AssertionError):
                verify_board.verify(target)

    def test_actual_evidence(self):
        self.assertEqual(verify_board.verify(EVIDENCE), (166, 4))

    def test_wrong_pad_net(self):
        self.reject('live-board.json', lambda d: d['pads']['C17']['pads'][0].update(net='/GND'))

    def test_bad_evidence_rejected(self):
        cases = [
            ('live-board.json', lambda d: d['inventory']['components'][0].update(value='wrong')),
            ('live-board.json', lambda d: d['pads']['C17'].update(source='file')),
            ('live-board.json', lambda d: d['identity_sync'].update(status='ready', changes=[{'reference':'J1'}])),
            ('drc-mcp.json', lambda d: d['violations'][0].update(description="Missing symbol field 'Other' in footprint")),
            ('drc-mcp.json', lambda d: d.update(design_rule_violations=1)),
            ('source-checkpoint.json', lambda d: d['design_sha256'].update({'kicad/make_music.kicad_pcb':'0'*64})),
        ]
        for filename, mutation in cases:
            with self.subTest(filename=filename, mutation=mutation):
                self.reject(filename, mutation)

    def test_pad_guard_negative_control(self):
        # Disable only this guard in an isolated function; prove the wrong-net
        # test fails to reject. Native sources and served verifier are untouched.
        source = Path(verify_board.__file__).read_text().replace(
            "assert actual == expected and len(actual) == 166, 'PCB/XML pad-net mismatch'",
            "assert len(actual) == 166, 'PCB/XML pad-net mismatch'")
        isolated = {'__file__': verify_board.__file__, '__name__': 'negative_control'}
        exec(compile(source, verify_board.__file__, 'exec'), isolated)
        with patch.object(verify_board, 'verify', isolated['verify']):
            with self.assertRaisesRegex(AssertionError, 'AssertionError not raised'):
                self.test_wrong_pad_net()


if __name__ == '__main__':
    unittest.main()
