# Make Music — first-prototype design requirements

Updated 2026-10-08. The native two-sheet schematic and routed carrier pass ERC/DRC/parity. Fabrication remains on hold for exact-part fit, final mechanical CAD, bench validation and factory process acceptance. The original firmware is preserved; carrier_prototype.py is a separate tested logic implementation. See kicad/PCB_STATUS.md for actual checks and assembly/FIT_CHECKLIST.md for precise remaining measurements.

## Working configuration

- Two-layer carrier board with a removable original non-wireless RP2040 Pico H SC0917 (selected prototype candidate), plugged into two 1x20 female socket headers at 2.54 mm pitch. The sockets are soldered to the carrier PCB; the Pico has matching male header pins and can be inserted or removed without soldering. Use a Pico supplied with male headers, or fit male headers once to a bare Pico. Confirm socket row spacing, height, pin engagement and USB/BOOTSEL clearance against the selected Pico mechanical drawing before finalizing the footprint. Removal/insertion is done with power disconnected.
- Eight note touch controls and two left-hand modifier touch controls. User permits firmware changes, including adapting input polarity after actual modules are checked. Retain original behavior as the provisional baseline; reprogramming is available for later changes.
- Two SunFounder ST0238 passive low-level-trigger buzzer modules selected by the user for the first prototype. Manufacturer PCB outline: 32 x 14 mm each; see [buzzer module evidence](components/BUZZER_MODULE.md). The first prototype preserves both buzzers at the same pitch; the held left modifiers add a semitone/octave. Independent voices are a future firmware/pin allocation change.
- First revision: removable protected 18350 Li-ion cell, charged in an external charger. User selected this simpler battery architecture on 2026-10-07. Exact cell, matching underside holder and charger remain to be verified; no onboard charger in this revision.
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

## Power architecture

Protected removable cell -> H1 -> upstream F1 -> S1 -> reverse-blocking TPS259474L U2 -> Pico VSYS. D2 is a VSYS shunt clamp, D3 a bidirectional input TVS; no carrier series diode. See power/branch-protection.md and kicad/power-integration.md for exact parts/pins/limits.
Pico 3V3(OUT) -> touch modules and compatible buzzer modules, subject to total current budget.

A conventional 3.7 V nominal cell reaches 4.2 V when fully charged. Do not connect raw battery voltage to 3V3 or GPIO. The Pico regulator supplies the regulated 3.3 V rail. USB/battery isolation must prevent USB from feeding the battery through VSYS.

If USB charging is requested, use a single-cell charger with appropriate power-path management, protection, and charge current matched to the selected battery. A Pico USB port does not charge a cell by itself. If removable external charging is selected, retain source isolation for safe USB programming with the battery installed.

Cell/holder dimensions, connector polarity, protection, regulator load budget, and charging method must be confirmed before selecting footprints. An 18350 holder must fit the actual cell, including any extra length from protection circuitry.

Battery runtime requires a measurement of average battery current; do not assume runtime from voltage alone.

## Placement concept

- Front: eight ascending note modules in a row. User requests approximately half-to-one finger of clear space between keys. Start with a proposed 10 mm clear gap between 24 mm module bodies (34 mm center pitch), then validate with a full-size paper fit test. Roughly 330 x 120 mm is a working reservation, not an approved outline.
- Left side: semitone and octave modifiers, positioned for the left hand while the right hand plays notes.
- Rear: USB-accessible Pico, buzzer modules, expansion headers and power switch.
- Battery: wired Keystone1101 solder-lug holder in a separate insulating underside cassette, connected by H1 JST PH. The cassette has independent carrier mounts; no holder-specific holes on this PCB. Protected P1835C2/1101 fit and contact ampacity remain unverified. Proposed >=35 mm underside supports keep playing force off the cell/cassette.
- Seventeen3.2 mm NPTH carrier holes: four corners, four cassette mounts, nine raised module-fixture mounts. These independent interfaces avoid undocumented module/holder hole positions. The raised acetal fixture uses proposed24 mm spacers, a28 mm support plane and24 measured-thickness edge keepers; final fit/CAD/tolerances remain pending.

The accompanying SVG is an arrangement sketch, not a scaled PCB drawing or a copper layout.

## Needed before fabrication release

1. Actual Pico H/socket engagement and USB/BOOTSEL/removal fit; actual touch/buzzer headers, heights and clear support lands.
2. Exact protected P1835C2/1101 fit, contact ampacity and matched external charger qualification.
3. Final paper fit/board size and measured fixture/cassette/feet CAD/tolerances. The proposed330 ×120 mm board is routed but its human/physical fit is untested.
4. Staged source-isolation, low-voltage/fault/current/thermal and functional validation, followed by factory process/quote acceptance. No total assembly quote exists.

These are recorded in assembly/FIT_CHECKLIST.md and power/prototype-validation.md. PM may continue independent layout/review work while actual-part measurements are pending.

## References

- https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf — selected original Pico H, power/pinout/source isolation and mechanical data.
- https://learn.adafruit.com/li-ion-and-lipoly-batteries/voltages — conventional Li-ion cell voltage behavior.

## Manufacturing and assembly

Bare PCB fabrication supplies the board without components. A separate PCB assembly order can include a back-mounted battery holder if the chosen service accepts that part, bottom-side placement, and its through-hole or surface-mount mounting method. Include the exact holder part number in the BOM and clearly specify its side and orientation in assembly documentation. Confirm part sourcing and assembly support before ordering. The battery cell is a separate item unless explicitly included by the supplier.

PCBWay documents both through-hole assembly and top/bottom/both-side assembly options:
- https://www.pcbway.com/pcb_prototype/Through_Hole_Assembly.html
- https://www.pcbway.com/quotesmt.aspx

## Local Pico references

User supplied official datasheets in `/Users/johnodell/Desktop/pico_datasheets/`: original Pico release 21 and Pico 2 release 5, both build date 03/07/2026. The Pico 2 mechanical Figure 3 was rendered and visually checked against socket geometry. PDFs remain outside the repository; manufacturer source URLs above are the portable references. The PM selected original Pico H SC0917 using the original datasheet ordering table. Pico2 is not the fitted prototype candidate; original Pico geometry was checked separately during carrier integration.

## Assembly preference

Prioritize a quote for a factory-populated carrier, including sockets, headers, power components, and battery holder where accepted. Separately quote the named touch/buzzer modules as supplied/sourced subassemblies. Keep Pico insertion and protected 18350 fitting as user steps. See [assembly and budget comparison](ASSEMBLY_BUDGET.md). Build quantity remains pending user input.
