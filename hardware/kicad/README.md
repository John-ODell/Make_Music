# Editable Pico instrument carrier

Open `make_music.kicad_pro` in KiCad 10, then open the schematic. The project-local `MakeMusic.kicad_sym` library and `sym-lib-table` resolve all symbols without a third-party library installation. `fp-lib-table` registers the merged `../libraries/MakeMusic.pretty` socket library as `MakeMusic`. The schematic is the editable source of truth; do not regenerate it from the review PDF.

- `make_music.kicad_sch`: one A3 sheet, two removable female sockets, ten touch interfaces, two buzzer interfaces, one expansion header, and a logical power integration block.
- `schematic-review.pdf`: readable schematic export, marked provisional.
- `pico-socket-map.csv`: all 40 Pico physical pins mapped to local socket pins and carrier nets.
- `verify_connectivity.py`: checks every endpoint in a fresh XML netlist against the reviewed interface contract.
- `../reviews/schematic.md`: verified facts, actual checks and unresolved design decisions.

J1 and J2 each use local pad numbers 1-20. J1 pin 1 is at the USB end; J2 pin 1 is at the opposite end. J2 pin 20 is beside USB. J1/J2 are assigned `MakeMusic:Samtec_SSQ-120-01-G-S_1x20_P2.54mm` as candidates. Place J1 pad 1 at USB and rotate J2 180 degrees relative to J1 so J2 pad 20 is at USB. This integration numbering supersedes the mechanical proposal's alternative right-row pad-1-at-USB convention; do not reverse the existing schematic nets to match that proposal.

J3-J14 pin order is an assumption, visibly labeled: 1=signal, 2=3V3_OUT, 3=GND. Do not assemble against this order until actual modules are identified. J15 expansion order is provisional. Only J1/J2 have assigned footprints; J3-J15 remain unset. Socket geometry is verified against the Samtec drawing, but selected Pico/male-header engagement, finished-hole tolerances and physical clearances still need validation. X1 is a logical interface excluded from BOM and board, with no physical connector implied. The inserted Pico and module electronics are off-board and not modeled.

Run from this directory (write generated logs/netlists outside the repository):

```sh
kicad-cli sch erc --severity-all --exit-code-violations --format json -o /tmp/make-music-erc.json make_music.kicad_sch
kicad-cli sch export netlist --format kicadxml -o /tmp/make-music-netlist.xml make_music.kicad_sch
python3 verify_connectivity.py /tmp/make-music-netlist.xml
kicad-cli sch export pdf -o schematic-review.pdf make_music.kicad_sch
```

The user permits firmware adaptation to confirmed touch polarity, including active-low. Confirm direct/momentary configuration and actual idle/touched levels first; no firmware changes are made by this follow-up.

This is a carrier connection plan, not a complete battery circuit or manufacturing package. Power integration and verified module/driver compatibility must precede routing.
