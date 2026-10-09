# Touch module evidence — HiLetgo / TTP223-BA6

Status: electrical reference identified; actual module configuration and complete mechanical interface remain unverified.

## User-provided evidence

- Product link: http://www.hiletgo.com/ProductDetail/1915450.html
- Supplied schematic: [touchbutton.jpg](reference/touchbutton.jpg).
- Quoted module size: 24 x 24 x 7.2 mm; four M2 positioning holes; weight 2 g.
- Quoted module supply range: 2.0–5.5 V, typically 3 V.

The vendor page could not be retrieved during this review. The quoted module dimensions and mounting details therefore remain user-supplied specifications, not independently measured dimensions. The chip is labeled TTP223-BA6 in the supplied schematic.

## Manufacturer verification

Primary datasheet: https://www.tontek.com.tw/uploads/product/243/TTP223-BA6_V2.1_EN.pdf

The IC supports a 2.0–5.5 V supply and CMOS output. Pins: 1 Q (output), 2 VSS, 3 I (electrode input), 4 AHLB, 5 VDD, 6 TOG. TOG=0 selects direct/momentary operation; AHLB=0 selects active-high and AHLB=1 active-low. Response at 3 V is specified up to 60 ms in fast mode and 220 ms in low-power mode. After a touch/release, fast mode persists about 12 seconds. Power-up settling is about 0.5 seconds. The manufacturer calls for local supply bypassing and short sensing traces.

## Implications for this instrument

- Use regulated 3.3 V for the touch modules, with a shared ground and a separate Q-to-GPIO connection for each module.
- Require momentary output for notes and held modifiers. Verify the actual TOG/AHLB configuration.
- The reference image appears to tie AHLB to VCC, selecting active-low; do not assume every supplied board matches that image. Existing firmware treats high as pressed. Determine idle/touched levels on the actual module before changing firmware or selecting external bias resistors.
- The image labels the connector signals as output, VCC and GND. This is not enough to establish physical header orientation, pin numbers or pitch. Verify those from the real board before assigning connector footprints.
- The image shows a touch sensitivity capacitor marked 22 pF and an indicator LED circuit. Do not treat the diagram as a complete verified PCB implementation or copy it without the manufacturer bypassing requirements.
- Allow for module LEDs in the power budget; the bare IC no-load current does not describe the complete module.
- Each touch channel can spend time in low-power mode independently. Test idle-to-touch and release response, rapid notes, simultaneous modifiers, and neighbor false triggers with battery and USB power.
- Eight 24 mm-wide modules already occupy at least 192 mm before gaps and side controls. Board dimensions must reflect the chosen arrangement; the concept sketch is not to scale.

## Still needed

Actual module photos/measurements: header labels and orientation, pitch, mounting-hole centers and diameters, touch face position, underside clearance, output mode, and presence of local bypassing. Confirm whether existing modules will be mounted on the carrier or whether integrated electrodes are desired in a later revision. Current baseline remains separate modules.
