# Make Music PCB

The first-prototype electrical project is now an editable, fully routed KiCad10 carrier with protected battery power, removable Pico H sockets, eight notes/two left-hand modifiers, two passive buzzer module connectors and exposed GPIO. Native ERC and integrated DRC/parity pass with **0 violations /0 unconnected items /0 schematic mismatches**. Exact-part fit and built-hardware tests remain pending; fabrication is held.

Open [kicad/make_music.kicad_pro](kicad/make_music.kicad_pro) in KiCad10. Keep the entire hardware directory so project-local symbols/footprints resolve. The two editable schematic sheets and routed PCB are sources; PDFs/SVGs are review aids.

- [Current PCB status and checks](kicad/PCB_STATUS.md)
- [Selected requirements and GPIO allocation](PCB_DESIGN_NOTES.md)
- [Native schematic and library instructions](kicad/README.md)
- [Held manufacturing/assembly review package](manufacturing/REVIEW_ONLY_DO_NOT_ORDER/README.md)
- [Actual-part measurements still needed](assembly/FIT_CHECKLIST.md)
- [Factory assembly and budget comparison](ASSEMBLY_BUDGET.md)
- [Module cable specification](assembly/MODULE_HARNESSES.md)
- [Raised module fixture](mechanical/MODULE_FIXTURE.md) and [wired underside holder cassette](mechanical/WIRED_HOLDER_PROPOSAL.md)
- [Protected power circuit](power/branch-protection.md) and [staged validation procedure](power/prototype-validation.md)

The proposed carrier is330 ×120 mm with a removable externally charged protected18350. The wired Keystone1101 holder/cassette and raised module fixture are engineering proposals. Protected-cell fit, connector engagement, module support regions, final mechanical CAD, power/load/thermal behavior and fabricator/assembler acceptance remain required. See the fit checklist for precise measurements; do not order from either the old concept sketch or the held exports.

`../Pico_Synth/carrier_prototype.py` provides the carrier pin map, configurable touch polarity and active-low ST0238 idle behavior. It preserves the original firmware; seven host logic tests pass, but no assembled instrument has been tested. Both buzzers play the same pitch, modified by held left semitone/octave controls. Independent voices require a pin/firmware change.

Next: verify actual parts and paper fit, finalize the custom mechanical subassemblies, review the factory quote/assembly process, and bring up one prototype using the current-limited validation procedure. PCB fabrication alone does not supply modules, cables, mechanical assembly, Pico, battery or charger. The published$67.54 setup/stencil example is not a full instrument quote.
