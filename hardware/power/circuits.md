# Proposed circuit connections

**2026-10-08 update:** [Concrete branch protection contract](branch-protection.md) supersedes the previous carrier series SS14 connection and fault/low-battery TBDs: upstream 1.25 A fuse, TPS259474 latch-off eFuse with nominal 1 A threshold, reverse insertion/USB isolation and hardware UVLO. Use its exact BOM and endpoint CSV for the next schematic integration. Prior charger/holder qualification remains applicable.

These editable text drawings specify functional connections. Connector numbering and final footprints are intentionally not assigned. `|>|` means anode on the left, cathode/bar on the right. Use a **protected cell/pack output** for BAT_PROT+ and GND; never bypass its protection by grounding an internal cell negative terminal.

## A — external charging, baseline

```text
Protected cell/pack + -- S1 battery ON/OFF -- D_EXT (SS14) --+-- Pico VSYS (39)
                                                          |
Pico USB VBUS ---------------- Pico onboard D1 ------------+
   (40)                 anode VBUS / cathode VSYS
Protected cell/pack - ---------------------------------------- GND (38)

Pico 3V3(OUT) (36) ----- compatible touch/buzzer modules + expansion 3V3
GND ------------------- all module/expansion returns
```

D_EXT anode is S1 output; cathode is VSYS. The cell's protection supplies overcharge, overdischarge and fault-current cutoff; the diode and switch do not supply cell protection. Only a conventional single 4.2 V-charge cell is covered; no LiFePO4, 4.35 V cell or series battery substitution.

S1 disconnects the **battery branch**. USB still powers the instrument when S1 is off. For instrument-off even during USB connection, use a second switch pole that grounds 3V3_EN (37) in OFF and releases it in ON. Do not drive this pin high from 3V3 or BAT. The Pico has its own pull-up to VSYS. This stops the regulator, but is not complete isolation of USB/charger circuitry. Signal lines from externally powered expansion must not back-power the disabled 3V3 rail.

Follow-up candidate S1 is **NKK MN12SS1W03**, a 4 A/30 VDC resistive-rated SPDT ON–ON switch with straight PC terminals and panel bushing. Common 2 connects to D_EXT anode, terminal 3 to battery positive in A (charger OUT in B), and terminal 1 is unconnected to make that throw OFF; verify physical orientation. See [comparison and provisional 1 A sizing allowance](candidate-comparison.md). Capacitive inrush and mechanical fit remain unverified. The original C&K JS102011SAQN is only 0.3 A at 6 VDC and is not the preferred power-branch switch under that allowance. Do not parallel poles to claim a higher rating. The optional two-pole control function needs a separately checked switch and footprint.

SS14 has 40 V reverse and 1 A average forward ratings (with manufacturer thermal conditions), and 0.50 V maximum forward drop at 1 A/25°C. At 3.0 V cell voltage this gives a 2.5 V illustrative VSYS value before other losses. This is not a temperature-wide guaranteed operating margin; include cold diode loss, switch/contact resistance, battery sag and load steps in prototype checks. Leakage also matters during USB-powered or stored operation.

## B — optional onboard charging with separate charge input

```text
Dedicated 5 V USB charge input ---- U1 IN(13)
                                    BQ24074RGTR
Protected cell/pack + ------------- U1 BAT(2,3)
Protected cell/pack - ------------- GND
                                    U1 OUT(10,11) -- S1 -- |>| D_EXT --+-- VSYS(39)
Pico programming USB VBUS ---------------- onboard D1 --------------+
                                    U1 VSS(8) + exposed pad ---------- GND
```

The dedicated charge input and Pico VBUS are **not electrically joined**. Grounds are common. The external diode prevents the higher Pico USB supply from feeding U1 OUT/BAT. Do not connect OUT directly to VSYS: the charger's normal battery-supplement path is not a guaranteed blocker for externally driven OUT. This option uses two USB receptacles unless a later reviewed connector/data design replaces it.

Place S1 after OUT so a cell can charge while the instrument is off. The charger remains connected to the cell; off-state consumption must be included in storage expectations. D_EXT applies in both options, not just A. A removable holder in B also needs a reviewed reverse-insertion safeguard: cell protection does not make U1 BAT tolerant of negative voltage. A mechanically constrained pack connector must have verified polarity, or add a charger-compatible reverse-polarity circuit before release. No extra diode between protected cell and BAT: it would interfere with charging and sensing. U1 is a **charger/power-path IC**, not a replacement for independent cell protection.

### U1 implementation specification (conditional; charging default disabled)

| Pin | Proposed connection |
|---|---|
| 1 TS | Cell-coupled 10 kΩ NTC to GND; candidate Semitec 103AT-2 from TI application example. Validate its temperature thresholds against chosen cell. Do not silently replace by a fixed resistor. |
| 2,3 BAT | Protected cell positive; ceramic 10 µF to GND near pins |
| 4 CE | High via 100 kΩ to OUT for default charging-disabled state; explicit configuration jumper to GND enables charging only after cell/settings review |
| 5 EN2; 6 EN1 | Both tied low initially: USB100 mode, maximum IN current 100 mA. Higher setting requires verified input source entitlement. |
| 7 PGOOD; 9 CHG | Optional open-drain indicators/test points; pull to 3V3 only for Pico GPIO monitoring. No direct 5 V signal into Pico. |
| 8 VSS; exposed pad | GND; connect VSS separately as well as thermal pad, with layout/thermal vias per TI guidance |
| 10,11 OUT | Joined; ceramic 10 µF to GND; then S1 and D_EXT |
| 12 ILIM | Resistor to GND, value TBD from authorized input budget. Must be populated; TI says leaving ILIM open disables charging. |
| 13 IN | Dedicated nominal 5 V charge-port supply; ceramic 1 µF to GND. Connector, ESD and source-policy implementation TBD. |
| 14 TMR | Open selects internal default safety timers; finalize duration for selected cell/rate. Do not ground to disable timers. |
| 15 ITERM | Open selects default termination; select explicit resistor if cell requires another termination current. |
| 16 ISET | Unpopulated initially; charging disabled. Fit cell-matched programming resistor only after approval of actual battery specification. |

Capacitor values are starting candidates within TI's specified ranges (IN 1–10 µF; BAT/OUT 4.7–47 µF). Verify effective capacitance after DC bias, voltage rating, inrush, and placement; no capacitor footprint or MPN is released.

TI §9.3.5 gives `I_CHG = K_ISET / R_ISET`; typical `K_ISET = 890 AΩ`. Use electrical-table worst-case factor and resistor tolerance, not just the typical equation. For illustration **only**, 4.53 kΩ gives about 196 mA typical; with 975 AΩ maximum factor and a 1% resistor, the illustrative maximum is about 217 mA. This is not a selected charging current. Input limiting and system load can reduce actual charge current. Supported programming range is 590 Ω–8.9 kΩ; a cell needing less than the IC's supported charge range needs another charger.

`I_IN_LIMIT = K_ILIM / R_ILIM` in EN2=1, EN1=0 resistor mode. K_ILIM depends on current range; use TI's electrical table. USB100 mode is EN2=0/EN1=0; USB500 is EN2=0/EN1=1; both high suspend input. Do not enable USB500 or resistor mode solely because a cable is plugged in. A dedicated charge port has no USB enumeration here. USB-C would require correct CC sink resistors, connector wiring and a current-advertisement policy; these are not yet designed. Default 100 mA limits charging speed, and requires reviewing timer compatibility once the cell is chosen. For the 1100 mAh minimum candidate capacity, even 100 mA needs at least 11 hours before CV taper and system demand; internal default timers must not be assumed suitable.

BQ24074 OUT is nominally 4.4 V (4.3–4.5 V specified under regulation conditions), then tracks the battery without valid IN. This suits VSYS after D_EXT. Linear charger heat estimate is `(V_IN - V_BAT) × I_CHG + (V_IN - V_OUT) × I_OUT` plus internal losses. Evaluate low battery, highest input and simultaneous playing/charging on the actual two-layer layout. Thermal regulation can reduce charge rate; it is not proof of adequate enclosure cooling.

Evidence: [TI BQ2407x datasheet SLUS810N](https://www.ti.com/lit/ds/symlink/bq24074.pdf), pin tables, electrical tables, §§9.3 and 10–12; [TI explanation of OUT-to-BAT reverse flow](https://e2e.ti.com/support/power-management-group/power-management/f/power-management-forum/1085075/bq24074-is-reverse-current-flow-from-out-to-bat-possible).

## Single Pico USB port charging alternative — unresolved

Raspberry Pi documents VBUS feeding a power-path charger IN and its OUT feeding VSYS through a VBUS-controlled P-channel FET. With valid nominal 5 V VBUS present that FET is OFF: the Pico's D1 powers the system directly. Consequently a charger on Pico VBUS does **not** limit the entire host-port current: budget is Pico/module USB current **plus charger IN current**. Even USB100 at the charger does not make that sum USB100 compliant. A simple diode OUT-to-VSYS also leaves the onboard D1 bypass.

This option is viable only after a reviewed shared-port input policy and total current budget; it is not the default proposal. Removing Pico D1 would change the removable module and needs an explicit PM decision. An external isolated-data programming cable or alternate data connection also needs a specified design. Do not assume a TP4056 module or charger BAT terminal provides proper system load sharing/termination.

## Operating-state review

| State | A | B |
|---|---|---|
| Battery only, switch on | Cell → D_EXT → VSYS | Cell → U1 battery path → OUT → D_EXT → VSYS |
| Pico USB only, battery absent | USB → onboard D1 → VSYS | Same; charger isolated by D_EXT |
| Pico USB + battery | Higher post-diode source supplies VSYS; nominal USB wins; no intended charging | Nominal Pico USB supplies VSYS; D_EXT prevents feeding charger OUT; no charge without dedicated charge input |
| Dedicated charge input + cell, no Pico USB | Not applicable | U1 prioritizes OUT load, reduces charging under input limit, supplements from battery when needed |
| Both USB inputs + cell | Not applicable | Pico typically supplies VSYS; U1 charges cell if enabled; supplies remain diode-isolated, source sharing possible at close voltages |
| Switch off + USB | Pico still on unless 3V3_EN switch added | Same; dedicated charging can continue |
| Protection opens / depleted cell | Battery stops supplying; USB can still run | USB can still run; protection reset/recovery depends on actual pack |

Loss of one source can cause a transient. Verify hot-plug/unplug behavior at load; diode ORing is not a measured brownout guarantee. USB host mode (powering a peripheral from Pico VBUS) is excluded.
