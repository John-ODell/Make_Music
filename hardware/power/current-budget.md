# Current-budget worksheet

Active prototype constraints: **0.70 A normal battery branch; 350 mA total 3V3 including Pico; 250 mA external ceiling; 100 µF total VSYS capacitance.** These are design limits from [branch-protection.md](branch-protection.md), not measured consumption. The active eFuse path replaces the carrier series diode; diode-drop illustrations below are historical sizing examples.

No component current has been measured. Blank values are **unknown**, not zero. Populate from the actual selected hardware at 3V3 with both buzzers operating, all touch LEDs active, expansion load connected and the intended firmware/clock. Record steady average, startup and coincident peak separately.

| 3V3 load | Quantity | Per-unit average mA | Per-unit peak mA | Evidence / measurement |
|---|---:|---|---|---|
| Pico processor + onboard loads | 1 | TBD | TBD | Selected Pico, clock, code; internal part of regulator load |
| Note touch modules | 8 | TBD | TBD | Exact module + LED state unknown |
| Modifier touch modules | 2 | TBD | TBD | Exact module + LED state unknown |
| Buzzer modules | 2 | TBD | TBD | SunFounder ST0238 selected, 3.3 V supply documented; onboard driver current/peaks unverified |
| Expansion | 1 budget | TBD | TBD | User-specified allowance; do not treat free GPIO as unlimited power |
| Added indicators / other rails | As fitted | TBD | TBD | Include optional indicators and external regulators |

`I_EXT_3V3 = 8*I_NOTE + 2*I_MOD + 2*I_BUZZ + I_EXP + I_OTHER`

`I_TOTAL_3V3 = I_PICO + I_EXT_3V3`

Use both average and simultaneous peak. Raspberry Pi's recommendation is **less than 300 mA external load** at pin 36, dependent on Pico load and VSYS; it is not an unconditional 300 mA power guarantee. Also check GPIO drive limits separately; power budget does not approve direct buzzer drive or 5 V logic.

Approximate battery-only estimates (not measured runtime):

- `P_3V3 = 3.3 * I_TOTAL_3V3` with currents in A.
- `V_SYS_A = V_CELL - V_D_EXT - I_BAT*R_SWITCH_CONTACTS_WIRING`.
- `V_SYS_B` also subtracts U1 battery-path drop; use its electrical table at applicable current.
- `I_BAT ≈ P_3V3 / (eta_PICO * V_SYS) + I_CHARGER_IDLE + I_OTHER_BAT`. Use measured conversion efficiency at low cell voltage; do not assume it is unity or add measured whole-system input and internal Pico current twice.
- `runtime_h ≈ usable_capacity_Ah / measured_average_battery_A`. Capacity depends on endpoint, temperature, aging and load; estimate from the selected cell's discharge curve and verify by test.

**Illustration only:** 100 mA total 3V3 load, 3.0 V cell, assumed 0.50 V diode drop, assumed 85% regulator efficiency and zero extra losses gives `I_BAT ≈ 3.3*0.100/(0.85*2.5) = 155 mA`. At 200 mA total it is about 311 mA, already above the original 0.3 A slide-switch rating before transients. This demonstrates why selecting a switch from 3V3 current alone is insufficient. The efficiencies, currents and diode drop are calculation inputs, not instrument specifications.

The [Tontek TTP223-BA6 datasheet](https://www.tontek.com.tw/uploads/product/243/TTP223-BA6_V2.1_EN.pdf) supports 2.0–5.5 V IC supply. Its no-load low-power current at 3 V is 1.5 µA typical / 3 µA maximum; these values exclude the module indicator LED and output load and must not be used as the module budget. Confirm local bypassing on each actual module and test false touches during USB/battery changes, as the datasheet warns about rapidly shifting supplies.

## USB and charging budget

For B's dedicated charge input, U1 IN current includes its OUT load plus charging and internal consumption. In the selected linear charger, charge current is not transformed by an efficiency ratio as in a buck charger. Reserve headroom for status LEDs/other input-side circuits. Default USB100 limits U1 IN to at most 100 mA, with OUT load prioritized and battery supplement possible. A larger ISET target does not override this limit; charging may be slow or suspended while playing.

For the unresolved single Pico-port alternative:

`I_USB_TOTAL = I_PICO_USB_BRANCH + I_CHARGER_IN + I_OTHER_VBUS`

U1's input limit only constrains its own branch. Measure and enforce the aggregate under USB connection, enumeration, suspend, bootloader and charger startup. The optional dedicated charge port does not limit current drawn from a separate Pico programming port; that port also needs its own reviewed module/Pico USB budget.

Record charger worst-case heat at low V_BAT/high V_IN, enclosure temperature, switch/diode temperatures, 3V3 minimum during hot-plug and buzzing, and ripple affecting touch detection. Off current must be measured with switch off, with/without USB, and with the optional charger populated. A BQ-connected cell is not electrically disconnected by S1 after OUT.

The follow-up [comparison](candidate-comparison.md) uses a provisional 1 A input-branch design allowance and a stronger NKK switch candidate. These are sizing assumptions, not measured loads or approval of the rest of the power chain.
