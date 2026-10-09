# Make Music working checkpoint

Updated 2026-10-09. Root `/Users/johnodell/Desktop/Make_Music`, branch
`codex/pcbway-prototype-package`, draft PR **28**:
https://github.com/John-ODell/Make_Music/pull/28.
Git remote git@github.com:John-ODell/Make_Music.git. Root merged latest
origin/master **acd08a4** through integration commit **ef6d013**.

## Current decisions

**LONG protected removable 18650**, external charging; previous18350 was a
naming mistake. Original Pico H SC0917 in female sockets; eight notes/two
left modifiers, two SunFounder ST0238 passive modules, exposed GPIO. Five
complete factory-assembled instruments (all SMT/THT/harness/mechanical work),
optional additional sixth bare keepsake. No purchases, supplier messages or
uploads. User at work, no actual parts and only coarse tape; factory precision
metrology can be explicitly priced. Screen/keypad/percussion/other Picos are
future revisions. Keep unrelated MOV and `.history/` untracked.

## Usage guard / restart

Check signed-in usage at start and between stages. At **5% remaining** in
300-minute window (usedPercent>=95), saveCAD through Konnect, commit/push,
write exact checkpoint, ask helpers to save/stop, rearm SAME heartbeat just
after actual `resetsAt`, and end turn. Do not spend reset/purchase credits.
Shared account budget includes helpers. Do not continue substantive work
below cutoff. Read actual limits on wake; rearm if still limited. At each
wake schedule next reset as fallback against interruption.

Heartbeat `resume-make-music-pcb-at-1-am`, name **Make Music PCB usage guard
and resume**, ACTIVE, next **2026-10-09 13:20 America/Chicago**, after reported
reset **13:17:54**, timestamp1791569874. Keep computer awake/app open for local
wake. Pause heartbeat only when independent work is done and only concrete
external fit/decisions remain, or complete. Latest read before this checkpoint:
**74%used /26%remaining**; weekly66%used. Check again before a new CAD stage.

## Integrated reviews and saved actual progress

Merged/reviewed PR24schematic audit,25power audit,26mechanical audit,
**27C17/C18 schematic**, **29protected18650 power**, **30MPD cassette geometry**.
PR28 remains draft for PM integration/exports.

- Root schematic48physicalparts/166endpoints,47purchased expected30SMT+17THT.
  Independent fresh ERC0; verify_connectivity passes all166,38connectednets,
  6intentionalNC,41powerendpoints. All162 old endpoints and46 part identities,
  values and footprints retained. PR27newcaps10uF/10V/X7R TDK
  C2012X7R1A106K125AC, standard0805, J13/J14 3V3_OUT/GND; J1/J2nativeMPN added.
- J3/J4 corrected y95->98 native, mechanical75->78. Original cleared baseline
  had398segments33vias,63fps,DRC/ERC/parity0. Later schematic update supersedes
  that zero-parity claim.
- H1 now **native(289,40)** /mechanical(269,20), moved+40mm, bottom/rotation/nets
  retained. Pads1positive2GND confirmedlive. Rerouted1.5mm positive:289,40 ->
 288.5,40.5 ->238,40.5, retaining238,40->238,50 and5mmF1padapproach.
  RemovedoldH1positive trace plus twooldgroundBsegments; GNDpour connectsnewpad.
  Firstdirecty40runwasnearGP26via; deletedthroughMCPandcorrectedy40.5.
- Saved/refilled fullDRC now **0copper/layout errors,0unconnected,4paritywarnings**:
  missingC17/C18footprints and missingMPNcustomboardfields J1/J2. Noignore/
  exclusions. PCB63fps (46electrical+17mount), estimated397segments33vias;
  countfreshafterfinalcaps. All17mountpositionsretained.
- Dwgs.User newcassette165,32..277,68 (112x36) andholdermax181.90,39.30..
 260.10,60.70 (78.20x21.40), eight separate importedborderbarsreadback.
  InitialgroupedSVGimportonlycreatedshortfirstbar; removedandfixedusing8
  individualunitlessSVGimports. Old70x36referencekept/labeledPARTIALB.CuRESTRICTION.
  Existingzone165,32..235,68 keepsvias/fillout, allows tracks/pads. Konnectno
  rule-areaCRUD. Loweredinsulatingplatformallowscopper; fullmechanicalreserve
  isunenforced. Fourboltexclusionsretained. ≥2mmloadedclearancestillunverified.
- MPD BH-18650-W revGofficialbody77.70x20.90x21.31, factory24AWG150±5mmleads.
  Reviewcassette112x36x44,holderplanez16,≥47mmundersidesupports. Actualprotected
  KeeppowerP1835Jopposite-endterminalversion/lot,fit,retention,currentunknown.
  L1charger remainsHOLD:4.2±1%upper4.242V vsunqualifiedcellpage4.20maximum.
- RootpartsCSVcorrectedfivequantities, MPDfactoryleadsnotdoublepurchased,
  AWG26modulecontactprocessOD0.9..1.6/strip3..4mm. Fullhandoffandbudgetscope
  written. No completeprice; old$67.54onlysetup/stencilexample.
- Two-pageLetterpaperfitPDFregeneratedwith18650outline/center201andvisually
  checkedbothpages. 4in/100mmbars and redregistrationcrosses; comfortonly.

## Critical remaining tooling/CAD work

Installed Konnect13 PCBsyncdryrun refused45existing root-prefixed paths,
knownupstream723 (exactcurrentroot-prefix vsnativeCLIrelativeidentity).
NoCADchangedbyrefusal. Officiallatestreleasealso13, fix725closedunmerged,
noRusttoolchainavailable. Rootmustnotrelaxidentitymatchingorfile-editCAD.

Existing schematic helper currently builds a **task-local temporary .net
S-expression export adapter**: realCLIpassthrough, exactallowlistroot/ref/
symbolUUID/sheetinstance/sourcehash; normalizesonlyknowncurrentrootprefix
for45oldparts+2caps,leavesTP1excluded. AllCADwritesstillKonnectMCP. Never
installglobalwrapper,transformnativeCAD,linkbyrefalone,acceptforeignroots
orignoreDRC. Reviewadaptertests/provenance beforeuse, then dryrun/apply exact
planrevision. Do not repeat uncertainwrite;inspectreadbackfirst.

Konnect788syncdoesnotcopycustomfields. Keepnative schematicMPNs and full
checksintact; any remainingmetadata-onlydiagnosticsmustbeexplicitlyreviewed
withstrict independentnet/UUID/footprint/value/BOMchecks. Do notcalloverall
DRC/parityzero unlessactualreportshowsit. Manufacturingpostprocessorgate
currentlystrictlyrequireszero, so itmustnotrunaspasswhile4findingsremain.

Proposedcapplacementsaftertoolfix: C17center(81.95,73), C18(119.95,73),rot0
(pad1 3V3 atx81/119;pad2GNDx82.90/120.90), justbelowJ13/J14y69. Queryactual
pads/tracesandclearancesbeforecommitroute; proposalnotapplied. ExistingC11
87.46,69/C12 125.46,69; R1 79,63/R2 117,63 stay. Refreshnewfootprintslibrary
viaMCPifbuilderomitsattributes/graphics. Runfreshcompletechecksreadback.

## Next stages

1. Collect/review schematichelperadapter; use exactroot PCBIPC, dryrun/apply;
   inspectfullcoverage. Place/routetwocaps,refill/save, freshall-severityERC/DRC,
   nativeXML166/liveall48parts/padsidentitycheck. Reviewmetadatafindingshonestly.
2. Finishreviewdocumentationwithactualcounts/findings. Nativefinalexportstage
   usesMCPonly; recordsourcehashafterrefilledchecks/beforeexports.
3. RegenerateheldGerber/drill/BOM/SMT-onlycentroid/manualTHT/IPC2581/drawings
   innewtempdir. ActualGerber/drillviewerandallPDFvisualchecks. Newnativeorigin
   (0,0),xright/yup, board20,-20..350,-140; J3 87.46,-98,J4 121.46,-98,H1 289,-40.
   Olderheldpackagebottomleftoriginobsolete;markedclearly. Nevermixfiles.
4. `manufacturing/prepare_pcbway_review.py`requires47nativeMPNparts,
   30SMT17THT,sourcehashcheckpointandconsistentorigin. Itdoesnotexport/editCAD.
   Guardvalidationprovedstalecadcheckpoint andcurrent4-findingPCBrefusedbefore
   outputcreation. Fullpositiveend-toendNOTyetobserved. Retiredexport_review.py
   nowrefusestorun. `manufacturing/README.md`documentssequence.
5. UpdatePR28title/bodyactualfinalscope,review/mergeonlycompletecontribution,
   pushpreservingunrelatedmedia. RemainREVIEWONLYhelduntilactualparts/process/
   benchgates. No fabrication-ready or newpriceclaim.

## Existing helpers (user-authorized)

- Schematic/toolingsupport `01a11931-3d20-7733-8e7e-296b88ba9abd`, branch
  codex/pcb-schematic-buzzer-bypass at8683a571; currentadapternotnativeCAD.
  Latestcursor b1f166be-c25c-48c5-b495-c57177afb74b:8. Inspectactualresult.
- Mechanical `01a11931-eed2-7820-85eb-496cfc97903b`, PR30ceeadce7merged,
  worktree /Users/johnodell/.codex/worktrees/module-fixture/Make_Music.
- Power `01a11931-cb05-7f20-8e09-075ef0c4c9c1`, PR29f3cedfcdmerged,
  worktree /Users/johnodell/.codex/worktrees/pcb-power-validation/Make_Music.
  Laterfactory-leadreplacementprocurementrowssupplementmaybepending;rootCSV
  alreadycorrectedbutreconcileexactsourcelead/insulationnotes.

## Runtime and evidence

Konnect `/Users/johnodell/Tools/konnect/v0.13.0/konnect`, config
`/Users/johnodell/Tools/konnect/konnect.toml`. ExactrootPCBcurrentlyopenin
standalonepcbnewUI. StartPCBeditorfirstifmanagerhidesIPC; closewhenunneeded.
No pcbnew/SWIG. AllnativechangesMCP. CUAUIboardEditorbindingpersistent,
rewriteCUAdocsaftercompaction. Do notclickPCBWaypluginRun(automaticupload).

WorkingstdioClient `/tmp/make-music-konnect-trial/probe.py`, caller
`/tmp/make-music-pcbway/mcp_call.py`, toolschemas `tools.json`.
PlanJSONarray id/tool/args, fullresponsefileid.json; decodedbriefprinting.
CurrentDRC `/tmp/make-music-pcbway/battery-bars-drc.json`, XML
`pr27-netlist.xml`, independentERC `pr27-independent-erc.json`.
Livebaselinecomponentlist `pre-sync-component-list.json`, beforeH1move.
BatteryMCPgraphics `battery-bars-readback.json`; SVG
`battery-revised-view.svg`, crop `battery-revised-detail.png` inspected.
Oldprecaptempmanufacturingexport `export-20261008-corrected`obsolete.

PDFPython `/Users/johnodell/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`,
ReportLabavailable;pdftoppm installed. Do notuseSWIG. PDFoutput
`output/pdf/make-music-paper-fit-letter.pdf`renderedchecked. SVG widthunitless
neededforMCPimport;groupedimportdidnotpreserveeverypolygon,useindividualbars.
Konnectexport_netlist(format=ipc)fails;IPC2581works,notIPC-D356replacement.
