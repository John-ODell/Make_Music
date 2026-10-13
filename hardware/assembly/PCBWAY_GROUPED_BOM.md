# PCBWay grouped carrier BOM

Prepared October 12, 2026 using PCBWay's supplied Excel template in response
to its request to combine designators with the same manufacturer part number.
Upload [PCBWAY_GROUPED_BOM.xlsx](PCBWAY_GROUPED_BOM.xlsx) in place of the
previous individual-designator `carrier-bom.csv` for the conditional quote.

The worksheet keeps the template's nine columns. `Qty` is **per board**;
the quote batch remains five boards. Each manufacturer/exact-part-number pair
appears once, with all corresponding designators comma-separated in that row.
SMD and thru-hole assembly types and mounting sides are retained.

Validation of the exported XLSX against the reviewed individual-designator BOM:

- 19 unique manufacturer/part-number groups.
- 47 distinct designators, each appearing exactly once.
- Quantity on every row equals its number of designators.
- 47 components per board: 30 SMD and 17 thru-hole; 235 components for five.
- Every designator retains its exact manufacturer, part number, footprint,
  assembly type and side; H1 remains the only bottom-side purchased part.
- All example parts from the template replaced; unchanged blank template tabs
  retained. Rendered worksheet inspected for legibility and clipping.

Source: `hardware/manufacturing/REVIEW_ONLY_DO_NOT_ORDER/carrier-bom.csv`
at reviewed revision `0d6191a0e0217e7140bbceed22aa4e59db78747e`.
The historical quote packet and native KiCad files are unchanged. This standalone
replacement is not a new manufacturing release and has not been sent by the
agent. External modules, Pico H, battery/holder, harnesses, mechanics, programming
and tests remain in the previously submitted full-instrument quote scope.
Physical-fit, qualification, mechanical and process holds remain in force.
