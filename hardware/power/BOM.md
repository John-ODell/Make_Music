# Candidate BOM — no purchasing or assembly release

Exact core part candidates below are electrically researched. Unselected interfaces and footprints remain explicitly TBD.

| Ref / option | Manufacturer / exact MPN | Quantity | Evidence and limits |
|---|---|---:|---|
| B1 / A or B | Keeppower **P1835C2** | 1 | Protected 18350, conventional 4.2 V maximum charge. Manufacturer advertises overcharge/overdischarge/overcurrent/short protection. Candidate only; actual lot/specification and holder still required. |
| D_EXT / A or B | Vishay **SS14-E3/61T** | 1 | SMA/DO-214AC Schottky, 40 V, 1 A with stated thermal conditions; cathode band toward VSYS. Reverse leakage is finite. |
| S1 / A or B | C&K **JS102011SAQN** | 1 | SPDT right-angle gullwing slide, non-shorting, silver contacts; 0.3 A at 6 VDC. Conditional on measured switched input/inrush current, not 3V3 output current. Higher-current substitute may be necessary. |
| U1 / B only | Texas Instruments **BQ24074RGTR** | 1 | 16-pin 3×3 mm VQFN RGT with exposed pad, 4.2 V single-cell charger with separate BAT/OUT power path; default disable until cell selected. Do not substitute BQ24075/79 without re-review. |
| NTC / B only | Semitec **103AT-2** | 1 | TI application example calls out this 10 kΩ NTC. Thermal coupling and allowed cell charge-temperature thresholds unresolved. Mechanical mounting not assigned. |
| IN/BAT/OUT capacitors / B | TBD MPNs | 3 | Candidate 1 µF IN and 10 µF each BAT/OUT; effective capacitance and voltage rating to be verified. |
| CE pull-up / B | TBD 100 kΩ MPN | 1 | OUT to CE; high disables charging. |
| ISET / ILIM / B | TBD resistor MPNs and values | 2 | ISET initially DNP; ILIM required before charging. Values depend on actual battery/source limits. |
| J_BAT / A or B | TBD holder or keyed pack connector | 1 | Protected-cell envelope, contact current, insertion polarity, pin order and footprint not selected. A keyed connector does not establish polarity without checking the actual pack. |
| J_CHARGE / B | TBD dedicated USB connector and ESD parts | 1 set | Dedicated input; never bridge to Pico VBUS. USB-C CC/current policy or micro-B source policy must be specified. |
| External charger / A | TBD compatible 4.2 V single-cell charger | 1, off-board | Must accept actual protected 18350 length and provide cell-matched CC/CV, temperature and recovery behavior. Not a carrier BOM component. |

## Primary evidence

- [Vishay SS12–SS16 datasheet, document 88746](https://www.vishay.com/docs/88746/ss12.pdf): ratings, polarity band, SMA package and E3/61T ordering scheme. [SS14 product page](https://www.vishay.com/en/product/88746/) is the family entry point. Verify final landing pattern against its mechanical drawing.
- [C&K JS datasheet](https://www.ckswitches.com/media/1422/js.pdf), revised 2026-01-14: rating and JS102011SAQN drawing on page 4. No switch footprint has been assigned.
- [TI BQ24074 datasheet](https://www.ti.com/lit/ds/symlink/bq24074.pdf), SLUS810N, October 2021: pin mapping, RGT package, charger programming and thermal/layout requirements. NTC identification is from TI's application example; cell-temperature compatibility remains unverified.
- [Semitec AT thermistor datasheet](https://www.semitec-global.com/uploads/2022/01/P12-13-AT-Thermistor.pdf): 103AT-2 is 10 kΩ at 25°C, with the AT-2 mechanical form; thermal mounting and cell limits still need review.
- [Keeppower China P1835C2](https://www.keeppower.com.cn/products_detail.php?id=566) and [Keeppower P1835C2](https://www.keeppower.com/product/keeppower-18350-1200mah-protected-li-ion-rechargeable-battery-p1835c2/): candidate properties checked on review date. Both list standard charge 220 mA and maximum 1.1 A, but these do not set our charger current. Obtain a lot-specific specification before use.

## Battery evidence conflict

The two manufacturer pages disagree on length: **39.1 ±0.2 mm** versus **38.5 ±0.2 mm**, both at diameter 18.5 ±0.2 mm. For mechanical investigation reserve at least the larger published envelope (39.3 mm length, 18.7 mm diameter), then add holder-contact travel and assembly clearance based on the actual holder. This is not a released holder dimension. A holder sized for an unprotected 35 mm-long cell may fail to fit this candidate.

The pages advertise 1200 mAh nominal but describe 1150 mAh typical and 1100 mAh minimum. Do not promise runtime from the headline capacity. Protection's published 2.5 V endpoint is not our desired normal-use shutdown threshold. Published protection features do not establish charge-temperature monitoring; B needs the reviewed NTC implementation.

If a pouch is preferred, select a documented protected 1S 4.2 V pack with its own exact MPN, connector polarity, capacity, charge rate, protection/recovery and mechanical constraints. No bare pouch cell substitution is authorized by this BOM. Board-level protection is not designed here because A/B deliberately require protected cells; a bare-cell choice triggers a separate protection circuit review.
