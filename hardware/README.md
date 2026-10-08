# Make Music PCB

This directory contains the developing design for a battery-powered touch instrument based on the existing Pico firmware.

- [Design requirements and provisional pin allocation](PCB_DESIGN_NOTES.md)
- [Component arrangement sketch](pcb-layout-concept.svg)
- [Helper tasks and integration plan](HELPER_TASKS.md)
- [Factory assembly and budget comparison](ASSEMBLY_BUDGET.md)
- [Editable KiCad carrier schematic](kicad/README.md)
- [Mechanical fit proposal](mechanical/README.md)
- [Battery power alternatives](power/README.md)

Current state: an editable provisional carrier schematic, candidate Pico socket footprint, mechanical reservation plan, and researched power alternatives. The complete instrument power circuit and PCB layout are not yet finalized or fabrication-ready.

## Milestones

1. Identify actual Pico, touch modules, buzzer modules, battery and charging requirements.
2. Verify Pico sockets, connector pinouts and battery power architecture.
3. Build and review the editable KiCad schematic.
4. Place verified footprints and agree on board/enclosure dimensions.
5. Route, run ERC/DRC, inspect the 3D model and review electrical/mechanical fit.
6. Generate reviewed manufacturing files and BOM; obtain a fabrication/assembly quote.
7. Assemble and test a prototype before a larger order.

Do not order from the concept sketch. Existing code drives both buzzers at one pitch; independent voices would require a pin and firmware change.
