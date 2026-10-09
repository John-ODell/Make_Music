# Routed first-prototype carrier — review hold

Updated 2026-10-08, KiCad 10.0.6. The native PCB is fully placed and routed with the fused TPS259474L branch, removable Pico sockets, twelve module cable headers, free-GPIO header, bottom battery JST, switch and all supporting passives/clamps. There are **46 schematic parts /162 physical pad endpoints**, plus **17 board-only mounting footprints**. This is a complete electrical layout for review, **not a fabrication release or tested instrument**.

## Native checks

Fresh root schematic ERC: **0 violations** (errors, warnings and exclusions). The connectivity checker verifies all162 endpoints,46 components,38 connected nets and6 intentional NC nets, including all41 power-contract endpoints. Integrated PCB DRC with schematic parity and all severities: **0 violations,0 unconnected items,0 parity issues**, with no excluded violations. The independent XML/PCB checker agrees by reference, assigned footprint, value, schematic UUID and pad net. Routed copper currently includes393 track segments,32 through vias and two filled grounded pours; no blind/buried vias or via-in-pad are specified. Full logs/netlists are generated outside Git; the held package contains a concise validation summary and source/output hashes.

Freerouting 2.4.1 routed remaining signals/power around manually placed and locked local power copper. Native KiCad checks are authoritative; the router cannot represent every custom local clearance/shape rule. Redundant router vias were removed, and J14's local front-ground island received a ground stitch. Both ground pours are filled with disconnected islands removed.

## Geometry and rules

Proposed **330 ×120 mm**, two layers,1.6 mm carrier requiring at least35 µm finished copper on both layers (supplier-specific stackup pending). KiCad coordinates are the mechanical top-left/y-down proposal plus (+20,+20) mm. J1 pad1=(131.11,21.30), J2 pad1=(148.89,69.56), J2 rotated180 degrees; socket row spacing17.78 mm. H1 is bottom-side and pad1 remains battery positive through the flip. Pico H SC0917 with fitted male headers is the selected inserted-module candidate; engagement remains untested.

Ten26 ×26 mm touch-body rule areas exclude copper pads, tracks, vias and pours on both layers. These give1 mm around the supplied24 mm bodies; they are engineering reservations, not a measured sensing-field limit. The underside battery-cassette area excludes copper fill and vias; insulated cassette material must isolate its contents from the carrier. Seventeen3.2 mm NPTH holes implement four corners, four cassette mounts and nine raised fixture mounts. Each has an8 mm diameter track/via/pour reservation. No undocumented module or holder holes are assumed.

Default clearance0.25 mm, signal width0.30 mm, via0.8/0.4 mm. Long power class routes use2.0 mm width and1.2/0.6 mm vias. Locked manual branch routes are1.5 mm with5.0 mm fuse-pad approaches; local package escapes are0.30 mm. Fine control routes are0.18 mm with normal0.25 mm clearance. The absolute minimum width/clearance is0.15 mm; a custom0.15 mm clearance rule applies only when both objects intersect U2's courtyard. U2's actual closest copper gap is0.20 mm, with nominal0.10 mm mask web and TI example0.100 mm stencil geometry. Fabricator/assembler process acceptance and power/thermal qualification remain required.

Plot/drill/placement origin is native(20,140) mm = mechanical bottom-left(0,120). Gerbers, Excellon drills and placement CSV all use that origin, x right/y up. Mechanical CSV conversion is(x,120−y). Review PDFs are A3 drawings, not machining templates.

## Circuit and assembly

Protected cell -> H1.1 -> F1 -> S1 common2/ON3 -> U2 IN5/OUT6 -> VSYS/Pico39. Carrier seriesD1 is removed; D2 is a shunt K1=VSYS/A2=GND, D3 is bidirectional input TVS. TP1 is USB VBUS only. The Pico's onboard USB isolation/regulator remain external to this schematic. No onboard charger or polymer hold-up bank; source changes may reboot. See [power integration](power-integration.md) for R3–R8/C13–C16 mapping and exact footprint evidence.

J3–J14 carrier pin order is1 SIG /2 regulated3V3 /3 GND, independently mapped to actual module labels by adapted cables. Note pitch is34 mm with10 mm nominal body gaps; semitone/octave modifiers are left. The [raised fixture](../mechanical/MODULE_FIXTURE.md) uses24 mm proposed spacers and removable edge keepers; module centers are references on Dwgs.User, not direct mounting footprints. Two ST0238 bodies are at(60,67.5)/(98,67.5); their carrier cable headers remain(61,49)/(99,49). The [1101 holder](../mechanical/WIRED_HOLDER_PROPOSAL.md) is wired in a separate insulated underside cassette. All carrier SMT is top-side; H1 is bottom THT.

## Review files and remaining gates

[Held manufacturing package](../manufacturing/REVIEW_ONLY_DO_NOT_ORDER/README.md): native-derived Gerbers/drills, placement CSV,45-component purchased carrier BOM, separate instrument parts, schematic/assembly/copper PDFs and hashed validation manifest. Regenerate with `../manufacturing/export_review.py`; it requires passing ERC/DRC/parity. Manufacturing exports remain prominently **REVIEW ONLY — DO NOT ORDER**.

Complete the exact [fit checklist](../assembly/FIT_CHECKLIST.md): protected cell/holder/charger pairing; Pico/socket engagement; actual module headers, support lands and heights; harness polarity; final fixture/cassette/feet CAD/tolerances and full-size paper fit. Then complete [staged power/functional testing](../power/prototype-validation.md), including measured loads, source isolation, UVLO/fault/thermal behavior and effective capacitance. Module, cell and holder measurements are not available. No bench test, supplier acceptance, complete quote, purchase or fabrication approval is claimed.
