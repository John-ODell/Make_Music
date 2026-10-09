# Make Music P1 — held manufacturing review

REVIEW ONLY — DO NOT ORDER OR UPLOAD.

This package derives from the revised long protected 18650 carrier, including
C17/C18, moved J3/J4 and underside H1. It uses native (0,0), x right/y up;
board corners (20,-20)..(350,-140) mm. Do not mix with obsolete exports.

47 purchased carrier parts: 30 top SMT and 17 THT. Use pcbway-centroid-smt.csv
for machine placement; manual-tht-positions.csv describes the THT assembly.
pcbway-bom-five.csv requests five complete instruments. Modules, Pico, holder,
battery, harnesses and mechanical work are additional scope in PCBWAY_HANDOFF.md.
An optional sixth bare keepsake is separate.

Read validation-summary.json and verification/ for the actual check scope.
Overall DRC retains the reviewed connector metadata warnings; electrical
integration has zero ERC/copper/layout/unconnected findings. No DRC categories
or findings are hidden. Physical fit, socket rear-edge/lip acceptance, final
mechanical CAD, charger matching, factory process/orientation acceptance and
bench qualification remain required. Gerber/drill and all drawing viewer
review must finish before this package can be accepted for the next stage.

No fabrication release, complete quote, runtime or hardware success is claimed.
