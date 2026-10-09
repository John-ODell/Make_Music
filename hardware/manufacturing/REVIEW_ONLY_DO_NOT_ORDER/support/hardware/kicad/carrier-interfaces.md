# Carrier connectors, reset bias and bypass contract

Updated 2026-10-09 for C17/C18 and native socket purchasing fields. These are carrier-mounted cable headers and circuit parts. They do not establish touch/buzzer module mounting holes or approve the cell/holder fit. The PM owns placement and updating the existing PCB from this schematic. The user's corrected battery format is 18650; earlier 18350/1101 mechanical references below are historical pending the separate holder review.

P4 preserves the P3 connectors/bias/bypass below and implements the revised [native power integration](power-integration.md). S1 common2 now joins BAT_FUSED_PLUS downstream of F1. The former series D1 is removed; the same SS14 footprint is assigned to shunt D2.

## Parts and assignments

| References | Qty | Exact MPN | Assigned footprint | Function |
|---|---:|---|---|---|
| J1, J2 | 2 | Samtec SSQ-120-01-G-S | MakeMusic:Samtec_SSQ-120-01-G-S_1x20_P2.54mm | Removable Pico sockets; native MPN and Samtec drawing fields |
| J3–J14 | 12 | Harwin M20-9990346 | MakeMusicCarrier:Harwin_M20-9990346_1x3_P2.54mm | Carrier cable header, 1=SIG, 2=3V3_OUT, 3=GND |
| J15 | 1 | Harwin M20-9991646 | MakeMusicCarrier:Harwin_M20-9991646_1x16_P2.54mm | Exposed unused GPIO and regulated supply |
| H1 | 1 | JST B2B-PH-K-S(LF)(SN) | Connector_JST:JST_PH_B2B-PH-K_1x02_P2.00mm_Vertical | Underside battery harness; 1=BAT_PROT_PLUS, 2=GND |
| S1 | 1 | NKK MN12SS1W03 | MakeMusicCarrier:NKK_MN12SS1W03_TerminalPattern_Candidate | SPDT: common2, battery ON3, OFF1 NC |
| D2 | 1 | Vishay SS14-E3/61T | MakeMusicCarrier:Vishay_SS14_SMA_K1_A2 | Shunt clamp: K1=VSYS, A2=GND |
| R1, R2 | 2 | Yageo RC0603FR-0710KL | Resistor_SMD:R_0603_1608Metric | 10k, 1%, 0.1W; R1 GP13/R2 GP12 pull-up to 3V3_OUT |
| C1–C12 | 12 | KEMET C0603C104K5RACTU | MakeMusicCarrier:KEMET_C0603_1608_LevelB | 100nF, 10%, 50V, X7R, 0603; 3V3_OUT to GND |
| C17, C18 | 2 | TDK C2012X7R1A106K125AC | Capacitor_SMD:C_0805_2012Metric | 10µF, 10%, 10V, X7R, 0805; 3V3_OUT to GND at J13/J14 |

J1/J2 retain the reviewed Samtec SSQ-120-01-G-S socket candidates and existing pad numbering for the selected Pico H SC0917. TP1 USB-VBUS measurement access now uses `TestPoint:TestPoint_Pad_D2.0mm`, a bare copper pad excluded from BOM. This table is a circuit assignment, not an orderable complete assembly BOM or manufacturing approval. Standard libraries use `${KICAD10_FOOTPRINT_DIR}`; custom carrier parts are in registered project-local `MakeMusicCarrier.pretty`. Additional power parts are listed in the P4 contract.

## Cable mapping

Carrier numbering is defined independently of module order. Harwin headers are unshrouded and unpolarized; the square pad and silkscreen identify the carrier's chosen pin1. The selected carrier-end mating set is Harwin M20-1060300 with three M20-1180046 contacts per cable, as specified in [MODULE_HARNESSES.md](../assembly/MODULE_HARNESSES.md). Module-end termination remains conditional on measured header pitch, contact size, engagement and actual labels. Verify continuity and orientation with power removed, then verify supply polarity before connecting modules. A three-wire cable need not be straight-through.

| Carrier contact | Touch module destination | ST0238 destination |
|---|---|---|
| J3–J14.1 SIG | Actual board output label DI/OUT, after revision/polarity verification | I/O |
| J3–J14.2 3V3_OUT | Actual VCC label | VCC |
| J3–J14.3 GND | Actual GND label | GND |

The [official ST0238 product](https://www.sunfounder.com/products/3-3-5v-passive-low-level-trigger-buzzer-alarm-sound-module) links the [manufacturer passive-buzzer tutorial](https://docs.sunfounder.com/projects/ultimate-sensor-kit/en/latest/components_basic/26-component_buzzer.html). Its [module image](https://docs.sunfounder.com/projects/ultimate-sensor-kit/en/latest/_images/26_passive_buzzer_module.png), with buzzer left and contacts right, labels the contacts **top to bottom GND, I/O, VCC**. Map carrier SIG to middle I/O, carrier 3V3 to pictured bottom VCC, and carrier GND to pictured top GND. The image does not supply numeric module pin identifiers, pitch or mounting-hole dimensions; verify the delivered revision. No direct ST0238 mounting footprint is assigned.

The HiLetgo touch reference has DI/VCC/GND labels but no verified physical pin order, header orientation or hole centers. No direct touch mounting footprint is assigned. Confirm direct/momentary behavior and actual active-high/low output before using the PM's configurable firmware. Continue supplying these modules from regulated 3V3_OUT, subject to measured load.

J15 carrier order: 1–12=GP0–GP11, 13=GP14, 14=GP15, 15=3V3_OUT, 16=GND. GP0/1 can be I2C; no bus pull-ups are fitted pending attached devices. This is an accessible expansion interface, not a module docking footprint.

H1 follows the PM-approved [wired 1101 underside cassette proposal](../mechanical/WIRED_HOLDER_PROPOSAL.md) (mechanical PR #17, merged): circuit1 red lead to verified holder '+' contact, circuit2 black lead to verified external protected negative. This polarity is the project's convention, not an intrinsic JST battery standard. Matching harness parts are PHR-2 and two SPH-002T-P0.5S contacts with AWG24 stranded wire in the stated insulation range. Factory assembly includes crimping, insulated holder-lug soldering with the cell absent, strain relief and end-to-end polarity/continuity inspection. Verify cavity numbers in mating and wire-entry views; color alone is insufficient. H1 is placed on the underside with KiCad Flip, outside the cassette, with plug/bend/service clearance. PM owns this placement. No holder electrical/mechanical holes are added to the carrier and protected-cell fit remains pending.

## Reset bias and bypass placement

The [official ST0238 circuit](https://docs.sunfounder.com/projects/ultimate-sensor-kit/en/latest/_images/26_passive_buzzer_module_schematic.png) shows a PNP S8550 driver, 1k series base input and buzzer to GND, with no base pull-up shown. R1 and R2 provide the PM-requested HIGH bias on GP13 and GP12 while Pico pins are high impedance. Firmware must initialize/idle both outputs HIGH for low-level triggering. Bias only applies with 3V3, GND and signal cables connected; it does not guarantee silence at an unplugged module or while firmware drives LOW.

At nominal 3.3V, each 10k consumes 0.33mA when its GPIO is LOW, 0.66mA for both; 1% minimum resistance gives at most approximately 0.667mA total at exactly 3.3V. Each resistor dissipates about 1.1mW. These numbers describe the added resistors only, not driver/base current, module current or a verified load budget. Locate R1/R2 near the carrier's buzzer signal connections and confirm HIGH/reset/startup silence and PWM behavior on actual hardware.

C1/J3, C2/J4, C3/J5, C4/J6, C5/J7, C6/J8, C7/J9, C8/J10, C9/J11, C10/J12, C11/J13 and C12/J14. Each capacitor is across the corresponding carrier header's 3V3/GND. Place it physically beside that header with short supply/ground paths; the grouped schematic drawing is not a centralized placement recommendation. These parts bypass the carrier end of each cable. They do not replace adequate module-local bypassing at the far end of a long cable. Cable length/noise and actual module decoupling still need testing.

### Buzzer bulk capacitors — C17/C18

C17 is associated with J13 and C18 with J14 through their hidden Header fields. Each nonpolar capacitor uses pin1=3V3_OUT/pin2=GND; the physical end terminations are interchangeable, and native footprint pads1/2 preserve that circuit convention. They add 20µF nominal on the **regulated 3V3 rail**, retaining C11/C12 100nF in parallel. They are separate from the C13/C14/C16 VSYS/input power-sheet ceramics. The existing 41 branch-protection endpoints are unchanged. PM should place each bulk capacitor beside its buzzer carrier header, with a short supply/ground path, then qualify 3V3 startup/inrush and actual effective capacitance at bias. No measured transient improvement is claimed.

Manufacturer evidence: [TDK exact-part page](https://product.tdk.com/en/search/capacitor/ceramic/mlcc/info?part_no=C2012X7R1A106K125AC) and [characterization sheet](https://product.tdk.com/info/en/documents/chara_sheet/C2012X7R1A106K125AC.pdf). These identify 10µF±10%, 10V X7R and a 2.00±0.20×1.25±0.20mm body, height1.25±0.20mm. The indexed TDK part page gives reflow recommendations PA (inner gap)=0.90–1.20mm, PB (pad length)=0.70–0.90mm and PC (pad width)=0.90–1.20mm. Konnect readback of the assigned KiCad IPC nominal footprint gives pads1.00×1.45mm at x±0.95, inner gap0.90mm, overall span2.90mm, body2.00×1.25mm and courtyard3.40×1.96mm. Body/terminal arrangement and inner gap agree; **pad length and width exceed TDK's recommended reflow ranges**. The explicitly selected standard footprint is retained as an engineering land choice, not claimed to reproduce TDK's recommendation. Assembler acceptance of the larger lands/paste and solder process remains open. Live TDK PDF downloads returned access errors; the manufacturer-indexed part/characterization data was available.

## Footprint evidence and limits

| Part | Verified dimensional basis | Engineering choices / release gates |
|---|---|---|
| Harwin 3/16-way | [M20-999 drawing issue23, 2018-12-17](https://content.harwin.com/asset/640f59f4-1860-40fe-82ef-f2a104ffa7d8/DRG-00479-Technical-Drawing-Datasheet-M20-999-pdf.pdf): 2.54±0.1 pitch, 1.02±0.05 recommended holes, 0.64±0.02 square contacts, 6.1 mating/3.0 tail; nominal 2.54-wide/high insulator, length N×2.54±0.5 | Pads 1.8 diameter (pin1 square); body/courtyard and labels are carrier library choices. Check finished holes, female mating connector, engagement and assembly access. [Exact 3-way](https://www.harwin.com/products/M20-9990346), [16-way](https://www.harwin.com/products/M20-9991646) identity verified. |
| JST H1 | [JST PH datasheet](https://www.jst-mfg.com/product/pdf/eng/ePH.pdf), pp1–3: 2.00±0.05 pitch, reference holes 0.70 +0.10/-0, body 5.9×4.5, height6; circuit1 mark matches installed KiCad pad1 after source-view rotation180 | Installed pads at (0,0)/(2,0), drills0.75, lands1.20×1.75, F.Fab x=-1.95..3.95/y=-1.70..2.80. Copper/courtyard are library choices. JST asks larger holes for glass-fiber board if needed; fabricator finished-hole fit remains a gate. PH rating2A with AWG24 is not branch protection. |
| SS14 D2 | [Vishay 88746](https://www.vishay.com/docs/88746/ss12.pdf), p4 recommended lands: width≥1.52, height≥1.68, gap≤1.88, overall5.28 reference; body maximum4.50×2.79 | Pads1.70×1.80 at x=±1.79 give gap1.88/overall5.28. K1/band left, A2 right. P4 shunt role: K1=VSYS/A2=GND. Body/courtyard allowance and silk are library choices. Copper/stencil/process and clamp-pulse qualification remain. |
| MN12 S1 | [NKK Series M](https://www.nkkswitches.com/pdf/MN_ToggleSections_DP.pdf), printed A60: single-pole straight PC03 terminal pattern, 4.7 pitch, 1.8 holes, terminal1/2/3 orientation; A56 common2 switching | Candidate pads3.2/drill1.8 at 1=(0,+4.7),2=(0,0),3=(0,-4.7). A61's 13×7.9 single-pole case is a reference body, not proof of the exact03 envelope. Verify current [exact MPN](https://www.nkkswitches.com/wp-content/themes/impress-blank/search/inc/part.php?part_no=MN12SS1W03) drawing, keyway, bushing/panel stack and lever travel before fit release. |
| Yageo R1/R2 | [Exact RC0603FR-0710KL specification](https://www.yageogroup.com/component-documentation/download/specsheet/RC0603FR-0710KL): 10k±1%, 0.1W, 0603 body1.6±0.1×0.8±0.1 | Installed KiCad IPC nominal R_0603 footprint: pads0.80×0.95 at x=±0.825, body1.6×0.825. This is a standard library engineering land pattern, not a claimed Yageo recommendation. Qualify the assembler's stencil/reflow process. |
| KEMET C1–C12 | [Exact part specification](https://search.kemet.com/component-documentation/download/specsheet/C0603C104K5RACTU): 100nF±10%, 50V X7R, body1.60±0.15×0.80±0.15. [C1002_X7R, 2026-09-01](https://content.kemet.com/datasheets/KEM_C1002_X7R_SMD.pdf), p12 Table3 levelB 0603: C=.80,Y=.95,X=1.00,V1=3.10,V2=1.50 | Local footprint uses pad centers±.80, pads.95×1.00, courtyard3.10×1.50 exactly from levelB diagram. Nominal body1.60×.80. Check solder process, board flex and local placement; voltage rating alone does not establish bypass effectiveness. |

Manufacturer PDFs/images and installed native footprints were visually inspected. KiCad CLI loaded/exported the assigned footprint candidates; pad-count/number agreement is also checked against each component by `verify_connectivity.py`. No production export or fit/current approval is implied by loading a footprint or passing ERC.
