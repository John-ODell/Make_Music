# Editable Pico instrument carrier

Open `make_music.kicad_pro` in KiCad 10, then open the schematic. The project-local `MakeMusic.kicad_sym` library and `sym-lib-table` resolve all symbols without a third-party library installation. `fp-lib-table` registers the merged `../libraries/MakeMusic.pretty` socket library as `MakeMusic`. The schematic is the editable source of truth; do not regenerate it from the review PDF.

- `make_music.kicad_sch`: one A3 sheet, two removable female sockets, ten touch interfaces, two buzzer interfaces, one expansion header, and the revision-1 battery switch/diode circuit.
- `make_music.kicad_pcb`: initial placement draft with two socket footprints, schematic net assignments, proposed outline and non-fabrication reference body drawings. No tracks or remaining component footprints yet; see [PCB status](PCB_STATUS.md).
- `schematic-review.pdf`: readable schematic export, marked provisional.
- `pico-socket-map.csv`: all 40 Pico physical pins mapped to local socket pins and carrier nets.
- `verify_connectivity.py`: checks every endpoint in a fresh XML netlist against the reviewed interface contract.
- `../reviews/schematic.md`: verified facts, actual checks and unresolved design decisions.

J1 and J2 each use local pad numbers 1-20. J1 pin 1 is at the USB end; J2 pin 1 is at the opposite end. J2 pin 20 is beside USB. J1/J2 are assigned `MakeMusic:Samtec_SSQ-120-01-G-S_1x20_P2.54mm` as candidates. Place J1 pad 1 at USB and rotate J2 180 degrees relative to J1 so J2 pad 20 is at USB. This integration numbering supersedes the mechanical proposal's alternative right-row pad-1-at-USB convention; do not reverse the existing schematic nets to match that proposal.

J3-J14 pin order is an assumption, visibly labeled: 1=signal, 2=3V3_OUT, 3=GND. Do not assemble against this order until actual modules are identified. J15 expansion order is provisional. Only J1/J2 have assigned footprints; J3-J15 and H1/S1/D1/TP1 remain unset. Socket geometry is verified against the Samtec drawing, but selected Pico/male-header engagement, finished-hole tolerances and physical clearances still need validation. The retired X1 handoff is replaced by H1 holder contacts, S1 MN12SS1W03 switch, D1 SS14-E3/61T isolation diode and TP1 USB-VBUS test access. H1 uses provisional logical `+`/`-` identifiers, not verified mechanical pad numbers; reconcile them with the actual holder before assigning a footprint. The inserted Pico and module electronics are off-board and not modeled.

Run from this directory (write generated logs/netlists outside the repository):

```sh
kicad-cli sch erc --severity-all --exit-code-violations --format json -o /tmp/make-music-erc.json make_music.kicad_sch
kicad-cli sch export netlist --format kicadxml -o /tmp/make-music-netlist.xml make_music.kicad_sch
python3 verify_connectivity.py /tmp/make-music-netlist.xml
kicad-cli sch export pdf -o schematic-review.pdf make_music.kicad_sch
```

The user permits firmware adaptation to confirmed touch polarity, including active-low. Confirm direct/momentary configuration and actual idle/touched levels first; no firmware changes are made by this follow-up.

Revision-1 source path: protected-cell external + -> H1 `+` -> BAT_PROT_PLUS -> S1 common 2; S1 throw 3 -> BAT_SW_PLUS -> D1 anode 2; D1 cathode/band 1 -> VSYS/Pico physical 39. S1 throw 1 is NC (battery OFF). H1 `-` joins GND. TP1 only joins USB VBUS/Pico physical 40, with no carrier bridge to the battery, VSYS or 3V3_OUT. The Pico's internal diode/regulator remain off-board.

Battery OFF does not stop USB power. Remove the cell for external charging; no onboard charger is present. Protected-cell PCM thresholds, branch fuse/current limit, reverse-insertion handling, holder polarity/fit and power/load/thermal validation remain unresolved. P1835C2 cell and L1 at 500 mA are review targets from the power handoff, not approved fit/purchase selections. The selected pair of SunFounder ST0238 modules retains provisional connector numbering; HIGH idle/startup handling and module current still need review.

This is meaningful circuit progress, not a manufacturing release. Complete fault protection, actual component/footprint/polarity checks and load/thermal validation before routing or assembly approval.
