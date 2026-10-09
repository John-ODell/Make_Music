# Final carrier export review — 2026-10-09

REVIEW ONLY — DO NOT ORDER OR UPLOAD.

Native design is root 21b2108: 330 x121.5 mm, native corners
(20,18.5)..(350,140). Later commits change ordinary documentation only.
The source checkpoint and original 18-artifact hashes bind the reviewed exports.

Independent power helper checked all 47 placements, rotations and sides
against recorded IPC, defined aperture/macro references in all eight layers,
a closed four-segment outline, 130 PTH drill hits (97 component holes and
33 vias), and all 17 NPTH 3.2 mm holes. Full pipeline passed 47/30/17 and
changed U2 rotation/C17 displacement rejected before destination creation.
See independent-export-review.txt. This is exported-data and recorded-evidence
review, not a new live ERC/DRC, graphical inspection or physical test.

PM loaded the final eight-layer job and both drill sets in native Gerber
Viewer. Whole front copper/mask/legend, whole back copper/mask/legend,
isolated back mask/legend and isolated top paste were inspected. Registration,
rear outline/socket markers, mounting-hole exclusions and H1 bottom legend
agree. No paste appears on through-hole/socket positions. Bottom legend is
mirrored in the through-top view. Detailed cursor navigation was unreliable.
The actual paste layer was printed locally from Gerber Viewer to PDF and its
power-section crop inspected: separate fine apertures and split centre area
are visible. This does not certify stencil thickness or solder yield.

All five native drawing pages were rendered and inspected: two schematic
pages, top assembly, bottom-through-top assembly and copper layout. They show
the current long 18650 reservation, C17/C18, relocated J3/J4 and final edge.
Both updated paper-fit Letter pages from mechanical PR34 were also rendered
and inspected; scale bars, labels and registration crosses are readable.

PM additionally printed the actual isolated front copper, front mask and front
legend from Gerber Viewer to local PDFs. Enlarged power crops show distinct
fine copper/mask apertures, the U2 orientation dot, D2 K mark and S1 3/ON,
2/COM,1/OFF numbering. Buzzer/note headers show1:S,2:3V3,3:G; C17/C18
and relocated J3/J4 labels agree with recorded IPC and assembly views.
The local fit-to-page prints are inspection aids, not dimensioned fabrication
outputs. Whole-layer, detail and all native PDF page visual review is complete
within this stated scope. Process margins still require factory acceptance.

External release holds: exact parts,
module pin/header/support geometry, Pico socket engagement/USB access,
18650/holder fit and current capability, qualified harness/crimps, final
mechanical tolerances/retention, charger voltage pairing, factory stencil/
annular-ring/land/panel/orientation acceptance and first-article/all-five
bench tests. No physical fit, supplier acceptance or fabrication release.
