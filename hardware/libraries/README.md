# Mechanical footprint candidates

`MakeMusic.pretty/Samtec_SSQ-120-01-G-S_1x20_P2.54mm.kicad_mod` is a new project-local candidate for a single female socket, not a Pico solder-down module. Geometry and sources are in `../mechanical/README.md`. No third-party models are bundled. No touch, buzzer, or battery footprint is assigned.

At integration, add `MakeMusic` to the main project's footprint library table with URI `${KIPRJMOD}/../libraries/MakeMusic.pretty` if the project remains in `hardware/kicad/`. This PR deliberately does not change that project's table. Use two socket symbols/footprints with explicit physical-pin mapping; socket pad 1 is not automatically Pico pin 1 on both rows. Do not substitute a castellated/SMD Pico footprint for a removable socket assembly.

The KiCad 10 installed generic `Connector_PinSocket_2.54mm:PinSocket_1x20_P2.54mm_Vertical` was inspected: 20 pads at 2.54 mm pitch, 1.00 mm drill, 1.70 mm pads, approximately 2.54 x 50.8 mm body. The local candidate follows the exact Samtec recommended 1.02 mm hole / 1.52 mm copper diameter and 2.41 x 51.31 mm nominal housing instead. Courtyard is an engineering allowance, not a manufacturer dimension. Validate finished-hole tolerance and annular ring with the fabricator before release.
