# Schematic review - prototype carrier P4

Reviewed 2026-10-08 using KiCad CLI 10.0.6. This assignment is complete as a provisional editable carrier schematic, with a readable two-page A3 PDF; the integrated instrument is not ready for fabrication.

## Delivered

Native root/child schematics, local symbols and socket/carrier/power footprint libraries, physical socket CSV, reproducible connectivity checker and two-page A3 `schematic-review.pdf`. P4 implements the merged power contract: upstream fuse, TPS259474L protection, divider/current/turn-on parts, ceramic bypass and shunt clamps. It removes carrier series D1, adds TP1's 2mm test pad, and preserves every instrument/expansion/reset-bias/header-bypass assignment. Pico H SC0917 is the selected prototype module. All 46 physical components have assigned native footprints. The PM must update PCB from this root schematic; PCB/project settings and firmware are unchanged. No manufacturing exports are included.

## Verified socket mapping

Checked the official Raspberry Pi Pico and Pico 2 datasheets, Figure 2 pin allocation (printed page 4 in both), against every entry in `pico-socket-map.csv`. Both non-wireless models have the same relevant 40-pin header mapping. The PM selected original non-wireless RP2040 Pico H SC0917 with manufacturer-fitted male headers as the default prototype. The original Pico datasheet ordering table confirms SC0917. Model selection is resolved; actual socket engagement still needs cold-fit verification.

The two physical 1x20 female sockets are J1 and J2, each with local numbers 1-20, rather than an SMT Pico footprint or a duplicate module with nonexistent carrier pads:

- Top view, USB at top: left socket J1 runs Pico physical 1-20 from top to bottom. J1 pin n maps to Pico physical n.
- Right socket J2 runs Pico physical 40-21 from top to bottom. J2 pin n maps to Pico physical n+20. Its pin 1 is opposite USB, and pin 20 is beside USB.
- The custom symbols show both local socket contact number and Pico physical number/function. A footprint must follow these local pad numbers; rotate the right socket appropriately. The drawing is a connectivity diagram, not a placement drawing.
- All Pico digital grounds (physical 3, 8, 13, 18, 23, 28, 38) and AGND (33) join GND. AGND is joined for digital touch inputs; revisit if analog sensing is introduced.
- Pico 30 RUN, 35 ADC_VREF and 37 3V3_EN are intentionally NC at the carrier; retain the Pico's internal defaults. This does not mean those signals are unconnected inside the Pico.
- GPIO23, 24, 25 and 29 are internal Pico functions, absent from the two socket rows and excluded from expansion.

Official Pico 2 Figure 3 (printed page 7) confirms 2.54 mm contact pitch, 17.78 mm between socket row centers, 48.26 mm between first/last contacts, and a 51 x 21 mm module body. These dimensions establish the socket placement contract, not approval of any selected socket footprint. Selected socket height, male-pin engagement, USB overhang, BOOTSEL access, insertion/removal clearance, battery clearance and carrier mounting remain for mechanical integration. J1/J2 now carry the mechanically reviewed candidate `MakeMusic:Samtec_SSQ-120-01-G-S_1x20_P2.54mm`, registered by `hardware/kicad/fp-lib-table` at `${KIPRJMOD}/../libraries/MakeMusic.pretty`. The merged footprint has 20 pads, 2.54 mm pitch, 48.26 mm span, 1.02 mm drills and 1.52 mm pad diameter per the Samtec recommended layout. It remains a candidate pending male-post/engagement trial, fabricator finished-hole/annular-ring review and enclosure clearance checks. See the [mechanical review](../mechanical/README.md) for source drawings and stack dimensions.

**Placement contract:** J1 pad 1 is at USB; J2 pad 20 is at USB, so rotate the assigned J2 footprint 180 degrees relative to J1. The schematic keeps J2 local n=Pico n+20. This explicitly supersedes the mechanical proposal's alternative convention placing right-row local pad 1 at USB. Do not copy that numbering or rotate both footprints alike. The PM has an initial native socket placement draft; this schematic revision leaves it unchanged. Recheck actual pad-to-net orientation during integration and before routing.

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

J3-J14 now have defined **carrier** contact order 1=SIG, 2=3V3_OUT, 3=GND and Harwin M20-9990346 cable-header candidates. They are not direct module mounting footprints. J13/J14 serve the selected SunFounder ST0238 driver modules. The official image labels GND/I/O/VCC top-to-bottom; this differs from the carrier order and needs a mapped cable, not an assumed straight-through connection. See the [carrier parts/cable contract](../kicad/carrier-interfaces.md) for source images and label-to-contact mapping. Actual module revision/polarity, cable details, PWM response and current remain validation gates. GP12/13 retain same-frequency behavior.

J15 exposes contacts1-12=GP0-GP11, 13/14=GP14/GP15, 15=3V3_OUT and16=GND. It now has the defined carrier order and exact Harwin M20-9991646 candidate. GP0/1 may serve I2C SDA/SCL; bus pull-ups remain absent pending actual devices and existing device pull-ups.

R1 is 10k from 3V3_OUT to GP13; R2 is 10k to GP12. Both are exact Yageo RC0603FR-0710KL, 1%, 0603/0.1W. The official ST0238 PNP/1k driver schematic shows no input pull-up, so these provide the PM-requested HIGH reset bias while Pico pins are high impedance. At3.3V the added resistor load is 0.66 mA nominal with both GPIOs LOW, approximately 0.667 mA at 1% minimum resistance. This is not module/base current or a completed supply budget. Firmware must initialize/idle HIGH; delivered hardware startup/silence and PWM still need testing. Bias requires connected signal/supply cables.

C1-C12 are KEMET C0603C104K5RACTU, 100nF±10%, 50 V X7R 0603, across 3V3_OUT/GND. Association C1/J3 through C12/J14 is stored as a hidden Header field and checked. Place each cap by its own carrier header with a short GND return; the grouped drawing is not centralized placement. Carrier-end bypass does not replace adequate module-local bypass across long cables. The local capacitor land pattern follows the manufacturer's level B 0603 recommendation.

## Touch reference received from PM during review

The PM supplied the [HiLetgo product reference](http://www.hiletgo.com/ProductDetail/1915450.html) and user image [`touchbutton.jpg`](../components/reference/touchbutton.jpg) (visually reviewed). The vendor page did not load in this review; PM-reported dimensions/specifications are 24 x 24 x 7.2 mm, four M2 holes, 2-5.5 V supply and 60/220 ms response. Hole centers, header pitch/orientation and exact module configuration remain unverified; keep footprints unassigned. Primary chat owns the fuller component evidence in [`hardware/components/TOUCH_MODULE.md`](../components/TOUCH_MODULE.md), incorporated from merged PR #2 (6a61587).

The [manufacturer TTP223-BA6 datasheet](https://www.tontek.com.tw/uploads/product/243/TTP223-BA6_V2.1_EN.pdf), pages 2-4, confirms 2-5.5 V IC operation and a CMOS output: TOG=0 selects direct mode; AHLB=0 selects active-high, AHLB=1 active-low. The existing firmware assumes direct active-high behavior. The user now permits firmware changes: after confirming actual output mode and idle/touched levels, primary may adapt input handling for direct active-low (TOG=0/AHLB=1), or retain active-high where confirmed. Module modification to active-high is not required. This follow-up does not change firmware. The supplied image appears to tie AHLB to VCC (active-low); this is an inference from the drawing, not verified actual board behavior. Its DI/VCC/GND interface labels do not establish physical contact numbers or orientation. The schematic visibly records the polarity uncertainty and firmware flexibility and continues using regulated 3V3_OUT.

Confirm module supply decoupling and measured latency/current, including indicator LED load. The manufacturer's no-load IC current is not the populated module current. The 220 ms low-power response and startup stabilization may affect musical responsiveness and should be tested on the actual module.

## Power and footprint integration

P4 implements [branch-protection.md](../power/branch-protection.md) and all41 CSV endpoints on the native `battery_power.kicad_sch` child sheet. H1 remains the physical JST B2B-PH-K-S(LF)(SN) for the off-board wired1101 cassette. Circuit1=BAT_PROT_PLUS, circuit2=GND is the project's convention. Place H1 underneath using KiCad Flip, outside the cassette with plug/wire/service clearance. The factory-assembled harness and protected-cell fit still need continuity/polarity/cold-fit inspection; no holder holes are added.

| Endpoint | Carrier net / role |
|---|---|
| H1.1 /F1.1 | BAT_PROT_PLUS, protected external positive |
| F1.2 /S1.2 common | BAT_FUSED_PLUS |
| S1.3 /U2.5 IN | BAT_SW_PLUS |
| S1.1 | NC, battery OFF throw |
| U2.6 OUT /D2.1 K | VSYS -> J2.19/Pico39 |
| U2.8 /D2.2 A /H1.2 | GND |
| D3.1 /D3.2 | BAT_SW_PLUS /GND, bidirectional SMAJ5.0CA |
| U2.4 PGTH | GND |
| U2.3 PG /U2.10 ITIMER | Explicit NC |
| TP1.1 | VBUS_USB only -> J2.20/Pico40 |

Power-document R1–R6 map to native R3–R8; power C1–C4 map to C13–C16. Existing buzzer R1/R2 and header C1–C12 retain their values/nets. The removed power-document polymer C5/C6 are not the native C5/C6 header capacitors. Carrier series D1 is deleted; D2 now uses the reviewed SS14 footprint as a shunt clamp. U2 has10 pins, including power lands5/6, and no pad11. [Native power integration](../kicad/power-integration.md) records every value/MPN/connection, actual TI L-shaped copper/anchor/centroid interpretation, stencil example, manufacturer fuse/TVS pattern and registered footprints. S1 retains the reviewed NKK straight PC03 terminal candidate; exact case/panel fit remains open. TP1 uses TestPoint_Pad_D2.0mm and is excluded from BOM.

Only VSYS/GND cross hierarchical ports; branch control/input nets are private under `/Battery protection/`. H1/S1 retain their symbol UUIDs but acquire the new child path. Check the PM PCB update for relocated hierarchy matches and removal of old D1. The checker strips the hierarchy prefix for contract comparison and rejects disjoint nets sharing a contract basename.

The selected circuit provides hardware UVLO and latched overload disconnect. Adopted limits are ≤0.70A battery branch, ≤350mA total3V3 including Pico, ≤250mA external3V3, ≤100µF totalVSYS capacitance including Pico, ambient0–40°C and resistor local temperature≤70°C. Nominal UVLO is3.221V disconnect/3.546V restart at U2 IN and nominal breaker threshold1.004A; published extrema/coordination remain in the power review. Output ceramics must provide >1µF effective. F1 is upstream backup and USB supply bypasses the battery eFuse. Stop playing before a source change; reboot is acceptable, then let the instrument restart/settle. Battery OFF permits USB operation; remove the cell for external charging. Assembly-specific fault response, PCM/recovery, reverse input, thermal/headroom/load/inrush and actual protected-cell/1101 fit remain bench gates. P1835C2 and L1 at500mA remain review targets.

## Actual validation and limits

- KiCad CLI10.0.6 root ERC, `--severity-all --exit-code-violations --format json`: exit0, **0 errors, 0 warnings, 0 excluded violations** across both sheets. Two nonphysical PWR_FLAG symbols declare external switched-battery power and ground; there are no explicit ERC exclusions.
- Fresh native XML passes `verify_connectivity.py`: **162 physical endpoints /46 components /38 connected nets /6 intentional NC nets**. All41 mapped power endpoints, U2 pin roles/electrical types, component values/MPNs, every original GPIO/socket/ground/NC/bias/bypass assignment, and all46 footprint files/pad-number sets are checked. Neither carrier D1 nor U2 pad11 is present.
- Eleven temporary negative netlists are rejected for swapped U2 IN/OUT, floating PGTH, extra U2.11, restored carrier D1, incorrect ILM resistance, polymer substitution, reversed DVDT damping endpoints, overwritten buzzer bias, battery-to-VBUS bridge disjoint hierarchical VSYS nets and an incorrect passive U2 power-input type. Generated test inputs/reports remain outside the repository.
- Both final A3 PDF pages were rasterized and visually inspected. Custom RPW copper/paste, UMT-H fuse and bidirectional TVS previews were inspected; TI/fuse drawings and exact coordinate evidence are recorded in the power contract.
- An isolated native PCB fixture with all14 U2/F1/D3 copper pads on distinct nets passes DRC at **0.15mm clearance/minimum:0 violations,0 unconnected items**. It checks the custom pad geometry, not the integrated carrier board. Minimum RPW copper gap is0.20mm; requested0.15mm local rules are required for these pads rather than the general0.25mm default.
- `make_music.kicad_pcb`, `PCB_STATUS.md` and `make_music.kicad_pro` are unchanged. No integrated PCB DRC or schematic-to-board agreement is claimed; PM must synchronize/place/route and run those checks.

U2 uses input/open-collector/power-input/power-output/output pin types from its functions; other carrier contacts/passives remain passive. Pico regulation, module drivers and cell PCM are external and unmodeled. ERC cannot establish voltage/current compatibility, load/inrush, cable polarity, actual protection timing or thermal/fit suitability.

The merged [staged assembly/bench procedure](../power/prototype-validation.md) applies using the native references above. After overload, remove the fault and USB, then keep S1 OFF until IN/enable discharge below the reset thresholds; measure the required OFF dwell. No measured results or immediate-reset promise is added by this schematic.

## Remaining integration gates

1. Cold-fit the selected Pico H SC0917 male headers/socket engagement, finished holes and USB/BOOTSEL/insertion clearances; preserve J1 pad1/J2 pad20 at USB.
2. Verify actual touch revision/polarity/direct mode, physical label-to-cable mapping, response/current, cable noise and far-end bypass; PM owns firmware adaptation.
3. Verify delivered ST0238 revision, mapped cable, HIGH idle/reset silence, PWM response/current and mounting geometry. Select mating female Harwin cable parts and cable length/strain relief.
4. Measure regulated loads/inrush including Pico, ten touch modules, two drivers, bias and expansion against the adopted350mA total/250mA external limits; verify effective ceramics and VSYS capacitance≤100µF.
5. Bench-check 1S overload/short/reverse input with/without USB, UVLO rebound/restart and source changes. Qualify holder≥0.70A normal/≥1.2A continuous, PCM/cell/charger compatibility, actual1101 fit, harness polarity, switch case/panel fit and thermal/headroom. Unfused holder-to-F1 leads need short insulated restrained wiring and cell PCM protection.
6. Update PM PCB from root schematic; remove old D1, inspect hierarchy reference matching, place local bypass/reset/power parts and underside H1/TP1, review ≥2A copper and5mm/35µm F1 approach, and complete routing, ERC/DRC, mask/stencil/assembler and mechanical review before fabrication.

## Primary sources

- [Raspberry Pi Pico datasheet](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf): Figure 2 header allocation, sections 2.1 and 4.4-4.6 for special pins/power. Downloaded and visually checked locally because browser extraction exceeded its size limit.
- [Raspberry Pi Pico 2 datasheet](https://datasheets.raspberrypi.com/pico/pico-2-datasheet.pdf): Figures 2-4; sections 3.1, 5.4-5.6 for pin functions, regulator output and USB/battery power. Figure 3 establishes the above socket placement dimensions.
- [Samtec recommended PCB layout, revision A, Figure 1](https://suddendocs.samtec.com/prints/ssq-1xx-xx-xx-x-xx-xxx-xx-xx.pdf): 2.54 mm pitch, 1.02 mm holes, 1.52 mm pad diameter; inherited body/courtyard evidence is recorded in the mechanical review.
- [NKK Series M drawing](https://www.nkkswitches.com/pdf/MN_ToggleSections_DP.pdf), printed page A56: common 2, ON-ON terminal pairs2-3/2-1, keyway orientation and unmarked physical terminals; [exact MN12SS1W03 page](https://www.nkkswitches.com/wp-content/themes/impress-blank/search/inc/part.php?part_no=MN12SS1W03): MPN, SPDT/ON-ON, PC-pin termination and 4 A/30 VDC resistive rating.
- [Vishay SS12-SS16 datasheet](https://www.vishay.com/docs/88746/ss12.pdf), page 1: SMA package, cathode band and SS14 ratings. Detailed load/thermal and leakage review is still required.
- [Carrier footprint/component/cable source register](../kicad/carrier-interfaces.md): Harwin, JST, ST0238, Yageo and KEMET primary sources and exact dimensional evidence.
- [P4 power part/footprint source register](../kicad/power-integration.md): TI RPW0010A, SCHURTER UMT-H, Littelfuse SMAJ, TDK capacitors and native reference mapping.
- Repository firmware: `Pico_Synth/octave_half_8_key.py`; project requirements: `hardware/PCB_DESIGN_NOTES.md`.

Primary chat should review and integrate this PR with the power and mechanical helpers, then rerun checks after any pinout/part changes. Leave merge and manufacturing approval to primary integration.
