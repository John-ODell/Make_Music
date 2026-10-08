# Native branch protection integration — P4

Reviewed 2026-10-08 with KiCad 10.0.6. Implements the merged [power contract](../power/branch-protection.md) and its [41 endpoints](../power/branch-endpoints.csv) in `battery_power.kicad_sch`. The main carrier retains all socket, instrument, expansion, R1/R2 and C1–C12 connections. The selected prototype module is the original non-wireless RP2040 **Pico H SC0917**, with manufacturer-fitted male headers. Socket engagement still needs a cold-fit trial.

## Native topology and references

`H1.1 -> F1.1 -> F1.2/BAT_FUSED_PLUS -> S1.2 common -> S1.3/BAT_SW_PLUS -> U2.5 IN -> U2.6 OUT/VSYS -> J2.19/Pico39`. H1.2 joins GND. S1.1 is NC. Carrier series D1 is removed; the Pico's onboard USB diode remains external to this carrier schematic. D2 is a shunt clamp, K1=VSYS/A2=GND. D3 is the bidirectional **CA** TVS across BAT_SW_PLUS/GND.

The native hierarchy is `/Battery protection/`. BAT_PROT_PLUS, BAT_FUSED_PLUS, BAT_SW_PLUS, EN_UVLO, OVLO, ILM, DVDT and DVDT_CAP export with that prefix. VSYS/GND cross genuine hierarchical ports and join the main sheet. TP1 remains VBUS_USB/Pico40 only; no carrier VBUS-to-battery or VBUS-to-VSYS link is added. H1/S1 retain their symbol UUIDs after moving into the child sheet; their hierarchy paths change. Update PCB from the complete root schematic and inspect matching/removal of old series D1.

Power-document references are role labels. The following mapping prevents collisions with the existing carrier parts:

| Power document | Native reference | Value / exact MPN | Endpoint1 / endpoint2 |
|---|---|---|---|
| R1 | R3 | 649k; RC0603FR-07649KL | BAT_SW_PLUS / EN_UVLO |
| R2 | R4 | 332k; RC0603FR-07332KL | EN_UVLO / GND |
| R3 | R5 | 1.05M; RC0603FR-071M05L | BAT_SW_PLUS / OVLO |
| R4 | R6 | 332k; RC0603FR-07332KL | OVLO / GND |
| R5 | R7 | 3.32k; RC0603FR-073K32L | ILM / GND |
| R6 | R8 | 100Ω; RC0603FR-07100RL | DVDT / DVDT_CAP |
| C1 | C13 | 4.7µF/25V X7R; C2012X7R1E475K125AB | BAT_SW_PLUS / GND |
| C2 | C14 | same 4.7µF ceramic | VSYS / GND |
| C3 | C15 | 10nF/50V C0G; C1608C0G1H103J080AA | DVDT_CAP / GND |
| C4 | C16 | same 4.7µF ceramic | VSYS / GND |

The power-document C5/C6 polymer hold-up additions are omitted as directed by the PM. **Native C5/C6 are existing 100nF header bypass parts and remain fitted.** Output additions total 9.4µF nominal; effective output ceramic capacitance must exceed 1µF. All VSYS capacitance, including the Pico, must remain ≤100µF. Source changes may reboot the instrument; stop playing, change source, then let it restart and settle. Seamless transfer is not a requirement.

U2 is TPS259474LRPWR, circuit-breaker/latch-off variant, RPW0010A ten-pin HotRod package. Native electrical pin types reflect the datasheet:

| Pin | Function | Net | KiCad type |
|---:|---|---|---|
| 1 | EN/UVLO | EN_UVLO | input |
| 2 | OVLO | OVLO | input |
| 3 | PG | NC | open collector |
| 4 | PGTH | GND | input |
| 5 | IN | BAT_SW_PLUS | power input |
| 6 | OUT | VSYS | power output |
| 7 | DVDT | DVDT | output |
| 8 | GND | GND | power input |
| 9 | ILM | ILM | output |
| 10 | ITIMER | NC | output |

No ground/exposed pad11 exists. Two virtual PWR_FLAG declarations identify external switched battery power and ground for ERC; they are excluded from BOM/board and are not protection parts. PGTH is tied to ground; PG and ITIMER have explicit NC marks. No GPIO is consumed by protection.

## Assigned parts and libraries

| Native parts | Footprint | Basis |
|---|---|---|
| U2 | MakeMusicPower:TI_RPW0010A_TPS259474_2x2mm | Exact TI RPW0010A copper and example stencil geometry below |
| F1, 3403.0275.23, 1.25A time-lag | MakeMusicPower:Schurter_UMT-H_3403-0275-23 | Manufacturer UMT-H lands below |
| D3, SMAJ5.0CA | MakeMusicPower:Littelfuse_SMAJ5-0CA_DO-214AC | Manufacturer SMAJ pad dimensions below; bidirectional, no cathode mark |
| D2, SS14-E3/61T | MakeMusicCarrier:Vishay_SS14_SMA_K1_A2 | Existing reviewed SMA pattern, now shunt K1=VSYS/A2=GND |
| R3–R8 | Resistor_SMD:R_0603_1608Metric | Standard KiCad engineering lands; exact Yageo 0603 parts |
| C13/C14/C16 | Capacitor_SMD:C_0805_2012Metric | Nonpolar TDK 0805 ceramic; standard KiCad engineering lands |
| C15 | Capacitor_SMD:C_0603_1608Metric | TDK 0603 ceramic; standard KiCad engineering lands |
| TP1 | TestPoint:TestPoint_Pad_D2.0mm | 2mm bare copper measurement pad; no purchased component |
| H1/S1 | Existing JST/NKK assignments | Preserved physical connector/switch terminal conventions |

`fp-lib-table` registers project-local MakeMusicPower and installed Capacitor_SMD/TestPoint using `${KICAD10_FOOTPRINT_DIR}`. All 46 physical components have assigned footprint files with exactly the schematic pin numbers. TP1 is on-board and excluded from BOM. No holder contacts, holes or module mounting geometry are inferred.

## TI RPW0010A coordinate audit

Source: [TI TPS25947 SLVSFC9C, May 2026](https://www.ti.com/lit/ds/symlink/tps25947.pdf), package drawing 4225183/A 08/2019, final RPW pages: package/land/stencil on PDF pages72/73/74. Pin functions are on printed pp5–6. The land/stencil drawings were rendered and visually inspected; PDF vector dimensions were cross-checked. All coordinates below are **top view in mm**, origin at package center, x right/y down. The body is nominally 2×2mm.

Each corner contact is the union of two overlapping rounded rectangles, not a generic rectangular QFN pad. Corner radius is 0.05mm. The custom native pad has one numbered anchor and two connected copper polygon primitives; 16 segments per quarter approximate each radius with <0.0001mm radial error.

| Pad | Native anchor = tongue center | Tongue W×H | Stem center | Stem W×H | Approximate union copper centroid |
|---:|---|---|---|---|---|
| 1 | (−0.900,−0.700) | 0.600×0.300 | (−0.725,−0.875) | 0.250×0.650 | (−0.8423,−0.8057) |
| 4 | (−0.900,+0.700) | same | (−0.725,+0.875) | same | (−0.8423,+0.8057) |
| 7 | (+0.900,+0.700) | same | (+0.725,+0.875) | same | (+0.8423,+0.8057) |
| 10 | (+0.900,−0.700) | same | (+0.725,−0.875) | same | (+0.8423,−0.8057) |

The union centroid is calculated from the rounded copper outline, area approximately 0.264817mm² per corner, and is **not the routing anchor**. TI's **1.75mm** callout is the y separation of upper/lower **stem centers** (−0.875/+0.875). It is not the tongue-center separation, which is 1.40mm, or the union-centroid separation. Stem x separation is1.45mm; tongue x separation is1.80mm. This explains the differing coordinates without replacing the L geometry by an assumed signal pitch.

| Other pads | Centers | Copper W×H / radius |
|---|---|---|
| 2/3 | (−0.900,−0.225)/(−0.900,+0.225) | 0.600×0.250 /0.050 |
| 9/8 | (+0.900,−0.225)/(+0.900,+0.225) | same |
| 5 IN /6 OUT | (−0.250,0)/(+0.250,0) | 0.300×2.400 /0.050 |

The closest copper separation is **0.20mm**, including IN/OUT. The mask expansion is0.05mm, leaving a nominal minimum0.10mm mask web; this needs fabricator approval. The ±1.45mm courtyard and external pin1 silk dot are engineering allowances, not manufacturer tolerances.

The F.Paste layer follows TI's **example 0.100mm stencil**: side pads use their copper outline; corner paste is the union of0.600×0.275 tongues centered at (±0.900,±0.6875) and0.225×0.650 stems at (±0.7125,±0.875), R0.05 (approximately93% coverage). Power pads5/6 each have two0.280×1.060, R0.05 windows centered at y±0.630 (approximately82% coverage). The copper remains continuous. Assembler approval of stencil thickness, aperture merging, paste, reflow and inspection is outstanding.

## Fuse, TVS and standard lands

[SCHURTER UMT-H datasheet](https://www.schurter.com/en/datasheet/typ_UMT-H.pdf), p2, recommends **3.75×5.60mm** solder pads with **10.00mm inner gap**. Native centers are x±6.875, y0; overall copper span17.50mm. Exact order3403.0275.23 appears in the variant table. The drawing envelope15.4×5.35mm supplies the reference F.Fab body; the ±9.25/±3.30mm courtyard is an engineering allowance. The fuse is symmetric; pad1/2 numbering is our circuit convention. The power contract's **5mm-wide, 35µm copper approach** to F1 describes routing/test-board conditions, not a replacement for the3.75mm pad dimension. PM must qualify ≥2A power copper and place F1 before any input branches.

[Littelfuse SMAJ datasheet](https://www.littelfuse.com/~/media/electronics/datasheets/tvs_diodes/littelfuse_tvs_diode_smaj_datasheet.pdf.pdf), RevGD12/02/25 V1, p5, gives recommended pad height≥1.8mm, length≥2.1mm and inner gap≤2.3mm. Native pads2.1×1.8 at x±2.2 give gap2.3mm and span6.5mm. Maximum body4.6×2.79mm is shown on F.Fab. Courtyard±3.75/±1.90mm is an engineering allowance. SMAJ5.0CA is bidirectional; pad1=BAT_SW_PLUS, pad2=GND is the carrier convention and no cathode band is drawn.

TDK confirms the exact [4.7µF 0805](https://product.tdk.com/en/search/capacitor/ceramic/mlcc/info?part_no=C2012X7R1E475K125AB) and [10nF 0603](https://product.tdk.com/en/search/capacitor/ceramic/mlcc/info?part_no=C1608C0G1H103J080AA) identities/ratings. Assigned standard KiCad lands are engineering choices, not claimed TDK recommended patterns: C0805 pads1.00×1.45 at x±0.95; C0603 pads0.90×0.95 at x±0.775. R0603 pads0.80×0.95 at x±0.825 remain the existing library choice. Qualify solder process and effective capacitance; nominal voltage/µF does not establish transient performance.

## Validation and pending qualification

Fresh root schematic ERC: **0 errors, 0 warnings, 0 exclusions**. Native XML contract check: **162 physical endpoints, 46 components, 38 connected nets and6 intentional NC nets**, including every mapped power endpoint and the original GPIO/socket/bias/bypass assignments. An isolated native KiCad PCB fixture puts all14 copper contacts of U2/F1/D3 on distinct nets and runs DRC at **0.15mm clearance/minimum**: **0 violations, 0 unconnected items**. This establishes native pad clearance at the requested rule; it does not validate the integrated PM PCB. Generated fixture/reports are outside the repository. Both A3 PDF sheets and custom copper/paste previews were visually inspected.

Adopted constraints, not measurements: branch≤0.70A, total3V3≤350mA including Pico, external3V3≤250mA, VSYS capacitance≤100µF, ambient0–40°C and resistor local temperature≤70°C. Hardware UVLO is nominal3.221V disconnect/3.546V restart at U2 IN; nominal breaker threshold1.004A. Published extrema and coordination limits remain in the power review. F1 is upstream backup, not a precise fast1.25A cutoff, and USB supply bypasses the battery eFuse.

Remaining qualification: measured loads/inrush and effective ceramics; 1S overload/short/reverse-input response with/without USB; low-battery rebound and source-change restart; harness polarity/continuity and protected-cell/holder fit; holder contacts≥0.70A normal and≥1.2A continuous; NKK exact case/panel fit; assembler/fabricator footprint, stencil, mask and copper review. The unfused lead before F1 still relies on insulated short wiring and the protected cell's PCM. No purchase, fit, production DRC, manufacturing output or manufacturing approval is claimed.

Use the merged [factory assembly and staged validation procedure](../power/prototype-validation.md) with this native reference map. Overload reset requires clearing the fault, disconnecting USB and keeping S1 OFF until BAT_SW_PLUS/enable discharge below the reset thresholds; qualify the actual dwell. Immediate switch cycling is not an established reset procedure. All measured-results fields remain blank until bench testing.
