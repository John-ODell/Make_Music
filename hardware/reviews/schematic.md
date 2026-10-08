# Schematic review - provisional carrier P0

Reviewed 2026-10-07 using KiCad CLI 10.0.6. This assignment is complete as a provisional editable carrier schematic, with a readable A3 PDF; the integrated instrument is not ready for fabrication.

## Delivered

Native project and schematic in `hardware/kicad/`, project-local symbols, complete socket mapping CSV, reproducible connectivity check, and `schematic-review.pdf`. There is no placeholder empty PCB or manufacturing export. No firmware changes were made.

## Verified socket mapping

Checked the official Raspberry Pi Pico and Pico 2 datasheets, Figure 2 pin allocation (printed page 4 in both), against every entry in `pico-socket-map.csv`. Both non-wireless models have the same relevant 40-pin header mapping. The exact fitted model remains a user decision.

The two physical 1x20 female sockets are J1 and J2, each with local numbers 1-20, rather than an SMT Pico footprint or a duplicate module with nonexistent carrier pads:

- Top view, USB at top: left socket J1 runs Pico physical 1-20 from top to bottom. J1 pin n maps to Pico physical n.
- Right socket J2 runs Pico physical 40-21 from top to bottom. J2 pin n maps to Pico physical n+20. Its pin 1 is opposite USB, and pin 20 is beside USB.
- The custom symbols show both local socket contact number and Pico physical number/function. A footprint must follow these local pad numbers; rotate the right socket appropriately. The drawing is a connectivity diagram, not a placement drawing.
- All Pico digital grounds (physical 3, 8, 13, 18, 23, 28, 38) and AGND (33) join GND. AGND is joined for digital touch inputs; revisit if analog sensing is introduced.
- Pico 30 RUN, 35 ADC_VREF and 37 3V3_EN are intentionally NC at the carrier; retain the Pico's internal defaults. This does not mean those signals are unconnected inside the Pico.
- GPIO23, 24, 25 and 29 are internal Pico functions, absent from the two socket rows and excluded from expansion.

Official Pico 2 Figure 3 (printed page 7) confirms 2.54 mm contact pitch, 17.78 mm between socket row centers, 48.26 mm between first/last contacts, and a 51 x 21 mm module body. These dimensions establish the socket placement contract, not approval of any selected socket footprint. Selected socket height, male-pin engagement, USB overhang, BOOTSEL access, insertion/removal clearance, battery clearance and carrier mounting remain for mechanical integration. No socket footprint was assigned without an exact part and drawing review.

## Firmware/interface allocation

Preserved `Pico_Synth/octave_half_8_key.py`. Buzzer numbering follows that file: buzzer1 is GP13, buzzer2 is GP12.

| Interface | Function | GPIO | Pico physical pin | Socket contact |
|---|---|---|---|---|
| J3 | C4 | GP16 | 21 | J2.1 |
| J4 | D4 | GP17 | 22 | J2.2 |
| J5 | E4 | GP18 | 24 | J2.4 |
| J6 | F4 | GP19 | 25 | J2.5 |
| J7 | G4 | GP20 | 26 | J2.6 |
| J8 | A4 | GP21 | 27 | J2.7 |
| J9 | B4 | GP22 | 29 | J2.9 |
| J10 | C5 | GP26 | 31 | J2.11 |
| J11 | Semitone up | GP27 | 32 | J2.12 |
| J12 | Octave up | GP28 | 34 | J2.14 |
| J13 | Buzzer 1 | GP13 | 17 | J1.17 |
| J14 | Buzzer 2 | GP12 | 16 | J1.16 |

All J3-J14 use provisional pin 1=signal, 2=3V3_OUT, 3=GND, prominently marked in the schematic. This is an interface assumption, not a claim about actual module pin orders. All module footprints are unassigned. J13/J14 assume three-pin buzzer driver modules with 3.3 V logic-compatible PWM inputs; raw two-terminal transducers need a reviewed driver circuit instead. GP12/13 share PWM frequency; the existing firmware plays both at the same pitch. Independent voices require reassignment and firmware changes.

J15 exposes exactly the fourteen unused GPIOs: contacts 1-12 map to GP0-GP11, contacts 13/14 to GP14/GP15, contact 15 to 3V3_OUT and contact 16 to GND. Header orientation/order/MPN is provisional. GP0/GP1 may serve I2C SDA/SCL; pull-ups are intentionally absent pending actual devices and existing module pull-ups.

## Touch reference received from PM during review

The PM supplied the [HiLetgo product reference](http://www.hiletgo.com/ProductDetail/1915450.html) and user image [`touchbutton.jpg`](../components/reference/touchbutton.jpg) (visually reviewed). The vendor page did not load in this review; PM-reported dimensions/specifications are 24 x 24 x 7.2 mm, four M2 holes, 2-5.5 V supply and 60/220 ms response. Hole centers, header pitch/orientation and exact module configuration remain unverified; keep footprints unassigned. Primary chat owns the fuller component evidence in [`hardware/components/TOUCH_MODULE.md`](../components/TOUCH_MODULE.md), incorporated from merged PR #2 (6a61587).

The [manufacturer TTP223-BA6 datasheet](https://www.tontek.com.tw/uploads/product/243/TTP223-BA6_V2.1_EN.pdf), pages 2-4, confirms 2-5.5 V IC operation and a CMOS output: TOG=0 selects direct mode; AHLB=0 selects active-high, AHLB=1 active-low. The instrument's existing firmware requires direct active-high behavior, so TOG=0/AHLB=0 must be confirmed or an explicit firmware/configuration change agreed by primary. The supplied image appears to tie AHLB to VCC (active-low); this is an inference from the drawing, not verified actual board behavior. Its DI/VCC/GND interface labels do not establish physical contact numbers or orientation. The schematic now flags this conflict visibly and continues using regulated 3V3_OUT.

Confirm module supply decoupling and measured latency/current, including indicator LED load. The manufacturer's no-load IC current is not the populated module current. The 220 ms low-power response and startup stabilization may affect musical responsiveness and should be tested on the actual module.

## Power handoff

X1 is a logical integration block, excluded from board and BOM, not an assigned physical connector. Pin 1=VSYS, pin 2=GND, pin 3=VBUS_USB. These nets reach Pico physical 39, the ground contacts, and physical 40 respectively. VBUS_USB and VSYS remain distinct on the carrier. The Pico's onboard USB-to-VSYS diode and regulator are inside the removable module, not duplicated on the carrier schematic.

The power helper must provide protected single-cell supply, switching and USB/battery source isolation into VSYS. No cell, charger, current-setting resistor, holder, protection, source-isolation circuit or raw battery connection is implied by X1. The actual allowable supply/current and USB interaction must be checked against the selected Pico and power circuit. 3V3_OUT is supplied by the Pico regulator at physical 36 (J2.16), feeding module and expansion interfaces, never by the raw battery.

## Actual validation and limits

- `kicad-cli sch erc --severity-all --exit-code-violations --format json`: exit 0, **0 errors, 0 warnings, 0 excluded violations**. No explicit ERC exclusions or PWR_FLAG symbols. KiCad defaults leave single-global-label, four-way-junction, simulation-model and footprint-filter checks ignored; none establishes component suitability here.
- Exported a fresh KiCad XML netlist and ran `verify_connectivity.py`: **all 95 endpoints match**, including all 40 socket contacts, 36 module contacts, 16 expansion contacts and 3 logical power contacts. Exactly 30 connected nets plus 3 intentional NC nets. The check rejects extra/missing connections, wrong GPIOs, changed power/ground assignments and unexpected footprints.
- Visually inspected the final PDF raster: all socket/contact numbers, interface labels, NC crosses, provisional notes and power boundaries are readable without overlaps or clipping.
- KiCad emitted a system Fontconfig cache-version warning during CLI exports; export/ERC succeeded and visual review found no font defects. No cache or system font changes were made.

All carrier contacts are correctly typed passive. The inserted Pico, touch-module electronics, buzzer drivers and power circuitry are external/unmodeled. Consequently ERC cannot verify signal direction, current, voltage tolerance, driver requirements, module pin polarity, supply sourcing or USB/battery isolation. Zero ERC violations certify this carrier connection drawing only. No PCB DRC/netlist-to-board comparison is possible before a PCB exists.

## Unresolved before routing/assembly

1. Exact Pico model and male-header arrangement; socket MPN, footprint, orientation and all access/clearances.
2. Confirm the exact HiLetgo/TTP223 module configuration and physical pin order. Resolve the apparent active-low reference versus active-high firmware, and verify decoupling, idle behavior, touch latency, cable length and noise behavior.
3. Buzzer module MPN, actual pin count/order, PWM response, voltage/current and onboard driver. If bare piezo/magnetic devices are selected, design drivers with suitable protection rather than direct GPIO drive.
4. Total 3V3_OUT budget: Pico plus ten touch modules, two buzzer drivers and any expansion loads. The Pico 2 datasheet recommends external load below 300 mA; actual available current also depends on VSYS and Pico load. This is not a completed budget.
5. Protected battery, switch, source isolation, external versus onboard charging, charger power path and battery-matched charge current; actual cell/holder polarity, dimensions and protection.
6. Whether both buzzers retain same-pitch behavior; expansion header MPN/order and optional I2C pull-ups.
7. Verified footprints, board/enclosure dimensions, mounting, back-side holder/standoff clearance, final ERC/DRC and integrated power/PCB review.

## Primary sources

- [Raspberry Pi Pico datasheet](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf): Figure 2 header allocation, sections 2.1 and 4.4-4.6 for special pins/power. Downloaded and visually checked locally because browser extraction exceeded its size limit.
- [Raspberry Pi Pico 2 datasheet](https://datasheets.raspberrypi.com/pico/pico-2-datasheet.pdf): Figures 2-4; sections 3.1, 5.4-5.6 for pin functions, regulator output and USB/battery power. Figure 3 establishes the above socket placement dimensions.
- Repository firmware: `Pico_Synth/octave_half_8_key.py`; project requirements: `hardware/PCB_DESIGN_NOTES.md`.

Primary chat should review and integrate this PR with the power and mechanical helpers, then rerun checks after any pinout/part changes. Leave merge and manufacturing approval to primary integration.
