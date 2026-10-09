# Regenerating the held PCBWay review package

All native CAD changes, saves, zone refills, checks and CAD exports go through
Konnect MCP. Ordinary Python only packages exported evidence. The retired
`export_review.py` refuses to run: its auxiliary-origin outputs and socket
MPN substitutions must not be mixed with the new native exports.

**Current source work must pass review before regeneration.** A stale checked-in
directory is not a passing result for the current sources. Keep outputs marked
REVIEW ONLY — DO NOT ORDER until actual fit, bench and supplier process gates
are satisfied. No script here uploads files or grants release.

## Export sequence

1. Bind the exact board in KiCad over IPC. Read each mutation response and
   saved/live readback. Resolve all electrical/layout/parity findings; preserve
   unavailable-check information and any explicitly reviewed exceptions.
2. Through Konnect, run root ERC at all severities; run PCB DRC at `info` with
   `sync_live_board=true` and `refill_zones=true`. Inspect full coverage and
   source evidence. Export a fresh native XML netlist and run
   `kicad/verify_connectivity.py`. Independently compare live pad nets, values,
   library IDs and symbol identities against that export.
3. After the saved/refilled checks, record a fresh source hash checkpoint:
   `python3 capture_review_sources.py /temporary/new/source-checkpoint.json`.
   Do not mutate CAD or libraries during the following export/package stage.
4. Use Konnect `export_manufacturing_package` with `fab_house="pcbway"`,
   eight layers F.Cu/B.Cu/F.Paste/F.Mask/B.Mask/F.SilkS/B.SilkS/Edge.Cuts,
   assembly included, both position sides, millimeter units, native MPN field
   and quantities. Use a **new output directory**. Inspect every emitted file
   and warning; source hashes alone cannot prove an export succeeded.
5. Through Konnect export both-sheet schematic PDF, top/bottom assembly and
   copper PDFs/SVGs. Verify drawing orientation and visual content. An
   IPC-2581 XML is supplemental; it is not IPC-D-356. The installed
   `export_netlist(format="ipc")` fails and must not be reported as produced.
6. Run `prepare_pcbway_review.py NATIVE_DIR NETLIST_XML ERC_MCP_JSON
   DRC_MCP_JSON NEW_OUTPUT_DIR --source-snapshot SOURCE_CHECKPOINT_JSON
   --electrical-evidence SOURCE_BOUND_EVIDENCE_DIR`.
   Inputs are the complete MCP result files, not stdout summaries. This checks
   sources stayed unchanged, native origin agreement and BOM/placement identity.
   It produces exact per-reference BOM, grouped five-unit BOM, SMT-only centroid,
   separate manual THT positions, copied evidence and SHA-256 manifest.
7. Inspect actual Gerbers and both drill sets in a local viewer, inspect
   placements/rotation/polarity and render every final PDF. Confirm all managed
   outputs are nonempty and hashes agree. Only then replace the old held
   directory as a complete revision, preserving its hold status. Commit the
   reviewed sources and regenerated package together via a PR.

The postprocessor requires source-bound live pad/identity evidence and retains
the exact four reviewed Konnect custom-field warnings from the current PCB.
It refuses other findings, wrong connections, mismatched evidence or stale
sources before creating output. The real 47-part/30-SMT/17-THT pipeline passed;
wrong-net, unreviewed-warning and stale-source negative cases refused. Overall
DRC remains four warnings in the manifest; no DRC rule or result is suppressed.
This electrical review does not grant fabrication release.

## Coordinate and assembly convention

Served native exports use (0,0), x right/y up; board (20,-20)..(350,-140) mm.
The mechanical proposal uses top-left x/y down: machine x=x_mechanical+20,
machine y=-(y_mechanical+20). J3=(87.46,-98), J4=(121.46,-98),
H1=(289,-40) mm in the revised placement file. Do not translate Gerbers,
drills or positions independently. The older held package uses a different
bottom-left origin and is obsolete once new sources change.

Expected purchased carrier scope is 47 parts: 30 top SMT and 17 THT. H1 is
bottom THT. TP1 and 17 mounting holes are bare-board features. The complete
instrument additionally needs the Pico, modules, harnesses, holder/cell and
mechanical assembly in `assembly/PCBWAY_HANDOFF.md`.
