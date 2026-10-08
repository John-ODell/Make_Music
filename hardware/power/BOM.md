# Candidate BOM — no purchasing or assembly release

**2026-10-08 update:** [Concrete branch protection contract](branch-protection.md) supersedes the previous carrier series SS14 connection and fault/low-battery TBDs: upstream 1.25 A fuse, TPS259474 latch-off eFuse with nominal 1 A threshold, reverse insertion/USB isolation and hardware UVLO. Use its exact BOM and endpoint CSV for the next schematic integration. Prior charger/holder qualification remains applicable.

Exact core part candidates below are electrically researched. Unselected interfaces and footprints remain explicitly TBD.

The active exact carrier BOM and pin connections are the table in [branch-protection.md](branch-protection.md). It selects F1 **3403.0275.23**, S1 **MN12SS1W03**, U2 **TPS259474LRPWR**, six specified 0603 resistors, four specified ceramic capacitors and two 10SVP47M polymer hold-up capacitors, D2 **SS14-E3/61T** as a shunt clamp and D3 **SMAJ5.0CA**. The old series D_EXT/PCB D1 is removed. No branch protection part/value is left TBD.

| Offboard / interface item | Exact review target | Status |
|---|---|---|
| Protected cell | Keeppower P1835C2 | Current-lot ratings/charging compatibility and actual fit pending |
| Charger | Keeppower L1 at 500 mA only | External equipment; complete compatibility pending as documented |
| Holder | Keystone 1101 in insulated cassette | PM-approved candidate; ampacity/fit unverified; no direct PCB footprint |
| Carrier battery header | JST B2B-PH-K-S(LF)(SN), circuit1 positive /2 GND | PM-directed candidate; 2 A harness design basis, assembled polarity must be checked |

BQ24074, NTC, charge-input connector and configuration parts are **omitted from revision 1**. Option B in circuits.md is future research only. Charger USB cable is external equipment; its 5 V adapter is separately required. No ordering or assembly release is authorized by this candidate BOM.

## Primary evidence

- [Vishay SS12–SS16 datasheet, document 88746](https://www.vishay.com/docs/88746/ss12.pdf): ratings, polarity band, SMA package and E3/61T ordering scheme. [SS14 product page](https://www.vishay.com/en/product/88746/) is the family entry point. Verify final landing pattern against its mechanical drawing.
- [NKK MN toggle drawing](https://www.nkkswitches.com/pdf/MN_ToggleSections_DP.pdf): MN12SS1W03 terminal arrangement, 4 A / 30 VDC resistive rating and straight PC terminal geometry.
- Historical / future-option references: [C&K JS datasheet](https://www.ckswitches.com/media/1422/js.pdf), revised 2026-01-14: rating and JS102011SAQN drawing on page 4. No switch footprint has been assigned.
- [TI BQ24074 datasheet](https://www.ti.com/lit/ds/symlink/bq24074.pdf), SLUS810N, October 2021: pin mapping, RGT package, charger programming and thermal/layout requirements. NTC identification is from TI's application example; cell-temperature compatibility remains unverified.
- [Semitec AT thermistor datasheet](https://www.semitec-global.com/uploads/2022/01/P12-13-AT-Thermistor.pdf): 103AT-2 is 10 kΩ at 25°C, with the AT-2 mechanical form; thermal mounting and cell limits still need review.
- [Keeppower China P1835C2](https://www.keeppower.com.cn/products_detail.php?id=566) and [Keeppower P1835C2](https://www.keeppower.com/product/keeppower-18350-1200mah-protected-li-ion-rechargeable-battery-p1835c2/): candidate properties checked on review date. Both list standard charge 220 mA and maximum 1.1 A, but the older model-specific test report gives a stricter 770 mA maximum; the L1 review target uses 500 mA only. Obtain a lot-specific specification before use.

## Battery evidence conflict

The two manufacturer pages disagree on length: **39.1 ±0.2 mm** versus **38.5 ±0.2 mm**, both at diameter 18.5 ±0.2 mm. For mechanical investigation reserve at least the larger published envelope (39.3 mm length, 18.7 mm diameter), then add holder-contact travel and assembly clearance based on the actual holder. This is not a released holder dimension. A holder sized for an unprotected 35 mm-long cell may fail to fit this candidate.

The pages advertise 1200 mAh nominal but describe 1150 mAh typical and 1100 mAh minimum. Do not promise runtime from the headline capacity. Protection's published 2.5 V endpoint is not our desired normal-use shutdown threshold. Published protection features do not establish charge-temperature monitoring; B needs the reviewed NTC implementation.

If a pouch is preferred, select a documented protected 1S 4.2 V pack with its own exact MPN, connector polarity, capacity, charge rate, protection/recovery and mechanical constraints. No bare pouch cell substitution is authorized by this BOM. Board-level protection is not designed here because A/B deliberately require protected cells; a bare-cell choice triggers a separate protection circuit review.
