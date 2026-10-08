# Mechanical fit review and dimensioned proposal

Reviewed 2026-10-07. **Preliminary candidate geometry; not a fabrication release.** Owns mechanical documentation and local footprints only. Read together with `../PCB_DESIGN_NOTES.md`. No main schematic, copper routing, module pin order, power circuit, or firmware was changed.

## Removable non-wireless Pico carrier

Verified from Raspberry Pi Pico 2 datasheet chapter 3, Figure 3 (printed page 7), visually inspected rather than relying on extracted PDF text:

| Feature | Drawing dimension, mm |
| --- | --- |
| Pico PCB | 21 wide x 51 long x 1 thick |
| Header rows, center to center | 17.78 |
| Pins per row / pitch / first-to-last span | 20 / 2.54 / 48.26 |
| Row center from side edge | 1.61 |
| Mounting holes | four, diameter 2.1 +/-0.05 |

Use two **Samtec SSQ-120-01-G-S** vertical 1x20 female sockets as the standard-force candidate. **SSQ-120-21-G-S** is the same series' low-insertion-force alternative, subject to configuration availability and a retention trial. Do not use the -03 tail by default: its 10 mm tail unnecessarily projects below the carrier.

Samtec series print revision BH, sheet 1, and catalog F-226 show single-row housing width 2.41 mm (reference), height 8.51 mm (reference), length `N*2.54+0.51` = **51.31 mm**, length tolerance +/-0.25 mm, 0.64 mm square tails, and style -01/-21 tail length 2.64 mm. Catalog insertion depth is **3.68 to 6.35 mm**. Recommended PCB layout revision A, sheet 1, specifies **1.02 mm holes and 1.52 mm pad diameter**, at 2.54 mm pitch. A local single-row footprint captures these dimensions. Body extends 1.525 mm past each end pad center; courtyard adds 0.5 mm, rounded outward. Pad 1 is square. No claim is made about an unselected male header's fit.

Assume a 1.6 mm carrier PCB: nominal unsoldered tail projection is 2.64-1.6 = **1.04 mm**, with solder fillet and tolerances additional. For an example 6.0 mm exposed male post, a 0.5 mm housing gap gives 5.5 mm engagement, inside the catalog range. This is a stack calculation, **not a selected male header or guaranteed Pico H stack height**. Confirm the supplied Pico/male header has the appropriate square mating post and measured engagement; it must neither bottom out nor float with too little contact overlap. Carrier-to-Pico underside height is 8.51 + socket-to-male-housing gap + male insulator thickness; top component height is additional. Keep the entire Pico underside clear of tall carrier components until that stack is measured.

### Placement and physical numbering

Proposal origin is carrier rear-left, viewed from the playing/top side; x right, y toward the front, in mm. Pico USB points toward the rear edge at y=0. Its PCB box is x=109.5..130.5, y=0..51. Header first-pad centers: left (111.11,1.30), right (128.89,1.30). Subsequent centers increase y by 2.54. Rounding of drawing offsets gives a last center at y=49.56; use the verified pad span, not an assumed symmetric end margin.

Left socket local pads 1..20 run from Pico physical pin 1 to 20. Right socket local pads 1..20 run from Pico physical pin **40 down to 21**. This is a top view with USB up; never assign GPIO number as the physical pad number. If integrated symbols instead number right socket pins 21..40, explicitly remap the footprint or its placement and verify every net. Place both footprint pad 1 ends toward USB when using the local convention above.

The socket housing starts about y=-0.225, slightly beyond the proposed carrier rear edge; this intentional overhang requires enclosure relief and manufacturer edge-to-hole review. Move the assembly inward or notch the enclosure if unacceptable. Reserve a **36 x 25 mm external USB cable approach** at x=102..138, y=-25..0 as an assumed cable-shell envelope; measure the actual plug. Keep BOOTSEL accessible through an open lid/service aperture; a provisional 12 x 12 mm access region around (116.5,14) must be adjusted to the selected Pico's actual button. Leave at least 5 mm side access beyond the Pico and unrestricted upward removal space; trial removal without bending the carrier. USB overhang and plug clearance are separate from the 51 mm PCB dimension.

## Underside 18350 holder options

Keystone's primary catalog page 28 explicitly covers cells with or without built-in protection circuitry. It supplies two usable PCB-mount approaches:

| Candidate exact MPN | Method | Catalog nominal envelope / mounting, mm | Assessment |
| --- | --- | --- | --- |
| Keystone **1095** | Through-hole, leaf springs | body 44.39 x 20.7; 18.0 reference height; contact center span 30.5; locating span 39.0 and width 16.0; contact holes diameter 1.2, locating holes diameter 2.4 | Preferred trial option: bottom-side holder, solder from top; verify exact locating geometry and polarity from individual drawing before creating footprint. |
| Keystone **1096** | SMT, leaf springs | body 44.4 x 20.7; 18.0 reference height; pad-layout overall length at least 53.3; pads at least 7.3 x 6.4; locating span 30.5 and width 16.0 | Alternative if assembler accepts bottom-side reflow/retention; pad layout larger than body. |
| Keystone **1095P** / **1096P** | Polarized variants | Family catalog; individual variant details require review | Consider with confirmed button-top contact geometry; do not assume drop-in pad/fit equivalence. |

Dimensions above come from the **manufacturer catalog diagrams**, not inferred from the name 18350. Individual 1095 PDF endpoint was reachable through the web reader but direct download returned an HTML challenge; therefore a detailed holder footprint is **not released**. Catalog extraction contains a contradictory conversion near one locating-hole annotation; resolve against the individual drawing. No hole pattern or polarity is guessed. The installed KiCad Battery library has no 1095/1096 or 18350 named footprint; no 18650 footprint is substituted.

Protected **Keeppower P1835C2** is a dimensional example only: manufacturer's page states diameter 18.5 x length 38.5 mm (+/-0.2 mm). Conservatively reserve **18.7 mm diameter and 38.7 mm length** until the tolerance wording and actual purchased cell are confirmed. The holder family says protected cells are supported, but that does not establish max spring travel, contact force or compatibility with every protected/button/USB-equipped cell. Trial-fit the selected SKU without forcing it; check wrapper integrity, both contacts, spring travel and polarity. The 18 mm reference cell silhouette in the holder catalog is not proof of clearance for an 18.7 mm cell. No battery purchase or charging-current selection is made here.

Reserve an underside **60 x 30 x 25 mm** design envelope at x=150..210, y=15..45 for either candidate including SMT lands and provisional vertical allowance. Holder long axis is x; insertion/removal points downward, accessible through a battery door. Keep all unrelated bottom-side pads, vias, leads, copper and metal hardware outside the holder/cell/contact region unless an insulated construction is explicitly verified. Mechanical retention of the downward-facing cell needs a nonconductive door/strap; do not rely on solder joints to take insertion or playing loads. Protection and source isolation remain the power helper's responsibility; raw cell power must not reach 3V3/GPIO.

Use four provisional M3 clearance holes diameter 3.2 mm at (6,6), (266,6), (6,106), (266,106), with 8 mm diameter hardware keepouts on both sides. These are carrier holes, not Pico's 2.1 mm holes. Proposed feet/standoffs give **30 mm clearance from carrier underside to supporting surface**: 25 mm reserved battery assembly plus 5 mm clearance. The 25/30 mm values are engineering reservations, not measured holder height. Final lower enclosure/door, cell projection, screw heads, PCB flex and insertion access must be measured before choosing spacers. Playing force goes through carrier/enclosure supports, not the battery. Four-corner support may need ribs or extra supports after a flex/load trial.

## Arrangement proposal and preserved controls

`placement-proposal.svg` is drawn to a consistent mm coordinate system with dimensions; it is **a reservation plan, not module footprints or an approved board outline**. Candidate board size is **272 x 112 mm**, assumed pending actual module measurements and enclosure selection.

Eight front note centers at y=90: x=52,80,108,136,164,192,220,248, in ascending **C4,D4,E4,F4,G4,A4,B4,C5** order; 26 x 26 mm module reservations and 28 mm center pitch (24 mm reference body plus 1 mm per side). Left-hand semitone and octave centers are (22,54) and (22,90), with 26 x 26 mm reservations. Their GPIO baseline remains GP27/GP28; note baseline remains GP16..22/GP26. Increase board size/spacing if actual module body, headers, touch pad, solder tails or finger access exceed these reservations. No module connector pin order is assumed. PM supplied the [HiLetgo reference](http://www.hiletgo.com/ProductDetail/1915450.html), 24 x 24 x 7.2 mm and four M2 holes. These are PM/user-supplied dimensions; hole center spacing, installed header/tail height, and connector orientation/pitch remain unverified. Reservations now accommodate that reference; no module-specific footprint is created. The merged `hardware/components/TOUCH_MODULE.md` was read after fast-forwarding to origin/master 6a61587. The quoted 7.2 mm module height does not include an independently verified carrier mounting gap, pin tail or enclosure clearance; measure the complete assembled stack.

Expansion has a dedicated **45 x 25 mm** accessible top-side zone x=45..90, y=10..35. Expose all 14 unused GPIOs **GP0..GP11, GP14, GP15**, plus 3V3 and GND: proposed two labeled 1x8 2.54 mm headers (17.78 mm end-to-end spans), exact order conditional on schematic review. Label GP0/GP1's optional I2C use; used pins/test points must not be advertised as free. Allow vertical wire/plug access with lid fitted and prevent plugged wires crossing touch controls or obstructing Pico removal. Buzzer reservations x=45..65 and 75..95, y=42..58 are assumptions; power/switch zone x=170..220, y=50..60 is also provisional and can move with power design.

## Assembly and release gates

PCBWay documents through-hole/manual assembly and a quotation form with top/bottom/both-side assembly. This demonstrates a service category, **not acceptance of these particular sockets/holders**. Ask for the selected MPN, bottom-side holder orientation, THT/manual/selective-solder method or SMT retention, sourcing, finished-hole tolerance, solder access and inspection in the assembly quotation. Supply both-side assembly drawings and battery polarity; bare PCB service does not install the holder. Assemble with no cell fitted. Solder sockets aligned using a nonpowered sacrificial mating jig, inspect all joints, then insert Pico; do not solder the Pico into its removable socket.

Before routing/manufacture: confirm Pico version and male header; trial 40-pin insertion/removal and USB/BOOTSEL access; obtain the holder's individual drawing, polarity mapping and selected-cell fit; measure all ten touch modules and both buzzer modules; confirm enclosure/door/support load path; integrate power isolation/protection; verify finished holes and edge margins; run integrated ERC/DRC/netlist agreement and inspect both sides. An unconnected reservation drawing cannot pass manufacturing validation.

## Source register and verification

Primary sources accessed 2026-10-07; copyrighted manufacturer drawings are linked rather than committed.

- [Raspberry Pi Pico 2 datasheet, chapter 3/Figure 3](https://datasheets.raspberrypi.com/pico/pico-2-datasheet.pdf): row geometry visually inspected. Pico model remains unselected; this footprint basis is non-wireless Pico 2.
- [Samtec exact SSQ-120-01-G-S candidate](https://www.samtec.com/products/ssq-120-01-g-s), [series print revision BH](https://suddendocs.samtec.com/prints/ssq-1xx-xx-xxx-x-xx-xxx-xx-x-mkt.pdf), [recommended PCB layout revision A](https://suddendocs.samtec.com/prints/ssq-1xx-xx-xx-x-xx-xxx-xx-xx.pdf), [catalog F-226](https://suddendocs.samtec.com/catalog_english/ssw_th.pdf): geometry and engagement checked; sourcing remains conditional.
- [Keystone primary catalog, printed page 28](https://beta.keyelco.com/userAssets/file/M70p23-33.pdf), [18350 family](https://www.keyelco.com/category.cfm/Holders-Plastic-PCB/18350-Lithium-Ion-Holders-and-Contacts/id/1200), [1095](https://www.keyelco.com/product.cfm/product_id/14033), [1096](https://www.keyelco.com/product.cfm/product_id/14034), [1095 individual PDF endpoint](https://www.keyelco.com/product-pdf.cfm?p=14033): catalog visually inspected; individual drawing download limitation recorded above.
- [Keeppower P1835C2 dimensional example](https://www.keeppower.com/zh/product/keeppower-18350-1200mah-protected-li-ion-rechargeable-battery-p1835c2/): size only; actual cell selection is open.
- [PCBWay through-hole assembly](https://www.pcbway.com/pcb_prototype/Through_Hole_Assembly.html), [assembly quotation options](https://www.pcbway.com/quotesmt.aspx): supplier support conditional on quote review.

Validation: local socket footprint exported successfully by KiCad 10 CLI and visually reviewed; pad count, numbering, pitch, span, drills, body and courtyard checked against cited dimensions. Proposal SVG XML parsed and visually reviewed. No PCB exists in this scope, so no board DRC, electrical compatibility or physical fit test is claimed.
