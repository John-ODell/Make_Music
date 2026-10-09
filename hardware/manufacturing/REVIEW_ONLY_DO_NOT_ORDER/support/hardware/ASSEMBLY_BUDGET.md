# Budget comparison for five complete instruments

Updated 2026-10-09. The selected scope is **five fully assembled Make Music
instruments**, plus an optional additional sixth bare carrier as a keepsake.
The battery is the long **protected 18650**, externally charged. The earlier
18350 name was a mistake. No complete quote, supplier acceptance or order exists.

## Compare the same five-unit design

| Route | Factory supplies | Work remaining outside the quote | Status |
|---|---|---|---|
| Five complete instruments | All 47 purchased carrier parts per board; 30 top SMT, 17 THT; twelve adapted module cables; ten touch/two passive buzzer modules; fixture, cassette, supports; Pico programming and specified testing | Removable cell insertion/external charging; unpacking or Pico insertion if agreed for shipping | **Selected quote scope**; assembly/metrology availability needs acceptance |
| Five SMT-populated carriers | All 30 top SMT parts per board | Seventeen THT parts including sockets/headers/switch/bottom JST; 60 module harnesses and all mechanical work; Picos/modules/cells and final tests | Price comparison only; requires a capable assembler for the remainder |
| Five bare carriers | PCB fabrication only | Every chip, capacitor, resistor, diode, fuse, socket, header and switch must be soldered; all harness/mechanical work remains | Not selected; user does not want this task |
| One extra bare carrier | Additional unpopulated PCB | None if kept as a design souvenir | Optional sixth board, priced separately |

Carrier SMT is entirely on the top. H1 is bottom through-hole. Consequently,
quote one-side SMT plus accepted THT/manual operations; underside battery
mounting does not automatically mean a two-side SMT setup. The tiny eFuse
package is a good reason to retain factory SMT in either assembled route.

A normal PCBA quotation may stop at the populated carrier. Our
[complete handoff](assembly/PCBWAY_HANDOFF.md) explicitly requests harness
adaptation, module mounting, custom mechanical parts, precise first-article
measurements, programming and five-unit functional records. Any declined
operation must be named and priced through another assembler before calling
an option complete. There is no planned capacitor or header soldering by John.

## What the earlier $67.54 represented

[JLCPCB's published fee table](https://jlcpcb.com/help/article/pcb-assembly-price),
checked 2026-10-09, lists these examples in USD. They are batch setup/stencil
fees from another supplier, **not a PCBWay quote or a complete-project budget**.

| Category | Setup | Stencil | Combined per batch | Combined / five units |
|---|---:|---:|---:|---:|
| Economic PCBA | $8.18 | $1.53 | $9.71 | $1.94 |
| Standard one side | $25.56 | $8.21 | $33.77 | $6.75 |
| Standard two sides | $51.12 | $16.42 | $67.54 | $13.51 |

That table also separately lists parts, feeder loading, manual assembly,
handling, fixtures and other fees. Board size/service eligibility and final
pricing require a real quote. None of the three combined figures includes
PCB fabrication, components, module/Pico/battery/charger sourcing, custom
fixtures, wire assemblies, metrology, programming/testing, shipping or tax.
Do not use $67.54 as the price for five assembled instruments.

## Quote worksheet

Obtain the following lines for both complete and SMT-only alternatives:

| Cost line | Complete five | SMT-only five | Evidence needed |
|---|---|---|---|
| Five 330 × 121.5 mm, two-layer carriers | Pending | Pending | Accepted stackup, finish, panel rails and process |
| SMT setup/stencil/parts/labor | Pending | Pending | Exact MPN BOM, 30 SMT/board, U2 stencil and C17/C18 lands |
| THT parts/labor | Pending | Excluded or separately priced | 17 THT/board, bottom H1, socket fit/edge handling |
| Ten ST0238 + fifty exact touch modules | Pending | Separate | Delivered revision, stock and module-end geometry |
| Five Pico H SC0917 | Pending | Separate | Original Pico H; other models deferred |
| Sixty module harnesses + five battery harnesses | Pending | Separate | Qualified crimps, adapted ends, measured lengths |
| Five holder/cassette/fixture/support sets | Pending | Separate | MPD BH-18650-W and final measured mechanical CAD |
| Five protected 18650 cells + one proposed shared charger/input set | Pending | Separate | Exact button-top opposite-end cell lot, fit and charging tolerance; shared quantity assumption HOLD |
| First-article metrology/qualification | Pending | Separate | Fit and current-limited bench record |
| Programming and all-five functional testing | Pending | Separate | Accepted firmware and per-unit records |
| Shipping/tax | Pending | Pending | Battery shipping and delivery terms |
| Optional sixth bare keepsake | Additional line | Additional line | Adds one fabricated unpopulated carrier |

`complete batch total = sum of accepted complete-five lines`

`SMT-only finished batch total = SMT quote + all separately completed lines`

Divide the complete total by five only after all required lines are included.
The difference measures the price of outsourcing the remaining work; it is
not a savings if that work is simply omitted. Fixed fixture/metrology costs
can dominate a small first run. A first-article checkpoint within the five-unit
order reduces the chance of repeating an unverified fit in all five units.

PCBWay describes [through-hole assembly](https://www.pcbway.com/pcb_prototype/Through_Hole_Assembly.html)
and [turnkey/consigned sourcing](https://www.pcbway.com/quotesmt.aspx).
Those services do not establish acceptance of our custom instrument assembly.
No shopping, automatic upload, supplier messaging or purchasing is authorized
by this worksheet. It is ready for the owner's review; manufacturing release
still requires the named fit/process evidence.
