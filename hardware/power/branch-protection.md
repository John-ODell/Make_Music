# Revision 1 branch protection — concrete integration contract

Review date 2026-10-08; based on master PR #15 and PM's offboard-holder/JST-PH decision. This replaces the unprotected carrier switch/SS14 branch from PR #14. **Implement the parts and limits below for the prototype.** No cell PCM trip current, measured load, assembled fit or production qualification is inferred.

## Selected topology and load limits

```text
protected cell / offboard holder
 H1.1 (+) -> F1 -> BAT_FUSED_PLUS -> S1.2 common
 S1.3 ON -> BAT_SW_PLUS -> U2.5 IN
 S1.1 OFF -> NC
 U2.6 OUT -> VSYS -> J2.19 / Pico physical39
 H1.2 (-) -> GND -> U2.8 / J2.18 / other grounds
 Pico USB -> Pico's onboard D1 -> VSYS
```

U2 is **TI TPS259474LRPWR**, the circuit-breaker/latch-off variant. It provides reverse-insertion protection, always-active reverse-current blocking, adjustable fault threshold and voltage disconnect. **Remove carrier D1 from the series path**; U2 takes over battery isolation with lower loss. The Pico's internal USB diode stays untouched. D2 below is a shunt transient clamp, not the series diode. A GPIO or bare cell is never a power source for 3V3_OUT. H1 is PM's **JST B2B-PH-K-S(LF)(SN)**: circuit1 positive, circuit2 ground; the assembled harness/holder polarity still needs confirmation. Do not reuse the withdrawn 1095P footprint.

Adopt these prototype design constraints now:

| Quantity | Design constraint |
|---|---|
| Normal branch current through F1/S1/U2 | **≤0.70 A**, including converter input, startup and input-side leakage |
| Total regulated load | **≤350 mA at 3V3**, including Pico; external loads **≤250 mA** and actual Pico regulator validation required |
| All VSYS capacitance, including Pico and external additions | **≤200 µF** for the selected turn-on slope |
| Operating environment | 0–40°C ambient; resistor local temperature ≤70°C |
| Connector / harness | PM's 2 A JST-PH/AWG24 candidate; do not equate connector rating with unknown holder-contact ampacity |
| Protected cell | P1835C2 conventional 1S only; existing cell/charger qualifications remain in rev1-handoff.md |

At minimum computed cutoff 3.053 V on U2 IN, 0.70 A ×45 mΩ switch-path loss and 30 mV additional branch allowance give approximately 2.992 V at VSYS. With a conservative **assumed** 75% Pico efficiency, 350 mA total 3V3 requires about `1.155/(0.75*2.992)=0.515 A`. This supports the 0.70 A limit as a design allowance; efficiency and module current are unmeasured. It does not guarantee the Pico's regulator output. If ST0238/touch/expansion measurements exceed either current constraint, reduce loads or revise the power design before use. USB-mode current remains a separate Pico/host limit; this battery eFuse cannot limit Pico USB's onboard path.

## Exact components and connections

The [endpoint CSV](branch-endpoints.csv) is the pin-by-pin source for schematic/checker integration. Passive two-terminal pin1/2 assignments are a proposed symbol convention; verify their footprint mapping.

| Ref | Exact MPN / value | Required connection / package |
|---|---|---|
| F1 | SCHURTER **3403.0275.23**, UMT-H 1.25 A time-lag | H1.1 to BAT_FUSED_PLUS; 5.3×16 mm SMT body. Upstream backup, not a fast current limiter. |
| S1 | NKK **MN12SS1W03** | 2 common=BAT_FUSED_PLUS; 3=BAT_SW_PLUS; 1 NC. Existing 4 A /30 VDC resistive candidate retained. |
| U2 | TI **TPS259474LRPWR** | 10-pin **RPW0010A VQFN-HR, 2×2 mm**; IN5, OUT6, GND8. Use this exact package drawing, not generic QFN+ground exposed pad. |
| R1 | YAGEO **RC0603FR-07649KL**, 649 kΩ 1% | BAT_SW_PLUS to EN_UVLO /U2.1 |
| R2 | YAGEO **RC0603FR-07332KL**, 332 kΩ 1% | EN_UVLO to GND |
| R3 | YAGEO **RC0603FR-071M05L**, 1.05 MΩ 1% | BAT_SW_PLUS to OVLO /U2.2 |
| R4 | YAGEO **RC0603FR-07332KL**, 332 kΩ 1% | OVLO to GND |
| R5 | YAGEO **RC0603FR-073K32L**, 3.32 kΩ 1% | ILM /U2.9 to GND |
| R6 | YAGEO **RC0603FR-07100RL**, 100 Ω 1% | DVDT /U2.7 to DVDT_CAP; series damping for C3 |
| C1 | TDK **C2012X7R1E475K125AB**, 4.7 µF 25 V X7R 10% | BAT_SW_PLUS to GND; nonpolar 0805, directly at IN/GND |
| C2, C4 | same TDK **C2012X7R1E475K125AB** | VSYS to GND, parallel 9.4 µF nominal; directly at OUT/GND |
| C5, C6 | Panasonic **10SVP47M**, each 47 µF 10 V ±20%, 50 mΩ ESR | Parallel VSYS (+) to GND (−); polarized SMT C6 case, 6.3 mm diameter /5.9 mm body length; hold-up for source transfer |
| C3 | TDK **C1608C0G1H103J080AA**, 10 nF 50 V C0G 5% | DVDT_CAP to GND; 0603 |
| D2 | Vishay **SS14-E3/61T** | Shunt only: anode GND, cathode/band VSYS; SMA/DO-214AC |
| D3 | Littelfuse **SMAJ5.0CA** | Bidirectional TVS BAT_SW_PLUS to GND; SMA/DO-214AC; **CA**, not unidirectional A |
| U2.3 PG | unused | Intentional NC; no pull-up / indicator |
| U2.4 PGTH | unused indication input | Tie GND, not floating; PG indication is not used |
| U2.10 ITIMER | minimum blanking | Intentional NC; no timer capacitor |

All resistors are 0603, 0.1 W, ±100 ppm/°C; dissipation here is far below rating. C1 is deliberately nonpolar because it sees a reversed cell. C2/C4 add output transient capacitance with ample nominal margin over TI's >1 µF recommendation; capacitance falls with DC bias, temperature and aging. Their nominal 9.4 µF is not an effective-capacitance guarantee. Do not substitute a tiny high-density capacitor solely on nominal µF; preserve >1 µF effective at VSYS ≤5.5 V. C3's 50 V rating covers the internal boosted DVDT node and USB-backed output. The series 100 Ω implements TI's advice for DVDT capacitance above 10 nF; it accommodates the positive tolerance of the nominal 10 nF part.

## Current/fault coordination

`ILIM_nom = 3334/3320 = 1.004 A`. TI's table at RILM=3.32 kΩ gives 0.85–1.15 A. Allowing resistor initial tolerance plus a conservative 0.5% temperature allowance gives **0.837–1.168 A** by inverse resistance scaling. This is a calculation using the published table conditions (**VIN=12 V**), not a newly guaranteed 1S characterization. Use **1.2 A** as the branch coordination envelope and verify the selected assembly's fault response at 3.1–4.25 V. The 0.70 A normal limit leaves margin below the published low threshold.

ITIMER open selects the shortest blanking. Overload disconnects/latches; clear the fault then switch OFF/ON. During startup the chip controls inrush/current. The nominal DVDT slope with 10 nF is 0.20 V/ms; 200 µF would add about 40 mA capacitive current. Datasheet timing includes approximately 2 µs breaker response and 500 ns severe-short response, **typical**, not maximum peak-current guarantees. Transient current can exceed ILIM; do not label this an instantaneous 1 A limiter or promise a bounded I²t from typical timing.

F1 is upstream of the switch, input capacitor and TVS, so it backs up input-component shorts and an eFuse failure. It is intentionally separate from electronic overload control. Published UMT-H data support 1.25 A/250 VDC and **1500 A breaking capacity**, greatly above common small chip-fuse interrupt ratings; 0.70 A is below its 0.60×In=0.75 A published 70°C endurance condition. F1 does not open at exactly 1.25 A: its series permits up to 120 s pre-arcing at 2×In and 10–100 ms at 10×In. Its opening time at a real cell fault is not established by the cell's 8 A operating rating. This proposal does not claim single-fault certification or coordinated clearing I²t for every conductor.

For layout/harness integration, qualify holder contacts for **0.70 A normal and at least 1.2 A continuous branch capability**; connector/harness 2 A and switch 4 A exceed that envelope. Route power copper for ≥2 A continuous with local temperature rise reviewed, and use **5 mm-wide /35 µm copper lands at F1**, matching the manufacturer's fuse test-board condition. Keep holder-to-F1 unfused conductors insulated, mechanically restrained and as short as the cassette allows. Put F1 at the board entry before any branches. Neither F1 nor U2 protects a short inside the cell/holder lead before F1; the protected cell's PCM remains required there, with no invented trip threshold. Unknown holder ampacity is a concrete qualification against the chosen limits, not a reason to defer the carrier circuit.

D3's 5 V standoff allows either polarity of a 4.25 V cell without deliberate shunting; rated clamp is 9.2 V at 43.5 A under its specified pulse conditions. It limits input inductive excursions, not continuous overvoltage; a failed-short D3 relies on F1/cell protection. D2 follows TI's recommended output negative-transient clamp. Its SS14 rating now applies to clamp pulses/leakage, not continuous instrument current. USB isolation is U2's back-to-back FET function; USB remains powered through Pico onboard D1, including when S1 is OFF or U2 is undervoltage-disabled.

The direct eFuse OR path has a finite recovery delay after USB removal. Add C5/C6 rather than relying on tiny ceramic bypass alone: minimum initial combined capacitance is 75.2 µF. At the **typical** 50 µs reverse-block recovery and 0.70 A design current, a simple hold-up estimate is `ΔV = I*t/C + I*ESR ≈ 0.483 V`, leaving about 2.57 V from the minimum cutoff input before other losses. This is a calculated transient margin, not a guaranteed recovery time or seamless switchover. Include the Pico's own capacitance in the 200 µF ceiling. **Pico USB charging of these capacitors bypasses the battery eFuse**: check host-side plug-in current and source-transfer reset behavior; battery soft-start does not establish USB inrush compliance. No polymer capacitor goes on the reversible input.

## Low-battery policy, adopted without firmware changes

Use U2's **hardware UVLO** as normal battery shutdown. For R1/R2, factor `1+649/332=2.95482`: nominal disconnect **3.221 V**, restart **3.546 V**, measured at BAT_SW_PLUS. F1/holder/wire loss means the cell terminal itself is at a somewhat higher voltage during load. This endpoint preserves margin above 2.5 V protection cutoff and intentionally sacrifices some capacity for simpler operation.

Including TI threshold extrema, ±0.1 µA pin leakage and ±1.5% resistance allowance, calculated disconnect is **3.053–3.430 V**, restart **3.363–3.752 V**. These ranges include different corners; they are not a particular device's hysteresis pair. UVLO recovery is automatic, unlike latched overcurrent; a depleted cell can rebound and restart. Normal user policy is switch OFF and recharge when battery operation stops, rather than continuing to play through repeated restarts. USB can continue powering the instrument independently; it does not charge the cell. No spare ADC/GPIO is consumed and no unreviewed VSYS-to-cell-voltage inference is required.

The battery is not fully disconnected while S1 is ON after UVLO: TI lists up to 130 µA disabled-state current at its table conditions, plus divider and TVS leakage. S1 OFF disconnects that input branch; remove the cell for storage/external charging. Low-voltage lockout is not indefinite-storage protection.

R3/R4 also gives nominal OVLO trip **4.995 V**, recovery **4.537 V**; corresponding conservative corners trip **4.710–5.315 V**, recovery **4.275–4.860 V**. This protects against an incorrect higher-voltage source; it does not authorize another cell chemistry, charging on the carrier, or reliance on OVLO against arbitrarily fast surges. Both input-derived top resistors exceed TI's 350 kΩ reverse-polarity recommendation: at reversed 4.25 V, worst top-resistor current is below 7 µA. U2's negative input capability covers reversed 1S with USB-backed VSYS; input/output differential is below its 21 V limit.

## Integration and evidence

Preserve J2.16=3V3_OUT, J2.17 NC, J2.18 GND, J2.19 VSYS, J2.20 VBUS_USB and all module/expansion assignments. Delete the old carrier D1 and update the connectivity checker to the CSV; add U2/F1 and support parts. **RPW has power pads5/6, not a ground pad11**; mechanical helper must build/check the land pattern from RPW0010A. No generic QFN substitution. Native schematic and PCB are owned by the other helpers; none edited here, and no KiCad windows were opened by this power task.

Focused prototype validation needed for this circuit: current-limited bench supply at 3.1/3.7/4.25 V with ≤0.70 A load and overload; actual fall/restart ramps; reversed −4.25 V with/without USB and verified harness polarity; startup/short transients at IN/VSYS. Confirm >1 µF output effective capacitance and normal load before a live cell. These determine the remaining assembly-specific behavior; schematic work can proceed with the exact circuit now.

Primary sources read on review date:

- [TI TPS25947 datasheet SLVSFC9C, May 2026](https://www.ti.com/lit/ds/symlink/tps25947.pdf): comparison table, pp.5–11 pins/ratings, §§7.3.1–7.3.8, application/layout and **RPW0010A** drawings. Pin and package pages visually inspected. [Exact orderable part](https://www.ti.com/product/TPS25947/part-details/TPS259474LRPWR).
- [SCHURTER UMT-H current datasheet](https://www.schurter.com/en/datasheet/typ_UMT-H.pdf) and [variant table](https://www.schurter.com/en/datasheet/UMT-H): exact order number, DC breaking rating, endurance, timing and fuse land/test-board condition. This bulky high-breaking backup is chosen for the prototype rather than inventing a safe interrupt rating for a small fuse.
- YAGEO exact manufacturer spec sheets: [649 kΩ](https://yageogroup.com/component-documentation/download/specsheet/RC0603FR-07649KL), [332 kΩ](https://yageogroup.com/component-documentation/download/specsheet/RC0603FR-07332KL), [1.05 MΩ](https://yageogroup.com/component-documentation/download/specsheet/RC0603FR-071M05L), [3.32 kΩ](https://yageogroup.com/component-documentation/download/specsheet/RC0603FR-073K32L), [100 Ω](https://yageogroup.com/component-documentation/download/specsheet/RC0603FR-07100RL); PDFs downloaded/read.
- TDK manufacturer characterization sheets: [4.7 µF X7R](https://product.tdk.com/system/files/dam/doc/product/capacitor/ceramic/mlcc/charasheet/c2012x7r1e475k125ab.pdf), [10 nF C0G](https://product.tdk.com/en/system/files/dam/doc/product/capacitor/ceramic/mlcc/charasheet/c1608c0g1h103j080aa.pdf). Nominal ratings read; effective capacitance is not bench-verified.
- [Panasonic 10SVP47M manufacturer specification](https://industrial.panasonic.com/ww/products/pt/os-con/models/10SVP47M): capacitance/tolerance, ESR, rated voltage, polarity and case.
- [Littelfuse SMAJ datasheet](https://www.littelfuse.com/~/media/electronics/datasheets/tvs_diodes/littelfuse_tvs_diode_smaj_datasheet.pdf.pdf), [Vishay SS14](https://www.vishay.com/docs/88746/ss12.pdf), [NKK MN drawing](https://www.nkkswitches.com/pdf/MN_ToggleSections_DP.pdf). Keep previously verified switch/polarity conventions.
