# First-prototype buzzer selection

User selected two SunFounder ST0238 passive low-level-trigger buzzer modules on 2026-10-07. This replaces the unidentified buzzer candidate; it does not approve a footprint or fabrication release.

## Manufacturer evidence

Product: https://www.sunfounder.com/products/3-3-5v-passive-low-level-trigger-buzzer-alarm-sound-module

- SKU: ST0238.
- PCB outline: 32 x 14 mm.
- Supply: 3.3 V or 5 V; use the carrier's regulated 3.3 V rail, subject to current-budget verification.
- Passive buzzer with a PNP transistor driver; input described as low-level trigger.
- Listing specifies square-wave drive at 2–5 kHz. The linked tutorial demonstrates musical notes below that range. Neither establishes adequate loudness across our complete note range; test the prototype.

Tutorial: https://docs.sunfounder.com/projects/ultimate-sensor-kit/en/latest/components_basic/26-component_buzzer.html

## Implementation and remaining checks

Reserve space for two 32 x 14 mm PCB bodies, with additional clearance for headers and sound openings. Height, header pitch/order/location, mounting-hole diameter and center, supply/input current, and input thresholds are not established by the product text. Do not derive a production footprint from the outline alone.

Keep the existing GP12/GP13 buzzer signal allocation for the same-pitch baseline. An active-low driver requires a HIGH idle signal to remain silent; verify the actual circuit and add the appropriate initialization and pull-up provision during electrical integration. PWM frequency sets pitch; the supply voltage is held at 3.3 V.

Use accessible, labeled signal, 3.3 V and GND connections so a replacement module can be wired in during prototype testing. Do not assume another module has an interchangeable connector or mounting geometry. Current schematic connector numbering is provisional and must be reconciled with this module before routing.

The user accepts trying replacement modules if the first prototype's sound is unsuitable. This is not authorization to purchase modules or boards. Five fabricated boards and five populated boards are different quote quantities; populated quantity remains unresolved.
