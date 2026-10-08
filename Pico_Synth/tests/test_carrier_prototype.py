"""Host checks of note behavior and active-low output handling, not hardware tests."""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('carrier', Path(__file__).parents[1] / 'carrier_prototype.py')
carrier = importlib.util.module_from_spec(spec)
spec.loader.exec_module(carrier)


class FakePin:
    IN, OUT, PULL_UP, PULL_DOWN = range(4)

    def __init__(self, number, mode, pull=None, value=None):
        self.number, self.mode, self.pull = number, mode, pull
        self.level = value if value is not None else int(pull == self.PULL_UP)

    def value(self):
        return self.level

    def init(self, mode, value):
        self.mode, self.level = mode, value


class FakePWM:
    def __init__(self, pin, freq, duty_u16):
        self.pin, self.frequency, self.duty = pin, freq, duty_u16
        self.deinitialized = False

    def freq(self, hz):
        self.frequency = hz

    def duty_u16(self, duty):
        self.duty = duty

    def deinit(self):
        self.deinitialized = True


class FakeMachine:
    Pin, PWM = FakePin, FakePWM


class CarrierTest(unittest.TestCase):
    def setUp(self):
        self.synth = carrier.CarrierSynth(FakeMachine)

    def press(self, pin):
        self.synth.inputs[pin].level = self.synth.levels[pin]

    def test_active_low_startup_and_release_are_high(self):
        self.assertEqual([p.level for p in self.synth.output_pins], [1, 1])
        self.assertEqual([b.duty for b in self.synth.buzzers], [65535, 65535])
        self.assertIsNone(self.synth.scan())
        self.press(16)
        self.assertEqual(self.synth.scan(), 262)
        self.synth.inputs[16].level = 1
        self.assertIsNone(self.synth.scan())
        self.assertEqual([b.duty for b in self.synth.buzzers], [65535, 65535])

    def test_note_and_combined_modifiers(self):
        self.press(21)
        self.assertEqual(self.synth.scan(), 440)
        self.press(27)
        self.assertEqual(self.synth.scan(), 466)
        self.press(28)
        self.assertEqual(self.synth.scan(), 932)
        self.assertEqual([b.frequency for b in self.synth.buzzers], [932, 932])
        self.assertEqual([b.duty for b in self.synth.buzzers], [32768, 32768])

    def test_first_note_priority_and_all_note_assignments(self):
        self.press(22)
        self.press(16)
        self.assertEqual(self.synth.scan(), 262)
        for pin, expected in zip(carrier.NOTE_PINS, (262, 294, 330, 349, 392, 440, 494, 523)):
            for input_pin in self.synth.inputs.values():
                input_pin.level = 1
            self.press(pin)
            self.assertEqual(self.synth.scan(), expected)

    def test_mixed_touch_polarities(self):
        levels = dict(carrier.TOUCH_ACTIVE_LEVELS)
        levels[21], levels[27] = 1, 1
        self.synth = carrier.CarrierSynth(FakeMachine, levels)
        self.assertIsNone(self.synth.scan())
        self.press(21)
        self.press(27)
        self.assertEqual(self.synth.scan(), 466)

    def test_shutdown_restores_driven_silence(self):
        self.press(21)
        self.synth.scan()
        self.synth.close()
        self.assertTrue(all(b.deinitialized for b in self.synth.buzzers))
        self.assertEqual([p.level for p in self.synth.output_pins], [1, 1])
        self.assertEqual([p.mode for p in self.synth.output_pins], [FakePin.OUT, FakePin.OUT])

    def test_legacy_active_high_buzzer_idle_is_supported(self):
        synth = carrier.CarrierSynth(FakeMachine, buzzer_active_low=False)
        self.assertEqual([b.duty for b in synth.buzzers], [0, 0])
        synth.close()
        self.assertEqual([p.level for p in synth.output_pins], [0, 0])

    def test_invalid_input_configuration_is_rejected_before_gpio_setup(self):
        with self.assertRaises(ValueError):
            carrier.CarrierSynth(FakeMachine, {16: 0})


if __name__ == '__main__':
    unittest.main()
