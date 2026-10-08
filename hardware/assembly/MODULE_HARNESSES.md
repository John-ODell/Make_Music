# Twelve module cable assemblies — carrier end specified

Updated 2026-10-08. Factory scope includes the cables and module attachment; Pico and protected cell remain removable user insertions. This specification resolves the carrier connector end. Module end geometry and installed cable length require an actual-part fit check. No cables were purchased or assembled.

## Carrier connector and conductors

For each of J3–J14 use one Harwin **M20-1060300** 3-position female housing with three **M20-1180046** tin-finish loose crimp contacts. Twelve carrier ends require **12 housings and 36 contacts**. These mate to the selected 0.64 mm square male contacts at 2.54 mm pitch. Use flexible stranded **AWG26** wire, insulation outside diameter no greater than the contact/tool's 1.7 mm allowance. Carrier assignment is cavity1 signal (white), cavity2 regulated 3V3 (red), cavity3 GND (black). Colors are assembly aids; verify continuity by cavity number.

Engineering cut-length allowance is **100 mm per conductor**, 36 conductors / 3.6 m total before process scrap. This is an initial allowance, not measured installed length. Adjust in the fixture mock-up to leave service slack without crossing touch faces, buzzer openings, Pico USB/BOOTSEL/removal access, switch travel or the battery cassette. Secure the cable to the fixture independently of contact friction; keep all wire ends insulated.

The housing is unkeyed on our unshrouded carrier header. Mark its signal end and align it with the square pad / pin1 label. Add a visible orientation mark to the assembled harness, and inspect all three circuits before power. A three-position plug can still be reversed or shifted; retention/orientation control is part of the fixture trial.

Harwin's manufacturer pages specify the mating contact size, housing family and contact AWG range. The IS-15 crimp-tool sheet specifies 4.0 mm maximum stripping length, 1.7 mm maximum wire diameter and **18 N minimum pull-off force for AWG26**. Use suitable production tooling/process; do not apply a destructive qualification pull to every installed board contact. Assembler validates the crimp process and contact retention on representative samples.

## End-to-end mapping

| Carrier | Function | Signal destination |
|---|---|---|
| J3 | C4 / GP16 | Touch DI/OUT |
| J4 | D4 / GP17 | Touch DI/OUT |
| J5 | E4 / GP18 | Touch DI/OUT |
| J6 | F4 / GP19 | Touch DI/OUT |
| J7 | G4 / GP20 | Touch DI/OUT |
| J8 | A4 / GP21 | Touch DI/OUT |
| J9 | B4 / GP22 | Touch DI/OUT |
| J10 | C5 / GP26 | Touch DI/OUT |
| J11 | Semitone / GP27 | Touch DI/OUT |
| J12 | Octave / GP28 | Touch DI/OUT |
| J13 | Buzzer1 / GP13 | ST0238 I/O |
| J14 | Buzzer2 / GP12 | ST0238 I/O |

Every red conductor goes to the module's verified VCC; every black conductor goes to its verified GND. The official ST0238 photo shows GND, I/O, VCC top-to-bottom with buzzer left / contacts right. Therefore its cable is permuted relative to carrier SIG, 3V3, GND. Do not specify a universal straight-through cable. See [carrier interface evidence](../kicad/carrier-interfaces.md).

Module-end socket MPN cannot be frozen until the delivered header pitch, contact section, engagement length, pin order and connector access are measured. If a module lacks the anticipated male header, prepare a drawing for that termination before assembly. The factory must source or receive the exact module revision and build/inspect the adapted cable; this remaining work is not assigned to the user as unannounced soldering.

## Inspection record

With no battery, USB, Pico or modules connected, verify each harness's signal/VCC/GND continuity and absence of cross-shorts, orientation marks and strain relief. Verify the carrier labels against the schematic and the module labels against the delivered revision. Complete module polarity/momentary-output checks on a current-limited 3.3 V supply before plugging into Pico GPIO. Record actual cable lengths and connector revisions in the assembly traveler.

Battery wiring uses a separate keyed JST-PH harness, **AWG24**, with the project's own positive/ground cavity convention; do not mix it with these 3.3 V module cables. See [battery cassette/harness specification](../mechanical/WIRED_HOLDER_PROPOSAL.md).

## Primary sources checked 2026-10-08

- [Harwin M20-1060300](https://www.harwin.com/products/M20-1060300): 3-way housing, mating 0.64 mm square pins, compatible contacts.
- [Harwin M20-1180046](https://www.harwin.com/products/M20-1180046): loose tin female contact, AWG22–30, M20-106 family.
- [Harwin IS-15, issue8](https://www.harwin.com/api/download/?document=https%3A%2F%2Fcontent.harwin.com%2Fm%2F7d24feda1954c6ac%2Foriginal%2FIS-15-IS-15-Z20-320-Hand-Crimp-Tool-Instruction-Sheet.pdf): strip/insulation/pull-force data.

Ratings do not verify the assembled module-end fit, cable life or polarity. Those named physical checks remain open.
