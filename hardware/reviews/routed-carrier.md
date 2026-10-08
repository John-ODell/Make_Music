# Routed carrier review — 2026-10-08

Reviewed electrical-board checkpoint: PR20, commit `87b6fb20bbeefa327711a751c1599701fda7a9cc`. Schematic power integration is merged PR23/master `aa4b407`. The PCB is held for review; none of these checks constitutes actual-part fit, built-hardware testing, assembler acceptance or fabrication approval.

## Independent results

The schematic reviewer reproduced native KiCad10.0.6 ERC and full DRC with schematic parity/all track errors/all severities: **0 violations,0 unconnected,0 parity issues**, no explicit exclusions. Fresh XML checks agree46 parts/162 endpoints, including all41 power endpoints. A separate audit checked complete root/child UUID paths, assigned part fields and every placed pad's transformed geometry against its library: position, numbering, shape, size, layers, drill, mask/paste margins, rounding and custom polygons. All46 matched. U2 paste graphics matched the TI footprint. All40 socket contacts were verified at17.78 mm row spacing/48.26 mm span with J2 rotated180 degrees. H1/S1 child paths and bottom H1 polarity were correct. No electrical synchronization defect was found; approved for the held review package.

The power reviewer independently reproduced the same clean native checks and full connectivity contract. H1/F1/S1/U2/VSYS topology, shunt D2, bidirectional CA TVS, absence of carrierD1/pad11/VBUS bridge, opposite-end power escapes, local programming components/ground stitches and grounded power-cluster return paths were reviewed. No blocking power-layout defect was found. The only rule correction was to set Control netclass clearance to0.25 mm while retaining the courtyard-scoped U2 minimum0.15 mm rule. That correction changes project settings, not copper; native checks remained clean after applying it.

The proposed fabrication requirement is at least35 µm finished copper on both layers. The power review's simplified room-temperature OUT-to-Pico centerline model estimated34.3 mΩ/24 mV at0.70 A, excluding via/socket losses and pad-spreading benefit. It is an engineering estimate, not a measured result; the existing30 mV copper/connection allowance still needs bench qualification. No supplier-specific stackup is assigned.

Mechanical review: native fixture-hole coordinates, exported17 NPTH3.2 mm holes,45-part placement exclusion of board-only mounts and common bottom-left plot origin were independently checked. Final clearance/access review is pending the mechanical helper's report. Actual module/holder engagement, height, support lands and fit remain unmeasured regardless of coordinate agreement.

## Held outputs and limits

The final generator reruns ERC, exact schematic contract and native DRC/parity before exporting the Gerbers, separate PTH/NPTH drills, BOM, positions and PDFs. Outputs are marked REVIEW_ONLY_DO_NOT_ORDER and hashed with their native inputs. The board has63 footprints (46 electrical +17 mounting),393 tracks,32 vias, two filled ground pours and28 rule areas. TP1 is a bare copper feature; purchased carrier BOM/position CSV contain45 parts.

Remaining qualification is explicitly listed in [FIT_CHECKLIST.md](../assembly/FIT_CHECKLIST.md) and [prototype-validation.md](../power/prototype-validation.md). Custom mechanical drawings remain proposals requiring final CAD/tolerances after actual-part metrology. Factory services and complete budget are unquoted; no purchase, supplier message or order was made.

## Local tooling incident

Three macOS KiCad Python3.9 SIGSEGV reports during the helper's temporary footprint audit identified `BOARD::FlipLayer -> PCB_TEXT::Flip -> FOOTPRINT::Flip`. The audit flipped a detached H1 library clone with no board parent. The helper confirmed the cause, completed the audit with the parent attached, and then stopped all further pcbnew launches. The saved project was never edited by those audit runs and its PCB hash matched the committed checkpoint. No KiCad GUI session was left open. Routine export generation now uses ordinary Python3 plus native KiCadCLI and does not invoke pcbnew/SWIG. The earlier independent verify_board.py result is retained as review evidence, not a required routine export step.
