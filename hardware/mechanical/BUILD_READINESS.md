# Mechanical build-readiness audit

Reviewed 2026-10-08 from master `6155ca0`, the held `carrier-positions.csv`, existing fixture/cassette drawings and primary manufacturer sources. Scope: the PM's J3/J4 move, raised fixture/cables, rear socket edge and protected-cell cassette. PM subsequently reported saving J3/J4 at mechanical y78/native y98 and passing full native DRC with zero unconnected items and zero parity errors; this helper did not independently read back that new board or its exports. No KiCad mutation, editor launch, pcbnew/SWIG call, physical measurement, supplier contact or order occurred here. This is a narrow mechanical assessment, not a new DRC or fabrication release.

User selected **five fully assembled instruments**, with an **optional sixth bare carrier as a keepsake**. No actual modules, Pico, cell or holder are available to the user yet. The [physical-fit checklist](PHYSICAL_FIT_CHECKLIST.md) assigns overall paper-fit/reach to the user and exact-part metrology, mechanical installation, harness work and acceptance tests to the assembler as explicitly priced services. No user soldering or precision measuring equipment is assumed.

## J3/J4 correction and fixture clearance

Mechanical coordinates are top-view rear-left, x right/y forward. Native KiCad adds (20,20). The held placement export instead uses x right/y up from bottom-left: `y_mechanical = 120 - y_export`. A note name such as C4 is not capacitor reference C4.

| Item | Mechanical coordinates, mm | Native coordinates, mm | Assessment |
|---|---|---|---|
| J3 pad1 / C4 note | (67.46,75) -> **(67.46,78)**, rotation 90 | (87.46,95) -> **(87.46,98)** | Header body centre becomes (70,78) |
| J4 pad1 / D4 note | (101.46,75) -> **(101.46,78)**, rotation 90 | (121.46,95) -> **(121.46,98)** | Header body centre becomes (104,78) |
| C1 / C2 capacitors | (76.46,75) / (110.46,75) | (96.46,95) / (130.46,95) | Retain locations; each reviewed courtyard is 3.10 x 1.50 |
| Buzzer body references | (60,67.5) / (98,67.5), 32 x 14 | (80,87.5) / (118,87.5) | Front body edge y74.5; fixture seats stay fixed |
| Touch seats | Note centres y94, x70,104,138,172,206,240,274,308 | Unchanged | Left modifiers (24,54)/(24,94) remain fixed |

[Detail drawing](header-clearance-review.svg) shows the reviewed geometry of the PM-reported move. The Harwin bare header insulator is nominal 7.62 x 2.54, long axis along x after rotation 90. Moving its centre to y78 gives **2.23 mm nominal body-to-buzzer separation** in y, versus a 0.77 mm overlap at y75. Header width tolerance alone reduces that separation to 2.18 mm; buzzer outline, assembly and placement tolerances are still unknown. Do not describe nominal plan clearance as measured fit.

The candidate 7.82 x 2.50 cable housing gives 2.25 mm nominal buzzer separation. Its right edge is x73.91/107.91, leaving **2.59 mm** to the corresponding rear touch keeper at x76.5/110.5. Its front edge y79.25 is **2.45 mm** behind the touch-seat opening at y81.7. C1/C2 courtyard projections are separated from that housing by 1.00 mm in both x and y (1.41 mm diagonal); the actual capacitor bodies are smaller. Thus no nominal plan collision requires moving C1/C2. PM must still reroute and check supply/ground bypass paths after moving the headers.

C1/C2 courtyards partly overlap the buzzer body/ledge **plan projection**, but they are below the raised fixture. The [exact KEMET C0603C104K5RACTU specification](https://search.kemet.com/component-documentation/download/specsheet/C0603C104K5RACTU), page 1 reviewed 2026-10-08, gives thickness 0.80±0.15, hence 0.95 mm body maximum. Against the proposed solid-plate underside z24, allowance 0.5 for deflection leaves **22.55 mm** before solder stand-off and dimensional allowances. This supports retaining the capacitor placement; it does not substitute for measuring module underside projections or wires.

The broader 12 x 8 service reservations are x64..76/y74..82 and x98..110/y74..82. They clear all nine fixture mount keepouts and the 24 keeper envelopes. They overlap buzzer body projections by **0.5 mm**, unlike the rigid housings, and touch-seat projections near their central rear opening. These are assembly/wire allowances at different heights, not physical apertures. Do not cut the corner ledges to make them look clear in plan.

Proposed wire corridors are x67..73 and x101..107, y78..81.7, leading forward beneath the solid plate to the central rear touch-seat opening. They avoid C1/C2 and both rear keepers. Keep the dressed bundle inside the measured corridor, off the electrode, fences and fasteners. The actual module-end header may demand a different route or a local fixture notch; preserve four-direction edge restraint. The two ST0238 cables remain on their independent carrier headers at (61,49)/(99,49). Service requires lifting the removable fixture, with all sources disconnected.

## Cable height: a candidate closes identity, not dressed fit

Primary Harwin evidence, inspected drawings and product pages:

- [M20-9990346 header](https://www.harwin.com/products/M20-9990346), [drawing issue 23](https://content.harwin.com/asset/640f59f4-1860-40fe-82ef-f2a104ffa7d8/DRG-00479-Technical-Drawing-Datasheet-M20-999-pdf.pdf): 0.64±0.02 square posts, 6.10 mm nominal mating length (general ±0.25), 2.54±0.10 insulator height/width, three-way length 7.62±0.50.
- **Candidate carrier cable end:** [M20-1060300](https://www.harwin.com/products/M20-1060300), [housing drawing issue 8](https://content.harwin.com/asset/b9496f9a-d89f-420f-aea9-abb4534be02f/DRG-00376-Technical-Drawing-Datasheet-M20-106-pdf.pdf): three circuits, nominal 7.82 x 2.50 x 14.00; length±0.30, width/height±0.20. Mating pin length 5.50..6.30. The nominal 6.10 post fits this interval; the header's upper tolerance extreme 6.35 does not, so inspect actual engagement/mating gap rather than promise every pair fully seats.
- Three [M20-1180046 tin contacts](https://www.harwin.com/products/M20-1180046) per housing; [drawing issue 13](https://content.harwin.com/asset/d742d022-1905-41c8-b996-8feb2ed262c8/DRG-00379-Technical-Drawing-Datasheet-M20-118-pdf.pdf): 22..30 AWG, insulation diameter 0.9..1.6, strip 3..4 mm, manufacturer crimp/tool guidance. AWG24 flexible wire is a planning choice; exact wire MPN, bend radius, insulation and complete cable construction remain to be agreed. M20 housings are unpolarized; inspect cavity mapping and orientation, not just colors.

Twelve carrier-end housings/36 contacts can be included as **candidates** in the assembly review; module ends and finished lengths are separate metrology-dependent items. This does not silently specify straight-through cables. Keep carrier 1 SIG / 2 3V3 / 3 GND mapped to actual module labels.

The nominal rigid mated height is **2.54+14.00 =16.54 mm**, plus any mating gap, leaving only **1.46 mm** within the existing 18 mm total wire/housing reservation. A vertical wire exit needs a bend; no minimum radius is invented from housing dimensions. The free space below the solid plate is nominal 24−16.54=7.46 mm before gap/tolerances/deflection, but the module underside can project into it.

For spacer height S, plate thickness 4, measured maximum downward module projection P, dressed carrier assembly height H and loaded deflection allowance D, require:

`min(S, S + 4 - P) - H - D - dimensional_allowance >= 2 mm`

At S=24 / P=6 / H=18 / D=0.5 this leaves 3.5 mm before dimensional allowance, as previously proposed. The same inputs permit H at most 19.5 before dimensional allowance; an H=20 dressed cable would already leave only 1.5 mm under a module projection. Measure the complete plug, bend, strain relief and screw-tip stack. Retain 24 mm spacers only when that check passes; otherwise adjust spacer/screw length or the cable end and repeat human reach checks. The nine carrier mounts need not change for spacer/seat refinements.

## J1/J2 rear socket edge: assess body and pad separately

The PM's live audit reports courtyard native y19.27..71.59 against rear Edge.Cuts y20. The held placement export/socket CSV confirm the nearest pad row at mechanical y1.30/native 21.30 and far row y49.56/native 69.56. [Samtec SSQ series drawing revision BH](https://suddendocs.samtec.com/prints/ssq-1xx-xx-xxx-x-xx-xxx-xx-x-mkt.pdf) and [recommended layout revision A](https://suddendocs.samtec.com/prints/ssq-1xx-xx-xx-x-xx-xxx-xx-xx.pdf) support the existing body and pad dimensions.

| Quantity | Nominal calculation, mm | Meaning |
|---|---|---|
| Body length | 20 x 2.54+0.51 =51.31 | Manufacturer length tolerance±0.25 |
| End beyond first pad centre | (51.31−48.26)/2 =1.525 | Centred footprint geometry |
| Rear plastic overhang | 1.525−1.30 =**0.225** | Small real body overhang; requires case relief |
| Supported body length in plan | 51.31−0.225 =**51.085** | Over 99.5% of nominal length is over the board, not a bearing-strength guarantee |
| Courtyard overhang | About **0.73** | About 0.5 additional service allowance/rounding, not 0.73 of plastic |
| Copper-to-edge | 1.30−1.52/2 =**0.54** | Nearest pad, including square J1.1, stays inside nominal outline |
| Finished-drill-to-edge | 1.30−1.02/2 =**0.79** | All 40 socket holes are inside the outline |
| Annular ring | (1.52−1.02)/2 =**0.25** | Nominal; fabrication tolerances still apply |

**Recommendation to PM: retain the intentional overhang pending fabricator/case/fit acceptance; the courtyard result alone does not establish a reason to move the outline.** Samtec's drawings do not specify a permissible carrier edge setback or certify this body support. The plastic must sit flat on the carrier, with an unobstructed rear lip, and solder fillets/tails must be clear below. Budget the full ±0.25 body-length tolerance conservatively at the rear until body-to-pin registration is confirmed; 0.225+0.25=0.475 is only an initial relief bound, before carrier-edge/placement tolerances. Do not use 0.73 courtyard as a released enclosure dimension.

[PCBWay's published capabilities](https://www.pcbway.com/capabilities.html), advanced row 19, list 0.25 mm line-to-edge for the normal CNC milling process. The nominal 0.54 mm copper margin exceeds that value; this is a preliminary comparison, not acceptance of this plated-hole edge geometry or its tolerance stack. Its [assembly FAQ, question 14](https://www.pcbway.com/assembly-faq.html), calls for break-away rails on the two longer parallel edges when edge-to-copper is under 3.5 mm for machine assembly. Include a rail/support and depanel sequence in the quote review: the rear plastic lip must not collide with a temporary rail. Installing the THT sockets after depaneling is a possible process for assembler review, not an approved sequence. Temporary panel rails do not by themselves require enlarging the finished 330 x 120 carrier outline.

PCBWay's same capability table, row 17, lists a component-hole outer annular ring of **≥10 mil (0.254 mm)** for its normal 35 µm process and **≥8 mil (0.2032 mm)** for medium difficulty. The reviewed 0.25 mm nominal socket ring is 0.004 mm below that published normal-process threshold. Request explicit process/tolerance acceptance or have PM revise the lands and rerun checks; the design's native DRC does not resolve this supplier-specific comparison. The held package specifies at least 35 µm finished copper, with stackup still to be accepted.

Accept finished-hole and copper-edge margins with PCBWay and check actual Pico H insertion/removal without bending the carrier or levering the unsupported lip. If the fabricator or enclosure cannot accommodate it, PM should adjust the outline or placement with fresh checks. GPIO/USB/BOOTSEL and upward removal access remain explicit. No mechanical approval of the actual assembly is given here.

## P1835C2 / Keystone 1101: what public evidence closes

| Gate | Source-backed conclusion | Remaining requirement |
|---|---|---|
| Holder identity/architecture | [Keystone 1101](https://www.keyelco.com/product.cfm/product_id/14075) is one 18350 holder with solder lugs. [Primary catalog p28](https://beta.keyelco.com/userAssets/file/M70p23-33.pdf) says the 18350 family accommodates protected and unprotected cells. | This is general family support, not a numeric maximum cell length or approval of P1835C2. |
| Cell envelope | [China page](https://www.keeppower.com.cn/products_detail.php?id=566), opened in this run: 18.5 x 39.1±0.2. [Global page](https://www.keeppower.com/product/keeppower-18350-1200mah-protected-li-ion-rechargeable-battery-p1835c2/): 18.5 x 38.5±0.2. | Retain the larger 18.7 x 39.3 cell-only planning envelope; confirm exact lot/button and cold fit. Search snippets are not stronger than the opened pages. |
| Holder body/mount relief | Earlier inspected manufacturer-authored 1101 drawing dated 2015-01-23: 45.15 x 20.65, plastic height 14.86 and broad 5 mm projection relief proposal. The current official PDF endpoint could not be visually compared in this run. | Do not infer revision C or changed dimensions from the download title. Confirm current/delivered drawing equivalence and measure full lug/boot/fitted-cell height. |
| Spring travel/retention | Neither the inspected drawing nor catalog gives exact protected-cell contact travel or force. The 36.98 cradle dimension is not a cell-length limit. | Actual insertion/removal, wrapper clearance, contact compression and retention are necessary. Never force the cell or bypass its protection. |
| Contact ampacity | No numeric 1101 contact-current rating was found in the primary product/catalog evidence. Cell 8 A and JST 2 A ratings cannot establish holder ampacity. | Power owner needs evidence supporting 0.70 A normal and ≥1.2 A continuous branch capability from an applicable rating or controlled qualification. A real-cell short is not that qualification. |
| Cassette interface | Four independent 3.2 NPTH mounts and PH interface isolate holder-specific geometry from the carrier. | Finish insulating retainers/door/strain relief after metrology. Check actual 32 mm stack against ≥35 mm supports, wire bend, bolt tips and carrier deflection. |

Public data confirms candidate identities, generic protected-cell support and a conservative cell envelope. It cannot close this exact pairing. The **shortest battery decision** is one unpowered fit/measurement session with the named cell, holder and charger, followed by an applicable contact/process qualification. The matched charger/current/electrical gates remain with the power helper. A failed 1101 pairing can be replaced within the independent cassette/PH architecture after measurement; no holder hole pattern has to be added to the carrier.

## Shortest concrete path and gate timing

The held PCBWay package can be reviewed and priced while measurements are pending. Existing project order/release holds remain in force; the following sequence does not waive them.

1. **PM completes the carrier review package:** the y78 correction and native checks are PM-reported complete; finish matching held exports and both-side assembly views. Resolve the socket rear-edge process allowance and remaining exact switch/socket footprint fit. No fixture mount, modifier, GPIO or buzzer-seat move is requested by this audit.
2. **One assembler metrology session unlocks mechanical CAD:** record representative exact parts from the intended lot, then check all ten touch boards/two ST0238 per instrument against the resulting limits. Include Pico H/socket pair, cell/1101/charger and dressed cable candidate. Record both-face bare tab/keeper lands, electrode/sound clearance, thickness, complete header/component projections, mating/labels, cell fit and lug/boot envelope as detailed in the checklist. Five instruments require 50 touch boards and 10 buzzers to meet the accepted limits; the optional bare keepsake needs no modules. Parts availability and sourcing remain subject to the PM's authorized process; no procurement is performed here. Dimensions from the TTP223 IC sheet or ST0238 product photos cannot close board-level measurements. If edge lands fail, redesign the seat/retention before machining; do not drill modules or clamp circuitry.
3. **Finish and price the measured mechanical subassembly:** issue toleranced machining CAD for plate/windows/fences, measured-thickness keepers, spacers, cassette retainers/door/feet and strain relief; agree material/process and inspect tool access. Keep supplied SVGs as review drawings. Request five complete instruments with factory harness crimp/solder/continuity, mechanical installation, metrology and acceptance explicitly included, plus the optional sixth bare carrier as a separate line. A partial-assembly comparison may inform price, but it is not the selected deliverable and must not shift soldering to the user. This audit does not claim a quote, sourcing acceptance or production CAD.
4. **Qualify the first instrument within the five, then repeat the accepted build:** after a controlled assembly exists, cold continuity/polarity and secure retention/loaded ≥2 mm clearance are required before playing. The assembler follows the existing current-limited [power procedure](../power/prototype-validation.md), including actual touch configuration/current, sound and source-isolation/fault behavior, before real-cell use; repeat unit-level acceptance on the remaining four. No separate sixth populated prototype is assumed. These measurements require assembled hardware; label them planned prototype acceptance, never pre-existing passes. No populated batch/real-cell release is established by DRC.

Necessary exact-part fit/retention, wire polarity, loaded clearance and safe first-power checks are distinct from optional **prototype characterization**: proposed 10 N / 20 N dummy-board targets, extended service/creep life, drop/vibration qualification and detailed latency/loudness/runtime optimization. Basic reliable notes/modifiers and secure supports remain necessary for a usable first instrument. No formal certification or endurance claim is made. A full-size reach/size trial still settles the user's board-size/spacing assumption.

Validation in this run: exported-coordinate conversion and reviewed deltas; nine mount keepout/24 keeper clearance checks; cap/housing projections and stack arithmetic; SVG parsing and rendered review; primary Harwin/Samtec drawings and Keystone catalog visually inspected. The native design and held exports were not modified. The completed header move/native-check result is PM-reported; matching export readback remains with PM. Actual-part and supplier result fields remain pending.
