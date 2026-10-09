# Held first-prototype review package — do not order

**OBSOLETE CHECKPOINT — 2026-10-09:** the files below predate J3/J4 clearance,
the moved H1, protected 18650 cassette and C17/C18 integration. Their old hashes
and zero-finding summary are historical, not evidence for the current sources.
Do not upload or order them. Final regeneration is pending the current
[PCB integration findings](../../kicad/PCB_STATUS.md); use the new
[Konnect export procedure](../README.md). The legacy `export_review.py` is retired.

This package is for inspection and assembly planning. It is **not a fabrication release**. Native KiCad ERC, full board DRC and schematic parity must pass before the generator produces files, but actual hardware fit and electrical behavior remain untested. See [PCB status](../../kicad/PCB_STATUS.md) and the [physical verification record](../../assembly/FIT_CHECKLIST.md).

## Included files

- `gerbers/`: two copper layers, front paste, both masks/silks, closed board outline, separate plated and nonplated Excellon drill files and Gerber job metadata.
- `carrier-bom.csv`: 45 purchased carrier components, one row per reference. TP1 is bare copper and the 17 mounting holes are PCB features. The inserted Pico and modules are separate.
- `carrier-positions.csv`: millimeter assembly positions, including accepted THT components. H1 is bottom; all SMT parts are top. Confirm rotation conventions with the assembler, particularly D2, U2 and underside H1. This is a KiCad placement export, not a supplier-specific converted file.
- `instrument-parts.csv`: removable Pico, ten touch modules, two buzzers, holder/cables and proposed mechanical hardware. Candidate/measurement status remains visible.
- `schematic-review.pdf`, `assembly-top-review.pdf`, `assembly-bottom-review.pdf`, `copper-review.pdf`: review drawings, not scaled machining templates. Bottom assembly view is mirrored for viewing from underneath.
- `validation-summary.json`, `manifest.json`: check outcomes and SHA-256 hashes of native source/output files. Full diagnostic logs are temporary, not checked in.

## Board and coordinate conventions

Proposed 330 × 120 mm, two layers, 1.6 mm FR4. The fabrication handoff requires **at least 35 µm finished copper on both layers**; the board has no supplier-specific stackup. Fabricator stackup and solder process remain to be accepted. Minimum design clearance/width is 0.15 mm at the tiny eFuse; normal clearance is 0.25 mm. U2 has 0.20 mm minimum copper separation and a nominal 0.10 mm mask web. Its footprint follows TI's example 0.100 mm stencil apertures, requiring assembler approval. No via-in-pad or blind/buried vias are specified. Standard signal vias are 0.8/0.4 mm; long power routes use 1.2/0.6 mm vias. Fuse lands have 5 mm copper approaches.

Gerbers, drill files and positions all use the same plot/drill origin: carrier **bottom-left**, native KiCad (20,140) mm, equivalent to mechanical (0,120). Exported coordinates are x right/y up. Convert the mechanical CSV's top-left, y-down convention using `x_export=x_mechanical; y_export=120−y_mechanical`. Do not mix absolute native coordinates, mechanical coordinates and exported positions. Assembly drawings use an A3 page and are not the machine coordinate origin.

The 17 holes are 3.2 mm NPTH: four corner supports, four independent cassette mounts and nine raised fixture mounts. Touch-module holes and holder holes are intentionally not part of this PCB. The wired holder and module fixture are separate insulating subassemblies; their drawings are engineering proposals and require actual-part metrology and manufacturing CAD before they can be machined.

## Release hold

Complete the cold-fit measurements for the exact protected cell/1101 holder, Pico H/socket engagement, module headers, support lands and component heights. Qualify cable pin order and retained module configuration. Agree final fixture/cassette/feet tolerances and load clearance. Complete the staged [power/functional validation](../../power/prototype-validation.md), including source isolation, low-voltage/fault behavior and measured load limits. Obtain fabrication/assembly process acceptance and a complete quote before ordering. No supplier has been contacted or accepted this package.

All carrier SMT parts are top-side; the bottom connector is THT. A two-side SMT fee is not automatically required. Quote the mixed THT/manual work and mechanical assembly separately, following the [budget comparison](../../ASSEMBLY_BUDGET.md). The previous $67.54 is setup/stencil overhead only, not a delivered instrument price.

Regenerate from `hardware/manufacturing/export_review.py` with KiCad 10. It always writes into this held directory and never changes the release status. Set `MAKE_MUSIC_KICAD_CLI` if your CLI installation is elsewhere. The generator uses ordinary Python3 and native KiCadCLI, with no pcbnew/SWIG calls. The separate verify_board.py supplement was also run successfully on the reviewed board, but is not required for routine exports. Recheck file hashes after any design change; old exports are obsolete when native sources change.
