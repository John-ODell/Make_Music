# Current-budget worksheet

Active prototype constraints: **0.70 A normal battery branch; 350 mA total 3V3 including Pico; 250 mA external ceiling; 100 µF total VSYS capacitance.** These are design limits from [branch-protection.md](branch-protection.md), not measured consumption. The active eFuse path replaces the carrier series diode.

**2026-10-09 cell correction:** use the protected **18650 P1835J candidate** and unresolved lot/charger/holder conditions in [18650-handoff.md](18650-handoff.md). Conventional 1S voltage is unchanged, so all current/protection limits and the 515 mA sizing calculation below remain. Larger capacity does not permit more carrier load. The published 3350 mAh minimum is not usable capacity at our loaded UVLO, and no runtime is inferred from it. Repeat resistance/thermal calculations if the longer cassette changes wire length/contact path.

No component current has been measured. Blank values are **unknown**, not zero. Populate from the actual selected hardware at 3V3 with both buzzers operating, all touch LEDs active, expansion load connected and the intended firmware/clock. Record steady average, startup and coincident peak separately.

| 3V3 load | Quantity | Per-unit average mA | Per-unit peak mA | Evidence / measurement |
|---|---:|---|---|---|
| Pico processor + onboard loads | 1 | TBD | TBD | Selected Pico, clock, code; internal part of regulator load |
| Note touch modules | 8 | TBD | TBD | Exact module + LED state unknown |
| Modifier touch modules | 2 | TBD | TBD | Exact module + LED state unknown |
| Buzzer modules | 2 | TBD | TBD | SunFounder ST0238 selected, 3.3 V supply documented; onboard driver current/peaks unverified |
| Carrier buzzer pull-ups | 2 | TBD | ~0.66 combined | Calculated at nominal 3.3 V with both 10 kΩ pull-ups held LOW; include tolerances |
| Expansion | 1 budget | TBD | TBD | User-specified allowance; do not treat free GPIO as unlimited power |
| Added indicators / other rails | As fitted | TBD | TBD | Include optional indicators and external regulators |

`I_EXT_3V3 = 8*I_NOTE + 2*I_MOD + 2*I_BUZZ + I_EXP + I_BIAS + I_OTHER`

`I_TOTAL_3V3 = I_PICO + I_EXT_3V3`

Use both average and simultaneous peak. Raspberry Pi's recommendation is **less than 300 mA external load** at pin 36, dependent on Pico load and VSYS; it is not an unconditional 300 mA power guarantee. Also check GPIO drive limits separately; power budget does not approve direct buzzer drive or 5 V logic.

Approximate battery-only estimates for the selected fuse/eFuse path (not measured runtime):

- `P_3V3 = 3.3 * I_TOTAL_3V3` with currents in A.
- `V_U2_IN = V_CELL - V_FUSE - I_BAT*R_SWITCH_HOLDER_HARNESS_INPUT_COPPER`.
- `V_SYS_A = V_U2_IN - I_BAT*R_U2_ON - V_OUT_TO_PICO_DROP`. The active carrier has no series D_EXT; measure fuse/contact/copper drops. F1's typical drop is not a maximum resistance specification.
- For future option B, calculate `V_SYS_B` from the charger OUT voltage and that option's actual switch/isolation drops, including U1's battery-path drop at applicable current. Do not assume the selected A path also applies to B.
- `I_BAT ≈ P_3V3 / (eta_PICO * V_SYS) + I_CHARGER_IDLE + I_OTHER_BAT`. Use measured conversion efficiency at low cell voltage; do not assume it is unity or add measured whole-system input and internal Pico current twice.
- `runtime_h ≈ usable_capacity_Ah / measured_average_battery_A`. Capacity depends on endpoint, temperature, aging and load; estimate from the selected cell's discharge curve and verify by test.

At the [branch contract's](branch-protection.md) conservative calculated 2.992 V at VSYS, 350 mA total 3V3 and assumed 75% efficiency require approximately **515 mA** battery current before input-side leakage. This leaves about 185 mA against the 0.70 A branch ceiling, subject to actual efficiency, losses and startup. It is a sizing calculation, not measured headroom.

The carrier's two 10 kΩ buzzer pull-ups add at most approximately **0.66 mA** at 3.3 V when both signals are LOW; include that load separately from the modules. Available expansion current is therefore `min(250, 350-I_PICO) - 10*I_TOUCH - 2*I_BUZZ - I_BIAS - I_OTHER`, all in mA, using simultaneous measured peaks. The 250 mA external allowance leaves 100 mA for Pico only if its measured load stays within that allocation.

**Allocation example, not consumption data:** reserving 70 mA for ten touch boards, 50 mA expansion and 0.66 mA pull-up load leaves 129.34 mA for the two buzzers, or 64.67 mA each with no remaining external margin. Allocating 60 mA per buzzer instead leaves only 9.34 mA external margin. The touch allocation is not a published module maximum, and SunFounder publishes no ST0238 module-current bound. These examples show which measurements can invalidate the budget; they do not qualify the instrument.

The [Tontek TTP223-BA6 datasheet](https://www.tontek.com.tw/uploads/product/243/TTP223-BA6_V2.1_EN.pdf) supports 2.0–5.5 V IC supply. Its no-load low-power current at 3 V is 1.5 µA typical / 3 µA maximum; these values exclude the module indicator LED and output load and must not be used as the module budget. Its application circuit requires 100 nF between VDD/VSS with very short traces. Confirm that capacitor on each actual module: a carrier capacitor before a 100 mm cable does not meet that placement instruction. Test false touches during USB/battery changes, as the datasheet warns about rapidly shifting supplies.

Pico already has regulator output bulk capacitance; the [historical readiness audit](pcbway-readiness.md#bulk-capacitance-and-review-heuristics) recommended two additional 10 µF capacitors at the buzzer supply headers. PM is integrating C17/C18; this worksheet does not claim completed routing/parity or established transient margin. Their 20 µF nominal total is on 3V3_OUT, not directly on VSYS, but still contributes to regulator startup demand. Measure module-end 3V3/GND during simultaneous buzzer edges and touch LED transitions, and include startup in source-current tests.

## USB and future-option charging budget

Revision 1 has no carrier charger. USB alone can power the whole instrument with S1 OFF and bypasses the battery eFuse. Qualify Pico plus all module startup/steady current against the selected USB source, including host connection/boot states; a passing battery-current test does not qualify USB consumption. The charging calculations below apply only to future option B.

For B's dedicated charge input, U1 IN current includes its OUT load plus charging and internal consumption. In the selected linear charger, charge current is not transformed by an efficiency ratio as in a buck charger. Reserve headroom for status LEDs/other input-side circuits. Default USB100 limits U1 IN to at most 100 mA, with OUT load prioritized and battery supplement possible. A larger ISET target does not override this limit; charging may be slow or suspended while playing.

For the unresolved single Pico-port alternative:

`I_USB_TOTAL = I_PICO_USB_BRANCH + I_CHARGER_IN + I_OTHER_VBUS`

U1's input limit only constrains its own branch. Measure and enforce the aggregate under USB connection, enumeration, suspend, bootloader and charger startup. The optional dedicated charge port does not limit current drawn from a separate Pico programming port; that port also needs its own reviewed module/Pico USB budget.

Record charger worst-case heat at low V_BAT/high V_IN, enclosure temperature, switch/diode temperatures, 3V3 minimum during hot-plug and buzzing, and ripple affecting touch detection. Off current must be measured with switch off, with/without USB, and with the optional charger populated. A BQ-connected cell is not electrically disconnected by S1 after OUT.

The historical [comparison](candidate-comparison.md) used a provisional 1 A input allowance. The active normal branch ceiling is **0.70 A**, with the selected NKK switch and fuse/eFuse in branch-protection.md. See [current 18650 qualification](18650-handoff.md) and the explicitly dated [historical package audit](pcbway-readiness.md); final package/fit/bench acceptance remains outstanding.
