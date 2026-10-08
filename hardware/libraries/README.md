# Mechanical footprint candidates

`MakeMusic.pretty/Samtec_SSQ-120-01-G-S_1x20_P2.54mm.kicad_mod` is a new project-local candidate for a single female socket, not a Pico solder-down module. Geometry and sources are in `../mechanical/README.md`. No third-party models are bundled. This PR supplies a battery holder library candidate only; it makes no new main-schematic assignment.

The merged schematic project registers `MakeMusic` in `hardware/kicad/fp-lib-table` with URI `${KIPRJMOD}/../libraries/MakeMusic.pretty` and assigns the candidate to J1/J2. This follow-up does not change that table or the schematic. Use two socket symbols/footprints with explicit physical-pin mapping; follow the merged schematic map: J1 local n = Pico physical n; J2 local n = Pico physical n+20. Place J1 at (111.11,1.30) rotation 0 degrees; place J2 at (128.89,49.56) rotation 180 degrees. J1 pad 1 and J2 pad 20 face USB; J2 square pad 1 faces away from USB. See `../mechanical/socket-placement.csv` for all 40 candidate pad positions. Do not substitute a castellated/SMD Pico footprint for a removable socket assembly.

The KiCad 10 installed generic `Connector_PinSocket_2.54mm:PinSocket_1x20_P2.54mm_Vertical` was inspected: 20 pads at 2.54 mm pitch, 1.00 mm drill, 1.70 mm pads, approximately 2.54 x 50.8 mm body. The local candidate follows the exact Samtec recommended 1.02 mm hole / 1.52 mm copper diameter and 2.41 x 51.31 mm nominal housing instead. Courtyard is an engineering allowance, not a manufacturer dimension. Validate finished-hole tolerance and annular ring with the fabricator before release.


## Polarized 18350 holder candidate

`MakeMusic.pretty/BatteryHolder_Keystone_1095P_1x18350_THT_Candidate.kicad_mod` follows Keystone's individual 1095P drawing revision A. Pad 1 is positive (right in source component view), pad 2 negative (left); two blank-number 3.45 mm NPTHs are plastic locating bosses. End electrical holes are **2.39 mm positive and 1.19 mm negative**. The nonpolar 1095 needs a different negative hole, so do not silently substitute it. See [holder evidence and assembly contract](../mechanical/HOLDER_1095P.md) for coordinates, drawing/mirror provenance, engineering land/courtyard choices and bottom-side flip review.

Geometry/polarity are documented; **39.3 x 18.7 mm protected-cell fit is not established**. The candidate is not added to the main schematic, BOM or PCB. Use KiCad Flip for underside placement, review both views and pad 1 → `BAT_PROT_PLUS` and pad 2 → `GND` mapping from the power handoff, and measure selected cell/button/spring travel before assigning or manufacturing. No module-specific ST0238 footprint is provided from its 32 x 14 mm outline alone.
