# Raised module fixture — dimensioned prototype proposal

Reviewed 2026-10-08. Propose one machined **unfilled acetal insulating plate**, open-backed seats, and removable insulating edge keepers for all ten touch boards and both ST0238 boards. Nothing passes through a module's undocumented mounting holes. Module wiring uses flexible, factory-installed leads; headers and solder joints carry no playing load. This is an engineering fixture proposal, **not verified actual-part fit, a strength certification, or manufacturing CAD**.

The editable [plan and detail drawing](module-fixture-plan.svg) and [carrier attachment CSV](fixture-mounting.csv) define the proposal. PM owns PCB edits. Dimensions use the carrier's top-view origin: rear-left (0,0), x right, y forward, millimetres. The PM's KiCad origin adds (20,20); both coordinate sets are in the CSV. z=0 is the carrier **top** surface, unlike the cassette document's underside z convention.

## Geometry and fixed carrier interface

Plate perimeter polygon, in order: **(2,36), (42,36), (42,56), (120,56), (120,68), (326,68), (326,119), (2,119)**. Bounding size 324 x 83. Main plate thickness **4 mm**, raised on **24 mm** custom insulating spacers (OD8, ID3.2), giving a module support plane z=28. Machine integral 1 mm-high locating fence segments from a 5 mm blank; main plate/fastener seats remain 4 mm thick. Stock material, machining radii, flatness and tolerances need fabricator agreement. Do not use carbon-filled plastic or conductive coatings.

Nine **3.2 mm NPTH carrier and plate holes**, with **8 mm diameter copper/component keepouts on both carrier faces**:

| ID | Mechanical (x,y) | KiCad (x,y) |
|---|---|---|
| F1 | (8,74) | (28,94) |
| F2 | (45,83) | (65,103) |
| F3 | (50,114) | (70,134) |
| F4 | (155,114) | (175,134) |
| F5 | (257,114) | (277,134) |
| F6 | (291,114) | (311,134) |
| F7 | (155,73) | (175,93) |
| F8 | (189,73) | (209,93) |
| F9 | (291,73) | (311,93) |

These are additional to the four corner supports and four cassette mounts; do not share bolts with the removable cassette. Plate-only 8 mm tool-access openings at the two existing front carrier supports (6,114) and (324,114) preserve access; the right opening forms an edge notch. No extra carrier holes are required for these openings. The minimum fixture attachment centre-to-plate-edge distance is 5 mm, leaving at least 1 mm beyond the 4 mm keepout radius.

## Twelve seats and removable keepers

| Boards | Centre coordinates | Nominal PCB body | Proposed seat opening / corner ledges |
|---|---|---|---|
| Eight notes C4..C5 | x=70,104,138,172,206,240,274,308; y=94 | 24 x 24, user reference | 24.6 x 24.6, with four integral 3 x 3 corner tabs retained in that opening |
| Semitone / octave | (24,54), (24,94) | 24 x 24, user reference | Same touch seat |
| Buzzer 1 / 2 | **(60,67.5), (98,67.5)** | 32 x 14, ST0238 listing | 32.6 x 14.6, with four integral 5 x 3 corner tabs |

The buzzer bodies move 1 mm left and 4.5 mm forward from the earlier body reservation, independently of the PM's fixed headers (61,49)/(99,49). Flexible leads bridge that offset. Body centres are not header pin coordinates. All touch centres, ascending order and left-hand modifiers remain fixed. Touch body gap remains 10 mm; fences extend the fixture width to 28 mm, leaving **6 mm between raised fence envelopes** at 34 mm pitch. Keeper hardware is concentrated along rear/front edges. Validate the assembled finger gap and reach; do not describe the complete fixture as having an unobstructed 10 mm gap.

For each touch seat, two diagonally opposed 2.2 mm **plate-only** keeper holes have local offsets **(-9.5,+14), (+9.5,-14)** from the module centre. Four underside corner tabs remain; the two keepers retain uplift rather than pressing every corner. Rock/lift and load trials remain necessary. Each stepped keeper is 6 mm wide x 6 mm deep x 1.5 mm upper thickness. Front keeper bounds are x=hole_x±3, y=centre_y+10.5..+16.5; rear is mirrored. Its underside pedestal occupies only y outside the seat boundary (|local y|≥12.3), with height **t**, the measured PCB thickness. This hard stop prevents screw tightening from bending the PCB. The overhang contacts nominal bare top-edge lands 5.5 x 1.5 near each corner; underside tabs overlap the nominal board by 2.7 x 2.7. Both contact regions must be free of pads, traces, components and electrode area on the actual module. Initial t=1.6 is a **shim/stack assumption**, not a measured module thickness.

For each buzzer, the two diagonal keeper hole offsets are **(-11,+9), (+11,-9)**; keepers are again 6 x 6 x 1.5 above measured t. Front bounds are x=hole_x±3, y=centre_y+5.5..+11.5; rear mirrored. Pedestals stay outside |local y|≥7.3. The wider corner ledges provide support beneath these keepers. Nominal bare top-edge contact is 6 x 1.5, with support overlap at least 2.7 x 1.5. Keepers avoid the centre sound opening; its actual position, diameter and height must still be checked. Do not clamp the sound can, header, components or solder joints.

Fence segments are 1.7 mm wide, 3 mm long, 1 mm high. East/west sides each have two segments at along-edge offsets ±7.5 for touch seats, ±3.5 for buzzers. Add a rear/north fence at local x=-7.5 for touch (-9 for buzzer), and a front/south fence at x=+7.5 (+9 for buzzer), on the **two corners without keepers**. These six segments restrain all four directions and avoid the keeper pedestals. They locate PCB edges with 0.3 mm nominal per-side clearance. Central north/south wiring remains open; its actual width depends on fence/header geometry. **Actual headers may require relocating fence segments or adding a wire notch.** Keep four-direction restraint and both diagonal keepers; do not remove a necessary stop and rely on friction. Window/ledge/keeper positions can be revised within the fixture without changing the nine carrier mounts.

## Clearance against the current carrier

Checked against the PM's 2026-10-08 placement handoff: J15 pad1 (50,12), vertical 16 ways at 2.54 pitch; note headers at their note x, y75; modifier headers (24,35)/(24,75); buzzer headers (61,49)/(99,49); power reservation x216..264,y44..68, switch centre (250,55); underside H1 pad1 (229,20). For conservative plan checks, reserve ±6 x ±4 around each module-header centre; this is a planning envelope, not a verified header body or pad1 convention. Expansion access is reserved x45..58,y8..55.1 (last pin y50.1 plus 5 mm). Pico/removal access extends to x104.5..135.5,y56; the fixture rear tongue starts at y56. All contacts with that service boundary are nominal and need actual tolerance/access checks.

Fixture holes and their 8 mm keepouts clear these reservations, the ten **26 x 26 touch-body copper keepouts**, both nominal buzzer bodies, cassette x145..215,y12..48 and its four bolts, battery connector access, and the corner supports. Some note headers lie below the buzzer seats, so keep all four corner tabs intact and provide vertical clearance rather than cut an aperture through a support. PM’s merged carrier interface specifies Harwin M20-999 headers with 2.54 mm insulator + 6.1 mm mating post = **8.64 mm nominal bare height**, before a female housing. Reserve **18 mm** for mated header/housing, joints and dressed wires as an engineering envelope, not a datasheet dimension. Exact mating cable selection and height remain required. The 24 mm stand-off is chosen to accommodate this envelope beneath module projections. Lift the removable fixture to mate/service covered headers; provide measured service-loop slack and strain relief without loops entering touch windows or the battery. Do not force a tall plug beneath the fixture.

At z=28, provisional module underside projection 6 mm, carrier mated-header/component envelope 18 mm, and fixture deflection allowance 0.5 mm leave **28−6−18−0.5 = 3.5 mm** before dimensional tolerances. Require at least **2 mm measured remaining clearance** after tolerance/deflection, including fastener tips, joints and wires. Increase spacers or relocate hardware if it fails. The quoted touch-board 7.2 mm overall height is not an underside projection or an enclosure stack. Actual buzzer height and total top enclosure height remain unmeasured. First-prototype Pico candidate is **Raspberry Pi Pico H SC0917**, with manufacturer-installed male headers, per PM selection and the official [Pico datasheet](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf) ordering table (local release21). The Samtec SSQ socket engagement, header/body height and plug/removal clearance remain actual-part fit checks; Pico 2 is not the current prototype candidate. Plate geometry leaves Pico, USB/BOOTSEL and vertical GPIO access open; verify with plugs fitted and during upward Pico removal.

## Hardware and factory assembly

Candidate natural nylon 6/6 hardware is documented in the [Essentra manufacturer catalog](https://essentracomponents.bynder.com/m/6e2e9b888468b393/original/2685970-pdf.pdf), visually checked at printed pp146,182,183,197 (PDF pp35,71,72,86). Material ratings apply to catalog parts, not the custom plate or whole instrument.

| Qty | Candidate | Source dimensions / purpose |
|---|---|---|
| 9 | 50M030050P035 | M3x0.5, 35 mm screw; head Ø5.3..5.6, height2.2..2.4; p146 |
| 9 | 04M030050HNDIN34814 | M3 nut, flats5.3..5.5, height2.2..2.4; p183 |
| 18 | MFW030A | M3 washer, ID3.2 OD7 thickness0.5; p197 |
| 9 | Custom acetal spacer | Proposed OD8 ID3.2 length24; dimensional design, not a sourced MPN |
| 24 | 50M020040P010 | M2x0.4, 10 mm keeper screw; headØ3.7..4.0, height1.4..1.6; p146 |
| 24 | 04M020040HN | M2 nut, nominal flats3.9, height1.2; p182; no locking feature or tolerance inferred |
| 48 | MFW010A | M2 washer, ID2.2 OD5 thickness0.3; p197 (MFW020A is for M2.5 and is not selected) |
| 20 + 4 | Custom stepped keepers | Touch + buzzer; thickness t+1.5 with relieved underside; exact t measured per lot |

M3 stack under the screw head: 0.5 washer + 4 plate + 24 spacer + 1.6 carrier + 0.5 washer + nut max2.4 = **33 mm**; M3x35 leaves nominal 2 mm beyond nut. M2 stack at assumed t=1.6: 0.3 washer + 1.5 keeper + 1.6 pedestal + 4 plate + 0.3 washer + nominal1.2 nut = **8.9 mm**; M2x10 leaves nominal1.1. Recheck actual tolerances, thread engagement, tool access and tip clearance; select another length if needed. No torque, pullout strength or long-term creep claim is made.

Factory scope includes machining/deburring/cleaning the plate, spacers and keepers; actual-module metrology and fixture fit; mounting the plate; installing all 12 modules and 24 keepers; making, labeling and testing 12 flexible harnesses; and retention/functional inspection. The prototype uses two diagonal keepers per board to reduce labor. **Machined acetal, custom measured-thickness keepers and manual fixture assembly are cost drivers** requiring a separately priced mechanical subassembly. After actual-part metrology, compare a simpler measured-hole/standoff mount if the modules have usable, documented mounting holes; that future alternative is not approved by this proposal. PM should quote it explicitly with partial assembly as a separate comparison. Do not transfer keeper fitting, soldering or crimping to the user by omission. User steps remain final Pico/cell insertion. No vendor contact, orders or sourcing acceptance occurred.

Factory sequence: populate/inspect carrier with Pico and cell absent; trial-fit measured modules and dummy boards in the fixture offline; install the nine spacers/plate without bowing carrier; place modules face/sound opening up; tighten keepers to their measured pedestal stops using supplier guidance; dress short service loops below windows with separate insulating strain relief and no wire pinch; continuity/polarity-check each harness against the actual module labels; connect and verify all inputs/buzzers. Do not infer signal order from a photograph or from the provisional schematic. Mount/module harnesses remain removable for service.

## Fit and release requirements

1. Measure all board outlines, thicknesses, underside/top components, headers, electrode/sound locations and both-face bare support lands. If proposed tabs/keepers touch circuitry or active surfaces, revise that seat before manufacture. Never drill or bend the modules to fit.
2. Verify nine mounts, spacers, tip and cable clearances, corner-support tool openings, cassette removal, switch/GPIO access and upward Pico removal on the complete assembly. Machine-seat clearances/flatness/tolerances are not released by this drawing.
3. Trial the fixture using representative dummy boards: proposed qualification target is 10 N downward per seat and 20 N distributed across several touch seats, ≤0.5 mm deflection, no permanent set, release or contact with carrier. These are engineering acceptance targets, not a certified real-module force rating. Check lift/tilt and rocking about the diagonal keeper axis, loose nuts and repeated service separately; adjust plate/supports if needed.
4. With actual modules fitted, test finger access, rapid notes, held left modifiers, neighbor false triggers, powered idle/recalibration and USB/battery behavior; compare before/after fixture installation. Insulating plastic does not guarantee unchanged capacitive response. Confirm sound openings and loudness.

Validation: three SVGs parsed and were rendered/visually checked. All nine fixture keepout circles fit inside the plate and clear the cassette/corner holes, conservative header boxes, power/Pico/J15 reservations, touch-body keepouts, buzzer bodies and proposed keepers. The 24 keeper envelopes do not intersect each other. CSV origin offsets, 33/8.9 mm nominal fastening stacks and 3.5 mm nominal component clearance were checked. Manufacturer fastener sheets and the Pico H ordering-table entry were inspected. No physical module/fixture test, PCB DRC, manufacturing approval or final fit claim is made.
