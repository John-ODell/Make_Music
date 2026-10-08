# PM decisions and integration handoff

## Selected architecture and remaining decisions

User selected removable protected 18350 and external charging for the first design on 2026-10-07. Integrate option A; option B charging circuitry is not populated in this revision. The [revision 1 handoff](rev1-handoff.md) narrows review to P1835C2 and L1 at 500 mA, with explicit evidence gaps; this does not approve holder fit or complete charging compatibility.

| Decision | Recommended starting point | Release dependency |
|---|---|---|
| Charging | A external charging selected | Verify compatible external charger; no onboard charger in revision 1 |
| Battery form | Protected 18350 selected; P1835C2 remains an exact-cell candidate | Exact cell/lot datasheet, protection thresholds, current limits, recovery and mechanical measurements |
| Pico | Non-wireless Pico/Pico 2 supported by reviewed interface | Exact model, header sockets, regulator/current validation |
| Holder/connector | Leave unassigned | Actual protected-cell envelope; two manufacturer length values conflict; connector polarity verified by measurement; B requires reverse-insertion safeguard |
| Switch behavior | Battery branch off; USB remains on | Decide whether instrument-off during USB needs 3V3_EN pole; current/inrush rating verified |
| Isolation loss | Schottky first revision | Measure low-battery margin, leakage and thermal behavior; P-FET improvement can be reviewed later |
| Onboard USB charging | Deferred to a future revision | B is research only; omit charger IC, charging receptacle and related circuitry from revision 1 |
| Charge/input/termination/timer settings | Not applicable to carrier revision 1 | Verify external charger against selected cell limits |
| Module supply and buzzers | Pico 3V3 for compatible modules | TTP223 touch supply supports 3.3 V per merged PM reference; measure full module LED loads, confirm polarity; SunFounder ST0238 selected at 3.3 V; driver/load current and peaks still unverified |
| Low battery shutdown | Normal shutdown above protection trip | Chosen endpoint/hysteresis and firmware/hardware policy; protection is a fault boundary |

## Schematic integration instructions

A/B are alternatives, not two battery paths to populate simultaneously. The selected isolated output goes to physical VSYS pin 39; GND uses pin 38 and the ground net. The carrier must not short VBUS pin 40 to VSYS. Module power is pin 36. Only connect a switch to pin 37 if the agreed OFF behavior needs regulator disable. Show existing Pico D1 explicitly in the review, even though it is inside the removable module.

For A require protected-cell/pack terminals, S1 and D_EXT with the cathode to VSYS. For B add U1, dedicated charge input and cell temperature sensing as circuits.md specifies; protected battery output is connected to BAT, OUT passes through S1/D_EXT. Do not make an unreviewed connector-pin-order choice. Footprints for diode/IC/switch must be checked against mechanical drawings during integration, and unresolved components must remain unassigned.

## Validation performed for this proposal

- Read power assignment and checked the primary chat's current requirements; used existing supplied power worktree on codex/pcb-power.
- Fetched origin; checked clean assigned worktree and compared guidance to origin/master.
- Downloaded original Pico/Pico 2 and BQ24074 PDFs; read power pin descriptions, source-ORing examples, charger pin mapping/programming, input-current and thermal tables. Visually inspected Pico 2 Figures 8–10.
- Read Vishay SS14 and C&K JS manufacturer ratings/order drawings, and both Keeppower candidate pages; documented their dimensional conflict.
- Reviewed all source states against drawn diode direction and existing Pico D1; calculation spot checks are in current-budget.md.
- Ran git diff --check and inspected the scoped diff before commit. No simulation, ERC, DRC, physical-cell measurement, thermal test or prototype test is claimed.

## Checks required after selection and integration

For revision 1, apply battery/USB and external-charger checks below; onboard charger, NTC, dedicated charge USB, timer and thermal-pad checks apply only to future option B.

1. Review connector/holder polarity, Pico power pin numbers, diode cathode, protected-pack return, charger pin mapping and all populated configuration resistors. Review USB source budget and cell/NTC/timer settings before enabling charging.
2. Complete electrical current worksheet. Check switched input/inrush against S1 rating, regulator and GPIO limits, diode voltage/heat/leakage, fuse/wiring fault coordination if required by the selected assembly, and charger thermal layout.
3. Run integrated ERC/DRC and netlist-to-PCB checks, document intentional exceptions, visually review layout, USB/BOOTSEL access, thermal pad and cell clearances. Review assembly services and actual part availability.
4. Prototype with current-limited supplies before fitting the battery. Exercise battery-only, each USB-only state, both USB inputs (B), removal/insertion, switch-off, load steps and low-voltage behavior. Measure 3V3/VSYS transients and check reverse currents into each supply, including diode leakage. Confirm no unexpected charge via the Pico USB port.
5. With the selected protected cell and charger settings, test valid charge, termination under changing load, cell-temperature suspension, protection recovery and enclosure temperature. Do not perform destructive short-circuit testing on a live cell; review protection documentation and validate fault behavior with suitable controlled equipment.
6. Measure real average battery current and discharge behavior before making runtime claims. PM integrates and merges the helper PR; this helper does not merge it.
