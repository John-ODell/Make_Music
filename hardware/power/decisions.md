# PM decisions and integration handoff

**2026-10-09 update:** [Current protected 18650 handoff](18650-handoff.md) supersedes the 18350/P1835C2/1101 selection. Keep the integrated [fuse/eFuse branch contract](branch-protection.md), voltage thresholds and current limits. Five complete instruments plus an optional sixth bare carrier remain the quote scope. Current-lot cell/charger compatibility, new holder/cassette fit and final exports/tests are open.

The [factory assembly and current-limited bring-up record](prototype-validation.md) provides staged tests and a blank measurement table. No bench results are available; qualify reset dwell, 1S fault response and source isolation on the actual assembly.

## Selected architecture and remaining decisions

User corrected the intended cell to long **protected 18650**. Option A remains removable external charging; option B is not populated. Recommend **Keeppower P1835J**, standard opposite-end-terminal **button-top** version, pending delivered-lot/terminal confirmation for **MPD BH-18650-W**. **L1 charger approval is held** because its published voltage tolerance exceeds the cell page's unqualified maximum; a 500 mA qualification setting does not resolve that gap.

| Decision | Recommended starting point | Release dependency |
|---|---|---|
| Charging | A external charging selected | Verify compatible external charger; no onboard charger in revision 1 |
| Battery form | Protected 18650; Keeppower P1835J opposite-end button-top review candidate | Confirm delivered terminal version, current-lot charge/discharge limits, PCM/recovery and actual fit |
| Pico | Original non-wireless Pico H SC0917, removable in female sockets | Actual engagement/USB access and regulator/current validation |
| Holder/connector | Mechanical PR #30 selects MPD BH-18650-W with included 24 AWG leads; retain JST-PH H1.1+/2GND | Exact-cell fit/contact travel/removal/ampacity; lead OD 0.8–1.5 mm and qualified crimp process; actual harness polarity |
| Cassette / H1 | Mechanical PR #30 proposes 112×36×44 mm cassette, ≥47 mm supports and H1 native (249,40)→(289,40) | Final loaded fit/toleranced CAD and PM native relocation/routing/parity/exports; proposed placement is not completed CAD |
| Instrument parts CSV | PM integrates [instrument-parts-handoff.csv](instrument-parts-handoff.csv) replacement rows | Replace seven matching categories, add charger-input accessory; included holder leads get no separate wire purchasing quantity |
| Switch behavior | Battery branch OFF; USB remains on | Preserve adopted behavior and qualify actual startup/current/low-load switching |
| Switch low-load endurance | MN12SS1W03 silver contacts retained | NKK recommends 0.1 A at 2 V minimum; actual idle/startup current and low-load contact endurance remain unverified. Gold logic contacts cannot carry the 0.70 A branch. See prototype-validation.md. |
| Isolation/protection | TPS259474LRPWR + 1.25 A upstream fuse specified | Integrate exact contract; validate current/reversal/transients on assembled circuit |
| Onboard USB charging | Deferred to a future revision | B is research only; omit charger IC, charging receptacle and related circuitry from revision 1 |
| Charge/input/termination/timer settings | Not applicable to carrier revision 1 | Verify external charger against selected cell limits |
| Module supply and buzzers | Pico 3V3 for compatible modules | TTP223 touch supply supports 3.3 V per merged PM reference; measure full module LED loads, confirm polarity; SunFounder ST0238 selected at 3.3 V; driver/load current and peaks still unverified |
| Low battery shutdown | Hardware UVLO nominal 3.221 V off /3.546 V restart | Adopted in branch-protection.md with tolerances; no firmware ADC changes |
| Added buzzer bulk | Merged schematic PR #27 added C17/C18, 10 µF each on 3V3_OUT | Final PCB synchronization/netlist/BOM/parity, effective capacitance and measured startup/transients |
| Factory scope | Five fully assembled instruments; optional sixth bare keepsake | Accepted complete SMT/THT/harness/mechanical scope and per-unit records; no actual parts for fit metrology yet |

## Schematic integration instructions

A/B are alternatives, not two battery paths to populate simultaneously. The selected isolated output goes to physical VSYS pin 39; GND uses pin 38 and the ground net. The carrier must not short VBUS pin 40 to VSYS. Module power is pin 36. Only connect a switch to pin 37 if the agreed OFF behavior needs regulator disable. Show existing Pico D1 explicitly in the review, even though it is inside the removable module.

For the selected A require protected-cell/pack terminals, F1, S1 and U2 with the support parts in branch-protection.md; U2 OUT connects directly to VSYS and the former series D_EXT is removed. D2 is a shunt clamp, cathode to VSYS. For future B add U1, dedicated charge input and cell temperature sensing as circuits.md specifies; protected battery output is connected to BAT, OUT passes through S1/D_EXT. Do not make an unreviewed connector-pin-order choice. Footprints for diode/IC/switch must be checked against mechanical drawings during integration, and unresolved components must remain unassigned.

## Historical proposal validation (2026-10-07)

- Read power assignment and checked the primary chat's current requirements; used existing supplied power worktree on codex/pcb-power.
- Fetched origin; checked clean assigned worktree and compared guidance to origin/master.
- Downloaded original Pico/Pico 2 and BQ24074 PDFs; read power pin descriptions, source-ORing examples, charger pin mapping/programming, input-current and thermal tables. Visually inspected Pico 2 Figures 8–10.
- Read Vishay SS14 and C&K JS manufacturer ratings/order drawings, and both Keeppower candidate pages; documented their dimensional conflict.
- Reviewed all source states against drawn diode direction and existing Pico D1; calculation spot checks are in current-budget.md.
- Ran git diff --check and inspected the scoped diff before commit. No simulation, ERC, DRC, physical-cell measurement, thermal test or prototype test is claimed.

## Checks required after selection and integration

For revision 1, apply battery/USB and external-charger checks below; onboard charger, NTC, dedicated charge USB, timer and thermal-pad checks apply only to future option B.

The earlier [checkpoint audit](pcbway-readiness.md) does not cover the corrected cell/holder or later header/bulk changes. PM must reconcile final instrument parts/assembly scope and regenerate checks/exports. No physical results are available; current source research and qualified calculations are in [18650-handoff.md](18650-handoff.md).

1. Review connector/holder polarity, Pico power pin numbers, diode cathode, protected-pack return, charger pin mapping and all populated configuration resistors. Review USB source budget and cell/NTC/timer settings before enabling charging.
2. Complete electrical current worksheet. Check switched input/inrush against S1 rating, regulator and GPIO limits, diode voltage/heat/leakage, fuse/wiring fault coordination if required by the selected assembly, and charger thermal layout.
3. Run integrated ERC/DRC and netlist-to-PCB checks, document intentional exceptions, visually review layout, USB/BOOTSEL access, thermal pad and cell clearances. Review assembly services and actual part availability.
4. Prototype with current-limited supplies before fitting the battery. Exercise battery-only, each USB-only state, both USB inputs (B), removal/insertion, switch-off, load steps and low-voltage behavior. Measure 3V3/VSYS transients and check reverse currents into each supply, including diode leakage. Confirm no unexpected charge via the Pico USB port.
5. With the selected protected cell and charger settings, test valid charge, termination under changing load, cell-temperature suspension, protection recovery and enclosure temperature. Do not perform destructive short-circuit testing on a live cell; review protection documentation and validate fault behavior with suitable controlled equipment.
6. Measure real average battery current and discharge behavior before making runtime claims. PM integrates and merges the helper PR; this helper does not merge it.
