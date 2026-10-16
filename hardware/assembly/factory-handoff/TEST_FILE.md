# Factory test file: procedure and blank results

For quotation and engineering review. **No physical tests have been performed.**
Do not start fabrication, assembly or first-article work without separate owner
release. The qualification below is required work to quote, not evidence that
the hardware is ready. Retain failures, measurements and scope captures.

## Scope and sequence

- Inspect and electrically test all **five populated carriers**, including all
  30 top SMD and 17 thru-hole parts; H1 is bottom thru-hole.
- Qualify one of the **two complete instruments first**. Stop for review of
  results before completing the second instrument. Test and document both.
- The other three carriers ship populated, without Pico, external modules,
  batteries, harnesses or custom fixture; they still need carrier inspection
  and power-path testing. Temporary test fixtures/controllers may be used
  for factory checks but are not part of their delivery.

Use calibrated DMM, scope, isolated adjustable current-limited supply/cell
emulator, electronic load and a separately current-limited USB fixture. Agree
the actual supplier test capability/price and return proposed changes before
release. A computer USB port or real cell is not a fault-test supply.

## 1. Cold assembly and harness inspection (all five carriers)

Identify serial, exact board/BOM revision and parts lots. Compare every installed
part with the approved 47-part carrier BOM. Inspect solder joints, U2 pin1 and
ten-terminal package, D2 cathode toward VSYS and D3 bidirectional CA suffix,
F1 rating, S1 operation, bottom H1 polarity, sockets and all header alignment.
Reconcile any historical local schematic references against the actual carrier
BOM; its C1-C18 capacitors remain populated as specified. Confirm no unintended
power short or VBUS/battery bridge against the reviewed netlist.

For the two complete instruments, verify all 24 module harnesses and two battery
harnesses against WIRE_SPEC.md with everything disconnected. Record exact
module revisions, pin order, touch active levels, crimps, routing and strain
relief. Check Pico seating/removal/USB/BOOTSEL access. Verify loaded clearances
of at least 2 mm between mechanics and bottom parts/tails/wires, with playing
loads carried by supports, never by the cell/holder. Nominal drawings do not
replace actual-part metrology or final toleranced mechanical drawings.

## 2. Carrier power-path qualification (each carrier)

Use accessible named-net test points and record both H1 input and U2 IN
(`BAT_SW_PLUS`), not just nominal supply settings. Scope/DMM grounds reference
GND/H1.2 only. Pico, USB, modules, real cell and charger remain absent unless a
step explicitly installs them. Switch/connect/disconnect with sources off.
Stop for incorrect polarity, unexpected heating, normal-test current-limit
operation, rail excursions or failure to latch; investigate before increasing
limits. Criteria below are existing engineering commissioning targets.

1. At emulator 4.20 V, 20 mA limit, switch OFF then ON: check no sustained short,
   VSYS follows valid IN, bare-carrier steady current <5 mA and no current-limit
   operation. Check switch OFF interrupts the input branch.
2. After pass, supply limit 0.75 A; electronic load at 0.10/0.35/0.70 A on VSYS:
   measure H1/IN/VSYS, current and temperature. At 0.70 A require IN-to-VSYS drop
   <=65 mV, stable output/no unintended latch and power-resistor local
   temperature <=70 C. This bare-path characterization is not approval to draw
   more than 0.70 A input in normal instrument use.
3. UVLO: use 100 ohm >=1 W load and 100 mA supply limit. Ramp H1 down from
   4.20 to 2.90 V then up to 4.25 V. Record **IN** disconnect/restart thresholds:
   falling 3.053-3.430 V; rising 3.363-3.752 V. Record loaded H1 cutoff too.
   Recovery should be automatic; distinguish UVLO from a latched fault.
4. Isolated fault latch: valid emulator input at 4.25 V, IN above actual UVLO,
   supply limit 1.30 A. Pulse load upward from 0.70 toward 1.20 A in increments;
   each above-0.70 A pulse <=20 ms. Capture actual current immediately before
   collapse, target 0.80-1.20 A; stop if 1.25 A demand fails to trip. Reduce
   demand to 0.10 A: output stays off until reset. Repeat after reset at H1
   3.70 V and near measured UVLO with IN >=0.10 V above the measured falling
   threshold. Supply CC or falling through UVLO invalidates a trip result.
   Never hard-short a real cell or intentionally blow F1.
5. Reset: sources removed/S1 OFF; verify BAT_SW_PLUS <1.0 V and EN_UVLO <0.45 V
   before restart. Record dwell. With only the 100 ohm load, emulator at
   100 mA limit, ramp IN toward **5.45 V maximum**, then down. Bare carrier
   only: expected OVLO trip 4.710-5.315 V, recovery 4.275-4.860 V.
6. Isolated reverse test: no Pico/USB/modules; S1 OFF, H1.1 at -4.25 V relative
   to GND with 20 mA limit, then ON. VSYS must not become negative or power a
   load; steady leakage <2 mA, no supply CC. Restore polarity with all sources
   OFF. Confirm reverse/USB setup isolation before combining sources.

Detailed original rationale: `hardware/power/prototype-validation.md` in the
already submitted review packet. Report anything the supplier cannot execute.

## 3. Complete-instrument tests (two units only)

After carrier tests and firmware readback pass, install Pico only, no modules
or real cell, from sources OFF. Use positive emulator 4.20 V / 0.20 A limit.
Account for actual current before increasing a limit. Add one correctly mapped
module at a time with sources OFF. Normal limits: <=0.70 A battery input,
<=250 mA external regulated 3V3 load, <=350 mA total 3V3 including Pico.
Measure currents on their actual rails; battery current does not equal 3V3
current. Steady 3V3 engineering screening band: 3.14-3.46 V, plus successful
module operation and startup/transient compliance with actual part limits.

Verify each touch module is momentary and its firmware polarity matches the
measured active level. Following the startup settling interval, both buzzer
outputs are HIGH/silent with no touch; releasing all notes restores silence.
Passive low-trigger modules must respond to changing PWM frequency. Both
buzzers intentionally play the same frequency; no independent percussion voice.

| Note/header | GPIO | No modifier, programmed Hz | Semitone, Hz | Octave, Hz | Both, Hz |
|---|---:|---:|---:|---:|---:|
| C4/J3 | 16 | 262 | 277 | 523 | 554 |
| D4/J4 | 17 | 294 | 311 | 587 | 622 |
| E4/J5 | 18 | 330 | 349 | 659 | 698 |
| F4/J6 | 19 | 349 | 370 | 698 | 740 |
| G4/J7 | 20 | 392 | 415 | 784 | 831 |
| A4/J8 | 21 | 440 | 466 | 880 | 932 |
| B4/J9 | 22 | 494 | 523 | 988 | 1046 |
| C5/J10 | 26 | 523 | 554 | 1046 | 1109 |

Semitone input: J11/GP27. Octave input: J12/GP28. Check all 32 combinations
at GP13 and GP12 using a scope/frequency counter; record measured frequencies,
both modules' audible output and any discrepancies. Listed integer targets are
the application commands, not an assertion of measured clock accuracy. Report
measurement uncertainty and any mismatch for engineering adjudication. A buzzer
sounding does not prove the programmed pitch or acceptable musical volume.

Hold C4 and a higher note: C4 wins. Release C4: held higher note takes over.
Modifiers alone remain silent. Test each buzzer individually, both together,
all note releases, reset/reboot and no-PC boot. There must be no unintended
sustained idle sound or stuck touch. Capture startup/VSYS/3V3 waveforms and
normal temperatures at 4.20 V, 3.70 V and just above measured UVLO.

USB/source isolation: with verified Pico and no modules initially, use a
separately current-limited 5 V USB fixture (initial 100 mA; stop on CC and
review actual Pico inrush/load before any increase). Confirm USB powers VSYS
with S1 OFF; test battery emulator at 4.25/3.70 V and reverse -4.25 V only after
the isolated reverse test passed. Measure signed battery-terminal current and
investigate repeatable USB-dependent charging/backfeed. USB bypasses battery
F1/U2; its inrush, thermal and fault behavior require separate qualification.
Do not short a computer port. Stop playing before changing sources; reboot is
permitted, then settle and retest. Carrier S1 does not switch off USB power.

## 4. Real cell, charger and final acceptance

Hold real-cell operation until cold fit/retention/removal, contact capability,
battery harness polarity, all power tests, normal current/rails and actual
cell/charger compatibility are accepted. The earlier L1 4.2V +/-1% reference
has an unresolved 4.242V maximum versus an unqualified 4.20V cell limit. Obtain
exact delivered cell/charger specifications and accepted pairing; changing
charge current alone does not resolve voltage tolerance. No onboard charging.

After accepted qualification, sources OFF, verify disconnected holder harness
polarity/voltage before carrier connection; first real-cell use is attended.
Remove cell for external charging/storage. UVLO stopping means switch OFF and
recharge, not repeated rebound operation. Return first-article results before
completing the second instrument. No hardware result is prefilled as PASS.

## 5. Per-unit result form (one copy per carrier, add instrument fields to two)

Unit ID: ____  delivery: COMPLETE / POPULATED CARRIER
Tester/date: ____  carrier/BOM revision: ____  instruments/calibration: ____
Assembly/netlist/polarity/solder inspection and evidence: ____
Cold current/leakage/VSYS and switch result: ____
0.10/0.35/0.70 A drops, temperatures and waveform IDs: ____
UVLO IN fall/rise, loaded H1 cutoff: ____
Fault trip current / actual IN / latch / repeated low-voltage results: ____
Reset dwell / IN / EN / OVLO trip and recovery: ____
Reverse voltage / leakage / minimum VSYS / result: ____
Carrier-only inspection/power disposition: ____
Complete-unit-only fields (mark NOT APPLICABLE for other three):
Pico/runtime/app version and hashes/readback: ____
Exact module lots, momentary behavior and ten-GPIO active-level map: ____
Harness/cavity/length/crimp/strain relief and mechanical fit evidence: ____
All 32 note/modifier combinations, both PWM measurements/audible outputs: ____
Release/priority/modifiers-alone/reset/boot/silence: ____
Battery input / external3V3 / total3V3 currents and rail transients: ____
USB/inrush/isolation/signed battery current and thermal records: ____
Cell/holder/charger accepted specifications and compatibility evidence: ____
Final loaded-clearance, retention, access and real-cell test record: ____
Failures/deviations/rework: ____  accepted by/date: ____

Blank means NOT MEASURED, never zero or PASS. Supply separate records for all
five carriers and complete-instrument evidence for exactly two. Preserve all
production holds until the owner reviews the required evidence and releases
the applicable next stage.
