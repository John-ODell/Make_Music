# Make Music working checkpoint

Updated 2026-10-09. Primary workspace: `/Users/johnodell/Desktop/Make_Music`.
Primary branch: `codex/pcbway-prototype-package`. GitHub repository:
https://github.com/John-ODell/Make_Music.

## Current user decisions

- **LONG 18650**, protected removable conventional 4.2 V-charge Li-ion,
  externally charged. The earlier 18350 selection was a naming mistake and
  is superseded. Do not restore it from older notes or automation prompts.
- Five fully assembled instruments, including small components, sockets,
  headers, switch, harnesses and mechanical work. Optional sixth bare carrier
  is an additional keepsake. No purchasing or supplier messaging/upload.
- Two SunFounder ST0238 passive modules, eight touch notes and two left-hand
  modifiers, removable original Pico H SC0917 in female sockets, exposed GPIO.
- Screen/buttons/metronome/different Pico versions are future expansion ideas.
- User has no actual parts yet and only an ordinary tape measure. Paper fit
  can check comfort; exact metric metrology can be an explicitly quoted
  assembler service. Do not silently assign soldering to the user.

## Usage guard and restart

User instructed us to stop with 5-1% of the five-hour allowance left. Use
**5% remaining** as the cutoff, measured through the app usage-limit tool.
Check at the start and between substantive stages. Account usage is shared
with helpers. At the cutoff, save through Konnect, commit/push reviewable
changes, update this checkpoint with exact hashes/PRs/next steps, ask helpers
to checkpoint and stop, and rearm the same heartbeat just after the reported
`resetsAt`. Do not spend reset credits or buy credits.

The heartbeat `resume-make-music-pcb-at-1-am` has been repurposed as
**Make Music PCB usage guard and resume**. Its next scheduled wake is
2026-10-09 13:20 America/Chicago, after the currently reported five-hour reset
at 13:17:54. At a later wake, read actual limits and rearm to the next reset;
do not assume a fixed five-hour schedule or restart completed work. Pause
when the authorized independent work is complete or only external physical
measurements/required decisions remain.

## Completed since master 6155ca0

- Reviewed and merged schematic audit PR24 and power audit PR25. Current
  merged base is `1a054f8`.
- Moved only J3/C4 and J4/D4 carrier header anchors from native y95 to y98
  (mechanical y75 to y78), retaining x/rotation. Updated their copper and
  silkscreen captions. Other component placements stayed fixed.
- Native saved/refilled board ERC/DRC: zero reported violations, zero
  unconnected items and zero schematic parity issues. Fresh exported XML
  and live IPC pads agree on all original 162 endpoints, 46 physical parts,
  references, footprints and values. Routed board: 398 segments, 33 vias.
- Trial FID1 was removed through Konnect; 63 footprints remain. Factory
  panel/tooling rails with fiducials need process acceptance.
- Konnect exported fresh temporary Gerbers/drills/BOM/positions/review
  drawings/IPC-2581 at `/tmp/make-music-pcbway/export-20261008-corrected`.
  These still predate C17/C18 and the 18650 cassette; DO NOT ORDER.
- Created and visually checked a two-page Letter 1:1 paper-fit PDF at
  `output/pdf/make-music-paper-fit-letter.pdf`, with 4-inch and 100-mm scale
  checks. Regenerate after the mechanical helper updates the battery outline.

## Active helper assignments

- `Build editable KiCad schematic` / `01a11931-3d20-7733-8e7e-296b88ba9abd`:
  owns root schematic changes C17/C18, 10uF 10V X7R
  TDK C2012X7R1A106K125AC beside buzzer headers, plus native Samtec J1/J2
  MPN/datasheet fields. Latest pre-limit checkpoint: connections exist,
  all 162 old endpoints retained and four added. Finish footprint evidence,
  ERC/connectivity/rendered review and focused PR. Expected 48 physical
  parts/166 endpoints/47 purchased/30 SMT+17 THT. PM owns PCB sync/routing.
- `Verify PCB mechanical fit` / `01a11931-eed2-7820-85eb-496cfc97903b`:
  PR26 is open for header/fixture/precise fit-check documentation. Review and
  merge it, then integrate the separate 18650 revision. Investigating wired
  Keystone 1044 solder-lug holder and enlarged cassette using primary
  drawings; report exact needed carrier geometry changes. No CAD mutation.
- `Design battery and USB power` / `01a11931-cb05-7f20-8e09-075ef0c4c9c1`:
  PR25 merged. Now selects documented protected 18650/external charger and
  revises current active power parts/handoff/limits in a new focused PR.
- All three hit the prior usage limit. Restart messages sent 2026-10-09,
  preserving checkpoints. Check their actual status before dispatching more.

## Immediate next work

1. Preserve/push the verified J3/J4 change, review/merge PR26.
2. Integrate helper schematic PR, then use Konnect's dry-run/apply PCB sync;
   place and route the two added bulk capacitors without disturbing other
   placements. Refill/save, rerun ERC/DRC/parity and exported netlist checks.
3. Integrate protected 18650 holder/cassette/power specs. Apply exact needed
   board reservations/mounts through Konnect; never invent physical fits.
4. Regenerate held manufacturing outputs, SMT-only centroid and separate
   manual THT positions; fully specified 47-part BOM and five-unit quantities;
   both-side instructions, instrument/harness/fixture scope and source hashes.
5. Finish PCBWay handoff and budget comparison; visual Gerber/drill/placement
   review; precise required fit/process evidence. Existing package is stale.

## Tool notes

Konnect v0.13.0 binary/config:
`/Users/johnodell/Tools/konnect/v0.13.0/konnect`,
`/Users/johnodell/Tools/konnect/konnect.toml`.
Native PCB must be the exact document open over IPC. Start PCB editor first
if the KiCad manager's socket hides it. One CAD owner at a time; all source
changes through Konnect. Never edit KiCad files as text or use pcbnew/SWIG.

Tool handlers remain callable through stdio MCP even when Codex only exposes
the meta-tools. Working ordinary Python client:
`/tmp/make-music-konnect-trial/probe.py`; orchestration wrapper/schema cache:
`/tmp/make-music-pcbway/mcp_call.py`, `tools.json`.

Served MCP exports currently use **native (0,0)** coordinates, x right/y up:
Gerber board corners (20,-20) to (350,-140) mm and placements have negative Y.
Older checked-in held files used auxiliary bottom-left origin (20,140).
Do not mix them. Choose one documented consistent convention for all new
Gerbers/drills/placements and verify it. Installed export_netlist(format=ipc)
fails with Invalid format; IPC-2581 export succeeds. Do not pretend that it
generated IPC-D-356.

A attempted replacement of `manufacturing/export_review.py` was refused by
apply_patch before any write (delete/add same path); it remains the old
CLI-based generator. No partially replaced script needs recovery.

Preserve the unrelated untracked ScreenRecording MOV and KiCad `.history/`.
Do not commit them. Do not click PCBWay plugin Run (it uploads automatically).
