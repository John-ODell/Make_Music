# Make Music working checkpoint

Updated 2026-10-09 at usage cutoff. Workspace /Users/johnodell/Desktop/Make_Music,
branch codex/pcbway-prototype-package; draft PR28:
https://github.com/John-ODell/Make_Music/pull/28.
Base origin/master acd08a4; previous pushed checkpoint661c622. This checkpoint
will be committed/pushed immediately; read actual git log on wake.

## Current requirements

Protected removable LONG 18650, external charging (18350 was a user naming
mistake). Original Pico H SC0917 in removable female sockets, eight notes and
two left modifiers, two ST0238 passive modules, exposed GPIO. Five complete
factory instruments, including SMT/THT/harness/mechanical work; optional sixth
bare keepsake. No actual parts, coarse tape only, assembler metrology can be
priced. No purchases, supplier messages or PCBWay uploads. Preserve unrelated
MOV and hardware/kicad/.history/. Future screen/keypad/percussion deferred.

## Usage / resume

Check usage at start/between substantive stages. At usedPercent>=95 in the
300-minute window, finish a bounded save/checkpoint/push only, ask existing
helpers to stop, rearm SAME heartbeat after actual resetsAt, and end turn.
Never spend reset credits. Cutoff reached95% used /5% remaining, weekly69%.
Actual reset1791569874 = 2026-10-09 13:17:54 America/Chicago.
Heartbeat resume-make-music-pcb-at-1-am, ACTIVE, wake13:20 Central; computer
must remain awake with Codex open. Check actual limits on wake, rearm next
reset as fallback. Pause only after independent work complete or user asks.

## Verified saved CAD

Merged reviewed PR24/25/26/27/29/30. Root schematic48parts/166endpoints;
47 purchased carrier parts =30 top SMT+17 THT. Fresh ERC0 and contract passes
all166 endpoints/38 connected nets/6 NC; all native MPNs retained.

PCB integration now COMPLETE electrically:65fps (48 electrical+17mounts),
405 trace segments, inherited33vias. C17(87.46,65.50), C18(125.46,65.50),
top/0degrees, TDK10u/10V0805. Refreshed through native library tool; routed
0.30mm beside C11/C12. All existing63 placements/values/library IDs unchanged.
J3/J4 native y98, H1 underside(289,40), corrected long18650 cassette references
remain. H1 reroute/old branch removal and eight Dwgs.User reservation bars
were already saved and verified; no rule-area enlargement is claimed.

Fresh saved/refilled all-severity DRC:0 copper/layout violations,0unconnected,
FOUR METADATA PARITY WARNINGS: C17/C18 missing Header custom board fields,
J1/J2 missing MPN custom board fields. No rules disabled/excluded. Overall
DRC is4 warnings. Source-bound evidence hardware/review/integration-20261009/
includes native XML, all166 live IPC pads,48 values/full library IDs, guarded
identity-sync noop, full ERC/DRC and placement score.

Replaced old SWIG verify_board.py with pure exported/live evidence verifier.
Circuit verifier no longer parses native footprint pad definitions. Both pass.
Four unittest methods cover actual evidence, seven rejection cases and a pad
negative control (disable guard in isolated function => wrong-net test fails).

Placement score flags J1/J2 courtyard y19.27 vsboard y20,0.73mm rear overhang.
This is UNRESOLVED physical edge/lip acceptance, not a placement-score pass.
Actual module/holder/Pico/cell fit and bench/process qualification remain held.

## Tooling workaround already reviewed/applied — do not redo

InstalledKonnect13 issue723 rejects root-prefixed vsnativeCLIrelativepaths.
Schematic helper task-local adapter /tmp/music-konnect-identity-adapter/
was independently reviewed; all21 tests passed. It changes ONLY temporary .net
export spans for exact48 reference/symbol/sheet/value/footprint/source hashes,
45existing+2caps; TP1 untouched. Installed connector/config unchanged. All
CAD writes still Konnect MCP. Dryrun ready2add/nootherchanges, applied exact
planrevision, refreshed2footprints, moved/routed through MCP. Final identity
preview noop. No further PCBsync needed unless schematic changes.

Wrapper /tmp/make-music-pcbway/mcp_call_adapted.py imports probe_adapted.Client.
Normal /tmp/make-music-pcbway/mcp_call.py uses installedCLI. Schemas tools.json.
Tool plans/results in same directory; review full results, one CAD owner=root.
No text-edit native CAD; no pcbnew/SWIG.

## Fresh raw exports and package stage

/tmp/make-music-pcbway/raw-held-20261009 has fresh8Gerbers, PTH/NPTH drills,
47line nativeMPN BOM and47line both-side positions, two-sheet schematicPDF,
assembly-topPDF, assembly-bottom-through-topPDF, copper-layoutPDF and IPC2581.
MCP complete13artifact package/no warnings; source hashes unchanged afterward.
Origin native0,0 xright/yup,board20,-20..350,-140. J3 87.46,-98;
J4 121.46,-98; H1 289,-40. No coordinate rewriting.
Source checkpoint /tmp/make-music-pcbway/integrated-export-source-checkpoint.json.
Raw output is NOT accepted for upload. Gerber/drill viewer review remains.

prepare_pcbway_review.py now requires --electrical-evidence plus source snapshot;
strict live pad/identity/source checks adjudicate only4 exact metadata warnings,
retain actual4 in summary. Native XML/ERC/DRC must byte-match evidence. Real
47part/30SMT/17THT pipeline passed; wrong-net/new-warning/stale-source refused
before output. Stage /tmp/make-music-pcbway/held-package-stage-20261009 was
created BEFORE later PDFs/IPC, so regenerate into NEW dir after viewer checks.
REVIEW_PACKAGE_README.md replaces old obsolete banner when preparing newpackage.
All staged manifest output hashes validated. No fabrication release granted.

Rendered all5PDF pages using pdftoppm; inspected both schematic pages, both
assembly crops and combined copper crop. Full raw PDFs are current and marked
review; bottom PDF is through-top view, not mirrored underside assembly view.
Combined copper image mostly solid ground; inspect actual separate Gerber layers.
Rendered files /tmp/make-music-pcbway/pdf-qa-20261009/. Capacitor SVG detail
also visually checked. Raw drawing export responses integrated-*-pdf.json.

Gerber Viewer native file picker did NOT successfully load job. GoTo UI text
resolved correct path, but Return resets to slash and accessibility actions
failed to select. No Gerber viewer pass claimed. gerbv CLI is not installed.
Current CUA binding musicGerber; boardEditor root PCB. Close sessions on stop.

## Next actions (independent work still remains)

1. Check actual usage, fetch GitHub/read actual PR28 latestcommit. Read current
skills/reliability contract. Do not redo completed capacitor work.
2. Complete actual Gerber/drill viewer inspection: registration,8layers,
17NPTH3.2mmholes, PTH vias/component holes, mask/paste/apertures/polarity. Resolve
native file-picker interaction or use a suitable official local viewer. Current
raw files are fresh. Do not claim viewer pass from native board PDF alone.
3. Add separated copper drawings if useful; verify all final artifacts and
bottom orientation annotations. Retain current source hashes or recreate checks
if any CAD changed. Manufacturing preflight coverage/actualprocess gates remain.
4. Regenerate full held package into fresh destination with postprocessor,
include all rawPDFs/IPC and verified inputs. Check manifest/BOM/SMT table/manual
THT/5unit totals, visual review. Only then replace obsolete checked-in held
outputs as one revision. No supplier upload/order. Final PRreview/mergeauthorized.
5. Complete remaining docs/full independent review, retain precise external
requirements: socket edge/lip/engagement, actualparts, MPDretention/cassetteCAD,
protectedcellfit/current, L1charger voltage HOLD, assemblerU2stencil/mask/
annular-ring/panelprocess acceptance, current-limited bench qualification.

## Existing authorized helpers

Schematic01a11931-3d20-7733-8e7e-296b88ba9abd completed adapter, idle;
latestcursor b1f166be-c25c-48c5-b495-c57177afb74b:10.
Mechanical01a11931-eed2-7820-85eb-496cfc97903b PR30merged, idle.
Power01a11931-cb05-7f20-8e09-075ef0c4c9c1 PR29merged; reconcile any later
factorylead procurement supplement, rootinstrumentCSV already corrected.

MPD BH-18650-W factoryAWG24 leads150±5mm. Review cassette112x36x44;
planez16/≥47mm supports. Actual P1835J terminal-version/fit/current unknown.
L1 charger HOLD4.2±1% =>4.242V vsunqualifiedcell4.20Vmax. Old$67.54 was
setup/stencil example only. PaperfitPDF2Letterpagescomfortonly updated18650.
