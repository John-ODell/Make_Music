# Quote request draft — five complete Make Music instruments

**For owner review. QUOTE ONLY — DO NOT FABRICATE OR ORDER.** No supplier
has been contacted, no files uploaded, and no project price accepted.

Please provide an itemized, nonbinding quotation and identify operations your
team cannot supply. The selected delivery is **five complete instruments**,
including one qualified first article within those five before completing the
remaining four. Quote an optional additional sixth bare carrier separately.
We request factory soldering, crimping, mechanical installation, programming
and testing; the owner has no parts or precision measurement equipment.

## Review inputs and quantity

- Carrier:330×121.5 mm, two layers,1.6 mm FR4, proposed≥35µm finished copper,
  ENIG, green mask/white legend; process/finish subject to your review.
- Each carrier:47 purchased parts,30 top SMT and17 THT. H1 is bottom THT;
  no bottom SMT. Five carriers total150 SMT and85 THT parts.
- Complete instruments add5 original Pico H SC0917,50 HiLetgo touch modules,
  10 SunFounder ST0238 passive modules,60 adapted three-wire module cables,
  5 protected removable18650/MPD BH-18650-W holder assemblies and5 complete
  insulating fixture/cassette/support sets. See the
  [complete assembly scope](support/hardware/assembly/PCBWAY_HANDOFF.md) and [parts allowances](support/hardware/assembly/instrument-parts.csv).
- One shared external charger/input set is a proposed quote assumption;
  the exact compatible cell/charger pair is unresolved and held.
- [Reviewed carrier outputs](README.md)
  include Gerbers, separate PTH/NPTH drills, exact MPN BOM, SMT centroid,
  manual THT positions, drawing PDFs and source-bound verification.

## Requested price lines

Please separate fabrication; SMT setup/stencil/parts/labor; THT parts/labor;
Picos and modules; module and battery harnesses; holder/cells/charger;
custom mechanical manufacture and assembly; precision metrology;
first-article qualification; programming/all-five testing; shipping/tax;
and the optional sixth bare keepsake. List assumed or provisional items
separately from firm prices, quote validity, lead time and minimum quantities.

Also quote five SMT-populated carriers as a comparison. Clearly exclude and
identify all17 THT parts per carrier, harnesses, external modules, Picos,
mechanical work and tests if absent from that price. The selected delivery
remains five complete instruments. See the [budget comparison](support/hardware/ASSEMBLY_BUDGET.md).
The earlier$67.54 setup/stencil example is not a complete-build price.

## Engineering work and production holds

Please price exact-part measurement, adapted module-end terminations,
final toleranced fixture/cassette/retainer drawings and process review.
The [fit checklist](support/hardware/assembly/FIT_CHECKLIST.md) and
[mechanical checklist](support/hardware/mechanical/PHYSICAL_FIT_CHECKLIST.md) specify records
needed; nominal SVG/DXF interfaces are review references, not machining release.

Confirm ability to handle U2 copper/mask/stencil details, nominal0.25 mm socket
annular rings, C17/C18 land choice, panel rails/fiducials/tooling,
depaneling/THT sequence, bottom H1 and orientation/polarity preview.
Record exact module revisions, header mapping, qualified crimps, Pico/socket
engagement and removal, battery/holder cold fit and contact current capability.
Return documentary evidence for a cell/charger pair within the cell's limits.

The design review reports ERC0, copper/layout DRC0 and unconnected0.
Native schematic parity retains4 reviewed custom-field metadata warnings;
pad nets, values and full footprint IDs have0 discrepancies. These checks
do not establish mechanical fit or tested hardware behavior.

Do not fabricate or start a first-article build until the owner separately
approves the parts, required drawing/process revisions and production release.
After release, use the [current-limited first-article procedure](support/hardware/power/prototype-validation.md)
and provide acceptance records for all five completed instruments.
