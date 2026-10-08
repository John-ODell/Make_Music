# Power candidate and budget comparison

Observed 2026-10-07 (America/Chicago). **Battery/charging choice remains open.** These are published USD retail listing prices, not a factory quotation or purchasing recommendation. Prices/stock can change; taxes, shipping, tariffs, power supplies, cables, carrier parts, assembly and enclosure are excluded unless stated. No parts were ordered, supplier contacted, charger instantiated or battery footprint assigned.

## Comparable protected battery candidates

| Candidate | Published electrical evidence | Mechanical / integration implications |
|---|---|---|
| Removable 18350: Keeppower **P1835C2** | Manufacturer identifies conventional 4.2 V charging and built-in overcharge, overdischarge, overcurrent and short protection. 1200 mAh headline; 1100 mAh minimum/1150 typical; standard charge 220 mA, maximum 1.1 A. | Requires a verified protected-cell holder and accessible nonconductive battery retention/door. Manufacturer lengths disagree: 38.5 versus 39.1 mm ±0.2. Use the larger 39.3 mm tolerance envelope for investigation; physical fit remains unverified. |
| Flat protected pack: Adafruit **SKU 258**, supplier-linked PKCELL **LP-503562 3.7 V 1200 mAh with PCM** | Seller documents voltage/short protection, 4.2 V charge, 3.0 V cutoff and **500 mA maximum charging**; linked cell PDF gives 1140 mAh minimum, 1.2 A maximum continuous discharge and 0–45°C charge range. | Seller body dimensions 34×62×5 mm are a candidate envelope, not a footprint. Two-pin JST-PH-style lead, no built-in thermistor; verify actual polarity, pack lot, lead exit, strain relief and insulated restraint. Do not solder/puncture/compress the pouch. |

The two nominal capacities make these a more useful comparison than mixing a 1200 mAh cylinder and a 2000 mAh pouch, but equal nominal capacity does not guarantee equal runtime. Use the selected pack's discharge curve and measured instrument current.

Primary battery evidence: [Keeppower China](https://www.keeppower.com.cn/products_detail.php?id=566), [Keeppower alternate page](https://www.keeppower.com/product/keeppower-18350-1200mah-protected-li-ion-rechargeable-battery-p1835c2/), [Adafruit SKU 258](https://www.adafruit.com/product/258), and its [PKCELL specification](https://cdn-shop.adafruit.com/product-files/258/C101-_Li-Polymer_503562_1200mAh_3.7V_with_PCM_APPROVED_8.18.pdf). SKU 258 is the orderable pack identifier; LP-503562-with-PCM identifies the linked specification, not a guaranteed current lot. The 2014 PDF's quick-charge allowance exceeds the current retail limit: retain the stricter 500 mA until supplier/lot confirmation, with tolerance margin when selecting charger current.

## Published price observations

| Item / role | One-unit USD listing | Observed availability / price context | Price source |
|---|---:|---|---|
| P1835C2 protected button-top cell | **$3.49 sale**, $7.49 regular | In stock on retrieved product page; sale is not a guaranteed long-term BOM price | [Illumn exact cell](https://illumn.com/18350-keeppower-p1835c2-1200mah-protected-button-top.html) |
| XTAR **ANT MC1 Plus**, off-board cylindrical charger | **$3.99 sale**, $6.90 regular | In stock; updated USB-C listing. Wall adapter not priced into this row | [Illumn exact charger](https://illumn.com/chargers/xtar-ant-mc1-plus-li-ion-usb-charger.html) |
| Protected flat pack, Adafruit **258** | **$9.95** | In stock on retrieved product page | [Adafruit exact pack](https://www.adafruit.com/product/258) |
| Adafruit **4755**, BQ24074 power-path breakout | **$14.95** | In stock; prototype module price only, not the cost of an integrated charger circuit | [Adafruit exact module](https://www.adafruit.com/product/4755) |
| NKK **MN12SS1W03**, stronger switch candidate | **$7.42** | US/USD direct product page; distributor indicates stock. Search excerpt showed a different $6.85: use the directly opened $7.42 observation, reconfirm at quote time | [DigiKey exact switch](https://www.digikey.com/en/products/detail/nkk-switches/MN12SS1W03/20839470) |

No cheap unprotected 18350 or undocumented pouch is substituted to lower the comparison. A 2000 mAh Adafruit 2011 pack was also checked ($12.50 listing, out of stock) but is omitted from the matched-capacity arithmetic.

## Known partial subtotals, not finished instrument prices

| Route | Battery + charging accessory/module | With one $7.42 candidate switch | Still excluded |
|---|---:|---:|---|
| A: protected 18350 + external ANT charger | **$7.48** at observed sale prices; **$14.39** at displayed regular prices | **$14.90 sale / $21.81 regular** | Holder, diode, battery retention, carrier PCB/assembly, enclosure, USB source/cable, tax/shipping |
| B prototype benchmark: protected flat pack + 4755 module | **$24.90** | **$32.32** | Charger configuration work, cell-coupled NTC/network, isolation diode, pack connector/restraint, carrier PCB/assembly, mounting and USB source/cable, tax/shipping |

These sums compare purchased battery/charging hardware for a prototype. They **do not establish a $17.42 manufacturing-cost difference** between A and an integrated B circuit. A factory-integrated BQ24074 design replaces the $14.95 breakout with an IC, passives, USB input/ESD, NTC network and assembly work; that cost is still unquoted. A shared external charger is a one-time accessory: for N instruments with one charger, A's observed accessory subtotal is `N × $3.49 + $3.99`, before the common carrier costs. Include one charger per instrument if each user needs independent charging.

## Charging compatibility and source revision checks

The [XTAR current manufacturer page](https://www.xtar.cc/product/xtar-ant-mc1-plus-charger-7.html) specifies automatic 0.5/1 A selection. Its linked [manual](https://www.xtar.cc/companyfile/xtar-mc1-plus-user-manual-10.html?wpdmdl=2360), visually inspected, includes 18350 but describes an older Micro-USB revision. The seller now lists USB-C. Both advertised current settings are below the P1835C2 published 1.1 A maximum, but exceed its 220 mA standard charge rate; use only after confirming the exact purchased revision, actual cell acceptance and cutoff tolerance. Manual revision, pack-temperature policy and real protected-cell fit are not verified. It is a priced off-board candidate, not an approved charger pairing. Do not automatically use zero-volt recovery on a cell of unknown condition.

For B, **Adafruit 4755 is not suitable unchanged for SKU 258**. Its [configuration guide](https://learn.adafruit.com/adafruit-bq24074-universal-usb-dc-solar-charger-breakout/pinouts) starts at a 1 A charge setting, above the pack's 500 mA retail maximum. Choose a lower target with worst-case tolerance margin, add and verify cell-coupled temperature sensing, and review input-current entitlement before use. Its input-current defaults also differ from circuits.md's disabled/default USB100 proposal; a purchased breakout is not an implementation of that proposal merely because both use BQ24074.

The pack PDF allows charge only at 0–45°C. [TI BQ24074](https://www.ti.com/lit/ds/symlink/bq24074.pdf) specifies nominal stock thermistor trip points of 0–50°C for a Vishay Type-2 curve; a generic 10 kΩ thermistor is **not proof of a 0–45°C window**. Derive the NTC network and tolerance limits for the selected pack and verify thermal coupling. The earlier Semitec 103AT-2 remains a candidate component, not a validated temperature-window choice. The charger module needs the same external-diode isolation from the Pico programming USB path as circuit B; two USB inputs and the onboard Pico D1 still require the documented source review.

## Factory assembly comparison

A can put the verified holder, switch and diode on the assembly BOM; the cell and off-board charger remain separately supplied items. Bottom-side holder installation may require through-hole/selective/manual solder and inspection. No holder footprint is released until protected-cell fit and manufacturer hole/polarity drawings are checked.

B can place an integrated charger, connector and passives on the factory BOM once chosen, with thermal-pad solder inspection and charger configuration checks. A purchased breakout adds another module and attachment/connectors; its retail price is a prototype benchmark, not automatically the best factory assembly route. The protected pouch is installed after PCB assembly with a verified connector and insulated mechanical restraint. Cell inclusion, final enclosure installation and lithium-battery shipping must be explicit line items in any quote.

The [PCBWay service description](https://www.pcbway.com/pcb_prototype/Through_Hole_Assembly.html) supports through-hole assembly as a service category. It does not quote acceptance or price for our holder/switch or battery installation. For a real comparison request separate fabrication, SMT, THT/bottom-side assembly, component procurement, charger setup/test, pack/holder installation, enclosure, shipping and accessory costs at the user's desired quantity. No supplier quotation has been fabricated or requested here.

## Higher-current switch candidate

Recommend considering **NKK MN12SS1W03** for the next prototype review. [NKK exact-part page](https://www.nkkswitches.com/wp-content/themes/impress-blank/search/inc/part.php?part_no=MN12SS1W03) and [manufacturer M-series datasheet](https://www.nkkswitches.com/pdf/MN_ToggleSections_DP.pdf) specify SPDT ON–ON, silver power contacts, **4 A at 30 V DC for resistive loads**, straight PC terminals, and a threaded panel bushing. This is the current candidate, rather than the older M2012SS1W03 replacement predecessor. It offers useful margin over the original C&K 0.3 A slide switch. It is larger, panel-supported and requires a checked PC-pin pattern/enclosure alignment; do not substitute its footprint for the slide switch.

For A, use manufacturer terminal **2 (common)** to D_EXT anode, **3** to protected battery positive and **1** unconnected. One ON–ON throw becomes battery ON; the other becomes battery OFF because that throw is open. For B, terminal 3 instead receives charger OUT. Confirm view/keyway orientation against the actual part before assigning pins or labeling ON. Terminal numbers are not marked on the switch. This single pole does not turn off Pico when USB is plugged in; use a separately reviewed enable switch/pole if that behavior is wanted.

Provisional conservative **switch sizing assumption**, not measured consumption: 100 mA internal Pico allowance + 250 mA external 3V3 allowance = 350 mA total. At assumed 75% regulator efficiency and 0.5 V isolation drop, estimated input is `3.3 × 0.350 / (0.75 × (3.0 - 0.5)) = 0.616 A`; at 2.5 V cell and the same drop it is `0.770 A`. Reserve **1 A power-branch current for design review** and measure capacitive inrush/steps. This is not a current limiter, regulator guarantee or cell shutdown policy. The 4 A resistive switch rating has margin for that assumption, but capacitive switching/inrush, diode heating and all other parts still need checks. The existing 1 A SS14 rating must not be interpreted as four-amp capability just because the switch is stronger.

## Verification and PM decisions

Read the user-provided official Pico/Pico 2 PDFs in `/Users/johnodell/Desktop/pico_datasheets`. SHA-256 comparison found them byte-identical to the official PDFs downloaded during PR #5; power pin numbers, VSYS range, onboard D1 and the external 3V3 load recommendation remain consistent. Read primary NKK electrical and switch-function tables; inspected the XTAR manual and linked pack specification. Recomputed subtotals/input-current examples; checked document links and git diff. No physical fit, supplier assembly acceptance, completed current budget, charger test or KiCad ERC/DRC is claimed.

PM still needs battery route, quantity/accessory distribution, exact battery lot, holder/pack restraint, USB charging source policy, charge current/termination/timer/NTC network and off-switch behavior. Firmware changes are allowed per PM, but no firmware change is made here; a low-battery warning/shutdown can be scoped after the cell endpoint and sensing accuracy are agreed. Reported the charger current/temperature mismatches and protected-cell envelope conflict to the PM before any implementation.
