# Rear socket edge — bounded correction for PR28

Reviewed 2026-10-09 against root commit `806457b`, its exported live IPC pad/inventory evidence, the project socket placement CSV and primary mechanical drawings. This review supersedes the earlier recommendation to retain the rear plastic overhang in BUILD_READINESS.md. No native CAD was read through a source parser, mutated or opened by this helper; root remains the CAD owner. No actual Pico, socket or cable was measured.

## Recommendation before root changes the outline

**Extend only the rear/top edge from native y20 to y18.5.** Keep left x20, right x350 and front y140: the resulting carrier is **330 x 121.5 mm**. Update the two adjoining outline segments to meet the new rear edge. Leave every footprint, hole, trace, fixture and service datum fixed; do not translate the board contents or redefine the mechanical datum.

The existing mechanical drawings retain their **legacy** datum native (20,20), so the new rear edge is legacy mechanical **y=-1.5** and the front remains y120. If root adopts the new outline's top-left as a new local origin, its native offset changes to **(+20,+18.5) only for that newly adopted y18.5 outline**; every old local y becomes `y_new = y_legacy + 1.5`, with all native placements unchanged. Do not combine old local coordinates with the new offset. The paper SVG uses viewBox `0 -1.5 330 121.5` so it shows the enlarged outline without moving any drawn component. See [datum table](DATUMS.md). In root's x-right/y-up manufacturing frame the rectangle becomes (20,-18.5)..(350,-140).

| Feature | Existing y20 edge | Proposed y18.5 edge |
|---|---:|---:|
| Native socket courtyard rear y19.27 | 0.73 outside | **0.77 inside** |
| Nominal housing rear y19.775 | 0.225 outside | **1.275 inside** |
| Rear body allowance using full 0.25 mm length tolerance | 0.475 outside | **1.025 inside**, before other tolerances/flash |
| Nearest socket pad centre y21.30 | 1.30 inside | **2.80 inside** |
| Copper edge, diameter/side 1.52 | 0.54 inside | **2.04 inside** |
| Finished-hole edge, diameter 1.02 | 0.79 inside | **2.29 inside** |
| Nominal annular ring | 0.25 | **0.25**, unaffected |

Samtec's [SSQ drawing revision BH](https://suddendocs.samtec.com/prints/ssq-1xx-xx-xxx-x-xx-xxx-xx-x-mkt.pdf), sheet 1, gives housing length `20*2.54+0.51 = 51.31`, tolerance +/-0.25, width 2.41 reference and height 8.51 reference. [Recommended layout revision A](https://suddendocs.samtec.com/prints/ssq-1xx-xx-xx-x-xx-xxx-xx-xx.pdf), sheet 1, gives 2.54 pitch, 1.02 holes and 1.52 lands. The 48.26 first-to-last span leaves nominal 1.525 at each body end; y21.30-1.525 = y19.775. The 0.5 service allowance, rounded outward, gives the existing courtyard y19.27. Root's exported IPC evidence confirms J1/J2 anchors (131.11,21.30)/(148.89,69.56), rotations 0/180, 20 pads each and the 1.52/1.02 geometry. The root placement scorer reports the courtyard boundary; that boundary is not included in the exported pad inventory itself.

This resolves the **nominal published geometry and reported courtyard/outline defect** without moving a routed 40-pin assembly. Root first applied y19 with every placement unchanged and no hard placement-score failure; fresh DRC then found the existing J1 pin1 F.SilkS marker at native y18.9 with 0.040 clearance versus 0.100 required. This PM-reported finding prompted the additional 0.5 mm extension to y18.5. Expected nominal marker clearance is 0.34; root must verify it with fresh all-severity DRC. The helper has not independently read that new DRC/export. No other outline or placement correction is justified by the reviewed geometry. The changed footprint support is preferable to relying on an intentional lip overhang for repeated unplugging. It does not certify finished-part tolerances or insertion strength.

## USB, BOOTSEL, GPIO and removal

The selected original Pico H remains fixed: PCB native x129.5..150.5/y20..71, rows 17.78 apart. Official original [Pico datasheet](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf), release 21, mechanical Figure 3, printed page 6, gives 21 x 51 PCB and 48.26 pin span. It describes the micro-USB port as overhanging the Pico's rear edge, but does **not** dimension the complete chosen cable boot or Pico H male-header stack. Do not infer an exact USB shell projection by scaling the picture.

The added strip lies below the raised Pico and extends only 1.5 mm rearward from its PCB datum. The Samtec housing top is nominal 8.51 above the carrier; the male insulator/mating gap adds to Pico height. Therefore the strip introduces no published PCB/socket interference and does not cover the top-side BOOTSEL button. Leave the full USB approach open above the carrier: mechanical x102..138/y-25..0 is an engineering cable reservation, including the new strip at y-1.5..0. A vertical enclosure wall or panel rail in that area requires its own aperture/clearance; the carrier extension does not approve that wall.

Retain provisional BOOTSEL access mechanical x110.5..122.5/y8..20, open lid, at least 5 mm side access beyond the Pico and unrestricted upward removal. The upper fixture remains outside mechanical x104.5..135.5/y<=56; its boundary at y56 is a service allowance, not a guaranteed hand gap. J15 access remains x45..58/y8..55.1. No left modifier, note, buzzer, GPIO, fixture mount, cassette mount or H1 move is needed for this correction.

Exact cable-boot depth, male engagement, seated stack, two-row alignment and removal force remain assembler acceptance checks. Measure lowest plug/boot/strain-relief surface relative to the added strip; require the agreed installed clearance. This is a cable/stack qualification, not an unresolved nominal reason to keep the overhang.

## Tolerance and factory process limits

Samtec also allows 0.25 maximum cut flash and specifies end-wall/lead conditions. The full body-length tolerance, flash, body-to-tail registration and assembly displacement are not a proved independent statistical stack. Do not claim the 1.275 support margin or 0.77 courtyard margin is a guaranteed worst-case finished clearance. For sensitivity, 1.275 minus full 0.25 body allowance, a separate conservative 0.25 flash allowance, 0.20 CNC edge allowance and 0.075 hole-position allowance reaches **0.500**. These deliberately conservative allowances demonstrate why actual process acceptance still matters; they are not a manufacturer-approved tolerance model.

[PCBWay capabilities](https://www.pcbway.com/capabilities.html) publish +/-0.2 outline tolerance for CNC routing, +/-0.5 for V-scoring, a normal hole-position entry +/-0.075, and normal 35 micrometre component annular ring >=10 mil (0.254). Prefer a reviewed CNC/depanel process for this edge. The unchanged 0.25 ring is 0.004 below that normal-process entry: root may obtain explicit process acceptance or revise lands through Konnect and rerun checks. This is independent of extending the outline.

[PCBWay assembly FAQ Q14](https://www.pcbway.com/assembly-faq.html) still calls for rails on the two long parallel edges when copper is less than 3.5 from the edge. New 2.04 socket copper clearance does not remove this process requirement. Accept rail/THT/depanel order and clean socket seating; installing sockets after depaneling is one candidate sequence for factory review. No supplier was contacted.

Root should save/read back the complete closed outline, refill, rerun all-severity DRC and placement scoring, verify every placement/166 pads remains unchanged, and regenerate source-bound review/manufacturing geometry. This helper's recommendation does not claim those future checks ran. Four root metadata warnings at 806457b remain separately visible.

## Evidence identity

The reviewed root `hardware/review/integration-20261009/live-board.json` is Git blob `7808764ba8c9f9f82d73b9323882b542596d650b`, SHA256 `48350c435dee54951c04063ba63164f75ed66b9ad09ae6cfe11b92c7a1e56d7a`. This is a held IPC export from root's checkpoint, not a new helper live readback. The user-supplied original Pico release 21 PDF was rendered at printed page 6 and visually reviewed; it remains outside the repository at `/Users/johnodell/Desktop/pico_datasheets/RP-008307-DS-2-pico-datasheet.pdf`. Samtec BH/layout A and MPD holder G were rechecked against primary sources on 2026-10-09.
