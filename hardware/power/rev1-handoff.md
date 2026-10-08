# Revision 1 power integration handoff

Reviewed 2026-10-07 against origin/master including PRs #10 and #11. User selected removable protected 18350 with external charging. **Exact review targets: Keeppower P1835C2 cell and Keeppower L1 external charger at 500 mA. Electrical ratings support this candidate pairing subject to the gaps below; neither physical fit nor complete charging compatibility has been verified.** No onboard charging parts belong in revision 1.

## Exact cell and external charger

| Item | Verified published evidence | Integration implication |
|---|---|---|
| Keeppower P1835C2 protected 18350 | Manufacturer product pages: 3.7 V nominal, 4.2 V charge, protection against overcharge/discharge/current/short, 1100 mAh minimum / 1150 typical despite 1200 headline; standard charge 220 mA, maximum 1.1 A, maximum discharge 8 A. | Use only the named protected assembly, not a bare 18350. These are operating ratings, not PCM trip thresholds. |
| P1835C2 test report S03A22100287L00101, 2022 sample | Printed pp. 4–5: CC/CV, 770 mA maximum charge, 4.25 V upper charge limit, 24 mA taper-off, 0–45°C charging; discharge maximum 10 A and endpoint 2.5 V. | Conflict with retail-era product data: use the stricter 770 mA charge and 8 A discharge bounds for planning. Obtain current-lot confirmation; the report applies to tested samples. |
| Keeppower L1, manufacturer manual V1.0 | Micro-USB input 5 V / 1 A; selectable 500/1000 mA output, 4.2 V ±1%; lists 18350 and specifically recommends 500 mA for it. USB cable and bag supplied. | Select and verify **500 mA each charging session**; no reliance on startup memory/default. Separate suitable 5 V supply required. L1 is off-board equipment, not a carrier component. |

L1 nominal 500 mA is below both published cell maxima. Its stated voltage range is 4.158–4.242 V, within the older report's 4.25 V upper limit, but above the product pages' unqualified 4.20 V maximum. This is evidence for a review target, not resolution of the current-lot voltage tolerance. The L1 manual does not specify current tolerance, termination current, cell-temperature sensing, protected-cell usable bay length or recovery of a tripped PCM. These are explicit gaps: confirm delivered charger revision and current-lot limits; verify termination against the reported 24 mA taper criterion, temperature handling and physical fit before approving the pair. Do not infer temperature protection from the cell's advertised PCM features. Do not use the 1 A setting: it exceeds the report's 770 mA limit.

The previously priced XTAR ANT MC1 Plus remains historical comparison only. L1 replaces it as this handoff's review target because its manual explicitly identifies the 500 mA setting for 18350; automatic current selection and charger revisions are not inferred.

Sources: [Keeppower China cell page](https://www.keeppower.com.cn/products_detail.php?id=566), [Keeppower global cell page](https://www.keeppower.com/product/keeppower-18350-1200mah-protected-li-ion-rechargeable-battery-p1835c2/), [original P1835C2 lab report hosted by distributor](https://cdn03.plentymarkets.com/i9a0e0hd8l6w/frontend/Datenblaeter/Keeppower/P1835C3/KEEPPOWER_P1835C2_IEC62133-2_2017_Test_report_S03A22100287L00101_20221103.pdf), [manufacturer-authored L1 manual hosted by TME](https://www.tme.eu/Document/f545a63a03e51e3b3ea513f2f0317887/L1_KeepPower_EN.pdf). Report and manual were read; no PDF is redistributed in this repository.

## Connection contract for schematic helper

```text
P1835C2 protected + -> HOLDER_PLUS -> BAT_PROT_PLUS -> S1 common 2
S1 throw 3 -> BAT_SW_PLUS -> D_EXT anode
S1 throw 1 -> unconnected (OFF)
D_EXT cathode/band -> VSYS -> J2.19 -> Pico physical 39
P1835C2 protected - -> HOLDER_MINUS -> GND -> J2.18 / other GND
Pico USB -> onboard D1 -> VSYS (inside removable Pico)
J2.20 / physical 40 -> VBUS_USB (existing separate net)
J2.16 / physical 36 -> 3V3_OUT -> module/expansion supplies
J2.17 / physical 37 -> retain current NC (Pico internal enable default)
```

S1 is NKK **MN12SS1W03**, SPDT ON–ON, manufacturer common terminal 2; verify symbol numbering against the drawing rather than assuming a generic SW_SPDT symbol has this map. The unconnected throw creates battery OFF. Mechanical orientation/label positions follow the manufacturer's keyway drawing and actual mounting. Rating: 4 A at 30 VDC resistive; capacitive inrush remains a separate check. D_EXT is Vishay **SS14-E3/61T**, SMA/DO-214AC, 40 V / 1 A under datasheet thermal conditions. Cathode faces VSYS. See [NKK drawing](https://www.nkkswitches.com/pdf/MN_ToggleSections_DP.pdf) and [Vishay datasheet](https://www.vishay.com/docs/88746/ss12.pdf).

Replace logical X1 with these real parts; X1 is not a physical three-pin connector. Preserve VBUS_USB separately; add no carrier bridge to VSYS, cell or 3V3_OUT. Existing Pico D1 and regulator stay inside the module. Carrier holder pad numbers are **not assigned** by this contract: mechanical helper must establish actual plus/minus pads and verify contacts before mapping. Battery negative is the protected assembly's external negative, never a bypass connection to its internal cell.

Battery-only uses D_EXT; nominal USB power uses Pico D1. Both may be connected with finite diode leakage. S1 OFF disconnects the battery branch but USB still powers the instrument. Pico USB does not charge the cell. If full OFF with USB attached is wanted, PM must authorize a revised enable/switch circuit. Disconnect USB and switch OFF before removing/inserting the cell or Pico. Remove the cell for external charging; no charger leads attach to the carrier.

After integration update the schematic helper's connectivity checker to replace its three logical X1 endpoints with the actual power endpoints. Preserve all socket mappings and intentional NC contacts. Run integrated ERC and review the source paths; an ERC pass does not certify load limits, polarity or fit. This helper has not edited KiCad or run integrated ERC.

## Holder and load handoff

Keep the largest previously observed manufacturer tolerance envelope, **39.3 mm length × 18.7 mm diameter**, as a lower planning bound. Public dimensional snapshots conflict; add verified contact travel, insertion and insulation clearances rather than treating this as a footprint or measured fit. Keystone 1095/1096 remain mechanical candidates, not approved P1835C2 holders. Mechanical helper owns exact holder, pad polarity, footprint, underside mounting, retention, reverse-insertion handling and charger-bay fit evidence. Existing enclosure reservations are provisional.

SunFounder **ST0238**, two modules, is now selected; its documented 3.3 V supply is appropriate for the intended 3V3_OUT rail. Actual idle, PWM, startup and simultaneous peak current remain unknown, including its onboard driver. Active-low behavior needs the module/firmware integration review. Do not replace unknown current with bare-buzzer or touch-IC current. See [buzzer evidence](../components/BUZZER_MODULE.md) and [current worksheet](current-budget.md).

The provisional 1 A input allowance is a sizing assumption, not consumption or a current limiter. SS14 thermal/headroom checks and Pico regulator validation remain necessary. An 8 A cell operating rating does not protect a 1 A diode or establish PCM fault cutoff: obtain PCM trip/recovery data and coordinate a branch fuse or other current limit with holder, switch, wiring and diode before fabrication. No fuse MPN/rating is assigned without those limits and measured inrush. Choose a normal low-battery shutdown above the cell's 2.5 V fault boundary. No runtime promise is supported.

## PM decisions still required

- Approve current-lot cell/charger limits, termination, temperature policy and protection recovery; current documents do not fully establish compatibility.
- Select and verify holder, polarity/reverse-insertion mitigation, contact rating and fit; determine branch fault protection.
- Decide USB-connected OFF behavior, exact Pico model, low-battery endpoint and expansion budget.
- Measure full instrument load and hot-plug behavior, then complete integrated electrical and mechanical checks before routing/fabrication release.
