# Electrical integration evidence — review hold

Captured 2026-10-09 through Konnect 0.13.0 / KiCad 10.0.6. Native source hashes
in source-checkpoint.json bind this saved-board snapshot. Recreate evidence
after CAD/library changes; do not reuse a stale passing summary.

Run from repository root:

    python3 hardware/kicad/verify_connectivity.py hardware/review/integration-20261009/netlist.xml
    python3 hardware/kicad/verify_board.py hardware/review/integration-20261009

The first checks the independently reviewed circuit/parts contract. The second
compares the fresh native XML with all live IPC pad nets, values and footprint
IDs and a guarded identity-sync noop. It checks source hashes and complete
saved/refilled all-severity ERC/DRC evidence. No pcbnew/SWIG is used.

Observed: 48 electrical parts, 17 mounts, 166 endpoints, 405 trace segments;
ERC 0, copper/layout DRC 0, unconnected 0. Overall DRC remains four warnings:
C17/C18 missing Header and J1/J2 missing MPN in board custom fields. Their
exact references/UUIDs/descriptions are reviewed only for electrical integration.
Native XML holds the correct Header and MPN values; no field is substituted or
removed to silence DRC. Konnect's current sync omits custom field copying.

placement-score-mcp.json reports socket courtyard edge overhang of 0.73 mm.
This remains a physical rear-edge/lip acceptance requirement; no placement
score pass or actual component fit is claimed. Cable connectors are intentionally
internal; aggregate heuristics do not supersede direct circuit/layout checks.

Manufacturing, actual module/cell/holder fit, socket engagement, final mechanical
CAD, supplier process acceptance and current-limited bench tests remain held.
These are design review files, not files to upload or order.
