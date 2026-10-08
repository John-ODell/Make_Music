# Hardware work instructions

## Agreed design

Read PCB_DESIGN_NOTES.md first. Build a two-layer Pico carrier for eight note touch controls and two left-hand modifiers, two passive buzzers, exposed unused GPIOs, a removable Pico in female sockets, and battery power. The SVG is a concept illustration, not a scaled footprint or approved board outline.

Exact Pico version, touch/buzzer module part numbers, battery type and dimensions, charging preference, and final pitch behavior remain unresolved. Preserve the existing firmware pin assignment as the provisional baseline. The user permits firmware changes; adapt confirmed touch polarity in software when appropriate rather than insisting on module hardware changes. User prefers roughly half-to-one finger gaps between keys; 10 mm clear gap / 34 mm center pitch is the current proposal. Factory assembly as much as possible is preferred, with a partial-assembly budget comparison. Label assumptions visibly. Do not invent module pin orders, charger current, battery-holder dimensions, or manufacturing approval.

## Coordination

Work on the assigned codex/* branch in the supplied workspace. Keep changes in the assigned paths. Fetch origin before work; inspect changes before committing. Never overwrite another session's work or force-push shared branches. Prepare a focused PR with validation results. The primary chat integrates helper PRs; helpers should not merge them.

## KiCad quality

Use editable native KiCad files and project-local libraries for custom parts. Verify symbols against official pinouts and footprints against manufacturer mechanical drawings. Distinguish physical pin numbers from GPIO numbers. Verify socket row spacing, USB/BOOTSEL access, insertion clearance, battery-holder clearance and mounting. A bare Li-ion cell must not directly feed GPIO/3V3. Provide protection and USB/battery source isolation; onboard charging requires a suitable charger/power path and battery-matched charge current.

Before fabrication, the integrated project needs electrical-rule and design-rule checks, reviewed intentional exceptions, netlist/PCB agreement, verified actual components, and a visual review. An empty board or schematic, or an unrouted board with unconnected nets, is not a completed design. Do not export files as production-ready while unresolved requirements remain.

Record what was verified, remaining uncertainty, and relevant source URLs. Avoid generated logs/backups and unrelated media in commits. No ordering, purchasing, or sending messages outside the authorized GitHub workflow.
