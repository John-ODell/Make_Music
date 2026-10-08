# Editable Pico instrument carrier

Open `make_music.kicad_pro` in KiCad 10, then open the schematic. The project-local `MakeMusic.kicad_sym` library and `sym-lib-table` resolve all symbols. `fp-lib-table` registers socket, carrier and power libraries plus installed KiCad 10 `Connector_JST`, `Resistor_SMD`, `Capacitor_SMD` and `TestPoint` libraries. The schematic is the editable source of truth; do not regenerate it from the review PDF.

- `make_music.kicad_sch`: A3 root with two removable female sockets, ten touch/two buzzer cable headers, expansion, two reset pull-ups and twelve header bypass capacitors.
- `battery_power.kicad_sch`: editable A3 child sheet with JST battery entry, upstream fuse, switch, TPS259474L protection and supporting passives/clamps; VSYS/GND connect through hierarchical ports.
- `make_music.kicad_pcb`: fully placed/routed two-layer carrier with all46 schematic parts,17 board-only mounting holes, two filled ground pours and module/cassette reference drawings; see [PCB status](PCB_STATUS.md).
- `schematic-review.pdf`: readable two-page A3 schematic export, marked prototype review.
- `pico-socket-map.csv`: all 40 Pico physical pins mapped to local socket pins and carrier nets.
- `verify_connectivity.py`: checks every endpoint in a fresh XML netlist against the reviewed interface contract.
- `carrier-interfaces.md`: exact carrier parts, cable mapping, footprint evidence and placement/release gates.
- `power-integration.md`: native reference mapping, power parts, RPW/fuse/TVS geometry, validation and qualification gates.
- `../reviews/schematic.md`: verified facts, actual checks and unresolved design decisions.

J1 and J2 each use local pad numbers 1-20. J1 pin 1 is at the USB end; J2 pin 1 is at the opposite end. J2 pin 20 is beside USB. J1/J2 are assigned `MakeMusic:Samtec_SSQ-120-01-G-S_1x20_P2.54mm` as candidates. Place J1 pad 1 at USB and rotate J2 180 degrees relative to J1 so J2 pad 20 is at USB. This integration numbering supersedes the mechanical proposal's alternative right-row pad-1-at-USB convention; do not reverse the existing schematic nets to match that proposal.

J3-J14 carrier order is defined as 1=SIG, 2=3V3_OUT, 3=GND. Assigned Harwin headers are cable adapters; actual module pin order is mapped separately by label, and no module mounting geometry is claimed. J15 has the exact Harwin 16-way candidate and defined GPIO order. H1 is the PM-approved underside JST PH battery harness, circuit1=BAT_PROT_PLUS/circuit2=GND; it does not put holder contacts or holes on the carrier. All 46 physical components have assigned footprints, including TP1's 2mm bare copper test pad. See [carrier interface contract](carrier-interfaces.md) for ST0238 cable permutation, reset bias and local bypass placement. The selected inserted module is original non-wireless RP2040 Pico H SC0917 with fitted male headers; its electronics and the module drivers remain off-board/unmodeled. Cold-fit/engagement checks remain. The routed PCB is synchronized to both schematic sheets. Native DRC with schematic parity and all severities passes with zero violations/unconnected/parity issues; physical fit remains pending.

Run from this directory (write generated logs/netlists outside the repository):

```sh
kicad-cli sch erc --severity-all --exit-code-violations --format json -o /tmp/make-music-erc.json make_music.kicad_sch
kicad-cli sch export netlist --format kicadxml -o /tmp/make-music-netlist.xml make_music.kicad_sch
python3 verify_connectivity.py /tmp/make-music-netlist.xml
kicad-cli sch export pdf -o schematic-review.pdf make_music.kicad_sch
```

The user permits firmware adaptation to confirmed touch polarity, including active-low. Confirm direct/momentary configuration and actual idle/touched levels first; the separate carrier_prototype.py firmware supports configurable active levels; no module polarity has been measured.

Revision-1 source path: protected-cell external + -> H1 circuit1 -> F1 -> BAT_FUSED_PLUS -> S1 common2; S1 throw3 -> BAT_SW_PLUS -> U2 IN5; U2 OUT6 -> VSYS/Pico physical39. S1 throw1 is NC (battery OFF). H1 circuit2 joins GND. Carrier series D1 is removed. D2 is a VSYS-to-GND shunt clamp; D3 is the bidirectional input TVS. TP1 only joins USB VBUS/Pico physical40. The Pico's internal USB diode/regulator remain off-board. See [native power integration](power-integration.md) for exact R3–R8/C13–C16 mapping and package evidence.

Battery OFF permits USB power. Remove the cell for external charging; no onboard charger is present. Source changes may reboot: stop playing and let the instrument restart before resuming. No polymer hold-up additions are fitted. Hardware UVLO/overload protection is implemented, while assembly-specific protection response, PCM thresholds, actual cell/holder fit and power/load/thermal validation remain open. Adopted limits are ≤0.70A battery branch, ≤350mA total3V3 including Pico, ≤250mA external3V3 and ≤100µF total VSYS capacitance including Pico. P1835C2 and L1 at500mA remain review targets. R1/R2 bias GP13/12 HIGH while pins are high impedance; firmware must idle HIGH and ST0238 startup/current/PWM still need testing. C1–C12 remain100nF at the carrier headers; native C5/C6 are retained and are unrelated to the removed power-document polymer C5/C6.

Electrical routing/checks are complete for review. Complete actual component/polarity/engagement checks, final mechanical CAD, bench/thermal/fit validation and fabricator/assembler acceptance before manufacturing approval. See ../assembly/FIT_CHECKLIST.md and ../manufacturing/REVIEW_ONLY_DO_NOT_ORDER/README.md. The export_review.py generator always keeps exports on review hold.
