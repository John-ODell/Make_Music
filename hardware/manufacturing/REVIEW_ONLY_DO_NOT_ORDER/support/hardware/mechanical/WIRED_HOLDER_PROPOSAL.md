# Protected 18650 in a wired underside cassette

Updated **2026-10-09** after the user's correction: the intended cell is the **long 18650**. The earlier P1835C2/Keystone 1101 selection and 70 x 36 x 32 cassette are superseded. Preserve a removable **protected conventional 4.2 V-charge Li-ion cell**, external charging, factory wiring/mechanical installation, five complete instruments and an optional sixth bare carrier. The power owner selects the exact cell and matched charger; no parts, procurement, supplier contact or physical fit results are available here.

**Primary holder candidate: MPD BH-18650-W**, a documented protected-18650 holder with factory leads. Install it in a removable insulating cassette. Exact-cell cold fit, comfortable replacement access, holder current capability and final machining remain gates. The user's anonymous 71.12 x 21.082 x 20.828 mm flat-top holder listing is not selected: no verified MPN/drawing and its stated removal limitations conflict with the requested external charging. Those dimensions do not size this cassette.

## Exact manufacturer evidence

[MPD's product description](https://products.memoryprotectiondevices.com/?page_id=753) identifies protected-cell use and factory leads. The [primary drawing](https://www.batteryholders.com/uploads/parts/BH-18650-W/datasheets/BH-18650-W-datasheet.pdf), **BH-18650-W revision G, 2024-08-21**, was downloaded, rendered and visually inspected. SHA-256: `7b09b755904dbd94c8a8012329911078f778e428c0b17dae053a517498b8bdfe`. Manufacturer PDFs are linked, not committed.

| Feature | Drawing evidence, mm unless stated | Consequence |
|---|---|---|
| Holder body | **77.70 long x 20.90 wide x 21.31 high** | Holder dimensions, not maximum cell dimensions or fitted-cell height |
| Decimal tolerance | ±0.5 mm (.020 inch); angular±3° | Body planning maxima **78.20 x 21.40 x 21.81** |
| Internal mounting | Two Ø3.20 holes, Ø5.08 recess; centres 55.61 apart, first 10.68 from illustrated left end | Cassette-platform interface only; no carrier holder holes |
| Leads | 24 AWG TR64,150±5 each, stripped 5±1 | Factory PH termination, routing and strain relief still required |
| Contacts/body | Nickel-plated 302 spring stainless; insulating thermoplastic polyester | Current and replacement-cycle ratings are not supplied |
| Intended cell | Drawing explicitly specifies protected 18650 batteries | Exact maximum cell length/diameter and allowed contact travel remain unspecified |
| Fastening guidance | 2-56 machine screws or specified eyelets | Factory selects measured screw length/head retention; adhesive alone is not our load path |

The open holder/cassette door provide the proposed replacement path with the instrument lifted and sources disconnected; the 3 mm floor clearance is not finger access. Factory details must allow door/platform servicing and retained fasteners. Verify actual unpowered insertion/removal of the selected protected cell without forcing contacts or damaging its wrapper; no cycle-life approval is implied. Keystone **1044** remains a solder-lug alternative: its [manufacturer family](https://beta.keyelco.com/category.cfm/18650-Lithium-Ion-Holders-and-Contacts/For-One-18650-Cell/p/418/id/1198/c_id/686) and [catalog p29](https://beta.keyelco.com/userAssets/file/M70p23-33.pdf) document protected-cell support and tool-free removal. Its catalog body is nominal 77.1 x 20.7 x 18.0. Its individual drawing could not be visually inspected here, so lug envelope/interchangeability with MPD are not approved.

## Revised cassette geometry

See [plan/section](wired-holder-cassette.svg) and [handoff CSV](cassette-18650-geometry.csv). Plan retains the legacy service datum, x right/y forward; native KiCad adds (20,20). For the proposed 330 x121.5 carrier the rear is legacy y=-1.5/native y18.5; cassette and all native mounting positions stay fixed. See DATUMS.md for the physical upper-left and optional new-origin conversion, and CASSETTE_INTERFACES.md for independent nominal interface CAD. **z is positive down from the carrier underside**, unlike the upper fixture. These are review geometry/factory measurement targets, not toleranced machining CAD or measured fit.

| Item | Revised geometry / status |
|---|---|
| Outer cassette | **112 x 36 x 44**, x145..257/y12..48, centre(201,30); grows **42 mm rightward** |
| Holder position | Centre(201,30), long axis x; nominal body x162.15..239.85/y19.55..40.45; tolerance-expanded x161.90..240.10/y19.30..40.70. Illustrated '+' at right; verify lead polarity |
| Wire/retainer region | Proposed 94 x 26, x154..248/y17..43; **7.90 mm** beyond each maximum body end and **2.30 mm** per side. Engineering allowances, not a known lead bend radius |
| Carrier mounts | Retain four 3.2 NPTH at **(150,17),(210,17),(150,43),(210,43)**; native (170,37),(230,37),(170,63),(230,63). Retain Ø8 both-face exclusions |
| Backplate/bolts | Retain 3 mm spacer +2 mm insulating backplate, z3..5, and M3x12/washer/nut proposal; under-head stack remains 10 mm nominal-to-max-nut |
| Holder platform | Insulating platform z14..16; holder mounting plane **z16**, 11 mm below backplate lower face. Require ≥2 mm between complete bolt-tip envelope and nearest holder/platform feature after tolerances/deflection |
| Holder platform holes | Nominal **(172.83,30),(228.44,30)** from MPD mounting view; **cassette-only**, confirm actual view/tolerances before drilling. Use manufacturer 2-56 guidance and measured screw length |
| Door/fitted height | Door z42..44. Complete fitted cell/holder/wire/fastener envelope plus loaded deflection/dimensional allowance must end **z≤40**, leaving ≥2 mm. Maximum bare holder reaches z37.81; remaining 2.19 mm is an allowance, not proof of cell fit |
| Supports | **≥47 mm carrier-underside-to-support**, 3 mm nominal under 44 mm cassette; replaces 35 mm. Verify actual load clearance, stable feet and changed playing height |
| H1 | Move pad1 **(229,20)->(269,20)**, same bottom side/rotation/nets/connector; access box moves to **x265..275/y15..27**, 8 mm nominal from cassette |

The four carrier mounts can stay as a **three-dimensional proposal**, not a flat plate substitution. Right-hand Ø8 bolt exclusions overlap the bigger holder's plan projection. The lowered z16 holder platform separates them vertically: M3x12 minus 0.5 top washer/1.6 carrier gives 9.9 mm nominal tip depth; platform upper face z14 is 4.1 mm below it before tolerances. Measure actual screw tips, holder projections and deflection. Do not put bolts through the cell bay. The 47 mm cassette overhang beyond the x210 mounts needs a stiffened insulating load path and factory retention/load inspection; ribs/material/fastening remain final CAD work.

Former H1 was inside the enlarged backplate/holder area. Root moved it to native (289,40), as present in the held 806457b inventory, avoiding an invented access cutout with unknown installed plug clearance. Proposed access x265..275/y15..27 clears cassette by 8 mm and power/switch reservation x216..264/y44..68 by 17 mm in y; right corner support (324,6) remains clear. Verify plug direction, lead bend and reachable disconnect.

Cassette y48 shares y44..48 with top-side power geometry and now overlaps it in x. Opposite-face placement requires the insulating backplate and actual tail/copper/wire clearance to be checked. Pico service ends x135.5,9.5 mm before cassette x145; upper fixture starts y68 here,20 mm beyond cassette y48. No relocation of Pico, switch, GPIO, modifiers, note/buzzer seats, nine fixture mounts or four cassette carrier holes is requested.

## Exact PM native-CAD handoff and held-checkpoint status

The held root 806457b IPC inventory confirms H1 at native (289,40), bottom/0 degrees, and all four carrier mounts retained. This helper reviewed that exported inventory; no fresh live readback, routed-net audit or physical harness fit is claimed here. The following records the native handoff for root; the move is already present in that checkpoint.

1. Through Konnect move **H1 pad1 native (249,40)->(289,40)**, delta(+40,0). Preserve bottom side, rotation, circuit1 BAT_PROT_PLUS/circuit2 GND and exact JST PH footprint. Reroute/refill affected battery nets and inspect underside service access.
2. Retain every carrier NPTH centre/drill. Update reservations to 112 x 36 x 44 and ≥47 supports, including lowered holder platform and bolt separation.
3. Run native DRC/parity/unconnected checks and mechanical review; regenerate matching held positions/both-side assembly views/review exports. This helper has made no native mutation or proposed-position readback claim.
4. After assembler metrology issue toleranced cassette/platform/door/retainer/strain-relief CAD and accepted fasteners. Revise cassette/feet if actual fit, height, lead bend or overhang strength fails; return any carrier change to PM.

## Mechanical reservation and rule-area coverage

For PM's visible geometry use **BATTERY_CASSETTE_18650_REVIEW**, native minimum(165,32), width112/depth36; and **BH18650W_BODY_MAX_REVIEW**, native minimum(181.90,39.30), width78.20/depth21.40. CSV records both. These are mechanical reservations, not new copper keepouts.

The insulating platform at z14..16 permits copper beneath it; the whole enlarged bay does **not** require a blanket copper prohibition. Retain the four existing bolt exclusions. All bottom components, solder tails, fasteners and routed leads still require ≥2 mm actual loaded clearance to the cassette/platform/holder. The top-side power projection alone does not establish underside clearance.

PM reports the installed Konnect version lacks rule-area CRUD. If the old underside rule area cannot be enlarged, keep its existing conservative restriction and label its coverage as **partial**; record the full enlarged mechanical reservation as unenforced review geometry. A smaller inherited rule area does not validate the new body/cassette extent. PM must inspect the complete underside assembly after moving H1; no new rule-area operation or CAD approval is claimed here.

## PH harness and factory acceptance

Retain **B2B-PH-K-S(LF)(SN)** underside header, **PHR-2** housing and two **SPH-002T-P0.5S** contacts. [JST PH datasheet](https://www.jst-mfg.com/product/pdf/eng/ePH.pdf) supports 2 A with AWG24 and contact insulation OD 0.8..1.5. MPD does not state wire OD: factory must measure it and confirm contact/tool compatibility or supply a qualified termination. Matching AWG alone does not certify the plug. MPD's supplied 5±1 mm stripping dimension is not a JST crimp instruction; factory re-prepares leads to the qualified JST contact/tool process. Trim/adapt the 150 mm leads only through the agreed factory process, retaining service slack and independent strain relief.

Circuit1 BAT_PROT_PLUS goes to the measured '+' contact, circuit2 GND to '-'. This is our convention, not inherent JST polarity. With no cell trace contact-to-lead continuity, verify cavities in both views, crimp/inspect and test the completed harness. Factory leads replace the former lug-solder operation; carrier soldering, PH crimping and mechanical installation remain factory work. **Battery AWG24 is separate from selected AWG26 module cables** in [MODULE_HARNESSES.md](../assembly/MODULE_HARNESSES.md).

Price metrology and five complete holder/harness/cassette installations, plus optional sixth bare PCB separately. Qualify the first within the five before repeating its accepted build. User has tape/no parts: overall paper fit is separate from factory precision work in the [checklist](PHYSICAL_FIT_CHECKLIST.md).

Open gates: exact protected 18650/charger selection and cold fit/removal; measured fitted envelope/bends/loaded 47 mm support clearance; holder current evidence for the power owner's 0.70 A normal/≥1.2 A continuous requirement; polarity and controlled first-power/protection/function acceptance. No numeric holder ampacity or exact contact-travel limit is published in the inspected evidence. PH 2 A and cell-current ratings do not establish holder ampacity. Existing order/release holds remain; no purchase, supplier contact, sourcing acceptance or fit pass is claimed.
