# Prototype recommendation: wired 1101 in an underside cassette

Reviewed 2026-10-08, including merged schematic power PR #14 and native PCB draft PR #15. **PM-approved carrier architecture:** use one Keystone **1101** solder-lug 18350 holder in a removable, insulated cassette beneath the carrier, connected by a factory-made two-wire JST PH harness. This preserves the underside removable-cell intent and removes the holder's hole pattern from the carrier PCB. The cassette bolts to the carrier independently; its holder retention features can change after measurement without changing electrical PCB holes.

PM approved the wired-holder/independent insulating cassette architecture on 2026-10-08 for revision-one carrier integration. Dimensions below remain engineering reservations. This is **not a certified P1835C2/1101 pairing**. Published evidence supports the holder identity, body envelope, lug polarity, off-board wiring and connector mating set. It does not supply a numeric maximum protected-cell length. The first acceptance step is a cold fit check with the exact cell/holder pair; do not energize or manufacture the integrated assembly before that check. Carrier placement/routing can proceed using the independent connector and mounting interface while the physical-fit gates remain open. No purchase, vendor contact or physical fit test occurred.

## Holder evidence and what it resolves

Keystone's [1101 product page](https://www.keyelco.com/product.cfm/product_id/14075) identifies a single-cell 18350 solder-lug holder. Its [solder-tab family page](https://www.keyelco.com/category.cfm/Cylindrical-Cell-Holders/Holders-Plastic-PCB/id/418) explicitly supports wire leads for off-board use; the [inline table](https://www.keyelco.com/category.cfm/keyelco/High-Performance-In-line-Battery-Holders/id/388) lists 1101 for one 18350 with **no listed cover**. A separate cassette door is therefore proposed.

The individual manufacturer drawing **1101**, dated **2015-01-23**, has a blank revision field, not a claimed revision A. [Official PDF endpoint](https://www.keyelco.com/product-pdf.cfm?p=14075); readable [manufacturer-authored drawing mirror](https://www.ic-components.com/files/0c/1101.pdf), SHA-256 `c3a6cac0712260a0450f168a440bd7bb07b19345041b65ace4f67612bb4ae6f2`. The complete sheet was rendered, rotated and visually inspected. Distributor category/size text is not used as drawing evidence. Confirm delivered-part equivalence before release.

| Feature | Manufacturer drawing evidence | Proposal implication |
|---|---|---|
| Plastic body | 45.15 x 20.65 mm; 14.86 mm height above mounting plane | Same nominal body reservation as earlier research; solder lugs extend beyond the plastic length. |
| Polarity | Component view '+' right lug, '-' left lug | Trace each lug to its contact with a continuity meter before harness assembly; no inferred PCB pad numbering. |
| Terminations | Two external solder lugs in plan/side/isometric views | Solder wires to lugs with the cell removed; no soldering to the cell. Lug tip span/hole size are not dimensioned, so no lug outline or solder process limit is invented. |
| Molded projections | Two 2.92 mm bosses; smaller 1.57 mm diameter x 1.57 mm feature; 3.43 mm two-place projection callout | Provide a broad relief cavity, not a close-fit mounting-hole pattern. Allow **5 mm clear behind the holder mounting plane**, then verify on the part. |
| Cradle opening | 36.98 mm along x | Not a cell-length limit. The 39.3 x 18.7 mm protected-cell target still requires trial fit. |
| Materials | Heat-resistant nylon Stanyl 46/equivalent; 0.012 inch stainless-steel contacts, nickel plate | The exact drawing says nickel plate; do not substitute a family-page finish claim for it. No contact ampacity or solder time/temperature is specified. |
| General tolerance | +/-0.25 mm linear, +/-1 degree unless specified | Nominal envelope is insufficient for a close-fitting production cassette. |

Unlike 1095P, the 1101 drawing has no two electrical PCB holes: its mounting layout shows only the molded-feature holes, while electrical terminations are external lugs. That provides additional evidence that the shared 2.39 mm hole belongs to a mechanical feature, but this proposal does **not** reinstate the withdrawn 1095P footprint. It avoids all three holder locating holes through a relieved cassette cavity.

## Dimensioned cassette and fastening proposal

See [cassette plan and section](wired-holder-cassette.svg). All cassette dimensions/locations below are **engineering proposals**, not Keystone dimensions or a manufacturing CAD release. Use an insulating cassette with a removable nonconductive door, adjustable retainers bearing on the holder's **plastic body**, and a separate wire strain-relief clamp. Keep clamps off spring contacts, solder lugs and cell wrapper; retainers/door details follow part measurements. Adhesive alone, electrical lugs and the PCB's solder joints are not the intended retention load path.

| Item | Proposed geometry / stack |
|---|---|
| Cassette reservation | **70 x 36 x 32 mm**, x=145..215, y=12..48, centered (180,30); replaces the historical 60 x 30 x 25 direct-holder reservation for this architecture. |
| Broad holder/lug working region | 56 x 24 mm inside cassette; **a working reservation, not a measured lug envelope**. Adjust if solder boots/bends require more room. |
| Independent carrier/cassette bolts | Four **3.2 mm NPTH** clearance holes at (150,17), (210,17), (150,43), (210,43), 60 x 26 mm center pattern. Carrier drill tolerance/clearance needs fabricator review. No holder holes are drilled in the carrier. |
| Hardware clearance | 8 mm diameter keepout around each bolt (spacer diameter governs); minimum cassette edge distance 5 mm leaves 1 mm outside the radius. Reserve this area on both carrier faces, no copper/components. |
| Bolt stack | Top nylon washer 0.5 + provisional carrier 1.6 + nylon spacer 3 + cassette backplate 2 + bottom washer 0.5 + nut max 2.4 = **10.0 mm** nominal-to-max-nut stack. M3 x 12 screw leaves approximately 2 mm tip beyond nut; other tolerances still require checking. |
| Behind-holder relief | Cassette plate facing holder at z=5 mm below carrier underside; holder mounting plane proposed z=10 mm, giving 5 mm projection cavity. No source-specific peg hole alignment required. |
| Assembly height | Holder/cell space provisionally z=10..30, door allowance z=30..32. These 20/2 mm allocations need actual stack measurement. The 14.86 mm plastic height does not establish fitted-cell height. |
| Support feet | **35 mm minimum underside-to-support proposal**, giving 3 mm nominal below the 32 mm cassette. Validate board deflection, door access and loads; feet/enclosure bear playing pressure. |
| Connector access | Separate 10 x 12 mm underside wiring zone x=225..235, y=15..27; plug/wire bend/service access must be checked before placement. |

The widened cassette remains inside the 330 x 120 mm proposal and clear of Pico/USB access, exposed GPIO, modifiers and buzzer bodies. The current power/switch reservation is x216..264,y44..68, so the cassette right edge x215 leaves **1 mm nominal planar separation**, with y44..48 shared by their projections. They occupy opposite carrier faces; the insulating backplate, wire routing and actual three-dimensional clearance must be checked. The earlier y50/2 mm gap description is superseded. No PCB layout or drill file is changed by this document.

### Named fastening hardware and source evidence

The [Essentra manufacturer fastener catalog](https://essentracomponents.bynder.com/m/6e2e9b888468b393/original/2685970-pdf.pdf) was rendered/visually checked at PDF pages 35, 72, 86 (printed pages **146, 183, 197**). It documents these exact natural nylon 6/6 parts; their material UL94 rating does not certify a printed/machined cassette or the whole instrument.

| Qty | Part | Documented dimensions |
|---|---|---|
| 4 | **50M030050P012** screw | M3 x 0.5, length 12.0; head height 2.2..2.4; head diameter 5.3..5.6 mm; printed p146 |
| 4 | **04M030050HNDIN34814** nut | M3 x 0.5, flats 5.3..5.5; height 2.2..2.4 mm; printed p183; ordinary hex nut, no locking feature claimed |
| 8 | **MFW030A** washer | ID 3.2, OD 7.0, thickness 0.5 mm; printed p197 |
| 4 | **13ME036** spacer | [Manufacturer product specification](https://www.essentracomponents.com/en-us/p/pcb-spacer-non-threaded-round-through/13me036): ID 3.2, OD 8.0, length 3.0 mm, nylon 6/6 |

This verifies a dimensional fastening stack, not pullout strength, torque or vibration life. Confirm clearance on the delivered parts, use the supplier's tightening guidance, and check loosening/creep after repeated cell removal. The cassette clamp/door still needs mechanical detailing and a load trial before release.

## Connector and harness contract for integration

Use the exact matching JST PH set below. [JST PH manufacturer datasheet](https://www.jst-mfg.com/product/pdf/eng/ePH.pdf), printed pp1–3, was rendered and visually inspected. It specifies **2 A AC/DC with AWG24**, 2.0 mm pitch, and 0.8..1.6 mm carrier thickness. That connector rating is above the power handoff's provisional 1 A allowance; it is not a current limiter or certification of holder/wiring/fuse fault coordination.

| Qty | Exact part | Evidence / use |
|---|---|---|
| 1 | **B2B-PH-K-S(LF)(SN)** | Two-circuit top-entry THT header; p3 body 5.9 x 4.5, height 6; p1 mated mounting height approximately 8 mm. Place on underside with KiCad Flip. |
| 1 | **PHR-2** | p3 matching two-position housing, width 5.8, depth 4.5, height 6.85 mm; verify circuit-1 locator in the drawing. |
| 2 | **SPH-002T-P0.5S** | p2 standard contact, AWG30..24, insulation OD 0.8..1.5 mm. Use AWG24 stranded red/black wire within this insulation range. Low-insertion-force suffix L is not selected. |

Recommended installed KiCad 10 footprint: **`Connector_JST:JST_PH_B2B-PH-K_1x02_P2.00mm_Vertical`**. Inspected editable native file: pad1 (0,0), pad2 (2,0), both **0.75 mm drill**, lands 1.20 x 1.75; F.Fab body x=-1.95..3.95, y=-1.70..2.80. This matches JST p1's 2.00 +/-0.05 mm pitch and 0.70 +0.10/-0 mm reference holes after rotating the source mounting-surface view 180 degrees. The source circuit-1 mark and footprint pad1 remain associated through that rotation. Copper lands/courtyard are library engineering choices. JST notes that FR4 may require larger holes; check finished-hole tolerance and header fit with the fabricator rather than enlarging silently. No custom footprint is needed and none is added here.

Proposed **carrier/harness convention**, subject to PM/schematic review: **header circuit 1 = BAT_PROT_PLUS**, red lead -> marked '+' lug; **circuit 2 = GND**, black lead -> marked '-' lug/external protected negative. This is our assignment, not an intrinsic JST battery polarity. A shrouded plug keys the connector orientation; it does not prevent reversed wires in a premade harness or a reversed cell in this nonpolar holder. Trace lug-to-contact continuity with no cell, and verify harness cavity numbering in both mating and wire-entry views. Test the completed harness end to end; do not choose polarity from a supplier photo or wire color alone. Initial **150 mm cut length per lead** is a routing allowance, to be trimmed after mock-up; keep excess off cell, modules and touch zones.

Factory assembly preference is retained: request a populated carrier with the underside PH header, plus a **separately assembled/tested holder harness and cassette**. The assembler crimps PH contacts with suitable tooling, solders/insulates lugs with the cell absent, adds strain relief and performs continuity/polarity inspection. Keystone's nickel-plated lug process limits require assembler confirmation. Add mechanical cassette attachment/inspection to the assembly scope; do not silently move soldering/crimping to the user. Separately compare partial assembly through the existing PM quote workflow. User insertion of Pico and protected cell remains the intended final step; no quote or sourcing acceptance has been obtained.

## Acceptance work that unlocks this proposal

The [build-readiness audit](BUILD_READINESS.md) rechecks primary manufacturer data, records the conflicting 38.5/39.1 mm cell lengths, and separates required cold fit/CAD/harness acceptance from later endurance characterization. The [physical-fit checklist](PHYSICAL_FIT_CHECKLIST.md) assigns exact-cell/holder metrology and harness/assembly work to a priced assembler service for five complete instruments, with an optional sixth bare carrier; the user has no actual parts or precision equipment yet. No public numeric 1101 contact rating or exact P1835C2 spring-travel limit was found. The current official 1101 PDF could not be visually compared in this run; do not infer a new revision or dimensions from its download title. The earlier inspected manufacturer-authored drawing remains conditional on delivered-part equivalence.

1. With exact P1835C2 and 1101 available through the PM's authorized process, record cell dimensions/button and test insertion, contact deflection, wrapper clearance and downward retention with power disconnected. Reject forced insertion. This single test decides the holder pairing; a nominal 18350 label does not.
2. Measure lug/solder-boot envelope and full fitted height; finish cassette clamps/door and verify the proposed 70 x 36 x 32 space plus bolt/connector access. Run repeated removal/retention and fastener checks before approving dimensions.
3. Power helper resolves holder contact rating, branch fault protection, reverse-cell mitigation and measured load/inrush. The 2 A connector does not resolve those power gates. If 1101 fails cell fit, the same off-board connector/cassette architecture can accept a measured replacement without changing the carrier's holder holes.
4. With PM architecture approval recorded, the schematic helper replaces logical holder +/- with the verified PH interface and runs integrated checks; PM carries the larger envelope and 35 mm support requirement into the carrier and factory assembly scope. Cell/charger electrical compatibility and L1 bay fit remain with the existing handoff and are not changed by this mount.

For schematic integration, replace existing H1 logical `+`/`-` terminals with the physical two-circuit PH connector interface, mapping the old `+` net to circuit 1 and old `-` net to circuit 2. Keep the existing switch/diode/VSYS source path unchanged. The schematic helper must update its symbol, footprint and connectivity checker together, then review the netlist/PCB agreement.

Validation: KiCad CLI loaded/exported the installed PH footprint; export was visually checked. All three proposal SVGs parse. Cassette and connector reservations were checked against Pico, GPIO, modifiers, buzzers, notes and power-zone boxes; bolt keepouts are contained and clear of the nominal holder body. Checked the 10 mm nominal fastening stack and 2 mm screw-tip allowance. These checks validate the proposal geometry, not physical cell fit or mechanical strength.

No current main schematic/BOM/PCB assignment is changed by this proposal. This recommendation reduces the carrier decision to one documented connector plus four independent fastening holes; holder-specific hole uncertainty is removed from that interface.
