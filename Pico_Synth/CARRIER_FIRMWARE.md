# First-carrier prototype firmware

`carrier_prototype.py` is a separate MicroPython entry point for the selected ST0238 modules. The original `octave_half_8_key.py` is preserved.

The new script keeps notes on GP16–22/26, semitone on GP27, octave on GP28, and both same-pitch buzzers on GP13/12. First-note priority and held modifiers are retained. Pitch is the square-wave frequency; the GPIO voltage remains digital 0/3.3 V. A 50% duty waveform drives both modules.

ST0238's driver is active-low. Startup, key release and orderly shutdown now drive its input HIGH, using PWM duty 65535 for silence rather than the original script's duty 0. After PWM shutdown the pins are explicitly restored to digital HIGH. Software cannot guarantee silence during reset, BOOTSEL or removal; schematic pull-ups and the actual module circuit must be reviewed independently.

## Before installing on the Pico

Verify each touch module is momentary, then check its idle and touched voltage at regulated 3.3 V. Set the corresponding `TOUCH_ACTIVE_LEVELS` entry to 0 for LOW when touched or 1 for HIGH when touched. Defaults follow the user-supplied active-low TTP223 schematic; they are not a measurement of the purchased modules. The input bias is selected from each configured polarity. Toggling touch modules do not provide the required held-note behavior.

Install MicroPython for the actual Pico model, copy this script as `main.py`, and retain a way to interrupt it over USB. Startup waits 600 ms for touch-controller settling. Test USB-powered/current-limited first: idle silence, each note, release, both modifiers together, multi-note priority, interruption, and repeated reset. Confirm loudness across the note range; ST0238's advertised 2–5 kHz range does not establish lower-note performance.

Host validation: `python3 -m unittest discover -s Pico_Synth/tests -v` uses simulated GPIO/PWM objects to check note behavior, mixed input polarities, active-low startup/release and shutdown. These checks do not verify MicroPython timing, boot transients, actual sound, touch response or board current. No hardware test is claimed.

Sources: [MicroPython PWM API](https://docs.micropython.org/en/latest/library/machine.PWM.html), [Pin API](https://docs.micropython.org/en/latest/library/machine.Pin.html), [ST0238 manufacturer listing](https://www.sunfounder.com/products/3-3-5v-passive-low-level-trigger-buzzer-alarm-sound-module), and `hardware/components/TOUCH_MODULE.md` for TTP223 power-up/polarity evidence. Check the API for the installed MicroPython release; no new development-only features are required.
