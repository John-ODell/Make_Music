"""MicroPython firmware for the first Make Music carrier prototype.

Confirm touch polarity on the actual modules before installing as main.py.
ST0238 buzzer inputs are active-low: silence is a constant HIGH output.
"""

NOTE_PINS = (16, 17, 18, 19, 20, 21, 22, 26)
NOTE_HZ = (261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25)
SEMITONE_PIN = 27
OCTAVE_PIN = 28
BUZZER_PINS = (13, 12)  # Shared PWM slice: both play the same note.

# The supplied TTP223 reference ties AHLB high (active-low). Set each entry to
# 1 for a module verified active-high; no rewiring of GPIO assignments needed.
TOUCH_ACTIVE_LEVELS = {pin: 0 for pin in NOTE_PINS + (SEMITONE_PIN, OCTAVE_PIN)}
BUZZER_ACTIVE_LOW = True


class CarrierSynth:
    def __init__(self, machine, active_levels=None, buzzer_active_low=True):
        self.machine = machine
        self.levels = dict(TOUCH_ACTIVE_LEVELS if active_levels is None else active_levels)
        required = NOTE_PINS + (SEMITONE_PIN, OCTAVE_PIN)
        if set(self.levels) != set(required) or any(v not in (0, 1) for v in self.levels.values()):
            raise ValueError('Specify a 0 or 1 active level for all ten touch inputs')
        self.idle = 1 if buzzer_active_low else 0
        self.silent_duty = 65535 if self.idle else 0
        # Establish silence as ordinary digital outputs before selecting PWM.
        self.output_pins = [machine.Pin(pin, machine.Pin.OUT, value=self.idle)
                            for pin in BUZZER_PINS]
        self.buzzers = [machine.PWM(pin, freq=440, duty_u16=self.silent_duty)
                       for pin in self.output_pins]
        self.inputs = {pin: machine.Pin(pin, machine.Pin.IN,
                       machine.Pin.PULL_UP if self.levels[pin] == 0 else machine.Pin.PULL_DOWN)
                       for pin in required}
        self.last_frequency = None

    def pressed(self, pin):
        return self.inputs[pin].value() == self.levels[pin]

    def scan(self):
        # Retain original first-note priority when multiple notes are touched.
        frequency = None
        for pin, base_hz in zip(NOTE_PINS, NOTE_HZ):
            if self.pressed(pin):
                frequency = base_hz
                if self.pressed(SEMITONE_PIN):
                    frequency *= 2 ** (1 / 12)
                if self.pressed(OCTAVE_PIN):
                    frequency *= 2
                frequency = round(frequency)
                break
        if frequency != self.last_frequency:
            if frequency is None:
                for buzzer in self.buzzers:
                    buzzer.duty_u16(self.silent_duty)
            else:
                # Changing one slice frequency affects both channels; write
                # the same value to both and then enable their 50% duty outputs.
                for buzzer in self.buzzers:
                    buzzer.freq(frequency)
                    buzzer.duty_u16(32768)
            self.last_frequency = frequency
        return frequency

    def close(self):
        for buzzer in self.buzzers:
            buzzer.duty_u16(self.silent_duty)
            buzzer.deinit()
        # deinit alone does not establish a driven idle voltage.
        for pin in self.output_pins:
            pin.init(self.machine.Pin.OUT, value=self.idle)


def main():
    import machine
    from time import sleep_ms

    synth = CarrierSynth(machine, TOUCH_ACTIVE_LEVELS, BUZZER_ACTIVE_LOW)
    try:
        sleep_ms(600)  # TTP223's documented power-up settling interval is ~500 ms.
        while True:
            synth.scan()
            sleep_ms(10)
    finally:
        synth.close()


if __name__ == '__main__':
    main()
