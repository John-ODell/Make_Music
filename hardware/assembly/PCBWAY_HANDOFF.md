# Five complete Make Music prototypes — assembly planning handoff

Updated 2026-10-09. **REVIEW ONLY — DO NOT ORDER.** This is a concrete scope for
an eventual quotation, not an accepted order or fabrication release. No files
have been uploaded and no supplier has been contacted.

## Quantity and finished result

The requested delivery is **five complete instruments**. Include all carrier
SMT components, through-hole parts, sockets, twelve adapted module cables,
module mounting fixture, battery cassette and underside supports. The user
should have no capacitor, resistor, chip, header or harness soldering to do.
Include five original Raspberry Pi Pico H SC0917, fifty HiLetgo touch modules
and ten SunFounder ST0238 passive buzzer modules. Insert the removable Pico
for programming/testing; agree its installed or separately packed shipping
condition. Cells are removable and externally charged; no onboard charger.

Quote an **additional sixth bare carrier** separately as an optional keepsake.
It does not replace any of the five populated instruments. Screen, keypad,
extra percussion buzzer and other Pico models are future revisions.

Quote metrology and one first-article fit/bring-up before completing the other
four instruments. Record functional acceptance for all five units. Unknown
module terminations and custom fixture details must be resolved in that
first-article work, rather than supplied as unspecified user assembly.

## Parts and operations

| Scope | Per instrument | Five instruments | Required operation |
|---|---:|---:|---|
| Purchased carrier parts | 47 | 235 | 30 top SMT + 17 THT per carrier; exact netlist-derived MPN BOM |
| Pico H SC0917 | 1 | 5 | Removable insertion in two Samtec SSQ-120-01-G-S sockets |
| HiLetgo touch modules, reference 1915450 | 10 | 50 | Eight notes + two left modifiers; verify delivered revision and momentary output |
| SunFounder ST0238 passive modules | 2 | 10 | Confirm signal order, passive variable-pitch operation and reset silence |
| Three-wire module harnesses | 12 | 60 | Adapt module ends; carrier end Harwin M20-1060300 + three M20-1180046 |
| Carrier-end module contacts | 36 | 180 | Qualified AWG26 crimps; identify pin1 and test each circuit |
| Protected conventional 18650 + holder | 1 each | 5 each | Candidate matching/fit gate; MPD BH-18650-W factory wire leads |
| Battery harness | 1 | 5 | JST PHR-2 + two SPH-002T-P0.5S; positive circuit1, ground circuit2 |
| Insulating cassette, raised module fixture, support feet | 1 set | 5 sets | Final machining drawings and loaded clearance after actual-part metrology |
| External charger | Per user | Separate line | Exact cell/charger compatibility must be established before inclusion |

The [instrument parts list](instrument-parts.csv) gives candidate hardware,
wire allowances and mechanical quantities. These allowances are not installed
wire lengths. The purchased carrier BOM excludes TP1 copper and 17 NPTH
mounting holes. It also excludes the removable Pico and external modules.

Carrier J3–J14 use **1 signal / 2 regulated 3V3 / 3 ground**. The unkeyed Harwin
housing needs a visible signal-end mark, retention and continuity inspection.
ST0238 module order differs from the carrier order; cables are adapted, not
assumed straight through. Follow [module harnesses](MODULE_HARNESSES.md).
Do not apply battery voltage to touch/buzzer power pins or exposed GPIO.

H1 is the **bottom-mounted THT** JST-PH, positive circuit1. Verify by cavity
number and continuity to F1; colors alone do not establish polarity. The
MPD holder has factory-installed AWG24 leads: qualify their insulation diameter
and crimp compatibility rather than automatically adding solder-lug wiring.
All other purchased carrier components are top-side. D2 is polarized (K1 on
VSYS, A2 ground); D3 must retain the bidirectional **CA** suffix. U2 has ten
physical terminals and no pad11. Do not substitute an active fixed-tone buzzer.

## Fabrication and assembly process review

Proposal: 330 × 120 mm, two layers, 1.6 mm FR4, at least 35 µm finished copper
on both layers, green solder mask, white legend, lead-free assembly. ENIG is a
proposed finish for the small U2 lands; request the fabricator's stackup and
assembler's accepted finish/stencil process. No controlled impedance,
blind/buried vias or via-in-pad. Seventeen 3.2 mm holes are NPTH.

Process questions to resolve before release:

- U2 has 0.20 mm closest copper gap, nominal 0.10 mm mask web and TI's example
  0.100 mm stencil apertures. Obtain mask/stencil/solder-joint acceptance.
- Pico socket holes have nominal 0.25 mm annular rings. Confirm finished-hole
  fit and accepted annular-ring process; do not assume rounding to a published
  10 mil (0.254 mm) normal-process rule is approved.
- C17/C18 use standard KiCad 0805 lands. Their pad length/width exceed TDK's
  example ranges, while the gap agrees. The documented engineering land choice
  needs assembly acceptance or a reviewed footprint revision.
- Copper approaches the board edge and sockets slightly overhang it. Factory
  panel/handling rails need fiducials and tooling holes. Agree depaneling and
  THT order so the sockets remain undamaged; carrier holes are mounting holes,
  not an approved substitute for factory tooling.
- The enlarged insulating 18650 cassette is a mechanical reservation, not a
  verified enclosure. Require ≥2 mm loaded clearance from bottom parts,
  solder tails and wires, including tolerances and deflection. The four cassette
  bolt exclusions remain enforced; any older partial copper restriction is
  identified separately in PCB status.

The centroid contains **only the 30 SMT parts**. Separate manual THT positions
cover sockets, headers, switch and bottom H1. Native exports use (0,0), x right
and y up: board corners (20,-20) to (350,-140) mm. Mechanical drawings use
top-left/y down: add20 to x and negate y+20 for machine coordinates. Never
mix the earlier bottom-left-origin package with this revision. Check rotations
against pin1 marks, particularly U2, D2 and bottom H1. A bottom-layer drawing
viewed through the top must be labeled that way, not called an underside view.

## Acceptance and release gates

Complete the [precise fit checklist](FIT_CHECKLIST.md) and
[mechanical readiness record](../mechanical/BUILD_READINESS.md) using actual
parts and suitable metric measurement tools. The user's tape measure and
[paper fit print](../../output/pdf/make-music-paper-fit-letter.pdf) can check
overall size and reach; they cannot certify pad pitch or connector engagement.

Complete the staged [power and functional procedure](../power/prototype-validation.md)
with a current-limited cell emulator before real-cell use. Record per-unit
polarity, source isolation, normal load, fault behavior, temperature, all ten
touch inputs and two variable-pitch outputs. Use
`Pico_Synth/carrier_prototype.py` as the current provisional firmware;
actual touch polarity and module behavior must be confirmed in hardware.
Design limits are 0.70 A battery branch, 250 mA external 3V3 and 350 mA total
3V3 including Pico. They are not measured performance or a runtime promise.

The exact protected cell lot, ordinary opposite-end terminals and external
charger tolerances remain gates. Do not replace these with anonymous battery
marketing dimensions. Final fixture/cassette CAD, supplier process acceptance,
first-article fit and bench evidence are required for release. Passing ERC/DRC
does not populate those physical evidence fields.

## Quote breakdown

Show PCB fabrication, carrier SMT setup/stencil/parts/labor, THT labor,
module sourcing, harness crimps/adaptation, fixture/cassette machining,
metrology, first-article qualification, five-unit programming/testing,
Picos/cells/charger, shipping/tax and optional sixth bare board as separate
lines. Price a five-carrier SMT-only alternative as a comparison, clearly
identifying every remaining soldering/mechanical operation. The selected
delivery remains five complete instruments. See [budget worksheet](../ASSEMBLY_BUDGET.md).

Sources checked 2026-10-09: [PCBWay assembly file requirements](https://www.pcbway.com/assembly-file-requirements.html),
[PCBWay capabilities](https://www.pcbway.com/capabilities.html),
[panel rails/fiducials/tooling](https://www.pcbway.com/helpcenter/design_instruction/PCB_Panelization__Breakaway_Rails__Fiducial_Marks__Tooling_Holes.html).
These describe supplier inputs and advertised processes; they do not establish
acceptance of this design or a project price.
