# First-prototype carrier — final integration / manufacturing hold

Updated 2026-10-09, KiCad 10.0.6 / Konnect 0.13.0. The proposed 330 ×121.5 mm
carrier retains eight notes, two left modifiers, removable original Pico H,
two ST0238 module interfaces and exposed GPIO. The corrected cell is **long
protected 18650**, externally charged. Five complete instruments and an
optional additional bare keepsake are the selected assembly scope.

## Actual current checks

The merged root schematic has **48 physical parts /166 endpoints**. Fresh
independent ERC reported zero findings. `verify_connectivity.py` confirms all
166 endpoints, 38 connected nets, six intentional NC nets, all 41 mapped power
endpoints and exact assigned footprint pads. All 162 original endpoints and
46 component identities/values/footprints were independently retained in the
capacitor update.

**Electrical PCB integration is complete; manufacturing release remains held.**
The saved/refilled board has 48 electrical footprints plus 17 mounting holes,
405 trace segments and the inherited 33 vias. Fresh all-severity DRC reports
**0 copper/layout violations, 0 unconnected items, and 4 metadata parity
warnings**: missing Header fields on C17/C18 and missing MPN fields on J1/J2.
No DRC rule was disabled or excluded. Overall DRC is four warnings, not zero.

A task-local exported-netlist adapter resolves the exact current-root identity
compatibility defect in [Konnect723](https://github.com/mixelpixx/Konnect/issues/723).
PM reviewed the code and reran all 21 refusal/passthrough tests. The apply added
only C17/C18; all 63 existing footprint placements/values/library IDs remained
unchanged. Library refresh, moves and routing used Konnect MCP only. A fresh
identity preview returns noop, with no conflicts, reassigned pads or missing
footprints. Custom fields remain a [Konnect788](https://github.com/mixelpixx/Konnect/issues/788)
limitation; all native schematic MPNs remain intact and authoritative.

The [source-bound review evidence](../review/rear-edge-20261009/README.md)
contains fresh native XML, ERC/DRC and live IPC readback. Every one of 166 pads
agrees with XML; all 48 values and full footprint IDs agree. The new board
verifier uses these exports and does not load pcbnew/SWIG. Tests reject wrong
nets/values, saved readback, pending identity changes, unreviewed warnings,
copper errors and stale sources; disabling the pad guard makes its negative
control fail as expected. These four exact metadata warnings are reviewed for
electrical integration only, not blanket fabrication approval.

## Changes saved and verified

- C17 is native (87.46,65.50), C18 (125.46,65.50), both top/0 degrees.
  Their power and ground branches use 0.30 mm copper beside C11/C12; all pad
  geometry/nets were read back and the exported detail was visually inspected.
- J3/C4 and J4/D4 anchors moved only from native y95 to y98, mechanical y75
  to y78, retaining x/rotation. Their copper/captions were updated. This clears
  the two buzzer body projections; dressed cable fit is still unmeasured.
- H1 moved from native (249,40) to **(289,40)**, mechanical (269,20), retaining
  bottom side/rotation and circuit1 positive/circuit2 ground. Live pad readback
  confirms both nets and positions. The positive route was rerouted with its
  existing 1.5 mm width and 5 mm fuse approach retained. Old ground branches
  were removed; ground pours connect the moved pad after refill. DRC verified
  its copper clearance and zero unconnected items.
- Visible Dwgs.User reservations mark the 112 ×36 mm cassette and maximum
  78.20 ×21.40 mm holder body. Eight imported bars were read back separately;
  a first grouped SVG import did not preserve the intended result and was
  removed before retry. These graphics are review geometry, not copper rules.

## Geometry, rules and assembly

The established mechanical/service datum remains native(20,20), with x/y
down. Native coordinates add(20,20); the new rear edge is mechanical y=-1.5.
Do not redefine that datum to the new physical corner. Socket
rows remain17.78 mm apart; actual Pico H SC0917/socket engagement, rear lip,
USB/BOOTSEL access and removal remain physical/process gates. The rear edge was extended through Konnect to native y18.5, giving a
330 ×121.5 mm board without moving components, tracks or mounting holes.
Nominal socket bodies have 1.275 mm rear margin; courtyards have 0.77 mm.
The final scorer reports zero hard failures. A first y19 trial clipped the
J1 pin-1 marking; the final y18.5 outline clears the marking with no edge
DRC finding. Actual engagement/lip and factory handling still need acceptance. The internal cable-header edge-distance
heuristic does not establish a defect in this carrier arrangement. Ten26 ×26 mm
both-face touch exclusions and seventeen3.2 mm NPTH mounts remain fixed.
Four cassette mounts stay at mechanical(150,17),(210,17),(150,43),(210,43).
Their Ø8 bolt exclusions remain enforced.

MPD **BH-18650-W** has factory AWG24 leads. The insulating review cassette
extends native(165,32)..(277,68), with lowered holder plane z16, 44 mm total
height and **≥47 mm underside supports**. It needs final measured retention,
platform/door/overhang CAD. The inherited B.Cu restriction native(165,32)..
(235,68) is deliberately retained and labeled **partial**. It forbids vias
and fill there, not tracks/pads. Konnect has no rule-area CRUD; no enlargement
is claimed. The lowered insulating platform permits copper under the enlarged
bay, while ≥2 mm actual loaded clearance to parts/tails/wires remains required.

Default clearance0.25 mm; normal signal width0.30 mm. Local U2 control routes
use0.18 mm with a bounded0.15 mm package clearance rule. Long power routes
use2.0 mm; locked branch routes1.5 mm with5 mm fuse approaches. U2 closest
copper gap0.20 mm, nominal mask web0.10 mm and TI example0.100 mm stencil
need factory process acceptance. Nominal socket annular ring0.25 mm and rear
edge margins need acceptance. All SMT is top; H1 is bottom THT. Factory
panel rails/fiducials/tooling and depanel/THT order are still to be agreed.

C17/C18 are10 µF/10 V/X7R **TDK C2012X7R1A106K125AC**, on 3V3_OUT/GND at
J13/J14, retaining C11/C12. Their standard KiCad0805 lands have a documented
pad-length/width deviation from TDK's example; accept or revise before release.

## Exports and remaining work

The checked-in `manufacturing/REVIEW_ONLY_DO_NOT_ORDER` files are **obsolete**:
they predate these connector/capacitor/18650 changes and use a different origin.
No current passing manufacturing manifest is claimed. The legacy generator
refuses to run. Follow [fresh Konnect export procedure](../manufacturing/README.md)
only after final PCB sync/placement/routing and independent review.

New native Gerbers, drills and positions must agree on(0,0), x right/y up,
board(20,-18.5)..(350,-140) mm. Do not mix older auxiliary-bottom-left files.
Expected new BOM is47 purchased parts:30 top SMT and17 THT; Pico/modules/
harnesses/mechanics are separate in the [five-unit handoff](../assembly/PCBWAY_HANDOFF.md).

Finish the held export postprocessor, drawings and actual Gerber/drill viewer
review. Fresh native raw exports exist, but their final package is not yet
accepted or published; the source-bound postprocessor now accepts only the four exact reviewed
metadata warnings and retains them in the report. Its real 47-part pipeline
passed; wrong-net, new-warning and stale-source cases refused before output.
Then complete the [actual-part fit checklist](../assembly/FIT_CHECKLIST.md),
cell/charger matching, final mechanical CAD, supplier acceptance and
[current-limited bench qualification](../power/prototype-validation.md).
No physical fit, bench result, runtime, complete quote or fabrication release
has been established. The paper-fit PDF checks overall comfort only.
