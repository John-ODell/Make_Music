# Wire specification

Quotation and engineering review; final cut lengths and module ends require
the delivered parts and fitted mechanical assembly. Two complete instruments.

## A. Touch and buzzer harnesses

| Requirement | Specification |
|---|---|
| Completed harnesses | 12 per instrument, 24 total: ten touch and two buzzer per instrument |
| Conductors | Three flexible stranded AWG26 conductors per harness: white signal, red regulated 3.3V, black ground |
| Insulation outside diameter | 0.9-1.6 mm, subject to exact contact/tool qualification |
| Carrier-end housing | Harwin M20-1060300, 3-position female, 2.54 mm pitch; 24 total |
| Carrier-end contacts | Harwin M20-1180046 tin loose crimp contacts; 72 total |
| Initial wire allowance | 100 mm per conductor; 72 conductors, 7.2 m total before scrap. This is a costing allowance, not an approved cut length |
| Carrier cavity 1 | Signal, white, aligned with carrier square pad/pin1 mark |
| Carrier cavity 2 | Regulated 3V3, red |
| Carrier cavity 3 | GND, black |
| Module end | Factory to identify and quote exact mating termination from actual module header/pads, then return drawing and measured engagement |

The exact Harwin drawing specifies 3-4 mm strip and 0.9-1.6 mm insulation OD.
Qualify suitable production tooling and crimp/retention on sample wires;
the existing Harwin tool reference gives 18 N minimum AWG26 pull-off for
qualification samples, not a destructive test on every installed harness.
Primary sources: [contact drawing](https://content.harwin.com/asset/d742d022-1905-41c8-b996-8feb2ed262c8/DRG-00379-Technical-Drawing-Datasheet-M20-118-pdf.pdf),
[housing](https://www.harwin.com/products/M20-1060300).

| Carrier header | Function | Pico GPIO | Module signal destination |
|---|---|---:|---|
| J3 | C4 | GP16 | Verified touch OUT/DI |
| J4 | D4 | GP17 | Verified touch OUT/DI |
| J5 | E4 | GP18 | Verified touch OUT/DI |
| J6 | F4 | GP19 | Verified touch OUT/DI |
| J7 | G4 | GP20 | Verified touch OUT/DI |
| J8 | A4 | GP21 | Verified touch OUT/DI |
| J9 | B4 | GP22 | Verified touch OUT/DI |
| J10 | C5 | GP26 | Verified touch OUT/DI |
| J11 | Semitone modifier | GP27 | Verified touch OUT/DI |
| J12 | Octave modifier | GP28 | Verified touch OUT/DI |
| J13 | Buzzer 1 | GP13 | Verified passive-module I/O |
| J14 | Buzzer 2 | GP12 | Verified passive-module I/O |

GPIO numbers are not physical Pico pin numbers. Every red wire goes to the
module's actual VCC and every black wire to actual GND. Supply is regulated
3.3V; raw battery voltage is prohibited on module supply and GPIO wires.
Do not assume the module contact sequence equals carrier SIG/3V3/GND.
Original ST0238 order differs; generic revisions must be measured separately.
Return module-end cavity/pad numbers, both connector views and continuity map.

Unshrouded headers are unkeyed: visibly mark signal/pin1, prevent reversal or
one-pin offset, provide retention/strain relief independent of contact friction,
and route away from touch electrodes, buzzer openings, Pico removal/USB/BOOTSEL,
switch travel and battery access. Approve dressed length and service slack
after fixture fit; do not cut all wires to the costing allowance by assumption.

## B. Battery harness

Two completed harnesses total. MPD BH-18650-W includes two factory AWG24 TR64
leads, 150 +/-5 mm each; do not allocate a second set of replacement wires.
Measure their actual insulation OD against the JST contact's 0.8-1.5 mm range.
Factory re-prepares/crimps leads to JST PHR-2 housing and two
SPH-002T-P0.5S contacts per instrument (two housings, four contacts total).
MPD's delivered stripping length is not a JST crimp instruction; use the
qualified exact contact/tool strip process and record it.

- PHR-2 circuit 1 to the holder's measured positive terminal, then carrier
  bottom H1 circuit 1/BAT_PROT_PLUS.
- PHR-2 circuit 2 to the holder's measured negative terminal, then H1 circuit
  2/GND. This is our circuit convention, not a universal JST polarity rule.
- Verify by cavity and contact continuity, not wire color. Return mating-face
  and wire-entry views and finished-length drawing for approval.
- Keep adequate slack and independent strain relief, with protected insulation
  and no cell, spring, screw, door or support chafing/pinch points.
- Actual holder/cell cold fit and current capability (0.70 A normal branch,
  at least 1.2 A continuous contact capability) remain qualifications.

Primary sources: [JST PH](https://www.jst-mfg.com/product/pdf/eng/ePH.pdf),
[MPD BH-18650-W drawing](https://www.batteryholders.com/uploads/parts/BH-18650-W/datasheets/BH-18650-W-datasheet.pdf).

## C. Cold inspection before connection

Battery, USB, Pico and modules disconnected: identify each harness/header,
measure all three signal/power/ground paths, exclude cross-shorts, verify
orientation and retention, and record actual lengths and contact/module lots.
Inspect battery polarity separately. Check delivered module output polarity
and momentary operation from a current-limited 3.3V supply before Pico connection.
Return any proposed termination/material change for review.
