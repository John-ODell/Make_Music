# Candidate BOM — no purchasing or assembly release

Exact core part candidates below are electrically researched. Unselected interfaces and footprints remain explicitly TBD.

| Ref / revision 1 | Manufacturer / exact MPN | Quantity | Evidence and limits |
|---|---|---:|---|
| B1 | Keeppower **P1835C2** | 1 | Exact protected-cell review target; current-lot ratings and fit pending. See [handoff](rev1-handoff.md), including conflicting charge limits. |
| D_EXT | Vishay **SS14-E3/61T** | 1 | SMA/DO-214AC Schottky, 40 V, 1 A with stated thermal conditions; cathode band toward VSYS. Reverse leakage is finite. |
| S1 | NKK **MN12SS1W03** | 1 | SPDT ON–ON, straight PC pins/panel bushing, 4 A at 30 VDC resistive. Common 2; throw 3 supplies diode; throw 1 NC. Footprint, orientation and inrush pending. |
| Holder | TBD, mechanical helper owns | 1 | Actual protected-cell envelope, contact current, insertion polarity/reversal handling and footprint unverified. No invented pad numbers. |
| Branch fault protection | TBD after coordination | TBD | PCM trip data and holder/wiring/diode limits required; operating current rating is not a fault limiter. |
| External charger | Keeppower **L1**, off-board | 1 | Exact review target at **500 mA only**, Micro-USB 5 V/1 A supply. Complete compatibility still pending as detailed in handoff; not carrier BOM. |

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
