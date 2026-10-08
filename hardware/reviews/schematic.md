# Schematic review - provisional carrier P2

Reviewed 2026-10-07 using KiCad CLI 10.0.6. This assignment is complete as a provisional editable carrier schematic, with a readable A3 PDF; the integrated instrument is not ready for fabrication.

## Delivered

Native project and schematic in `hardware/kicad/`, project-local symbols and registered socket footprint library, complete socket mapping CSV, reproducible connectivity check, and `schematic-review.pdf`. There is no placeholder empty PCB or manufacturing export. No firmware changes were made.

## Verified socket mapping

Checked the official Raspberry Pi Pico and Pico 2 datasheets, Figure 2 pin allocation (printed page 4 in both), against every entry in `pico-socket-map.csv`. Both non-wireless models have the same relevant 40-pin header mapping. The exact fitted model remains a user decision.

The two physical 1x20 female sockets are J1 and J2, each with local numbers 1-20, rather than an SMT Pico footprint or a duplicate module with nonexistent carrier pads:

- Top view, USB at top: left socket J1 runs Pico physical 1-20 from top to bottom. J1 pin n maps to Pico physical n.
- Right socket J2 runs Pico physical 40-21 from top to bottom. J2 pin n maps to Pico physical n+20. Its pin 1 is opposite USB, and pin 20 is beside USB.
- The custom symbols show both local socket contact number and Pico physical number/function. A footprint must follow these local pad numbers; rotate the right socket appropriately. The drawing is a connectivity diagram, not a placement drawing.
- All Pico digital grounds (physical 3, 8, 13, 18, 23, 28, 38) and AGND (33) join GND. AGND is joined for digital touch inputs; revisit if analog sensing is introduced.
- Pico 30 RUN, 35 ADC_VREF and 37 3V3_EN are intentionally NC at the carrier; retain the Pico's internal defaults. This does not mean those signals are unconnected inside the Pico.
- GPIO23, 24, 25 and 29 are internal Pico functions, absent from the two socket rows and excluded from expansion.

Official Pico 2 Figure 3 (printed page 7) confirms 2.54 mm contact pitch, 17.78 mm between socket row centers, 48.26 mm between first/last contacts, and a 51 x 21 mm module body. These dimensions establish the socket placement contract, not approval of any selected socket footprint. Selected socket height, male-pin engagement, USB overhang, BOOTSEL access, insertion/removal clearance, battery clearance and carrier mounting remain for mechanical integration. J1/J2 now carry the mechanically reviewed candidate `MakeMusic:Samtec_SSQ-120-01-G-S_1x20_P2.54mm`, registered by `hardware/kicad/fp-lib-table` at `${KIPRJMOD}/../libraries/MakeMusic.pretty`. The merged footprint has 20 pads, 2.54 mm pitch, 48.26 mm span, 1.02 mm drills and 1.52 mm pad diameter per the Samtec recommended layout. It remains a candidate pending male-post/engagement trial, fabricator finished-hole/annular-ring review and enclosure clearance checks. See the [mechanical review](../mechanical/README.md) for source drawings and stack dimensions.

**Placement contract:** J1 pad 1 is at USB; J2 pad 20 is at USB, so rotate the assigned J2 footprint 180 degrees relative to J1. The schematic keeps J2 local n=Pico n+20. This explicitly supersedes the mechanical proposal's alternative convention placing right-row local pad 1 at USB. Do not copy that numbering or rotate both footprints alike. No PCB placement exists yet; actual pad-to-net orientation must be checked at placement and before routing.

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

All J3-J14 use provisional pin 1=signal, 2=3V3_OUT, 3=GND, prominently marked in the schematic. This is an interface assumption, not a claim about actual module pin orders. All module footprints are unassigned. J13/J14 now represent the selected pair of SunFounder ST0238 low-level-trigger driver modules, supplied from 3V3_OUT. Their physical connector numbering/pitch remains provisional. Verify HIGH idle/startup behavior, output silence and current before firmware/load approval; raw two-terminal transducers would need a different driver circuit. See [buzzer evidence](../components/BUZZER_MODULE.md). GP12/13 share PWM frequency; the existing firmware plays both at the same pitch. Independent voices require reassignment and firmware changes.

J15 exposes exactly the fourteen unused GPIOs: contacts 1-12 map to GP0-GP11, contacts 13/14 to GP14/GP15, contact 15 to 3V3_OUT and contact 16 to GND. Header orientation/order/MPN is provisional. GP0/GP1 may serve I2C SDA/SCL; pull-ups are intentionally absent pending actual devices and existing module pull-ups.

## Touch reference received from PM during review

The PM supplied the [HiLetgo product reference](http://www.hiletgo.com/ProductDetail/1915450.html) and user image [`touchbutton.jpg`](../components/reference/touchbutton.jpg) (visually reviewed). The vendor page did not load in this review; PM-reported dimensions/specifications are 24 x 24 x 7.2 mm, four M2 holes, 2-5.5 V supply and 60/220 ms response. Hole centers, header pitch/orientation and exact module configuration remain unverified; keep footprints unassigned. Primary chat owns the fuller component evidence in [`hardware/components/TOUCH_MODULE.md`](../components/TOUCH_MODULE.md), incorporated from merged PR #2 (6a61587).

The [manufacturer TTP223-BA6 datasheet](https://www.tontek.com.tw/uploads/product/243/TTP223-BA6_V2.1_EN.pdf), pages 2-4, confirms 2-5.5 V IC operation and a CMOS output: TOG=0 selects direct mode; AHLB=0 selects active-high, AHLB=1 active-low. The existing firmware assumes direct active-high behavior. The user now permits firmware changes: after confirming actual output mode and idle/touched levels, primary may adapt input handling for direct active-low (TOG=0/AHLB=1), or retain active-high where confirmed. Module modification to active-high is not required. This follow-up does not change firmware. The supplied image appears to tie AHLB to VCC (active-low); this is an inference from the drawing, not verified actual board behavior. Its DI/VCC/GND interface labels do not establish physical contact numbers or orientation. The schematic visibly records the polarity uncertainty and firmware flexibility and continues using regulated 3V3_OUT.

Confirm module supply decoupling and measured latency/current, including indicator LED load. The manufacturer's no-load IC current is not the populated module current. The 220 ms low-power response and startup stabilization may affect musical responsiveness and should be tested on the actual module.

## Revision-1 power circuit integration

Implemented Option A from [`hardware/power/rev1-handoff.md`](../power/rev1-handoff.md), following the user's externally charged protected 18350 choice. The obsolete X1 logical block is removed from the schematic and local symbol library. Native local symbols now represent holder contacts H1, switch S1, Schottky D1 and USB test point TP1. No firmware changes, PCB or routing are included.

| Endpoint | Carrier net / role |
|---|---|
| H1 `+` | BAT_PROT_PLUS: protected assembly's external positive |
| H1 `-` | GND: protected assembly's external negative |
| S1 terminal 2 | BAT_PROT_PLUS, manufacturer common |
| S1 terminal 3 | BAT_SW_PLUS, battery ON throw |
| S1 terminal 1 | Intentional NC, battery OFF throw |
| D1 terminal 2 / A | BAT_SW_PLUS, diode anode |
| D1 terminal 1 / K | VSYS, banded cathode -> J2.19/Pico physical 39 |
| TP1 terminal 1 | VBUS_USB only -> J2.20/Pico physical 40 |

S1 is NKK **MN12SS1W03**, SPDT ON-ON. The manufacturer's Series M drawing, printed page A56, shows common 2 and switched pairs 2-3 and 2-1. The local symbol uses that numbering rather than a generic SPDT convention. Leaving throw 1 open creates battery OFF. Terminal numbers are not printed on the actual switch; orient against the keyway drawing and confirm continuity during assembly. The manufacturer exact-part page confirms this MPN and PC-pin termination, despite the general ordering page's restrictive bushing/termination footnotes; verify the current exact-part drawing/availability before footprint release. Switch footprint remains unset.

D1 is Vishay **SS14-E3/61T**, SMA/DO-214AC. Manufacturer datasheet page 1 identifies the colored band as cathode. **1=K and 2=A are this project's KiCad numbering convention**, not numbers marked by Vishay on the two leads. The visible symbol and exported pin roles preserve K1/A2; the banded end goes to VSYS. No diode land pattern is assigned by this schematic change; verify pads/band orientation against the manufacturer package drawing before footprint release. The 1 A device rating is conditional on datasheet thermal conditions, not a current limiter or verified instrument current budget.

H1 `+`/`-` are explicitly **provisional logical terminal identifiers**, not inferred holder pad numbers or verified contact polarity. No holder MPN/footprint is assigned. The corrected merged [1095P review](../mechanical/HOLDER_1095P.md) explicitly withdraws the earlier footprint after a hole-leader interpretation error and supplies no numeric electrical pad map; no geometry or polarity from that withdrawn candidate is used here. The mechanical helper must provide the actual footprint and contact/polarity evidence, then replace/remap these identifiers and update verification. The diagram assumes only the protected assembly's external terminals; it does not bypass its protection. Exact P1835C2 cell and L1 external charger at 500 mA remain review targets, not approved fit/purchase/charging compatibility selections. Current-lot charge-voltage/current, termination, temperature policy, charger-bay fit and protection recovery gaps stay in the power handoff.

Battery branch is H1+ -> S1 common2 -> ON3 -> D1 anode2 -> cathode1 -> VSYS. VBUS_USB, BAT_PROT_PLUS, BAT_SW_PLUS, VSYS and 3V3_OUT are distinct carrier nets. TP1 is USB-VBUS measurement access only; its footprint is unset and it is not a battery/charger connector. Pico's onboard USB diode feeds VSYS internally and its regulator generates 3V3_OUT at physical 36/J2.16; neither is duplicated on the carrier. S1 OFF isolates the battery branch, but USB can still power the instrument. Disconnect USB and switch OFF before removing/inserting the Pico or cell; remove the cell for external charging. No onboard charger or external charger leads attach to the carrier.

**Fault protection is unresolved.** The protected cell's operating discharge rating does not establish a suitable PCM cutoff for the diode, holder or wiring. Obtain PCM trip/recovery data and coordinate a branch fuse/current limiter with actual holder, switch, wiring, diode and measured inrush before fabrication. No fuse MPN/value, cell polarity protection or cutoff threshold is invented here. Reverse insertion, diode leakage/thermal loss, low-battery headroom, module current and USB/battery hot-plug behavior still need review/measurement. A complete power safety/fit assessment is not claimed.

## Actual validation and limits

- `kicad-cli sch erc --severity-all --exit-code-violations --format json`: exit 0, **0 errors, 0 warnings, 0 excluded violations**. No explicit ERC exclusions or PWR_FLAG symbols. KiCad defaults leave single-global-label, four-way-junction, simulation-model and footprint-filter checks ignored; none establishes component suitability here.
- Exported a fresh KiCad XML netlist and ran `verify_connectivity.py`: **all 100 endpoints match**, including all 40 socket contacts, 36 module contacts, 16 expansion contacts and 8 real power/test contacts. Exactly 32 connected nets plus 4 intentional NC nets (three Pico defaults plus S1 OFF). The check rejects extra/missing connections, wrong GPIOs, changed power/ground assignments and unexpected footprints. Only the exact SSQ candidate assignment is allowed on J1/J2; J3-J15 and H1/S1/D1/TP1 must remain unset. Switch common/throws, diode K/A roles and exact S1/D1 values are also checked. The registered local footprint file must exist.
- Negative checks on temporary XML netlists confirmed the checker rejects a wrong J2 socket footprint, an unexpected J3 module footprint, a changed GP16 net, reversed diode pins, swapped switch common/ON terminals, a battery-to-VBUS bridge and a battery-to-3V3 bridge.
- Visually inspected the final PDF raster: all socket/contact numbers, interface labels, NC crosses, provisional notes and power boundaries are readable without overlaps or clipping.
- KiCad emitted a system Fontconfig cache-version warning during CLI exports; export/ERC succeeded and visual review found no font defects. No cache or system font changes were made.

All carrier contacts are correctly typed passive. The inserted Pico, touch-module electronics, buzzer drivers and protected cell PCM are external/unmodeled; the switch/diode branch itself is now modeled. Consequently ERC cannot verify signal direction, current, voltage tolerance, driver requirements, module pin polarity, supply sourcing or USB/battery isolation. Zero ERC violations certify this carrier connection drawing only. No PCB DRC/netlist-to-board comparison is possible before a PCB exists.

## Unresolved before routing/assembly

1. Exact Pico model and male-header arrangement; confirm SSQ-120-01-G-S candidate sourcing, mating engagement, finished holes, insertion/removal and all access/clearances. Enforce J1 pad1/J2 pad20 at USB during placement.
2. Confirm the exact HiLetgo/TTP223 module configuration and physical pin order. Use confirmed module polarity to select active-high or authorized active-low firmware handling, and verify decoupling, idle behavior, touch latency, cable length and noise behavior.
3. Buzzer module MPN, actual pin count/order, PWM response, voltage/current and onboard driver. If bare piezo/magnetic devices are selected, design drivers with suitable protection rather than direct GPIO drive.
4. Total 3V3_OUT budget: Pico plus ten touch modules, two buzzer drivers and any expansion loads. The Pico 2 datasheet recommends external load below 300 mA; actual available current also depends on VSYS and Pico load. This is not a completed budget.
5. Selected external-charge architecture is implemented electrically; confirm current-lot protected cell/charger compatibility, actual holder polarity/fit, reverse-insertion mitigation, branch fuse/current limit, switch/diode footprints, thermal/headroom, low-battery handling and inrush.
6. Whether both buzzers retain same-pitch behavior; expansion header MPN/order and optional I2C pull-ups.
7. Verified footprints, board/enclosure dimensions, mounting, back-side holder/standoff clearance, final ERC/DRC and integrated power/PCB review.

## Follow-up integration status

Fetched current master containing the merged socket, selected ST0238 buzzer, externally charged protected 18350 and revision-1 power handoff PRs. Preserved every existing socket/GPIO assignment and Pico NC. The checker replaces X1's three endpoints with eight real power/test contacts, for 100 total. Only J1/J2 carry the existing candidate socket footprints. Physical power-part footprints and holder terminal numbering remain gates; no empty PCB, copper routing or firmware edits are included.

## Primary sources

- [Raspberry Pi Pico datasheet](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf): Figure 2 header allocation, sections 2.1 and 4.4-4.6 for special pins/power. Downloaded and visually checked locally because browser extraction exceeded its size limit.
- [Raspberry Pi Pico 2 datasheet](https://datasheets.raspberrypi.com/pico/pico-2-datasheet.pdf): Figures 2-4; sections 3.1, 5.4-5.6 for pin functions, regulator output and USB/battery power. Figure 3 establishes the above socket placement dimensions.
- [Samtec recommended PCB layout, revision A, Figure 1](https://suddendocs.samtec.com/prints/ssq-1xx-xx-xx-x-xx-xxx-xx-xx.pdf): 2.54 mm pitch, 1.02 mm holes, 1.52 mm pad diameter; inherited body/courtyard evidence is recorded in the mechanical review.
- [NKK Series M drawing](https://www.nkkswitches.com/pdf/MN_ToggleSections_DP.pdf), printed page A56: common2, ON-ON terminal pairs2-3/2-1, keyway orientation and unmarked physical terminals; [exact MN12SS1W03 page](https://www.nkkswitches.com/wp-content/themes/impress-blank/search/inc/part.php?part_no=MN12SS1W03): MPN, SPDT/ON-ON, PC-pin termination and 4 A/30 VDC resistive rating.
- [Vishay SS12-SS16 datasheet](https://www.vishay.com/docs/88746/ss12.pdf), page 1: SMA package, cathode band and SS14 ratings. Detailed load/thermal and leakage review is still required.
- Repository firmware: `Pico_Synth/octave_half_8_key.py`; project requirements: `hardware/PCB_DESIGN_NOTES.md`.

Primary chat should review and integrate this PR with the power and mechanical helpers, then rerun checks after any pinout/part changes. Leave merge and manufacturing approval to primary integration.
