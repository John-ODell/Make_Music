# Native PCB: initial placement draft P0

Updated 2026-10-07. Open `make_music.kicad_pro` in KiCad, then PCB Editor. The editable `.kicad_pcb` exists; it is **incomplete, unrouted and not for fabrication**. Do not order it or export it as a manufacturing release.

## Present in the board

- Two copper layers and provisional 1.6 mm thickness, with the proposed 330 x 120 mm rectangular outline.
- J1/J2 native local Samtec socket candidates with all 40 pad nets and schematic UUID associations. J2 is rotated 180 degrees, with pad 20 at the USB end.
- Reference-only body rectangles on Dwgs.User for eight note touch modules, two left-hand modifiers, two 32 x 14 mm ST0238 buzzer modules, Pico body and battery/power/expansion reservations. These rectangles are not component footprints, mounting holes, copper keepouts or manufacturing instructions.
- Existing KiCad project settings were expanded by KiCad's native board writer; defaults are not an agreed fabricator specification.

Board coordinates are translated by (+20,+20) mm from `../mechanical/socket-placement.csv` and the mechanical proposal, so the proposed rear-left outline corner is (20,20) mm. J1 pad 1 is (131.11,21.30), rotation 0; J2 pad 1 is (148.89,69.56), rotation 180. All 40 pad locations were independently compared with the CSV and their net assignments with a fresh schematic netlist.

## Actual checks and limitations

KiCad 10.0.6 loaded/saved/reloaded the board and exported a temporary placement PDF for visual review. Socket positions and orientation, 40 pad nets, two-layer count and lack of routing were checked. The temporary files stay outside the repository.

DRC with schematic parity is deliberately **not passing**: the current draft has seven unconnected items (shared socket nets) and 17 missing component footprints. No geometry violations were reported for this limited content. Those results cannot certify a complete instrument, and no rule exclusion was added to conceal missing components or connections.

The omitted footprints are D1, H1, S1, TP1, J3-J15. Only socket footprints were assigned in the schematic, so the PCB does not invent the remaining part geometry. The earlier 1095P holder footprint was withdrawn; no holder holes are included. No touch/buzzer mounting holes, carrier mounting holes, bottom-side holder placement, traces, vias or copper zones are supplied yet.

## Remaining implementation

Finish branch fault/reversal protection and verified connectors/part footprints. Add actual components through KiCad's Update PCB from Schematic workflow, preserving references and UUID associations. Reconcile the protected-cell holder and module mounting/cable arrangements, then finalize the outline and mounting features after the paper fit review. Route all nets, add suitable ground/decoupling and power layout, and perform complete schematic parity, ERC/DRC, polarity and mechanical reviews.

Only after those checks can the project supply a reviewed Gerber/drill package, assembly BOM/placement files, assembly instructions and meaningful quote comparison. Five bare PCBs and five assembled instruments remain separate quantities.
