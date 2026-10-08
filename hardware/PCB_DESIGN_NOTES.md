# Make Music — preliminary PCB plan

Status: concept only; not a fabrication-ready schematic or PCB. No existing source code has been changed.

## Working configuration

- Two-layer carrier board with a removable non-wireless Pico/Pico 2 (model to confirm), plugged into two 1x20 female socket headers at 2.54 mm pitch. The sockets are soldered to the carrier PCB; the Pico has matching male header pins and can be inserted or removed without soldering. Use a Pico supplied with male headers, or fit male headers once to a bare Pico. Confirm socket row spacing, height, pin engagement and USB/BOOTSEL clearance against the selected Pico mechanical drawing before finalizing the footprint. Removal/insertion is done with power disconnected.
- Eight note touch controls and two left-hand modifier touch controls. User permits firmware changes, including adapting input polarity after actual modules are checked. Retain original behavior as the provisional baseline; reprogramming is available for later changes.
- Two SunFounder ST0238 passive low-level-trigger buzzer modules selected by the user for the first prototype. Manufacturer PCB outline: 32 x 14 mm each; see [buzzer module evidence](components/BUZZER_MODULE.md). Existing firmware drives both at the same pitch; independent pitch operation remains an open choice.
- Single-cell conventional 4.2 V-charge Li-ion/LiPo battery, protected cell or board-level protection.
- Power switch and exposed GPIO expansion headers.
- Separate touch and buzzer modules retained for the first revision. The user supplied a HiLetgo TTP223-BA6 touch reference; see [touch module evidence](components/TOUCH_MODULE.md). Actual header orientation, mounting geometry and output configuration remain unverified. Buzzer model is selected; its connector and mounting geometry still need verification.

## Proposed GPIO allocation (existing firmware)

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

Expose unused GPIOs with labeled 2.54 mm headers, 3V3 and GND. GP0/GP1 can be reserved as an I2C expansion pair. Used signals may have labeled test points, but are shared with onboard circuitry and are not free GPIOs. Header orientation and pin order are not yet finalized.

## Power architecture

Battery -> protection -> power switch -> USB/battery source isolation -> Pico VSYS.
Pico 3V3(OUT) -> touch modules and compatible buzzer modules, subject to total current budget.

A conventional 3.7 V nominal cell reaches 4.2 V when fully charged. Do not connect raw battery voltage to 3V3 or GPIO. The Pico regulator supplies the regulated 3.3 V rail. USB/battery isolation must prevent USB from feeding the battery through VSYS.

If USB charging is requested, use a single-cell charger with appropriate power-path management, protection, and charge current matched to the selected battery. A Pico USB port does not charge a cell by itself. If removable external charging is selected, retain source isolation for safe USB programming with the battery installed.

Cell/holder dimensions, connector polarity, protection, regulator load budget, and charging method must be confirmed before selecting footprints. An 18350 holder must fit the actual cell, including any extra length from protection circuitry.

Battery runtime requires a measurement of average battery current; do not assume runtime from voltage alone.

## Placement concept

- Front: eight ascending note modules in a row. User requests approximately half-to-one finger of clear space between keys. Start with a proposed 10 mm clear gap between 24 mm module bodies (34 mm center pitch), then validate with a full-size paper fit test. Roughly 330 x 120 mm is a working reservation, not an approved outline.
- Left side: semitone and octave modifiers, positioned for the left hand while the right hand plays notes.
- Rear: USB-accessible Pico, buzzer modules, expansion headers and power switch.
- Battery: plan a back/underside-mounted PCB holder if an 18350 is selected. A LiPo pouch instead uses a connector and enclosure restraint. Exact cell, holder footprint, mechanical clearance, and protection remain TBD. Add feet/standoffs so the battery and holder do not bear playing pressure.
- Four mounting holes, with final positions based on module dimensions and enclosure.

The accompanying SVG is an arrangement sketch, not a scaled PCB drawing or a copper layout.

## Needed before schematic and layout

1. Exact Pico version and touch/buzzer module pinouts and measurements.
2. Confirm existing modifier behavior versus independently pitched buzzers.
3. Battery choice, capacity, protection, charging method, and physical dimensions.
4. Final board/enclosure size from a paper fit test; user prefers factory assembly as much as possible, with a budget comparison against partial assembly.

## References

- https://datasheets.raspberrypi.com/pico/pico-2-datasheet.pdf — power, pinout, source isolation, and charging examples.
- https://learn.adafruit.com/li-ion-and-lipoly-batteries/voltages — conventional Li-ion cell voltage behavior.

## Manufacturing and assembly

Bare PCB fabrication supplies the board without components. A separate PCB assembly order can include a back-mounted battery holder if the chosen service accepts that part, bottom-side placement, and its through-hole or surface-mount mounting method. Include the exact holder part number in the BOM and clearly specify its side and orientation in assembly documentation. Confirm part sourcing and assembly support before ordering. The battery cell is a separate item unless explicitly included by the supplier.

PCBWay documents both through-hole assembly and top/bottom/both-side assembly options:
- https://www.pcbway.com/pcb_prototype/Through_Hole_Assembly.html
- https://www.pcbway.com/quotesmt.aspx

## Local Pico references

User supplied official datasheets in `/Users/johnodell/Desktop/pico_datasheets/`: original Pico release 21 and Pico 2 release 5, both build date 03/07/2026. The Pico 2 mechanical Figure 3 was rendered and visually checked against socket geometry. PDFs remain outside the repository; manufacturer source URLs above are the portable references. The presence of both PDFs does not select the fitted Pico model.

## Assembly preference

Prioritize a quote for a factory-populated carrier, including sockets, headers, power components, and battery holder where accepted. Separately quote the named touch/buzzer modules as supplied/sourced subassemblies. Keep Pico insertion and battery fitting as user steps. See [assembly and budget comparison](ASSEMBLY_BUDGET.md). Battery/charging choice and build quantity remain pending user input.
