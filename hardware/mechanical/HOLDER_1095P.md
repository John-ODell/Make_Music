# Underside protected-18350 holder: drawing-backed candidate

Review date 2026-10-07. Revision one uses a removable protected 18350 with **external charging**, as selected in merged PR #11; this review incorporates the power contract in [rev1-handoff.md](../power/rev1-handoff.md) from merged PR #12. Cell model/lot and holder are still candidates. This review supplies a native **Keystone 1095P** polarized through-hole footprint whose geometry and polarity are supported by the individual drawing; **it does not certify fit for the conservative 39.3 x 18.7 mm cell envelope**.

## Evidence and document provenance

The primary documents are Keystone's **1095P drawing revision A**, dated 2014-09-24 (ECN 14-101; initial drawing 2014-07-30), and **1095 drawing revision A**, dated 2014-09-24 (ECN 14-100). Both individual drawings were downloaded, rotated as temporary PDF pages and visually inspected at readable resolution. Text extraction yielded almost no dimensions, so it was not used as mechanical evidence.

- Manufacturer [1095P product](https://www.keyelco.com/product.cfm/product_id/14087) and [individual PDF endpoint](https://www.keyelco.com/product-pdf.cfm?p=14087).
- Readable mirror of the **manufacturer-authored** [1095P drawing revision A](https://www.rxelectronics.sg/datasheet/85/1095p.pdf). SHA-256: `5fddd5d3d01150c1967b63c82e5822e87281f608d16e803a0f4c0bf093cab1aa`.
- Manufacturer [1095 product](https://www.keyelco.com/product.cfm/product_id/14033) and [individual PDF endpoint](https://www.keyelco.com/product-pdf.cfm?p=14033).
- Readable mirror of the **manufacturer-authored** [1095 drawing revision A](https://www.rxelectronics.sg/datasheet/ec/1095.pdf). SHA-256: `0b3144d6b590e66b38966713e4e4f1af26cedcff102771e9c5285527c5a951e0`.
- [Keystone family catalog, printed page 28](https://beta.keyelco.com/userAssets/file/M70p23-33.pdf): broad protected-cell support, not a specified maximum fit envelope.

The main manufacturer PDF downloads returned HTML challenges in this environment. The mirror preserves the Keystone title block, exact part/drawing number, revision, dimensions and polarity marks; no distributor dimensional claims are used. Manufacturer drawings are linked, not copied into the repository. Latest-revision equivalence and selected part provenance must be checked before release; a 2014 drawing is a documented candidate basis, not proof that today's supplied lot is unchanged.

## Geometry and polarity contract

All dimensions below are mm, copied from drawing callouts. Source orientation is the drawing's component/top view: negative at left, positive at right. Footprint origin is the body center, x right, y down. Electrical pad numbering is the carrier convention **1 = positive, 2 = negative**, not manufacturer pin numbers (the drawing labels polarity rather than numbering contacts).

| Feature | Coordinate / size | Evidence |
| --- | --- | --- |
| Housing nominal outline | x +/-22.575, y +/-10.325; 45.15 x 20.65 | 1.778 and 0.813 inch callouts |
| Housing height above mounting plane | 14.86 | 0.585 inch; cell projection is additional |
| Pad 1, positive electrical contact | (+19.89,0); finished drill 2.39 | right contact, 0.094 inch hole |
| Pad 2, negative electrical contact | (-19.89,0); finished drill **1.19** | left contact, 0.047 inch hole for **1095P** |
| Contact center span | 39.78 | 1.566 inch |
| Plastic locating boss hole, negative side | (-15.24,+8.00); **NPTH diameter 3.45** | 0.136 inch hole in mounting pad layout |
| Plastic locating boss hole, positive side | (+15.24,-8.00); **NPTH diameter 3.45** | diagonal second boss, 0.136 inch |
| Boss center spacing along x / y | 30.48 / 16.00 | 1.200 inch and two 0.315 inch offsets |
| Contact-to-boss x offset at each end | 4.64 | 0.183 inch |
| Boss diameter / projection | 2.92 / 3.55 | 0.115 / 0.140 inch, two places |
| Contact projection | 3.43 | 0.135 inch, two places |
| Cradle opening callout along x | 36.98 | 1.456 inch; **not stated as max cell length** |
| General drawing tolerance | +/-0.25 linear; +/-1 degree angular | title block, unless otherwise specified |

The **large diagonal holes are nonplated plastic locating holes**, not electrical contacts. The two unequal holes on y=0 are the electrical contacts. This corrects the earlier family-catalog interpretation in which 1.2 mm holes were described generically as contacts and 2.4 mm holes as locating holes. A catalog diagram is not a substitute for this individual-part mounting layout.

The nonpolar **1095** individual drawing has the same nominal outline/contact span/boss layout but its negative electrical hole is **1.32 mm (0.052 inch)**, rather than 1095P's 1.19 mm. **Do not substitute 1095 into the 1095P footprint without a separate review.** No 1095 footprint is supplied in this PR. The 1096 SMT layout is a separate design, also unassigned.

Native file: `../libraries/MakeMusic.pretty/BatteryHolder_Keystone_1095P_1x18350_THT_Candidate.kicad_mod`. Drills, pitch, NPTH geometry and nominal F.Fab body follow the individual 1095P drawing. Copper sizes (3.80 mm square positive, 2.20 mm round negative) are engineering choices; the drawing specifies holes but not copper lands. Nominal annular rings are 0.705 and 0.505 mm respectively, before hole tolerances. Courtyard +/-23.20 by +/-10.95 includes housing dimensional tolerance and an additional 0.50 mm placement allowance. Those lands/courtyard need fabricator and assembler acceptance; solder mask defaults are not a verified manufacturing specification. No 3D model is supplied.

## Protected-cell fit: still unresolved

`../power/BOM.md` gives the conservative **39.3 mm length, 18.7 mm diameter** envelope due to conflicting P1835C2 manufacturer pages (39.1 vs 38.5 mm length, both +/-0.2). Holder overall length 45.15 mm exceeds cell length, but **overall body length cannot prove cell fit**. The 36.98 mm cradle callout is 2.32 mm shorter than the reserved 39.3 mm cell; the drawing does not give a permitted cell-length range, contact-deflection limit, insertion force, usable diameter or button-aperture dimensions. The cradle callout alone proves neither compatibility nor incompatibility. The family's protected-cell statement supports investigating this part but not releasing it for this exact cell.

The polarized end also requires a compatible positive button shape. Measure the selected protected cell including its wrapper, button and protection extension; obtain the holder's current cell/contact acceptance limits and trial-fit the exact pair. Record safe spring travel, reliable contact, cell retention when downward-facing, wrapper clearance and nonconductive door access. The drawing does not specify contact current rating or establish reverse-insertion behavior for the selected button. Those limits and fault coordination remain release gates with the power helper. Keeppower L1 charger bay usable length is also undocumented in the current power handoff, so this mechanical review does not certify external charger fit. No ordering, vendor contact or physical trial was performed. If this candidate fails, select a different documented holder/cell pair; do not force the cell, trim protection or assume any nominal 18350 fits.

## Underside assembly proposal

Keep the existing 60 x 30 x 25 mm underside reservation at x=150..210, y=15..45. The nominal 45.15 x 20.65 mm body and 46.40 x 21.90 mm courtyard fit that planar reservation. A proposed holder body center at (180,30) leaves space around it; final bottom-side pad coordinates are **not released** until its flip/orientation and polarity are verified in the PCB editor. Authoring footprint is on F.Cu in component view; place it on the carrier underside using KiCad's **Flip** command so Fab/Silk/Courtyard move to B layers. Do not manually mirror net numbers or merely change the text to say bottom side. The proposed carrier convention maps pad 1 / HOLDER_PLUS to `BAT_PROT_PLUS` and pad 2 / HOLDER_MINUS to `GND`, using the cell's external protected negative terminal. Confirm this mapping after placement against the reviewed power contract; no schematic assignment is made here. Check both top and bottom views and the source '+' marking; placement/flip may change global coordinate signs.

Through-hole leads and plastic bosses enter from the underside; solder contacts from the carrier top side. With a provisional 1.6 mm carrier, contact projection beyond the opposite face is approximately 3.43-1.6 = **1.83 mm**, and boss projection is 3.55-1.6 = **1.95 mm**, before tolerances. Reserve at least 2.5 mm top-side vertical clearance over this assembly as an engineering allowance and revise after joint/part measurements. The existing reservation is clear of the Pico footprint and expansion area. Do not place power components, screw heads or other top components over those protrusions without a verified clearance stack.

Retain the provisional 25 mm underside assembly-height reservation and 30 mm underside-to-support spacing. The 14.86 mm holder height is verified, but cell projection and enclosure/door thickness remain unmeasured; neither the 25 nor 30 mm engineering allowance becomes an approved height. Use a nonconductive retaining door/strap and a support load path that does not bear on cell or solder joints. Provide hand access for regular external charging, with power disconnected before removal/insertion.

Factory assembly is preferred: request bottom-side THT/manual/selective-solder acceptance for exact MPN 1095P, NPTH bosses, top-side solder access and pin clipping restrictions through the PM's assembly workflow. This review does not contact a vendor or approve a quote. The cell and external charger are separate items; assemble and inspect with no cell installed. The holder's polarized shape does not replace electrical source isolation/protection or verified polarity.

## Validation and limits

KiCad CLI loaded/exported the candidate; exported geometry and polarity were visually inspected. Checked contact centers/drills, two blank-number NPTH bosses, housing/courtyard and fit inside the planar reservation. No schematic assignment, bottom placement, copper routing, physical cell fit, manufacturing approval, ERC or PCB DRC is claimed. Release requires actual cell/holder fit, current drawing confirmation, polarity/flip review, assembled stack and supplier process review.
