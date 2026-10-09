# Battery and USB power proposal

**2026-10-09 correction:** the user intended **long protected 18650**, superseding the 18350 cell/holder selection. The [current 18650 handoff](18650-handoff.md) recommends exact cell **Keeppower P1835J**, requiring a confirmed opposite-end **button-top** version for mechanical PR #30's **MPD BH-18650-W** holder. External-charger approval remains held pending current-lot voltage/current/termination and fit evidence. Included factory 24 AWG leads need measured insulation OD and qualified JST termination. Mechanical owns physical cassette fit/tolerances; PM completed H1 relocation and reconciled the [main procurement CSV](../assembly/instrument-parts.csv). The power CSV remains a supplementary candidate specification.

The [fuse/eFuse branch](branch-protection.md) is integrated in the routed carrier. The [current rear-edge evidence](../review/rear-edge-20261009/README.md) binds native commit `21b2108`; the [final held export review](../review/manufacturing-20261009/README.md) records package publication at `d987896`. The placement-guard defect from the historical `806457b` review was fixed in merged [PR #33](https://github.com/John-ODell/Make_Music/pull/33); current U2 rotation/C17 displacement controls reject before output creation. Four exact metadata warnings remain. The [bounded review](pr28-power-review.md) distinguishes completed document/export work from remaining physical gates. **No physical parts, fit measurements, bench validation or manufacturing release are available.**

## Recommendation

Implement **A: removable protected conventional 4.2 V-charge 18650 cell, externally charged, switched through the specified fuse/eFuse into Pico VSYS**. The eFuse supplies the battery with reverse-current blocking alongside the Pico's existing USB diode, preserving an unmodified removable original Pico H **SC0917**. Retain 0.70 A battery input, 350 mA total/250 mA external 3V3 and all existing protection values. **B: separate USB charge input + BQ24074 power path + protected cell** remains future research and is omitted from revision 1. The Pico USB port supplies programming/USB power and does not charge the battery.

Updated quote preference (2026-10-08): **five fully assembled instruments**, including populated SMT/THT carriers, harnesses and mechanical work, plus an **optional sixth bare carrier keepsake**. Fit measurements and supplier scope/pricing remain pending; the optional bare board does not replace any of the five assembled units. See the current 18650 handoff for exact remaining holds.

- [Factory assembly and staged prototype validation record](prototype-validation.md)
- [Current protected 18650 parts and integration handoff](18650-handoff.md)
- [Historical PCBWay audit of the 18350 checkpoint](pcbway-readiness.md)
- [Superseded 18350 cell/charger research](rev1-handoff.md)
- [Circuit connections and operating states](circuits.md)
- [Candidate BOM and verification evidence](BOM.md)
- [Historical battery budget comparison and switch research](candidate-comparison.md)
- [Current and runtime worksheet](current-budget.md)
- [Open decisions and integration checks](decisions.md)

## Verified Pico interface

Both non-wireless Pico and Pico 2 documentation specify these **physical header pins**, not GPIO numbers:

| Signal | Physical pin | Carrier use |
|---|---:|---|
| VBUS | 40 | USB voltage/sense only in A; do not join to VSYS or battery |
| VSYS | 39 | Isolated carrier power input, 1.8–5.5 V allowed |
| GND | 38 | Common circuit return; also use other ground pins as appropriate |
| 3V3_EN | 37 | Pull to GND to disable regulator, if full USB-connected instrument-off is required |
| 3V3(OUT) | 36 | Regulated module supply; Raspberry Pi recommends external load below 300 mA, dependent on processor load and VSYS |

USB supplies VSYS through the Pico's onboard D1 Schottky diode. The active U2 eFuse completes the battery OR path; its OUT is VSYS. The earlier carrier series-diode alternative used anode toward the battery and cathode toward VSYS. The higher voltage after its diode drop supplies the instrument; nominal USB wins over a cell. Diodes block ordinary reverse supply current, with finite leakage. The Pico USB port does not charge the cell. Do not connect battery to 3V3, GPIO, or VBUS.

The 1.8 V VSYS capability is a regulator specification, not permission to discharge a Li-ion cell that low. A protected cell and a chosen normal discharge endpoint remain necessary. The identified TTP223 touch IC supports 3.3 V; complete touch-module current/LED behavior and selected SunFounder ST0238 load current remain unverified. See [buzzer evidence](../components/BUZZER_MODULE.md). See the PM's [touch reference](../components/TOUCH_MODULE.md), incorporated from origin/master commit 6a61587.

Evidence: Raspberry Pi [Pico datasheet](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf), pin descriptions and §§4.4–4.6; [Pico 2 datasheet](https://datasheets.raspberrypi.com/pico/pico-2-datasheet.pdf), pin descriptions and §§5.4–5.6. Both PDFs were downloaded and their relevant sections read. Pico 2 Figures 8–10 were visually inspected. Wireless models are outside this verification.

## What this review establishes

Manufacturer documents support the conventional 1S circuit topology, power pin mapping and identified cell candidate. They do not establish current-lot charging compatibility, holder fit, real current draw, PCB thermal performance, USB compliance or a tested instrument. Source-bound review and the coherent held export package are complete for the stated checkpoint. PM retains release ownership; the physical/process checks in decisions.md and prototype-validation.md remain open, and any later CAD change requires matching evidence and exports.
