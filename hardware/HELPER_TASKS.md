# Helper sessions

All helpers read `hardware/AGENTS.md` and `hardware/PCB_DESIGN_NOTES.md`. Use the assigned worktree and branch. Check scope against the current primary-chat decisions. Do not route a production board or finalize unidentified module footprints.

## 1. Schematic — codex/pcb-schematic

Own `hardware/kicad/` and `hardware/reviews/schematic.md`.

Create an editable KiCad 10 carrier schematic/project for the documented provisional GPIO allocation. Verify Pico physical pin mapping from Raspberry Pi documentation and represent the two removable 1x20 female sockets accurately. Include ten 3-pin touch-module interfaces, two buzzer-module interfaces, and labeled unused GPIO/3V3/GND expansion. Module connector ordering is unconfirmed: clearly mark provisional choices and leave module-specific footprints unassigned until identified. Keep power as clearly labeled interface points for the separate power review; never imply a raw battery-to-3V3 connection. Use local libraries as needed. Export a readable schematic review, run ERC, and document actual findings and unresolved power/module issues. Do not treat passing ERC as proof of component compatibility. Commit, push, open a focused PR, attach it to the helper chat and leave it for primary integration.

## 2. Power — codex/pcb-power

Own `hardware/power/`.

Research and propose battery/USB power for a socketed Pico instrument: protected single-cell conventional Li-ion/LiPo, power switch, source isolation and regulated module power. Compare removable externally charged 18350 versus onboard USB charging with proper power-path management. Verify against primary datasheets. Provide candidate parts with exact MPNs, circuit drawings or editable KiCad sheet where justified, BOM, current-budget worksheet and open decisions. Charging current and physical battery choice must remain conditional until the actual cell is selected. Verify the Pico USB/VSYS interaction and behavior with battery present. Do not edit the main KiCad project. Commit, push, open and attach a focused PR; leave it for primary integration.

## 3. Mechanical and footprints — codex/pcb-mechanical

Own `hardware/mechanical/` and `hardware/libraries/`.

Verify the removable Pico female-socket geometry using official mechanical drawings. Specify exact candidate sockets and inspect available KiCad footprints; create project-local footprints only when needed and include dimensional evidence. Investigate underside PCB-mounted 18350 holder options, protected-cell fit, standoffs, enclosure clearance, and supplier assembly support. Keep all unidentified touch/buzzer module geometry provisional. Preserve eight ascending notes across the front and semitone/octave controls on the left. Provide a dimensioned proposal with explicit assumptions, source links, and fabrication/assembly considerations. No copper routing or edits to the main schematic. Commit, push, open and attach a focused PR; leave it for primary integration.

## Primary integration

Resolve parts and behavior with the user, review helper results, combine the selected power design and verified footprints with the schematic, then commission routing. Verify every used GPIO and power net, current budgets, connector polarity and all mechanical clearances before manufacturing exports. Keep PR descriptions accurate about provisional versus verified work.
