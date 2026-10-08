# Prototype assembly and budget comparison

Updated 2026-10-07. User preference: factory assembly as much as possible, with a cheaper comparison option. Exact battery, buzzer, quantity and all module footprints are not finalized. No complete supplier quote has been obtained or order placed.

## Battery tradeoff

| Option | First-prototype implications | Physical result | Additional items |
|---|---|---|---|
| Protected removable 18350, external charging | Simplest selected-topology candidate: switch and isolation into Pico VSYS, no onboard charger | Taller underside holder/compartment | Verified holder, matching protected cell, external charger |
| Protected flat LiPo, onboard USB charging | More circuit/layout work: power path, charge-current/thermal/source policy | Potentially thinner, still needs an enclosure pocket/restraint | Pack connector, charger and supporting parts, charge port, battery temperature provisions as required |

Recommendation for easiest electrical prototype: protected externally charged 18350. Recommendation for a thin integrated product: protected flat pack with a reviewed charging circuit. Neither battery is selected yet. Voltage alone does not establish protection, charging compatibility or runtime.

## Assembly routes

| Route | Factory work | User work | Cost drivers |
|---|---|---|---|
| Bare PCB | Fabrication only | All component soldering, module attachment, Pico/battery installation | Lowest service cost; loose components, shipping and tools extra |
| Partial assembly | Carrier SMT power parts; optionally sockets/headers/holder where supported | Remaining through-hole parts or module attachment; Pico/battery installation | SMT setup/stencil/placement plus parts; manual work depends on accepted quote |
| Mostly factory assembled (preferred quote) | Carrier components plus sockets/headers/holder and touch/buzzer subassemblies if supplier accepts sourcing and mounting | Plug in Pico, fit battery, inspect/test and load firmware | Mixed assembly, parts sourcing/consignment, both-side work and subassembly mounting can add fees |

Separate removable Pico insertion from soldered carrier sockets. A quoted PCBA order does not automatically include instrument firmware, functional testing, an enclosure, the battery cell, or installing purchased breakout modules. Explicitly request those services if needed. Do not silently replace the retained modules with integrated touch circuitry solely to simplify assembly.

PCBWay offers turnkey, consigned and mixed sourcing, as well as both-side and through-hole assembly categories. Acceptance and price for the actual touch modules, buzzer modules, socket strips and chosen holder require the eventual quote and assembly drawings.

## Published fee examples (USD; not a project quote)

JLCPCB's price table, checked 2026-10-07, lists these setup and stencil fees. They illustrate batch overhead only; they do not establish service eligibility or a delivered instrument price.

| Service category | Setup | Stencil | Combined per order | Combined divided over 5 assembled boards (illustration only) |
|---|---:|---:|---:|---:|
| Economic PCBA | $8.18 | $1.53 | $9.71 | $1.94 |
| Standard, one side | $25.56 | $8.21 | $33.77 | $6.75 |
| Standard, two sides | $51.12 | $16.42 | $67.54 | $13.51 |

Not included: PCB fabrication, components, feeder-loading, placement/manual joints, handling, fixtures, programming/test, shipping, taxes, battery, external charger, enclosure or module sourcing. Fees and eligibility can change, and a holder on the underside does not automatically mean two-side SMT assembly; the accepted THT/manual process may be different. A bare PCB has no PCBA setup/stencil fee. Supplier size documentation has inconsistent economic-service summaries; confirm the proposed approximately 330 x 120 mm board in the actual quote flow rather than assuming the lowest service category applies.

An example protected flat pack is Adafruit product 1578, listed at $7.95 at quantity 1–9 when checked, with a JST-PH lead and protection circuitry. This 500 mAh pack is an illustrative price anchor, not a selected capacity, runtime promise or charging-current decision.

## Quote worksheet

For each supplier compare:

`total = fabricated boards + assembly overhead + assembly labor + populated parts + module sourcing + shipping/tax + off-board Pico/battery/charger + enclosure`

Record fabricated quantity separately from populated quantity. Compare one assembled prototype with spare bare boards against five populated units, depending on the user's selected quantity. Reusing owned modules reduces purchased parts cost but may introduce consignment shipping/handling. For a small run, factory population of small parts with user attachment of large modules may be the best compromise; price both instead of assuming.

Required before a meaningful full quote: exact BOM/MPNs and availability, actual module mounting interfaces, selected cell/holder or pack/connector, charging topology, accepted board dimensions, number of populated boards, finished assembly drawings and reviewed manufacturing outputs.

## Sources

- https://www.pcbway.com/quotesmt.aspx — sourcing and assembly options; price remains quote-specific.
- https://www.pcbway.com/pcb_prototype/Through_Hole_Assembly.html — through-hole assembly category.
- https://jlcpcb.com/help/article/pcb-assembly-price — published fee examples (page last updated September 9, 2026).
- https://jlcpcb.com/capabilities/pcb-assembly-capabilities — confirm size/service eligibility with quote.
- https://www.adafruit.com/product/1578 — illustrative protected LiPo retail price and construction.
