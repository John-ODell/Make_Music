# Hardware work instructions

## Agreed design

Read PCB_DESIGN_NOTES.md first. Build a two-layer Pico carrier for eight note touch controls and two left-hand modifiers, two passive buzzers, exposed unused GPIOs, a removable Pico in female sockets, and battery power. The SVG is a concept illustration, not a scaled footprint or approved board outline.

Current user decisions supersede older research: original Pico H SC0917, removable female sockets, ten touch modules (eight notes plus two left-hand modifiers), two passive buzzer modules, protected removable **long 18650** with external charging. The earlier 18350 name was a mistake. On October 15 the user revised delivery to **two complete factory-assembled instruments and three populated carriers**, five carriers total. All five retain all 47 purchased carrier parts; only two receive controllers, external modules, harnesses, batteries and full mechanical/programming/test work. The optional sixth bare keepsake is not included in this revised count. Generic TTP223 and 3.3V transistor-driven low-trigger passive buzzer modules may be priced as alternatives to the HiLetgo/ST0238 references; actual-part fit and electrical behavior still require verification. See assembly/REVISED_QUOTE_2_COMPLETE_3_CARRIERS.md. No actual parts are available; precise metrology may be quoted to the assembler. Preserve current carrier_prototype.py pin assignment as the provisional baseline. The user permits firmware changes; adapt confirmed touch polarity in software. User prefers roughly half-to-one finger gaps; 10 mm clear gap /34 mm center pitch is the proposal. Screens/keypads/extra percussion/other Pico models are future revisions. Label assumptions visibly. Do not invent module pin orders, current/charging compatibility, physical fit or manufacturing approval.

## Coordination

Work on the assigned codex/* branch in the supplied workspace. Keep changes in the assigned paths. Fetch origin before work; inspect changes before committing. Never overwrite another session's work or force-push shared branches. Prepare a focused PR with validation results. The primary chat integrates helper PRs; helpers should not merge them.

## KiCad quality

Use editable native KiCad files and project-local libraries for custom parts. Verify symbols against official pinouts and footprints against manufacturer mechanical drawings. Distinguish physical pin numbers from GPIO numbers. Verify socket row spacing, USB/BOOTSEL access, insertion clearance, battery-holder clearance and mounting. A bare Li-ion cell must not directly feed GPIO/3V3. Provide protection and USB/battery source isolation; onboard charging requires a suitable charger/power path and battery-matched charge current.

All KiCad source mutations must use Konnect MCP, with one CAD mutation owner.
Never text-edit protected KiCad source/libraries or use pcbnew/SWIG. Read the
Konnect reliability contract; bind the exact document, inspect full responses,
and verify actual readback. Exported netlists and ordinary documentation are
separate from native source. Preserve unrelated media and KiCad history.

Before fabrication, the integrated project needs electrical-rule and design-rule checks, reviewed intentional exceptions, netlist/PCB agreement, verified actual components, and a visual review. An empty board or schematic, or an unrouted board with unconnected nets, is not a completed design. Do not export files as production-ready while unresolved requirements remain.

Record what was verified, remaining uncertainty, and relevant source URLs. Avoid generated logs/backups and unrelated media in commits. No ordering, purchasing, or sending messages outside the authorized GitHub workflow.
