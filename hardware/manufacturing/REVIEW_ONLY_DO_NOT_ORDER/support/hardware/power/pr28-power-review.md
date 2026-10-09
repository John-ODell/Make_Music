# Bounded independent power and packaging review

## Current disposition — 2026-10-09 follow-up

The defects below are a **historical record of `806457b`**, not open correction tasks for the current package. Merged [PR #33](https://github.com/John-ODell/Make_Music/pull/33) compares every purchased placement's finite X/Y/rotation/side and identity with source-bound IPC before writing output. The final native checkpoint is `21b2108`; PM published its coherent held package at `d987896`.

- [Current electrical evidence](../review/rear-edge-20261009/README.md): 166 endpoints /48 parts, all 41 power endpoints; recorded ERC 0, copper/layout DRC 0 and unconnected 0. **Four exact metadata warnings remain; overall DRC is not zero.**
- [Final export review](../review/manufacturing-20261009/README.md): 47 placements agree, full preparation passes 47 purchased /30 SMT /17 THT, and altered U2 rotation/C17 displacement reject before output creation. PM records Gerber/drill and native PDF visual review. No repeat CAD check or bench test is claimed by this documentation follow-up.
- [Current instrument parts](../assembly/instrument-parts.csv) include opposite-end **button-top** P1835J, BH-18650-W factory leads without duplicate wire purchase, and a charger input supply/cable. One shared charger/input set is a **quote assumption, HOLD**, not an approved accessory pair. [Design notes](../PCB_DESIGN_NOTES.md) reflect long 18650, five complete instruments and the current dimensions/warnings.

| Remaining power gate | Required evidence |
|---|---|
| Delivered cell | Opposite-end button-top identity, lot-specific charge/discharge/PCM limits and recovery |
| External charger | Accepted voltage/current/termination/temperature/recovery and bay fit; **L1 upper tolerance 4.242 V versus unqualified cell maximum 4.20 V** remains unresolved by the bounded primary-source follow-up |
| Holder and harness | Exact-cell fit/removal/contact capability for 0.70 A normal and ≥1.2 A continuous branch capability; MPD lead OD within JST 0.8–1.5 mm; qualified strip/tool/crimp/polarity/strain relief |
| Mechanical and factory process | Toleranced cassette, retention and ≥2 mm loaded clearance; accepted U2 stencil/mask, capacitor lands, socket rings, panel/orientation and assembly handling |
| Powered instrument | Effective capacitance, low-load switch endurance and measured current/thermal/isolation/UVLO/fault/reset performance; separate USB source/inrush qualification because USB bypasses F1/U2 |
| Unit acceptance | First-article and all-five records remain blank; no runtime or hardware success claim |

See [current handoff](18650-handoff.md) and [procedure](prototype-validation.md). Factory process acceptance and fabrication release remain held.

## Historical review — checkpoint `806457b`

Reviewed **2026-10-09 America/Chicago**, root [PR #28](https://github.com/John-ODell/Make_Music/pull/28) commit **806457bb189214c41c3d3b49db4457fc497c4590**. Read exported XML/JSON/CSV and ordinary Python guard code only. No CAD mutation, editor operation, new ERC/DRC execution, supplier contact or root-file write occurred. Physical release remains **INCOMPLETE**.

### Material defect: placement coordinates and rotations are not fully guarded

`hardware/manufacturing/prepare_pcbway_review.py`, lines110–123 at the reviewed commit, checks each exported reference/value/package/side but copies X/Y/rotation unchanged. It checks coordinates only for J3/J4/H1 and no rotations. `verify_board.py` checks live pad nets, values and footprint IDs; it does not validate the native position export.

**Reproduced:** copied `/tmp/make-music-pcbway/raw-held-20261009` into an isolated temporary directory, changed only U2's `positions.csv` rotation **0→180°**, then called the actual `prepare()` with the unchanged current XML/ERC/DRC/source snapshot/electrical evidence. It completed: **47 parts /30 SMT /17 THT /38 held files**, with U2 **180°** in `pcbway-centroid-smt.csv`. Temporary negative-control outputs were removed. This can produce a wrong assembly instruction while all electrical/source checks still pass. The actual unmodified export independently agrees with all47 live X/Y/rotations; no current misplaced U2 is alleged.

**PM fix before accepting the final package:** compare every exported placement with the source-bound IPC inventory: X, negated Y for the documented native origin, rotation modulo360, side and exact identity. Require finite coordinates/angles and suitable export-precision tolerance. Do this before `copytree` or output creation. Add a U2-rotation refusal test and a non-anchor coordinate refusal test, preserving the existing wrong-net/warning/stale-source cases. Native Gerber/drill viewing and polarity/rotation inspection remain separate requirements.

### Procurement and requirements reconciliation

Root's `hardware/assembly/instrument-parts.csv`, lines5–8, already includes the **MPD factory 150±5 mm AWG24 leads**, OD/crimp qualification and no duplicate wire purchase. Preserve that scope. It now has **seven columns**, with five-unit quantities; the earlier six-column power supplement must not be applied unchanged.

Root's cell row at line18 specifies opposite-end terminals but omits the **positive button top** required by [MPD's exact product page](https://www.batteryholders.com/part.php?original=Li-ion+18650&override=Li-ion+18650&pn=BH-18650-W). Neither a P1835J SKU nor its customizable terminal list establishes the delivered version. The table also has no charger input supply/cable row despite the L1's specified5 V/1 A input. [The revised seven-column supplement](instrument-parts-handoff.csv) closes those procurement-document gaps for PM integration, preserving20 unrelated rows and producing28 data rows. Charger/accessory distribution remains a PM decision; compatibility remains held.

Root's instruction-authoritative `hardware/PCB_DESIGN_NOTES.md` is stale at lines10/44/53/61/86: it still selects18350/P1835C2/Keystone1101, ≥35 mm supports and a pending build quantity. PM should align it with protected long18650/P1835J button-top/BH-18650-W, proposed112×36×44 cassette/≥47 mm supports, five complete instruments and optional sixth bare carrier. Qualify its opening parity-pass statement with the actual four metadata warnings. This helper left that root-owned file unchanged.

### Evidence established for this checkpoint

- Re-ran `verify_connectivity.py` against the recorded native XML: **166 endpoints /48 parts**, all41 power endpoints, distinct battery/VSYS/VBUS/3V3, H1 polarity, C17/C18 and exact native MPN/footprint contract agree.
- Re-ran `verify_board.py` against source-bound recorded IPC/XML/ERC/DRC evidence: all166 pad nets and48 values/full footprint IDs agree; identity-sync noop; **ERC0, copper/layout DRC0, unconnected0, four exact metadata warnings retained**. This verifies recorded results, not a new CAD check or zero overall DRC.
- C17/C18 readback: 10 µF on 3V3_OUT/GND, top/0°, anchors(87.46,65.50)/(125.46,65.50); H1 bottom anchor(289,40), pad1 positive/pad2GND. Existing C11/C12 remain. Local routing is supported by the recorded filled-board DRC, not a measured transient result.
- Independently compared all47 current raw placement X/Y/rotations with recorded live IPC inventory: no mismatch. Four verifier unit tests, including its negative-control test, pass.
- `prepare()` requires matching native-source hashes and exact evidence-file hashes, untruncated/all-severity saved/refilled IPC-backed DRC, no copper errors/unconnected items, and only exact reviewed reference/description/UUID metadata warnings. This limited exception does not suppress a DRC category or authorize release. The centroid gap above remains despite those successful guards.

### Remaining release requirements

The current checked-in held package predates this CAD and is explicitly obsolete. Regenerate one coherent package after the placement guard fix; verify every Gerber/drill/PDF/centroid, origin, polarity and hash before replacing it. Preserve the four warnings or resolve them through the CAD owner; do not relabel overall DRC zero.

Keep [18650-handoff.md](18650-handoff.md) and [prototype-validation.md](prototype-validation.md) gates: exact button-top lot and current limits; **L1 4.242 V upper tolerance versus unqualified4.20 V cell maximum**, termination/current/temperature/PCM recovery and bay fit; actual holder removal/contact ampacity and lead OD/crimps; module/socket/fixture/cassette loaded fit and toleranced mechanical CAD; U2/stencil/0805 lands/socket-edge/annular-ring/panel process acceptance; current-limited emulator isolation/UVLO/fault/thermal/full-load checks and five individual acceptance records. None is replaced by this source review or paper-fit drawing.
