# Schematic review - provisional carrier P3

Reviewed 2026-10-08 using KiCad CLI 10.0.6. This assignment is complete as a provisional editable carrier schematic, with a readable A3 PDF; the integrated instrument is not ready for fabrication.

## Delivered

Native project/schematic, local symbols and socket/carrier footprint libraries, physical socket CSV, reproducible connectivity check, and readable A3 `schematic-review.pdf`. P3 adds carrier cable/expansion header footprints, a physical JST battery harness connector, switch/diode candidate footprints, two buzzer reset pull-ups and twelve header bypass capacitors. The existing PM PCB draft and project settings are preserved; PM must update PCB from this schematic before further placement/DRC. No manufacturing export or firmware edits are included in this PR.

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

P3 preserves the existing Option A switch/diode path from [rev1-handoff.md](../power/rev1-handoff.md). H1 now represents physical JST B2B-PH-K-S(LF)(SN), matching the PM-approved off-board wired 1101 cassette proposal, rather than logical holder '+'/'-' contacts. Circuit 1=BAT_PROT_PLUS, circuit 2=GND; the connector convention is ours, not a universal JST battery polarity. The installed native Connector_JST footprint was checked against the JST mounting-surface view and circuit 1 mark. PM places it with KiCad Flip on the underside, outside the cassette with plug/wire/service clearance. No direct holder holes or inferred cell-fit approval are introduced. The holder harness is a separately factory-assembled/tested subassembly; exact cell/holder cold fit remains pending.

| Endpoint | Carrier net / role |
|---|---|
| H1 circuit 1 | BAT_PROT_PLUS: protected assembly external positive |
| H1 circuit 2 | GND: protected assembly external negative |
| S1 terminal 2 | BAT_PROT_PLUS, manufacturer common |
| S1 terminal 3 | BAT_SW_PLUS, battery ON throw |
| S1 terminal 1 | Intentional NC, battery OFF throw |
| D1 terminal 2/A | BAT_SW_PLUS, diode anode |
| D1 terminal 1/K | VSYS, banded cathode -> J2.19/Pico physical 39 |
| TP1 terminal 1 | VBUS_USB only -> J2.20/Pico physical 40 |

S1 is NKK MN12SS1W03, with a local straight PC03 terminal-pattern candidate: common 2, ON 3, OFF 1. D1 is SS14-E3/61T with local manufacturer-land-based SMA candidate: banded K1 to VSYS, A2 to battery switch. JST H1 and Yageo resistors use installed KiCad 10 libraries. All other newly assigned carrier footprints are project-local. See [dimensional evidence/release limits](../kicad/carrier-interfaces.md) for exact coordinates, source pages and distinction between manufacturer dimensions and engineering pad/courtyard choices. NKK exact 03 case/bushing/lever fit remains open; the case outline is explicitly a reference.

VBUS_USB, BAT_PROT_PLUS, BAT_SW_PLUS, VSYS and 3V3_OUT remain distinct. TP1 footprint is still unset and is only VBUS measurement access. Pico's USB diode and regulator remain external and unmodeled. Battery OFF still permits USB operation; remove the cell for external charging, with no onboard charger. No withdrawn 1095P footprint or electrical pad interpretation is used.

**Branch fault protection remains unresolved in P3.** The PM has requested a subsequent integration from the power helper's incoming verified eFuse/fuse contract; that replacement is deliberately outside this focused connector/bias PR. Protected-cell PCM/recovery thresholds, reverse insertion, thermal/headroom/load/inrush and actual protected-cell/1101 fit still require evidence/testing. P1835C2 and L1 at 500 mA remain review targets rather than approved purchase/fit/charging selections.

## Actual validation and limits

- KiCad CLI 10.0.6 ERC with `--severity-all --exit-code-violations --format json`: exit 0, **0 errors, 0 warnings, 0 excluded violations**. No explicit ERC exclusions or PWR_FLAG symbols. Ordinary ignored/default rule categories do not establish component suitability.
- Fresh native XML export passes `verify_connectivity.py`: **128 endpoints**, comprising 40 socket,36 cable-header,16 expansion,8 power/test and28 resistor/capacitor contacts. Exactly 32 connected nets plus 4 intentional NC records. Every original GPIO/socket/ground/NC assignment is preserved. Checks include diode K1/A2, switch common/throws, H1 circuits/polarity, GP13/12 bias, all 12 caps, exact carrier-header/R/C/H1 MPNs/values/associations and assigned footprint files/pad numbers. TP1 stays unset.
- Negative temporary-netlist checks reject reversed H1 polarity, a pull-up on the wrong GPIO, a capacitor on battery voltage, wrong reset resistance, missing bypass, reversed diode roles, a battery-to-VBUS bridge and an incorrect assigned footprint. Generated netlists/logs remain outside the repository.
- The updated A3 PDF raster was visually inspected: socket numbers, header roles, physical H1 contact numbers, switch/diode polarity, reset bias, cap rails and provisional notes are readable without overlap/clipping. Manufacturer source diagrams and exported footprint previews were visually inspected as documented in the carrier contract.
- This PR leaves `make_music.kicad_pcb`, `PCB_STATUS.md` and `make_music.kicad_pro` unchanged. No PCB DRC or netlist-to-board agreement is claimed for this newer schematic; PM must update the existing PCB and run those checks.

All carrier contacts/passives have passive electrical pin types. Pico sourcing/regulation, module drivers/output configuration and cell PCM are external and unmodeled. ERC cannot determine voltage/current compatibility, load budget, startup behavior, cable polarity or protection coordination. Passing ERC verifies this connection drawing only.

## Remaining integration gates

1. Confirm exact Pico/male headers, socket engagement, finished holes and USB/BOOTSEL/insertion clearances; preserve J1 pad 1/J2 pad 20 at USB.
2. Verify actual touch revision/polarity/direct mode, physical label-to-cable mapping, response latency/current, cable noise and far-end bypass; PM owns firmware adaptation.
3. Verify delivered ST0238 revision, mapped cable, HIGH idle/reset silence, PWM response/current and module mounting geometry. Select mating female Harwin cable parts and cable length/strain relief; avoid reversed/unkeyed connections.
4. Complete measured 3V3 load/inrush budget including Pico, ten touch modules, two drivers, added bias and expansion. Pico 2 guidance recommends external load below 300 mA; available current also depends on VSYS/Pico consumption.
5. Integrate the verified branch-protection replacement; validate reverse insertion, cell/charger compatibility, actual 1101 fit, harness continuity/polarity, switch exact case/panel fit, thermal/headroom and low-battery/hot-plug behavior.
6. Update PM PCB from schematic, place local bypass/reset parts and underside H1, finish TP1, actual module/holder clearances, routing, final ERC/DRC and visual/mechanical review. No fabrication release yet.

## Primary sources

- [Raspberry Pi Pico datasheet](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf): Figure 2 header allocation, sections 2.1 and 4.4-4.6 for special pins/power. Downloaded and visually checked locally because browser extraction exceeded its size limit.
- [Raspberry Pi Pico 2 datasheet](https://datasheets.raspberrypi.com/pico/pico-2-datasheet.pdf): Figures 2-4; sections 3.1, 5.4-5.6 for pin functions, regulator output and USB/battery power. Figure 3 establishes the above socket placement dimensions.
- [Samtec recommended PCB layout, revision A, Figure 1](https://suddendocs.samtec.com/prints/ssq-1xx-xx-xx-x-xx-xxx-xx-xx.pdf): 2.54 mm pitch, 1.02 mm holes, 1.52 mm pad diameter; inherited body/courtyard evidence is recorded in the mechanical review.
- [NKK Series M drawing](https://www.nkkswitches.com/pdf/MN_ToggleSections_DP.pdf), printed page A56: common 2, ON-ON terminal pairs2-3/2-1, keyway orientation and unmarked physical terminals; [exact MN12SS1W03 page](https://www.nkkswitches.com/wp-content/themes/impress-blank/search/inc/part.php?part_no=MN12SS1W03): MPN, SPDT/ON-ON, PC-pin termination and 4 A/30 VDC resistive rating.
- [Vishay SS12-SS16 datasheet](https://www.vishay.com/docs/88746/ss12.pdf), page 1: SMA package, cathode band and SS14 ratings. Detailed load/thermal and leakage review is still required.
- [Carrier footprint/component/cable source register](../kicad/carrier-interfaces.md): Harwin, JST, ST0238, Yageo and KEMET primary sources and exact dimensional evidence.
- Repository firmware: `Pico_Synth/octave_half_8_key.py`; project requirements: `hardware/PCB_DESIGN_NOTES.md`.

Primary chat should review and integrate this PR with the power and mechanical helpers, then rerun checks after any pinout/part changes. Leave merge and manufacturing approval to primary integration.
