# Programming file and installation

Candidate firmware for quotation and first-article qualification, not a tested
hardware release. Program only the two complete instruments after separate
owner production authorization. The other three deliveries are populated
carriers without a Pico or permanently installed application.

## Supplied programming files

1. `RPI_PICO-20260824-v1.29.0.uf2`: official stable MicroPython v1.29.0 runtime
   for the **original RP2040 Raspberry Pi Pico/Pico H**, not Pico W/Pico 2.
   Source checked October 16, 2026:
   https://micropython.org/download/RPI_PICO/
   Direct binary:
   https://micropython.org/resources/firmware/RPI_PICO-20260824-v1.29.0.uf2
   SHA256: `e1160e602e277d85920adb5fe741435edccba9ba6ecadc85fdab75252eeff4e9`.
   Interpreter licensing/source: https://github.com/micropython/micropython/tree/v1.29.0
2. `main.py`: byte-for-byte copy of the current project application
   `Pico_Synth/carrier_prototype.py`. The bundle manifest records its exact hash.
   This is the application file, not a standalone compiled UF2 image.

The runtime binary's UF2 block framing was checked on download. The application
passes seven CPython host tests with fake GPIO/PWM. Neither check proves actual
execution on MicroPython v1.29.0 or musical performance; confirm on the first
real Pico and return the runtime/version and final application hash.

## Configuration before connecting modules

Use a current-limited 3.3V supply to measure idle and touched levels of all ten
delivered touch modules; confirm direct/momentary output, not a latching toggle.
`TOUCH_ACTIVE_LEVELS` initially has 0 for every GPIO, reflecting the original
active-low reference. Generic TTP223 modules may be active-high. Set each GPIO's
entry to the measured active value (0 or 1). Keep all ten assigned GPIOs and
record the resulting map. Do not power the instrument with an assumed polarity.

`BUZZER_ACTIVE_LOW = True` matches the requested transistor-driven low-trigger
passive modules. Require HIGH for idle silence and variable-pitch response to
PWM. Return any incompatible module for review; do not install a fixed-tone
active buzzer as a substitute. No firmware frequency/pin change is implied.

Return any polarity-only configured application and its hash for review; record
what was changed. Other application changes require engineering review.

## Factory installation steps

1. Battery removed, carrier/modules disconnected. Use a separately powered
   Pico H and USB data cable for programming; follow normal ESD handling.
2. Hold Pico BOOTSEL while connecting USB. Copy the supplied official runtime
   UF2 onto its `RPI-RP2` USB drive. The Pico reboots. This step alone installs
   only the interpreter, not our application.
3. Open the MicroPython USB REPL using Thonny or an equivalent factory tool.
   Record `sys.implementation` and `os.uname()` output. Copy the configured
   application onto the Pico's **MicroPython filesystem** as `/main.py`.
   Do not copy it onto the temporary BOOTSEL drive.
4. Read the stored `/main.py` back to the programming computer and compare its
   bytes/hash to the approved configured application. Remove unrelated startup
   scripts from the factory Pico image only; do not modify an owner's used Pico.
5. Disconnect all sources before inserting the removable Pico in the carrier
   sockets. Carry out the staged electrical/functional test, starting with a
   current-limited emulator; real-cell operation remains gated.
6. Confirm boot with no PC, startup silence, all eight notes and both modifiers,
   correct release silence and both buzzer outputs. Record exact application
   and interpreter hashes/version in the traveler for each complete instrument.

Expected behavior: a 600 ms software startup settling delay, scans approximately
every 10 ms afterward; lowest-index touched note wins when several notes are
held; semitone adds a factor of 2^(1/12), octave a factor of 2, and both combine.
GP12/13 share a PWM slice and intentionally play the **same pitch**. No loop,
drum, display or independent-voice behavior is included in this revision.

Primary flashing instructions are on the official MicroPython download page
above. Full pin/function and acceptance procedure: `WIRE_SPEC.md`, `TEST_FILE.md`.
