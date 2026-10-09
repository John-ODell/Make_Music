# Make Music — first-prototype design requirements

Updated 2026-10-09 for the saved PR28 rear-edge revision. The native two-sheet schematic has 48 electrical parts and 166 endpoints. The recorded integration checks report ERC 0, copper/layout DRC 0 and unconnected items 0; overall DRC retains **four metadata parity warnings**: C17/C18 missing Header fields and J1/J2 missing MPN fields on the board. Native schematic fields remain intact, and all 166 live pad nets, 48 values and full footprint IDs agree with the exported circuit contract. These reviewed metadata limitations do not establish fabrication readiness. See [actual PCB checks](kicad/PCB_STATUS.md) and [source-bound evidence](review/rear-edge-20261009/README.md). Exact-part fit, final mechanical CAD, bench validation and factory process acceptance remain held. Original firmware scripts are preserved; [carrier_prototype.py](../Pico_Synth/carrier_prototype.py) is the current provisional carrier implementation. Its host logic tests pass; hardware qualification is still required.

## Working configuration

- Two-layer carrier board with a removable original non-wireless RP2040 Pico H SC0917, plugged into two Samtec SSQ-120-01-G-S 1x20 female socket headers at 2.54 mm pitch and 17.78 mm row spacing. The factory solders the sockets and fits the supplied-header Pico for programming/testing. Confirm actual engagement, socket/body height, USB/BOOTSEL access and upward removal before release. Removal/insertion is done with power disconnected; agree installed or separately packed shipping condition rather than assuming user assembly.
- Eight note touch controls and two left-hand modifier touch controls. User permits firmware changes, including adapting input polarity after actual modules are checked. Retain original behavior as the provisional baseline; reprogramming is available for later changes.
- Two SunFounder ST0238 passive low-level-trigger buzzer modules selected by the user for the first prototype. Manufacturer PCB outline: 32 x 14 mm each; see [buzzer module evidence](components/BUZZER_MODULE.md). The first prototype preserves both buzzers at the same pitch; the held left modifiers add a semitone/octave. Independent voices are a future firmware/pin allocation change.
- First revision: removable protected **long 18650** conventional 4.2 V-charge Li-ion cell, charged externally. The user's 2026-10-09 correction supersedes the earlier 18350/P1835C2/Keystone 1101 proposal. Current candidates are **Keeppower P1835J with ordinary opposite-end terminals** and the wired **MPD BH-18650-W** holder; exact lot/terminal identity, cold fit, contact capability and charger compatibility remain unverified. No onboard charger. See [current power handoff](power/18650-handoff.md) and [holder proposal](mechanical/WIRED_HOLDER_PROPOSAL.md).
- Power switch and exposed GPIO expansion headers.
- Separate touch and buzzer modules retained for the first revision. The user supplied a HiLetgo TTP223-BA6 touch reference; see [touch module evidence](components/TOUCH_MODULE.md). Actual header orientation, mounting geometry and output configuration remain unverified. Buzzer model is selected; its connector and mounting geometry still need verification.

## Carrier GPIO allocation (preserved baseline)

| Function | GPIO |
|---|---|
| C4 | GP16 |
| D4 | GP17 |
| E4 | GP18 |
| F4 | GP19 |
| G4 | GP20 |
| A4 | GP21 |
| B4 | GP22 |
| C5 | GP26 |
| Semitone up | GP27 |
| Octave up | GP28 |
| Buzzer outputs, same pitch | GP12, GP13 |
| Free expansion | GP0–GP11, GP14, GP15 |

GPIO numbers are not physical header pin numbers. GP12/GP13 share a PWM frequency; independently pitched buzzers require a different allocation (for example GP12/GP14) and a firmware change.

Expose unused GPIOs with labeled 2.54 mm headers, 3V3 and GND. GP0/GP1 can be reserved as an I2C expansion pair. Used signals may have labeled test points, but are shared with onboard circuitry and are not free GPIOs. J15 has GP0–GP11,GP14,GP15,3V3,GND in that order. Its physical pin1 is GP0. No I2C pull-ups are fitted; add compatible bus hardware for a later peripheral.

J3–J14 use carrier contacts **1 SIG / 2 regulated 3V3 / 3 GND**. The ST0238 module order differs, so its cable must be permuted to the actual I/O, VCC and GND labels. Touch-module output polarity/configuration and module-end contact geometry require delivered-part checks. The unkeyed Harwin carrier plugs need pin1 marks, retention and continuity/polarity inspection; do not assume straight-through wiring. Factory scope includes all twelve adapted harnesses and module attachment. See [module harness specification](assembly/MODULE_HARNESSES.md).

## Power architecture

Protected removable cell -> H1 -> upstream F1 -> S1 -> reverse-blocking TPS259474L U2 -> Pico VSYS. D2 is a VSYS shunt clamp, D3 a bidirectional input TVS; no carrier series diode. See power/branch-protection.md and kicad/power-integration.md for exact parts/pins/limits.
Pico 3V3(OUT) -> touch modules and compatible buzzer modules, subject to total current budget.

C11/C12 remain 100 nF bypasses at J13/J14; C17/C18 add 10 µF each on 3V3_OUT/GND. Their effective capacitance and regulator startup/transient behavior require bench qualification. Limits are 0.70 A normal battery input, 250 mA external 3V3 and 350 mA total 3V3 including Pico; these are design limits, not measured performance. The USB branch bypasses the battery eFuse, so USB supply/inrush/fault qualification remains separate. See [power validation](power/prototype-validation.md).

A conventional 3.7 V nominal cell reaches 4.2 V when fully charged. Do not connect raw battery voltage to 3V3 or GPIO. The Pico regulator supplies the regulated 3.3 V rail. USB/battery isolation must prevent USB from feeding the battery through VSYS.

If USB charging is requested, use a single-cell charger with appropriate power-path management, protection, and charge current matched to the selected battery. A Pico USB port does not charge a cell by itself. If removable external charging is selected, retain source isolation for safe USB programming with the battery installed.

The selected power architecture remains conditional on actual protected-cell/holder fit, contact and harness ampacity, polarity, effective capacitance and measured load/fault behavior. Nominal bare-cell dimensions do not prove protected-cell fit. The MPD holder has factory AWG24 leads; qualify their actual insulation OD and JST-PH crimp compatibility, strain relief and installed length rather than adding solder-lug wiring by assumption.

External charger compatibility remains **HOLD**. Keeppower L1 is an evaluation target only: its published 4.2 V ±1% range reaches 4.242 V, above the current P1835J page's unqualified 4.20 V maximum. No approved cell/charger pair is established. Resolve current-lot CC/CV voltage/current/termination/temperature limits, charger revision/tolerances and usable bay travel before supply or use; selecting 500 mA alone does not resolve that voltage conflict.

Battery runtime requires a measurement of average battery current; do not assume runtime from voltage alone.

## Placement concept

- Front: eight ascending note modules in a row. User requests approximately half-to-one finger of clear space between keys. Start with a proposed 10 mm clear gap between 24 mm module bodies (34 mm center pitch), then validate with a full-size paper fit test. Roughly 330 x 121.5 mm is a working reservation, not an approved outline.
- Left side: semitone and octave modifiers, positioned for the left hand while the right hand plays notes.
- Rear: USB-accessible Pico, buzzer modules, expansion headers and power switch.
- Battery: wired MPD BH-18650-W in a separate insulating **112 × 36 × 44 mm** underside cassette proposal, with holder plane z16 and **≥47 mm underside supports**. H1 is bottom THT, circuit1 positive/circuit2 GND, moved to mechanical (269,20), native (289,40). Four existing cassette mounts remain; holder holes are cassette-only. Exact P1835J/holder fit, contact ampacity, lead bends, replacement access, retention and final platform/door/overhang CAD remain unverified. Require ≥2 mm actual loaded clearance to bottom parts, solder tails and wires, including tolerances and deflection; keep playing load off the cell/holder. The inherited B.Cu restriction is explicitly partial, not a full enlarged-cassette copper keepout.
- Seventeen 3.2 mm NPTH carrier holes: four corners, four cassette mounts, nine raised module-fixture mounts. These independent interfaces avoid undocumented module/holder hole positions. The raised acetal fixture uses proposed 24 mm spacers, a 28 mm support plane and 24 measured-thickness edge keepers; final fit/CAD/tolerances remain pending.

The accompanying SVG is an arrangement sketch, not a scaled PCB drawing or a copper layout.

## Needed before fabrication release

1. Actual Pico H/socket engagement, rear lip and USB/BOOTSEL/removal fit; actual touch/buzzer headers, permuted cable polarity, heights and clear support lands. The rear edge is now native y18.5; nominal socket bodies have 1.275 mm rear margin and courtyards 0.77 mm. Actual engagement/lip and factory handling acceptance remain open.
2. Exact opposite-end-terminal protected P1835J/BH-18650-W cold fit/removal, retention, holder/contact/harness ampacity and matched external charger qualification. The L1 voltage-tolerance conflict remains held.
3. Final paper fit/board size and measured fixture/cassette/feet CAD/tolerances, including ≥2 mm loaded internal clearance. The proposed 330 × 121.5 mm board is routed but its human/physical fit is untested.
4. Staged source-isolation, low-voltage/fault/reset/current/thermal and functional validation, including actual touch polarity/momentary mode, reset silence and both same-pitch buzzers. Qualify the first instrument within the five, then record acceptance for all five; battery and USB branches need their respective tests.
5. Actual Gerber/drill/placement viewer review and factory process/quote acceptance: U2 mask/stencil, nominal 0.25 mm socket annular rings, C17/C18 standard 0805 lands versus TDK's example, panel rails/fiducials/tooling and depanel/THT order. The old checked-in manufacturing package is obsolete; fresh raw exports and pipeline checks are not a final accepted package. No total assembly quote or fabrication release exists.

These are recorded in assembly/FIT_CHECKLIST.md and power/prototype-validation.md. PM may continue independent layout/review work while actual-part measurements are pending.

## References

- https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf — selected original Pico H, power/pinout/source isolation and mechanical data.
- https://learn.adafruit.com/li-ion-and-lipoly-batteries/voltages — conventional Li-ion cell voltage behavior.

## Manufacturing and assembly

The requested result is **five complete factory-built instruments**, with an **additional sixth bare carrier** quoted separately as an optional keepsake. Each carrier has 47 purchased parts: 30 top SMT and 17 THT, with only H1 mounted on the bottom. TP1 copper and 17 NPTH mounts are excluded from purchasing. Removable Pico, ten touch boards, two ST0238 modules, twelve adapted harnesses, protected cell, holder/cassette, raised fixture and supports are separate instrument items, not SMT placements. Specify their sourcing, assembly, metrology, programming and per-unit testing in the [five-unit handoff](assembly/PCBWAY_HANDOFF.md). Factory holder lead termination and mechanical installation are included; it is not a direct PCB-mounted holder substitution. No supplier acceptance, upload or order is implied.

PCBWay documents both through-hole assembly and top/bottom/both-side assembly options:
- https://www.pcbway.com/pcb_prototype/Through_Hole_Assembly.html
- https://www.pcbway.com/quotesmt.aspx

## Local Pico references

User supplied official datasheets in `/Users/johnodell/Desktop/pico_datasheets/`: original Pico release 21 and Pico 2 release 5, both build date 03/07/2026. The Pico 2 mechanical Figure 3 was rendered and visually checked against socket geometry. PDFs remain outside the repository; manufacturer source URLs above are the portable references. The PM selected original Pico H SC0917 using the original datasheet ordering table. Pico2 is not the fitted prototype candidate; original Pico geometry was checked separately during carrier integration.

## Assembly preference

Quote five complete instruments, including all small components, THT soldering, 60 complete module harnesses, five holder harnesses/cassettes, module attachment, precision fit work, programming and acceptance testing. Agree removable Pico/cell shipping condition and external charger supply after qualification; normal-use removal/external charging does not make missing factory assembly a user task. Qualify the first instrument within the five before repeating its accepted build on the other four. A partial-assembly price may be compared, with remaining work explicit, but the selected delivery must not depend on user soldering or crimping. Price the optional sixth bare carrier separately. See [assembly and budget comparison](ASSEMBLY_BUDGET.md); complete pricing and supplier process acceptance remain pending.
