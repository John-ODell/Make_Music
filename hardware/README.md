# Make Music PCB

This directory contains the developing design for a battery-powered touch instrument based on the existing Pico firmware.

- [Design requirements and provisional pin allocation](PCB_DESIGN_NOTES.md)
- [Component arrangement sketch](pcb-layout-concept.svg)
- [Helper tasks and integration plan](HELPER_TASKS.md)

Current state: design concept and requirements only. There is no fabrication-ready schematic or PCB yet.

## Milestones

1. Identify actual Pico, touch modules, buzzer modules, battery and charging requirements.
2. Verify Pico sockets, connector pinouts and battery power architecture.
3. Build and review the editable KiCad schematic.
4. Place verified footprints and agree on board/enclosure dimensions.
5. Route, run ERC/DRC, inspect the 3D model and review electrical/mechanical fit.
6. Generate reviewed manufacturing files and BOM; obtain a fabrication/assembly quote.
7. Assemble and test a prototype before a larger order.

Do not order from the concept sketch. Existing code drives both buzzers at one pitch; independent voices would require a pin and firmware change.
