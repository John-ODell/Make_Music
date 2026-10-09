# Current power candidate BOM — protected 18650

Updated **2026-10-09** for **five fully assembled instruments** and an optional sixth bare carrier keepsake. The user's corrected long **18650** selection supersedes P1835C2/18350 and Keystone 1101. This is a candidate specification, not purchase or manufacturing approval. Exact lot, terminal form, holder fit and charger compatibility remain held in [18650-handoff.md](18650-handoff.md).

The active carrier protection BOM/pins are in [branch-protection.md](branch-protection.md) and [branch-endpoints.csv](branch-endpoints.csv): F1 **3403.0275.23**, S1 **MN12SS1W03**, U2 **TPS259474LRPWR**, six exact resistors, four ceramic capacitors, shunt D2 **SS14-E3/61T** and bidirectional D3 **SMAJ5.0CA**. Native references are power R3–R8/C13–C16; original R1/R2 and C1–C12 serve buzzer bias/header bypass. Carrier series D1 is removed. PM owns the final exported purchased-part BOM after ongoing CAD integration.

| Item | Exact candidate / specification | Per instrument | Five assembled units | Status |
|---|---|---:|---:|---|
| Protected conventional 18650 cell | **Keeppower P1835J**, standard opposite-end-terminal product, [manufacturer page id510](https://www.keeppower.com.cn/products_detail.php?id=510) | 1 | 5 | Confirm delivered terminal configuration, current-lot ratings and fit; 18.8×69.3 mm tolerance envelope before clearance |
| External charger | **Keeppower L1** evaluation target; initially 500 mA qualification setting | Shared accessory | PM to specify distribution | **Compatibility HOLD**: 4.242 V upper charger tolerance versus unqualified 4.20 V cell maximum; no approved pair |
| Charger input supply/cable | Delivered L1 revision needs suitable 5 V/1 A supply and matching USB cable | Per accepted charger | TBD with charger quantity | Supply SKU/revision remains unselected; do not omit from quote |
| Wired holder and insulating cassette | Protected-18650-compatible, exact holder selected by mechanical helper | 1 | 5 | Longer cassette/contact travel/removal/ampacity/CAD required; old 1101 and anonymous flat-top holder are not frozen |
| Carrier battery header H1 | **JST B2B-PH-K-S(LF)(SN)**, circuit1 positive/circuit2 GND | 1 | 5 | Existing carrier interface; underside THT orientation and actual harness continuity must pass |
| Factory harness | **JST PHR-2** housing + two **SPH-002T-P0.5S** contacts, AWG24; lengths set by new cassette | 1 housing, 2 contacts | 5 housings, 10 contacts | Crimp/solder/insulation/strain relief/polarity qualification; holder ampacity is separate |
| Added buzzer supply bulk | PM-directed native **C17/C18**, each **TDK C2012X7R1A106K125AC**, 10 µF/10 V/X7R/0805 on 3V3_OUT | 2 | 10 | CAD/BOM/export and effective capacitance/startup/transients pending; retain existing 100 nF |

The optional sixth bare PCB gets no populated-component, cell or harness allocation. Include all small SMT parts, all THT sockets/headers/switch/H1, harness/module installation and accepted mechanical work for each of the five complete instruments. Confirm how accepted cells/chargers are supplied and fitted; no supplier exclusion should silently become user soldering. Fit/process and unit acceptance remain required. Main instrument procurement CSV is PM-owned and must be reconciled to the new cell/holder before quoting.

**No change to carrier load/protection limits:** ≤0.70 A battery input; ≤350 mA total and ≤250 mA external 3V3; ≤100 µF total VSYS. Higher cell capacity does not increase these limits. BQ24074, NTC and dedicated charging-input parts are omitted from revision 1. A real cell is fitted only after [the bring-up gate](prototype-validation.md) and cell/charger qualification pass.

## Primary evidence and history

- [Current 18650 handoff](18650-handoff.md) links the standard/global P1835J pages, explicitly dated current-rating catalogue and L1 manufacturer documents, with unresolved voltage/termination/lot/terminal evidence.
- [TI TPS25947](https://www.ti.com/lit/ds/symlink/tps25947.pdf), [SCHURTER UMT-H](https://www.schurter.com/en/datasheet/typ_UMT-H.pdf), [NKK MN12SS1W03 drawing](https://www.nkkswitches.com/pdf/MN_ToggleSections_DP.pdf), [Vishay SS14](https://www.vishay.com/docs/88746/ss12.pdf) and [TDK added 10 µF part](https://product.tdk.com/en/search/capacitor/ceramic/mlcc/info?part_no=C2012X7R1A106K125AC) support carrier component choices; their mechanical/electrical limits are not measured assembly results.
- [Superseded 18350 handoff](rev1-handoff.md), [historical budget comparison](candidate-comparison.md) and [dated PCBWay audit](pcbway-readiness.md) retain the earlier research/checkpoint. Those sources do not qualify the new 18650 assembly or charger.
