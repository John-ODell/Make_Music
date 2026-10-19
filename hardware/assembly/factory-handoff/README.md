# Make Music factory handoff

Prepared October 16, 2026 for supplier quotation and engineering review.
**QUOTE ONLY. No purchase, fabrication or assembly release.**

Confirmed requested delivery: **two complete instruments plus three populated
carrier boards, five carriers total**. All five receive the unchanged 47-part
carrier BOM. Only two receive the Pico H, modules, harnesses, battery/holder,
mechanical work, programming and complete-instrument tests. The first article
is one of those two complete instruments; do not add an extra board.

The three requested inputs are:

1. [WIRE_SPEC.md](WIRE_SPEC.md): conductor specifications, connectors, cavity
   mapping, quantities and the actual-part termination/length approval points.
2. [PROGRAMMING.md](PROGRAMMING.md): application and interpreter files,
   installation, configuration and version/hash recording.
3. [TEST_FILE.md](TEST_FILE.md): factory inspection/qualification procedure and
   a blank per-unit result form, including expected note frequencies.

October 19 supplement: [cable connection drawings, Rev A](../../../output/pdf/MakeMusic_Cable_Drawings_RevA_QUOTE_ONLY.pdf)
visually show the module and battery harness circuits. This three-sheet PDF is
a separate supplement to the previously sent archive; the old ZIP is unchanged.
It is for quotation/engineering review, not a dimensioned physical connector
view or released cable build drawing. Supplier-selected module ends and final
dressed lengths require measured parts and returned mating-face/wire-entry
drawings. Rebuild with `draw_cables.py`; the builder reconciles header/GPIO
mapping, connector names and quantities with WIRE_SPEC.md before rendering.

The sendable archive includes these files, the unchanged current application
as `main.py`, official stable MicroPython RP2040 runtime UF2, `SHA256SUMS.txt`,
and the revised mixed-delivery quote request. The UF2 is the interpreter only:
the application must also be copied to the Pico filesystem. No custom
application-embedded UF2 is claimed.

Seven existing host logic checks pass. They verify software behavior using
fake GPIO/PWM; they do not verify a real Pico, MicroPython runtime execution,
module pitch/volume/current, harnesses, mechanical fit or power protection.
All physical qualification and factory-process acceptance remain pending.
Please quote and confirm your ability to perform them, and identify missing
inputs or work your team cannot supply. Do not treat these procedures as
completed test results or authorization to begin a build.

Generic TTP223 and low-trigger transistor-driven passive modules are permitted
as candidates. Supply exact delivered revisions, pin order and measurements
before final mechanical drawings, wire cut lengths and touch polarity are
frozen. The protected cell/charger qualification and nominal mounting-structure
holds in the original packet remain in force. No revision of carrier CAD or
the grouped 47-part carrier BOM is made by this handoff.
