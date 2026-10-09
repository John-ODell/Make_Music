# Mechanical build-readiness audit — current 18650 correction

**2026-10-09 final edge review:** [SOCKET_EDGE_REVIEW.md](SOCKET_EDGE_REVIEW.md) supersedes the historical rear-overhang recommendation below: extend only native rear y20 to y18.5, giving **330 x121.5**, every native placement fixed. Existing mechanical service datum stays native (20,20), so the new edge is legacy y=-1.5. [DATUMS.md](DATUMS.md) makes the physical upper-left (20,18.5) and optional new-frame conversion explicit. [Cassette interface CAD](CASSETTE_INTERFACES.md) completes the independently known nominal backplate/platform geometry. No new native mutation, actual fit or manufacturing release is claimed here.

Updated 2026-10-09 for protected 18650; header/socket review remains historical 2026-10-08 from master `6155ca0`, the held `carrier-positions.csv`, existing fixture/cassette drawings and primary manufacturer sources. Scope: the PM's J3/J4 move, raised fixture/cables, rear socket edge and protected-cell cassette. The current cassette/cell specification below supersedes earlier 18350/P1835C2/1101 research. PM subsequently reported saving J3/J4 at mechanical y78/native y98 and passing full native DRC with zero unconnected items and zero parity errors; this helper did not independently read back that new board or its exports. No KiCad mutation, editor launch, pcbnew/SWIG call, physical measurement, supplier contact or order occurred here. This is a narrow mechanical assessment, not a new DRC or fabrication release.

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

## Cable height and selected AWG26 module-harness process

Primary Harwin evidence, inspected drawings and product pages:

- [M20-9990346 header](https://www.harwin.com/products/M20-9990346), [drawing issue 23](https://content.harwin.com/asset/640f59f4-1860-40fe-82ef-f2a104ffa7d8/DRG-00479-Technical-Drawing-Datasheet-M20-999-pdf.pdf): 0.64±0.02 square posts, 6.10 mm nominal mating length (general ±0.25), 2.54±0.10 insulator height/width, three-way length 7.62±0.50.
- **Candidate carrier cable end:** [M20-1060300](https://www.harwin.com/products/M20-1060300), [housing drawing issue 8](https://content.harwin.com/asset/b9496f9a-d89f-420f-aea9-abb4534be02f/DRG-00376-Technical-Drawing-Datasheet-M20-106-pdf.pdf): three circuits, nominal 7.82 x 2.50 x 14.00; length±0.30, width/height±0.20. Mating pin length 5.50..6.30. The nominal 6.10 post fits this interval; the header's upper tolerance extreme 6.35 does not, so inspect actual engagement/mating gap rather than promise every pair fully seats.
- Three [M20-1180046 tin contacts](https://www.harwin.com/products/M20-1180046) per housing; [drawing issue 13](https://content.harwin.com/asset/d742d022-1905-41c8-b996-8feb2ed262c8/DRG-00379-Technical-Drawing-Datasheet-M20-118-pdf.pdf): 22..30 AWG, insulation diameter 0.9..1.6, strip 3..4 mm, manufacturer crimp/tool guidance. Use selected **AWG26** module wire from [MODULE_HARNESSES.md](../assembly/MODULE_HARNESSES.md), superseding this audit's earlier AWG24 module-wire suggestion; battery leads remain separate AWG24. Exact wire MPN/bend radius and installed module-end construction remain pending. M20 housings are unpolarized; inspect cavity mapping and orientation, not just colors.

Twelve carrier-end housings/36 contacts are the selected module-harness carrier end; module ends and finished lengths remain metrology-dependent. This does not silently specify straight-through cables. Keep carrier 1 SIG / 2 3V3 / 3 GND mapped to actual module labels.

The [primary IS-15 issue 8 instruction sheet](https://cdn.harwin.com/pdfs/IS-15.pdf), page 2 visually inspected, specifies **4.0 mm maximum strip**, tool maximum insulation Ø1.7 mm and **18 N minimum pull-off for AWG26**. The exact contact drawing specifies strip 3..4 mm and insulation Ø0.9..1.6 mm, so use the intersection: **strip 3..4 mm, OD 0.9..1.6**, selected AWG26 and correct manufacturer-qualified tooling/process. A 2 mm maximum-strip interpretation does not match IS-15: its 2 mm reference on page 4 is the calibration hex key. The assembly owner should tighten the module-harness insulation sentence from 1.7 to the contact's 1.6 mm maximum; no out-of-scope assembly-file edit is made here. Qualify crimp samples without pulling on installed module boards.

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

**Historical assessment, superseded by the final y18.5 recommendation:** the courtyard alone did not prove a cut hole or electrical defect. The [new source-bound review](SOCKET_EDGE_REVIEW.md) resolves nominal body support and courtyard containment by extending the rear 1.5 mm. Samtec does not certify carrier edge support; actual tolerances, cut flash, body seating and insertion/removal remain process/fit checks. Do not use 0.73 courtyard as a released enclosure dimension.

[PCBWay's published capabilities](https://www.pcbway.com/capabilities.html), advanced row 19, list 0.25 mm line-to-edge for the normal CNC milling process. The nominal 0.54 mm copper margin exceeds that value; this is a preliminary comparison, not acceptance of this plated-hole edge geometry or its tolerance stack. Its [assembly FAQ, question 14](https://www.pcbway.com/assembly-faq.html), calls for break-away rails on the two longer parallel edges when edge-to-copper is under 3.5 mm for machine assembly. Include a rail/support and depanel sequence in the quote review: the rear plastic lip must not collide with a temporary rail. Installing the THT sockets after depaneling is a possible process for assembler review, not an approved sequence. Temporary panel rails do not by themselves require enlarging the finished 330 x 120 carrier outline.

PCBWay's same capability table, row 17, lists a component-hole outer annular ring of **≥10 mil (0.254 mm)** for its normal 35 µm process and **≥8 mil (0.2032 mm)** for medium difficulty. The reviewed 0.25 mm nominal socket ring is 0.004 mm below that published normal-process threshold. Request explicit process/tolerance acceptance or have PM revise the lands and rerun checks; the design's native DRC does not resolve this supplier-specific comparison. The held package specifies at least 35 µm finished copper, with stackup still to be accepted.

Accept finished-hole and copper-edge margins with PCBWay and check actual Pico H insertion/removal without bending the carrier or levering the unsupported lip. If the fabricator or enclosure cannot accommodate it, PM should adjust the outline or placement with fresh checks. GPIO/USB/BOOTSEL and upward removal access remain explicit. No mechanical approval of the actual assembly is given here.

## Current protected 18650 / MPD BH-18650-W evidence

The user's 18650 correction supersedes the earlier P1835C2/1101 pairing. The [current cassette specification](WIRED_HOLDER_PROPOSAL.md) and [geometry CSV](cassette-18650-geometry.csv) replace the 70 x 36 x 32 cassette and 35 mm feet; no old cell-length allowance is transferred.

| Gate | Source-backed result | Required result before release |
|---|---|---|
| Holder | MPD BH-18650-W primary drawing rev G, 2024-08-21 explicitly specifies protected 18650 use and factory 24 AWG leads; body 77.70 x 20.90 x 21.31, decimal±0.5 | Exact selected protected-cell cold fit/removal/retention; maximum cell length/contact travel and ampacity are not published |
| Cassette | Review proposal 112 x 36 x 44 at x145..257/y12..48; lowered holder plane z16; door z42..44 | Complete fitted/tolerance/loaded envelope z≤40; final stiffened overhang/retainers/platform CAD |
| Mounts | Existing four 3.2 NPTH stay; right bolt/holder projections overlap at different heights | Actual bolt/holder/platform features maintain≥2 mm clearance; no flat-plate interchangeability assumption |
| Connector | Proposed H1 mechanical(269,20), native(289,40), delta(+40,0); PH access x265..275/y15..27 | PM native move/reroute/readback/check/export, correct underside plug direction and measured bend/service access |
| Feet | ≥47 mm underside-to-support,3 mm nominal below 44 cassette | Loaded actual clearance/stability and human playing-height check |
| Leads/current | Factory 24 AWG leads; their insulation OD is unspecified | PH crimp compatibility/polarity and holder-current evidence to meet power-owner 0.70 A normal/≥1.2 A continuous requirement |
| Cell/charger | Protected conventional 4.2 V-charge Li-ion 18650, removable/external charging | Power-owner exact MPN/lot/dimensions, charger fit/current and controlled prototype validation |

Manufacturer body maxima plus engineering wire/retainer/vertical allowances size this **review envelope**. They do not guarantee an unspecified protected cell fits. One assembler metrology session with the exact selected parts unlocks final machining CAD. No sourcing, ordering or supplier contact occurred.

## Shortest concrete path and gate timing

The held PCBWay package can be reviewed and priced while measurements are pending. Existing project order/release holds remain in force; the following sequence does not waive them.

1. **PM completes the carrier review package:** the y78 correction and native checks are PM-reported complete; finish matching held exports and both-side assembly views. Apply the proposed H1 move for the enlarged18650 cassette and review loaded 47 mm supports. Resolve the socket rear-edge process allowance and remaining exact switch/socket footprint fit. No fixture mount, modifier, GPIO or buzzer-seat move is requested by this audit.
2. **One assembler metrology session unlocks mechanical CAD:** record representative exact parts from the intended lot, then check all ten touch boards/two ST0238 per instrument against the resulting limits. Include Pico H/socket pair, selected protected 18650/BH-18650-W/charger and dressed cable candidate. Record both-face bare tab/keeper lands, electrode/sound clearance, thickness, complete header/component projections, mating/labels, cell fit and factory-lead/fitted-holder envelope as detailed in the checklist. Five instruments require 50 touch boards and 10 buzzers to meet the accepted limits; the optional bare keepsake needs no modules. Parts availability and sourcing remain subject to the PM's authorized process; no procurement is performed here. Dimensions from the TTP223 IC sheet or ST0238 product photos cannot close board-level measurements. If edge lands fail, redesign the seat/retention before machining; do not drill modules or clamp circuitry.
3. **Finish and price the measured mechanical subassembly:** issue toleranced machining CAD for plate/windows/fences, measured-thickness keepers, spacers, cassette retainers/door/feet and strain relief; agree material/process and inspect tool access. Keep supplied SVGs as review drawings. Request five complete instruments with factory harness crimp/solder/continuity, mechanical installation, metrology and acceptance explicitly included, plus the optional sixth bare carrier as a separate line. A partial-assembly comparison may inform price, but it is not the selected deliverable and must not shift soldering to the user. This audit does not claim a quote, sourcing acceptance or production CAD.
4. **Qualify the first instrument within the five, then repeat the accepted build:** after a controlled assembly exists, cold continuity/polarity and secure retention/loaded ≥2 mm clearance are required before playing. The assembler follows the existing current-limited [power procedure](../power/prototype-validation.md), including actual touch configuration/current, sound and source-isolation/fault behavior, before real-cell use; repeat unit-level acceptance on the remaining four. No separate sixth populated prototype is assumed. These measurements require assembled hardware; label them planned prototype acceptance, never pre-existing passes. No populated batch/real-cell release is established by DRC.

Necessary exact-part fit/retention, wire polarity, loaded clearance and safe first-power checks are distinct from optional **prototype characterization**: proposed 10 N / 20 N dummy-board targets, extended service/creep life, drop/vibration qualification and detailed latency/loudness/runtime optimization. Basic reliable notes/modifiers and secure supports remain necessary for a usable first instrument. No formal certification or endurance claim is made. A full-size reach/size trial still settles the user's board-size/spacing assumption.

Validation in this run: exported-coordinate conversion and reviewed deltas; nine mount keepout/24 keeper clearance checks; cap/housing projections and stack arithmetic; SVG parsing and rendered review; primary Harwin/Samtec drawings and Keystone catalog visually inspected. The native design and held exports were not modified. The completed header move/native-check result is PM-reported; matching export readback remains with PM. Current 18650 cassette/CSV/primary MPD drawing and Harwin IS-15 process review are separate from that historical carrier audit. Actual-part and supplier result fields remain pending.
