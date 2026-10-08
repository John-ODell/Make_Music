# Battery and USB power proposal

**2026-10-08 update:** [Concrete branch protection contract](branch-protection.md) supersedes the previous carrier series SS14 connection and fault/low-battery TBDs: upstream 1.25 A fuse, TPS259474 latch-off eFuse with nominal 1 A threshold, reverse insertion/USB isolation and hardware UVLO. Use its exact BOM and endpoint CSV for the next schematic integration. Prior charger/holder qualification remains applicable.

Review date: 2026-10-07. **Architecture A selected by the user for the first revision: removable protected 18350 with external charging. P1835C2 cell and L1 at 500 mA are exact review targets; holder and complete charger compatibility remain unverified; no fabrication release, routed PCB, or bench validation.** The basic branch was integrated in PR #14; the protected replacement now needs integration.

## Recommendation

Implement **A: removable protected conventional 4.2 V-charge 18350 cell, externally charged, switched through the specified fuse/eFuse into Pico VSYS**. The eFuse supplies the battery with reverse-current blocking alongside the Pico's existing USB diode, preserving an unmodified removable Pico. **B: separate USB charge input + BQ24074 power path + protected cell** remains reference material for a future revision, not part of the first-revision BOM. Exact cell, holder, switch and compatible external charger still require verification. The Pico USB port is for programming and USB power; it does not charge the battery.

- [Revision 1 exact parts and schematic integration handoff](rev1-handoff.md)
- [Circuit connections and operating states](circuits.md)
- [Candidate BOM and verification evidence](BOM.md)
- [Protected battery budget comparison and stronger switch](candidate-comparison.md)
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

Manufacturer documents support the circuit topology, power pin mapping and candidate component limits. They do not establish holder fit, real current draw, PCB thermal performance, USB compliance, or a tested instrument. No ERC/DRC was run because this deliverable contains connection drawings and research, not an instantiated KiCad schematic or board. Integration must instantiate the selected option, then run the project checks and prototype tests listed in decisions.md.
