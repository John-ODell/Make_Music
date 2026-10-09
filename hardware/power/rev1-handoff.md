# Revision 1 power integration handoff

**Historical 18350 research — superseded 2026-10-09.** The user corrected the intended cell to long protected 18650. Use [18650-handoff.md](18650-handoff.md) for current exact parts, limits and charger HOLD. The original 18350 sources, numerical limits and fit proposals below are retained as history and do not qualify P1835J or its holder/charger.

**2026-10-08 update:** [Concrete branch protection contract](branch-protection.md) supersedes the previous carrier series SS14 connection and fault/low-battery TBDs: upstream 1.25 A fuse, TPS259474 latch-off eFuse with nominal 1 A threshold, reverse insertion/USB isolation and hardware UVLO. Use its exact BOM and endpoint CSV for the next schematic integration. Prior charger/holder qualification remains applicable.

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

The basic branch was integrated in PR #14. For the next revision use [branch-protection.md](branch-protection.md) and [branch-endpoints.csv](branch-endpoints.csv): fuse before S1, TPS259474LRPWR after S1, U2 OUT directly to VSYS, carrier series diode removed. The complete support-part pin map and current/voltage limits are defined there. Preserve the socket power mappings and Pico's onboard USB diode. USB remains on with the battery switch OFF; external charging remains off-board.

## Holder and load handoff

Keep the largest previously observed manufacturer tolerance envelope, **39.3 mm length × 18.7 mm diameter**, as a lower planning bound. Public dimensional snapshots conflict; add verified contact travel, insertion and insulation clearances rather than treating this as a footprint or measured fit. PM now approves an offboard Keystone 1101 candidate in an insulated underside cassette with a factory-assembled JST-PH harness, not exact protected-cell fit certification. The withdrawn 1095P footprint is not usable. Mechanical helper owns exact holder, pad polarity, footprint, underside mounting, retention, reverse-insertion handling and charger-bay fit evidence. Existing enclosure reservations are provisional.

SunFounder **ST0238**, two modules, is now selected; its documented 3.3 V supply is appropriate for the intended 3V3_OUT rail. Actual idle, PWM, startup and simultaneous peak current remain unknown, including its onboard driver. Active-low behavior needs the module/firmware integration review. Do not replace unknown current with bare-buzzer or touch-IC current. See [buzzer evidence](../components/BUZZER_MODULE.md) and [current worksheet](current-budget.md).

Active design limits and exact fuse/eFuse, reverse-insertion mitigation and normal hardware low-battery policy are now set in branch-protection.md. Cell PCM trip data remains unknown, without deferring downstream branch protection. No runtime promise is supported.

## PM decisions still required

- Approve current-lot cell/charger limits, termination, temperature policy and protection recovery; current documents do not fully establish compatibility.
- Verify holder ampacity against the chosen branch limits, harness polarity and fit; implement the selected fuse/eFuse protection.
- Preserve battery-only OFF behavior and adopted hardware UVLO; confirm exact Pico and constrain expansion within the selected budget.
- Measure full instrument load and hot-plug behavior, then complete integrated electrical and mechanical checks before routing/fabrication release.
