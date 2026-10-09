# Underside protected-18350 holder: corrected drawing review

**Historical superseded 18350 research.** On 2026-10-09 the user corrected the requirement to protected removable 18650. Current holder/cassette specs are in [WIRED_HOLDER_PROPOSAL.md](WIRED_HOLDER_PROPOSAL.md); no dimensions or cell-fit assumptions here apply to that 18650 assembly.

Review date 2026-10-07. Revision one uses a removable protected 18350 with **external charging**, as selected in merged PR #11; this review incorporates the power contract in [rev1-handoff.md](../power/rev1-handoff.md) from merged PR #12. Cell model/lot and holder are still candidates. The previously supplied **Keystone 1095P** footprint has been withdrawn after PM review identified a mounting-layout interpretation error. The corrected five-hole geometry is recorded below, but **no native holder footprint or verified electrical pad map is supplied**. Fit for the conservative 39.3 x 18.7 mm cell envelope also remains unverified.

## Evidence and document provenance

The primary documents are Keystone's **1095P drawing revision A**, dated 2014-09-24 (ECN 14-101; initial drawing 2014-07-30), and **1095 drawing revision A**, dated 2014-09-24 (ECN 14-100). Both individual drawings were downloaded, rotated as temporary PDF pages and visually inspected at readable resolution. Text extraction yielded almost no dimensions, so it was not used as mechanical evidence.

- Manufacturer [1095P product](https://www.keyelco.com/product.cfm/product_id/14087) and [individual PDF endpoint](https://www.keyelco.com/product-pdf.cfm?p=14087).
- Readable mirror of the **manufacturer-authored** [1095P drawing revision A](https://www.rxelectronics.sg/datasheet/85/1095p.pdf). SHA-256: `5fddd5d3d01150c1967b63c82e5822e87281f608d16e803a0f4c0bf093cab1aa`.
- Manufacturer [1095 product](https://www.keyelco.com/product.cfm/product_id/14033) and [individual PDF endpoint](https://www.keyelco.com/product-pdf.cfm?p=14033).
- Readable mirror of the **manufacturer-authored** [1095 drawing revision A](https://www.rxelectronics.sg/datasheet/ec/1095.pdf). SHA-256: `0b3144d6b590e66b38966713e4e4f1af26cedcff102771e9c5285527c5a951e0`.
- [Keystone family catalog, printed page 28](https://beta.keyelco.com/userAssets/file/M70p23-33.pdf): broad protected-cell support, not a specified maximum fit envelope.

The main manufacturer PDF downloads returned HTML challenges in this environment. The mirror preserves the Keystone title block, exact part/drawing number, revision, dimensions and polarity marks; no distributor dimensional claims are used. Manufacturer drawings are linked, not copied into the repository. Latest-revision equivalence and selected part provenance must be checked before release; a 2014 drawing is a documented candidate basis, not proof that today's supplied lot is unchanged.

## Corrected drawing interpretation; footprint withdrawn

PM review identified that the initial four-hole footprint incorrectly assigned the 2.39 mm hole to the positive electrical contact and omitted its separate location. The drawing actually shows **five holes**. The 0.047 [1.19] callout explicitly says **2 PLS**; its leader points to the small right hole on the middle horizontal row, matching the small left hole on that row. The separate 0.094 [2.39] leader points to the right hole on the lower horizontal row. The initial KiCad export only verified that the erroneous file loaded; it did not validate this source interpretation.

Coordinates below transcribe the mounting pad layout with the two small-hole centers on y=0, x right and y down. This is a drawing-coordinate convention, **not a released top/bottom placement transform or electrical pad numbering**.

| Feature in mounting layout | Coordinate / size | Drawing evidence |
| --- | --- | --- |
| Left small hole | (-19.89,0); diameter 1.19 | 0.047 inch, 2 PLS |
| Right small hole | (+19.89,0); diameter 1.19 | same 2 PLS callout |
| Additional right lower hole | (+19.89,+8.00); diameter 2.39 | separate 0.094 inch leader |
| Left lower large hole | (-15.24,+8.00); diameter 3.45 | 0.136 inch, 2 PLS |
| Right upper large hole | (+15.24,-8.00); diameter 3.45 | same 2 PLS callout |
| Small-hole center span | 39.78 | 1.566 inch |
| Large-hole x spacing / row offsets | 30.48 / +/-8.00 | 1.200 / 0.315 inch callouts |
| Nominal housing | 45.15 x 20.65, height 14.86 | component projections |
| Two large boss diameters / projection | 2.92 / 3.55 | 0.115 / 0.140 inch, 2 PLS |
| Contact projection | 3.43 | 0.135 inch, 2 PLS |
| Smaller projected feature | diameter 1.57 x 1.57 long | 0.062 inch diameter x length callout in end projection |
| Cradle opening along x | 36.98 | 1.456 inch; not max cell length |
| General tolerance | +/-0.25 linear; +/-1 degree | title block unless otherwise specified |

The two small holes align with the two contacts in the long side projection, making **two 1.19 mm electrical holes** the supported interpretation. The two 3.45 mm holes align with the 2.92 mm molded bosses. The separate 2.39 mm hole plausibly clears the smaller 1.57 mm locating/key feature visible in the end projection. **That last function is an inference:** the drawing does not explicitly label it as plastic, polarity key, NPTH or electrical. The nonpolar 1095 drawing has the same additional 2.39 mm hole, so it must not be described as uniquely providing polarized-cell protection. Its small-hole callout is **1.32 mm, 2 PLS**, rather than unequal 1.32/2.39 mm contact holes.

Before a new native candidate is supplied, resolve the additional hole's material/function and plating requirement, the mounting-layout view orientation relative to the component '+' mark, and contact-to-pad mapping. The power contract requires HOLDER_PLUS -> `BAT_PROT_PLUS` and HOLDER_MINUS -> `GND` at the external protected negative terminal; **no numerical holder pad assignment is released by this review**. Obtain an unambiguous manufacturer annotation or inspect/measure an exact part without ordering or contacting a vendor under this task. No land sizes, courtyard or manufacturing footprint remain approved from the withdrawn candidate.

## Protected-cell fit: still unresolved

`../power/BOM.md` gives the conservative **39.3 mm length, 18.7 mm diameter** envelope due to conflicting P1835C2 manufacturer pages (39.1 vs 38.5 mm length, both +/-0.2). Holder overall length 45.15 mm exceeds cell length, but **overall body length cannot prove cell fit**. The 36.98 mm cradle callout is 2.32 mm shorter than the reserved 39.3 mm cell; the drawing does not give a permitted cell-length range, contact-deflection limit, insertion force, usable diameter or button-aperture dimensions. The cradle callout alone proves neither compatibility nor incompatibility. The family's protected-cell statement supports investigating this part but not releasing it for this exact cell.

The polarized end also requires a compatible positive button shape. Measure the selected protected cell including its wrapper, button and protection extension; obtain the holder's current cell/contact acceptance limits and trial-fit the exact pair. Record safe spring travel, reliable contact, cell retention when downward-facing, wrapper clearance and nonconductive door access. The drawing does not specify contact current rating or establish reverse-insertion behavior for the selected button. Those limits and fault coordination remain release gates with the power helper. Keeppower L1 charger bay usable length is also undocumented in the current power handoff, so this mechanical review does not certify external charger fit. No ordering, vendor contact or physical trial was performed. If this candidate fails, select a different documented holder/cell pair; do not force the cell, trim protection or assume any nominal 18350 fits.

## Underside assembly proposal

Historical direct-mount proposal (later superseded by the 1101 cassette, then by the current [18650 cassette](WIRED_HOLDER_PROPOSAL.md)): 60 x 30 x 25 mm underside reservation at x=150..210, y=15..45. The nominal 45.15 x 20.65 mm body fits that planar reservation; no holder courtyard is released. A proposed holder body center at (180,30) leaves space around it. Final pad/hole coordinates and top/bottom transform remain unresolved. A future verified footprint must be placed with KiCad's Flip command, then checked in both views against the source polarity and power contract. The current SVG rectangle is only a nominal body reservation, not a placement or hole template.

Through-hole leads and plastic bosses enter from the underside; solder contacts from the carrier top side. With a provisional 1.6 mm carrier, contact projection beyond the opposite face is approximately 3.43-1.6 = **1.83 mm**, and boss projection is 3.55-1.6 = **1.95 mm**, before tolerances. Reserve at least 2.5 mm top-side vertical clearance over this assembly as an engineering allowance and revise after joint/part measurements. The existing reservation is clear of the Pico footprint and expansion area. Do not place power components, screw heads or other top components over those protrusions without a verified clearance stack.

Retain the provisional 25 mm underside assembly-height reservation and 30 mm underside-to-support spacing. The 14.86 mm holder height is verified, but cell projection and enclosure/door thickness remain unmeasured; neither the 25 nor 30 mm engineering allowance becomes an approved height. Use a nonconductive retaining door/strap and a support load path that does not bear on cell or solder joints. Provide hand access for regular external charging, with power disconnected before removal/insertion.

Factory assembly is preferred: request bottom-side THT/manual/selective-solder acceptance for exact MPN 1095P, NPTH bosses, top-side solder access and pin clipping restrictions through the PM's assembly workflow. This review does not contact a vendor or approve a quote. The cell and external charger are separate items; assemble and inspect with no cell installed. The holder's polarized shape does not replace electrical source isolation/protection or verified polarity.

## Validation and limits

Reinspected both complete manufacturer drawing sheets, including mounting layouts and component projections, after PM review. Corrected the two-place contact-hole callouts and recorded all five holes. Removed the erroneous native footprint and all claims that it supplied a verified pad map. SVG body reservations and selected buzzer dimensions remain valid as proposals; no physical fit, bottom placement, routing, ERC, PCB DRC or manufacturing approval is claimed. Release requires resolution of the additional hole and view mapping, exact cell/holder fit, current drawing confirmation, assembled stack and supplier process review.
