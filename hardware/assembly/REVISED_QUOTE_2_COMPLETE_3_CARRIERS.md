# Revised quote: two complete instruments and three populated carriers

October 15, 2026. **NONBINDING QUOTE ONLY. DO NOT FABRICATE OR PURCHASE.**

This request supersedes the earlier five-complete-instrument quantity for this
inquiry. There are **five carrier boards total**, not seven:

- Two fully completed playable instruments, with all sourcing, soldering,
  crimps, mounting, programming and testing done by the factory.
- Three additional populated carrier boards, with all 47 carrier components
  supplied and soldered, including female Pico sockets, headers and switch.
  These three do not include Picos, external modules, batteries, harnesses or
  custom mounting structures. Provide carrier electrical/assembly inspection.

The existing grouped carrier BOM and Gerbers remain unchanged. The reported
$326.65 quotation covers the five populated carriers ($199.85 components,
$29 assembly, $97.80 PCBs). Please retain that as the base and separately
quote the additional parts and work needed to finish **two** instruments.
The new mixed-delivery total has not been quoted or accepted. No optional
sixth bare keepsake is included in this revised quantity.

## Additional sourcing and assembly for two instruments

| Item | Per complete instrument | Total for the two | Requirement |
|---|---:|---:|---|
| Raspberry Pi Pico H | 1 | 2 | Original RP2040 Pico H SC0917, removable in existing sockets |
| Generic TTP223 touch modules | 10 | 20 | 3.3 V operation, direct/momentary output, eight notes plus two modifiers; report delivered revision/logic/pin order |
| Generic passive buzzer modules | 2 | 4 | 3.3 V, transistor-driven, low-level trigger, variable pitch from PWM; not fixed-tone active buzzers |
| Adapted three-wire module harnesses | 12 | 24 | Exact module-end terminations; carrier end as below; dressed length after fit |
| Carrier-end Harwin M20-1060300 housings | 12 | 24 | Included in the 24 harnesses, not extra completed harnesses |
| Harwin M20-1180046 contacts | 36 | 72 | Three per carrier-end housing; qualified AWG26 crimps |
| Protected removable long 18650 cell | 1 | 2 | P1835J reference; ordinary opposite-end terminals; exact cell/holder/charger qualification held |
| MPD BH-18650-W wired holder | 1 | 2 | Protected-cell fit/contact capability; included factory AWG24 leads |
| JST PHR-2 battery plug housing | 1 | 2 | Carrier H1 mate, crimp onto holder leads; do not duplicate H1 already in carrier BOM |
| JST SPH-002T-P0.5S contacts | 2 | 4 | Qualify exact holder lead insulation OD and crimp; continuity/polarity inspection |
| Module fixture, insulating cassette, retainers, feet and fasteners | 1 complete set | 2 sets | Factory measured and toleranced design, manufacture and installation |
| Shared external charger, required cable and input supply | Shared | 1 set proposed | Itemize separately; exact cell/charger pairing must be accepted before use |

Generic touch and passive buzzer modules are authorized as price/engineering
candidates. The linked retail examples are not an instruction to buy from
those retailers. Please quote equivalent locally sourced modules and return
their exact links/photos, dimensions, pin order, operating current and sample
test results. Carrier component substitutions are not authorized by this
generic external-module request.

The budget touch example is **15 x 11 mm**, compared with the original
24 x 24 mm proposal. The generic buzzer example is **32 x 13 mm**, compared
with ST0238's 32 x 14 mm reference. Existing drawings are nominal interfaces,
not final machining drawings. Adapt the fixture to actual measured parts,
retain the note positions/comfortable touch access, and confirm usable touch
area before final drawings are approved. Do not assume matching mounting
holes, pin order, support lands or electrical behavior.

Carrier module connectors remain 1 signal / 2 regulated 3V3 / 3 ground.
Harnesses must adapt to each delivered module's labels. Do not feed raw cell
voltage into module power pins. Preserve access to exposed GPIO and Pico
USB/BOOTSEL and removal. All final wiring and mounting are factory work.

## Retail price references, not a PCBWay quote

USD listings checked October 15, 2026. Excludes shipping, tax, tariffs,
procurement charges, scrap, engineering and labor. Stock/prices may change.

| Reference item | Purchase quantity | Listed unit/pack price | Extended reference cost |
|---|---:|---:|---:|
| [ICStation TTP223 item 12675, 10-pack](https://www.icstation.com/10pcs-ttp223-capacitive-touch-switch-touching-button-switch-module-self-lockingno-locking-module-arduino-p-12675.html) | 2 packs / 20 modules | $2.79 per pack | $5.58 |
| [Generic low-level passive buzzer](https://easyelecmodule.com/product/passive-buzzer-module-low-level-trigger/) | 4 | $0.99 | $3.96 |
| [Pico H with headers](https://www.pishop.us/product/raspberry-pi-pico-h-pre-soldered-headers/) | 2 | $5.00 | $10.00 |
| [Keeppower P1835J protected cell](https://illumn.com/18650-keeppower-3500mah-sanyo-ncr18650ga-protected-button-top.html) | 2 | $9.99 | $19.98 |
| [MPD BH-18650-W](https://www.digikey.com/en/products/detail/mpd-memory-protection-devices/BH-18650-W/3029217) | 2 | $3.64 | $7.28 |
| **Main add-on electronics subtotal** | | | **$46.80** |
| [Harwin M20-1060300](https://www.digikey.com/en/products/detail/harwin-inc/M20-1060300/3728192) | 24 | $0.124 at 10+ | $2.98 rounded |
| [Harwin M20-1180046](https://www.digikey.com/en/products/detail/harwin-inc/M20-1180046/3728125) | 72 | $0.1038 at 50+ | $7.47 rounded |
| **Subtotal including bare carrier-end harness connectors** | | | **$57.25 rounded** |

The ICStation price is the indexed advertised sale price; direct page retrieval
failed during this check, so confirm the two-pack checkout price. Its indexed
regular price is $3.99/pack; at that price the main electronics subtotal would
be $49.20 instead. The original [ST0238 reference](https://www.sunfounder.com/products/3-3-5v-passive-low-level-trigger-buzzer-alarm-sound-module)
lists $5.99 each; using four of those instead of the generic $0.99 modules
adds $20 to either main subtotal.

The [Keeppower L1 charger reference](https://illumn.com/chargers/keeppower-l1-li-ion-single-bay-usb-charger.html)
is $14.99 including a micro-USB cable, **budget reference only, pairing held**.
Its listed 4.2 V +/-1% output permits 4.242 V; compatibility with the delivered
cell's allowed charging limits has not been established. Do not treat its
availability or 500 mA setting as qualification. Please propose and document
a compatible cell/charger pair and itemize any needed input supply.

$326.65 base + $46.80 main electronics = **$373.45 partial subtotal**.
With the bare carrier-end connectors it is **$383.90 rounded**. Neither figure
is the finished mixed-order price: wire, module-end terminations, battery plug
parts, crimps, all mounting materials, fasteners, charger/input supply,
engineering/metrology, programming, tests, shipping and tax remain unpriced.

## Required supplier response

1. Confirm all five carriers include all 30 SMD and 17 thru-hole parts each,
   including the bottom H1 connector. Confirm the $326.65 base remains valid.
2. Itemize the added sourcing and work for **two complete instruments only**.
   Mark unavailable services and provisional costs explicitly. Confirm whether
   your assembly and mechanical teams can own the complete build.
3. Quote actual-part metrology, adapted harness manufacture, final toleranced
   mechanical CAD/fixtures/cassette/feet and installation. Existing nominal
   SVG/DXF drawings are not machining release. Return drawings for review.
4. Confirm carrier assembly process/orientation acceptance and the existing
   power, clearance and cell/charger qualification requirements in the original
   packet. No physical-fit or hardware-test gate is discharged by this request.
5. After separate owner production release, qualify **one of the two complete
   instruments first**, then finish the second after acceptance. Provide test
   records for both complete instruments and carrier inspection records for
   the other three. Do not charge a sixth carrier as the first article.
6. Provide the revised total, lead time, quote validity, shipping/tax and any
   restrictions/costs for battery shipment. If batteries cannot ship with the
   instruments, quote them separately and explain the remaining user steps.

Provisional firmware remains `Pico_Synth/carrier_prototype.py`; actual touch
polarity may be adapted in firmware after testing. Looping, screen, keypad,
speaker and percussion expansions are not additions to this first build.

The original packet's fit/harness/process/power procedures remain technical
references. All statements requiring five complete instruments are superseded
by this two-complete/three-populated delivery split. Final mechanical CAD,
qualified cell/charger pair, process acceptance and first-article hardware
evidence remain outstanding. No order or production release is authorized.
