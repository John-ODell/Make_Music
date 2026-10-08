# Native PCB P1 — carrier placement and routing work

Updated 2026-10-08. Open `make_music.kicad_pro` in KiCad 10. The editable PCB now has all assigned carrier parts: removable Pico sockets, twelve module cable headers, free-GPIO header, bottom battery JST, switch, the interim isolation diode, two buzzer pull-ups and twelve local bypass capacitors. Eight board-only M3 clearance holes implement the corner support and independent battery-cassette interfaces. This checkpoint is **unrouted and not for fabrication**; the reviewed eFuse contract is being integrated before final routing.

## Geometry and connections

Two copper layers, provisional 1.6 mm board, proposed 330 x 120 mm outline. PCB coordinates are mechanical proposal coordinates plus (+20,+20) mm. All existing socket positions/nets remain aligned with `socket-placement.csv`; J1 pad1 is at (131.11,21.30), J2 pad1 at (148.89,69.56), rotation180. The bottom H1 JST is flipped in KiCad; contact1 remains positive through that flip.

The ten 26 x 26 mm touch-body rule areas exclude copper pads, tracks, vias and pours on both faces. These areas allow 1 mm around the user-supplied 24 mm bodies; they are engineering clearances, not a measured sensing-field limit. The battery cassette excludes underside copper fill and vias. The eight M3 positions have 8 mm diameter copper/component reservations. Board mounting holes are 3.2 mm NPTH; these independent fixture dimensions do not reuse an undocumented module or holder hole pattern.

J3–J14 carrier pin order is defined 1=SIG,2=3V3,3=GND, independent of module physical order. The wiring specification is `../assembly/MODULE_HARNESSES.md`. Note/modifier centers and 10 mm note gaps remain the proposal. Body rectangles are references on Dwgs.User, not direct module mounting footprints.

## Checks at this checkpoint

KiCad 10.0.6 loaded/saved/reloaded all forty footprints (32 electrical +8 mechanical). Native DRC reports **zero geometry/silkscreen violations**, **91 unconnected items** and **one missing-footprint parity issue (TP1)**. No exclusions hide these conditions. Current complete carrier netlist verifies 128 endpoints in the schematic; the planned `verify_board.py` comparison will be run against the integrated routed board.

A temporary Freerouting 2.4.1 trial connected all currently placed nets with zero remaining unconnected items and zero copper geometry violations. It was imported to a temporary board outside the repository and is not the final protected power design. The final route must use the incoming eFuse circuit and net classes. Saved design rules use 0.30 mm default signal width, 1.50 mm power width and 0.18 mm local control width; 0.15 mm absolute minimum clearance/width is for the tiny eFuse escapes. Fabricator/process acceptance is still required.

## Work remaining

Integrate U2 TPS259474LRPWR, upstream fuse and support circuitry from power PR18, remove carrier D1, assign TP1, then route and review. Integrate raised module-fixture attachment points without inventing module holes. Finish filled ground planes, full schematic parity/ERC/DRC, readable assembly views, complete BOM and held review exports. Actual module terminations, protected-cell/holder fit, switch/socket engagement, touch response, sound/current and power bring-up remain physical verification gates. Do not place a fabrication/assembly order from this checkpoint.
