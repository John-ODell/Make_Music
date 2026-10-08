# Editable Pico instrument carrier

Open `make_music.kicad_pro` in KiCad 10, then open the schematic. The project-local `MakeMusic.kicad_sym` library and `sym-lib-table` resolve all symbols. `fp-lib-table` registers the socket and carrier libraries plus installed KiCad 10 `Connector_JST` and `Resistor_SMD` libraries. The schematic is the editable source of truth; do not regenerate it from the review PDF.

- `make_music.kicad_sch`: one A3 sheet, two removable female sockets, ten touch/two buzzer cable headers, expansion, JST battery harness, switch/diode circuit, two reset pull-ups and twelve header bypass capacitors.
- `make_music.kicad_pcb`: initial placement draft with two socket footprints, schematic net assignments, proposed outline and non-fabrication reference body drawings. No tracks or remaining component footprints yet; see [PCB status](PCB_STATUS.md).
- `schematic-review.pdf`: readable schematic export, marked provisional.
- `pico-socket-map.csv`: all 40 Pico physical pins mapped to local socket pins and carrier nets.
- `verify_connectivity.py`: checks every endpoint in a fresh XML netlist against the reviewed interface contract.
- `carrier-interfaces.md`: exact carrier parts, cable mapping, footprint evidence and placement/release gates.
- `../reviews/schematic.md`: verified facts, actual checks and unresolved design decisions.

J1 and J2 each use local pad numbers 1-20. J1 pin 1 is at the USB end; J2 pin 1 is at the opposite end. J2 pin 20 is beside USB. J1/J2 are assigned `MakeMusic:Samtec_SSQ-120-01-G-S_1x20_P2.54mm` as candidates. Place J1 pad 1 at USB and rotate J2 180 degrees relative to J1 so J2 pad 20 is at USB. This integration numbering supersedes the mechanical proposal's alternative right-row pad-1-at-USB convention; do not reverse the existing schematic nets to match that proposal.

J3-J14 carrier order is defined as 1=SIG, 2=3V3_OUT, 3=GND. Assigned Harwin headers are cable adapters; actual module pin order is mapped separately by label, and no module mounting geometry is claimed. J15 now has the exact Harwin 16-way candidate and defined GPIO order. H1 is the PM-approved underside JST PH battery harness, circuit1=BAT_PROT_PLUS/circuit2=GND; it does not put holder contacts or holes on the carrier. All circuit parts except TP1 have assigned candidate footprints. See [carrier interface contract](carrier-interfaces.md) for exact parts, sources, ST0238 cable permutation, reset bias and local bypass placement. The inserted Pico and module electronics remain off-board/unmodeled. The existing PM PCB draft requires a schematic update before layout/DRC; this revision leaves it unchanged.

Run from this directory (write generated logs/netlists outside the repository):

```sh
kicad-cli sch erc --severity-all --exit-code-violations --format json -o /tmp/make-music-erc.json make_music.kicad_sch
kicad-cli sch export netlist --format kicadxml -o /tmp/make-music-netlist.xml make_music.kicad_sch
python3 verify_connectivity.py /tmp/make-music-netlist.xml
kicad-cli sch export pdf -o schematic-review.pdf make_music.kicad_sch
```

The user permits firmware adaptation to confirmed touch polarity, including active-low. Confirm direct/momentary configuration and actual idle/touched levels first; no firmware changes are made by this follow-up.

Revision-1 source path: protected-cell external + -> H1 circuit1 -> BAT_PROT_PLUS -> S1 common2; S1 throw3 -> BAT_SW_PLUS -> D1 anode2; D1 cathode/band1 -> VSYS/Pico physical39. S1 throw1 is NC (battery OFF). H1 circuit2 joins GND. TP1 only joins USB VBUS/Pico physical40, with no carrier bridge to the battery, VSYS or 3V3_OUT. The Pico's internal diode/regulator remain off-board. A separately verified eFuse replacement is expected from the power helper; it is not implemented in P3.

Battery OFF does not stop USB power. Remove the cell for external charging; no onboard charger is present. Protected-cell PCM thresholds, branch protection, reverse-insertion handling, actual cell/holder fit and power/load/thermal validation remain unresolved. P1835C2 and L1 at 500 mA remain review targets. R1/R2 bias GP13/12 HIGH while pins are high impedance; firmware must idle HIGH and actual ST0238 startup/current/PWM still need testing. C1-C12 are 100nF at the carrier headers, not a substitute for far-end module bypassing.

This is meaningful circuit progress, not a manufacturing release. Complete fault protection, actual component/footprint/polarity checks and load/thermal validation before routing or assembly approval.
