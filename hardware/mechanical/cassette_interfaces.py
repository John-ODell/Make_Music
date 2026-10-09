#!/usr/bin/env python3
"""Generate nominal cassette interfaces for review; no native KiCad I/O or CAM."""

import argparse
import json
from html import escape
from pathlib import Path


def dxf_document(outline, holes, pending, name):
    """Small ASCII DXF with separate pending/reference and candidate layers."""
    pairs = []

    def add(*values):
        pairs.extend(str(v) for v in values)

    def entity(kind, layer, subclass, *geometry):
        add(0, kind, 100, "AcDbEntity", 8, layer, 100, subclass, *geometry)

    def line(layer, a, b):
        entity("LINE", layer, "AcDbLine", 10, a[0], 20, -a[1], 30, 0,
               11, b[0], 21, -b[1], 31, 0)

    def circle(layer, x, y, diameter):
        entity("CIRCLE", layer, "AcDbCircle", 10, x, 20, -y, 30, 0,
               40, diameter / 2)

    add(0, "SECTION", 2, "HEADER", 9, "$ACADVER", 1, "AC1015",
        9, "$INSUNITS", 70, 4, 9, "$MEASUREMENT", 70, 1, 0, "ENDSEC")
    add(0, "SECTION", 2, "TABLES", 0, "TABLE", 2, "LTYPE", 5, "10", 330, "0", 100, "AcDbSymbolTable", 70, 1,
        0, "LTYPE", 100, "AcDbSymbolTableRecord", 100, "AcDbLinetypeTableRecord",
        2, "CONTINUOUS", 70, 0, 3, "Solid line", 72, 65, 73, 0, 40, 0,
        0, "ENDTAB", 0, "TABLE", 2, "LAYER", 5, "20", 330, "0", 100, "AcDbSymbolTable", 70, 5)
    for layer, color in [("0", 7), ("CANDIDATE_OUTLINE", 7),
                         ("CARRIER_HOLES", 5), ("HOLDER_HOLES_PENDING", 1),
                         ("REVIEW_REFERENCE", 8)]:
        add(0, "LAYER", 100, "AcDbSymbolTableRecord", 100, "AcDbLayerTableRecord",
            2, layer, 70, 0, 62, color, 6, "CONTINUOUS")
    add(0, "ENDTAB", 0, "ENDSEC", 0, "SECTION", 2, "ENTITIES")
    x, y, w, h = outline
    corners = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
    for a, b in zip(corners, corners[1:] + corners[:1]):
        line("CANDIDATE_OUTLINE", a, b)
    for hx, hy, d in holes:
        circle("CARRIER_HOLES", hx, hy, d)
    for hx, hy, d in pending:
        circle("HOLDER_HOLES_PENDING", hx, hy, d)
    entity("TEXT", "REVIEW_REFERENCE", "AcDbText", 10, x, 20, -y + 5,
           30, 0, 40, 2.5, 1, f"REVIEW ONLY - {name} - mm; x right/y up",
           50, 0, 7, "STANDARD")
    add(0, "ENDSEC", 0, "EOF")
    return "\n".join(pairs) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--parameters", type=Path,
                    default=Path(__file__).with_name("cassette-interfaces.json"))
    ap.add_argument("--out-dir", type=Path, default=Path(__file__).parent)
    args = ap.parse_args()
    p = json.loads(args.parameters.read_text())
    assert p["status"] == "REVIEW_ONLY_NOT_MACHINING_RELEASE"
    c, b, f, h = (p[k] for k in ["cassette", "backplate", "platform", "holder"])
    cx, cy = h["center"]
    length, width, height = h["body_nominal"]
    tolerance = h["decimal_tolerance"]
    max_length, max_width, max_height = (v + tolerance for v in h["body_nominal"])
    hx, hy = cx - length / 2, cy - width / 2
    holder_holes = [(hx + h["first_mount_from_left"], cy, h["mount_diameter"]),
                    (hx + h["first_mount_from_left"] + h["mount_pitch"], cy,
                     h["mount_diameter"])]
    carrier_holes = [(x, y, p["carrier_hole_diameter"])
                     for x, y in p["carrier_holes"]]
    mounting_z = f["z"] + f["thickness"]
    clearance = p["minimum_loaded_clearance"]
    # Physical review invariants: the intended stack and fixed hardware fit.
    assert cx - max_length / 2 - f["x"] >= clearance
    assert f["x"] + f["width"] - cx - max_length / 2 >= clearance
    assert cy - max_width / 2 - f["y"] >= clearance
    assert f["y"] + f["depth"] - cy - max_width / 2 >= clearance
    assert f["z"] - p["carrier_hardware_review_z"] >= clearance
    assert p["door"]["z"] - p["fitted_loaded_limit_z"] >= clearance
    assert p["fitted_loaded_limit_z"] >= mounting_z + max_height
    assert p["support_surface_min_z"] - c["height"] >= 3
    for x, y, _ in carrier_holes:
        radius = p["carrier_hardware_diameter"] / 2
        assert min(x - c["x"], c["x"] + c["width"] - x,
                   y - c["y"], c["y"] + c["depth"] - y) >= radius
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for file, rect, fixed, proposed, name in [
        ("cassette-backplate-review.dxf", (c["x"], c["y"], c["width"], c["depth"]),
         carrier_holes, [], "backplate / carrier interface"),
        ("cassette-platform-review.dxf", (f["x"], f["y"], f["width"], f["depth"]),
         [], holder_holes, "platform / holder holes PENDING")
    ]:
        (args.out_dir / file).write_text(dxf_document(rect, fixed, proposed, name))

    svg = ['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="1000" viewBox="0 0 1100 1000">',
           '<style>text{font:16px sans-serif;fill:#243449}.head{font-size:22px;font-weight:bold}.small{font-size:14px}.dash{stroke-dasharray:5 4}</style>',
           '<rect width="1100" height="1000" fill="#f8fafc"/>']

    def text(x, y, value, css=""):
        svg.append(f'<text x="{x}" y="{y}" class="{css}">{escape(value)}</text>')

    def rect(x, y, w, d, fill, stroke="#334155", css=""):
        svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{d}" fill="{fill}" stroke="{stroke}" stroke-width="1.5" class="{css}"/>')

    def circle(x, y, radius, stroke, css=""):
        svg.append(f'<circle cx="{x}" cy="{y}" r="{radius}" fill="none" stroke="{stroke}" stroke-width="1.5" class="{css}"/>')

    text(35, 40, "Cassette interface CAD - REVIEW ONLY", "head")
    text(35, 68, "2026-10-09 | original mechanical x right / y down | dimensions mm; not full-size")
    text(35, 95, "Factory fit, fastening, retention, shell/rib load path and tolerances remain pending.")
    scale = 4
    ox, oy = 70, 175

    def plan_point(x, y):
        return ox + scale * (x - c["x"]), oy + scale * (y - c["y"])

    text(35, 137, "Backplate z3..5 / unchanged four carrier holes", "head")
    rect(ox, oy, scale * c["width"], scale * c["depth"], "#e2e8f0")
    for i, (x, y, diameter) in enumerate(carrier_holes):
        px, py = plan_point(x, y)
        circle(px, py, scale * p["carrier_hardware_diameter"] / 2, "#64748b", "dash")
        circle(px, py, scale * diameter / 2, "#2563eb")
        text(px + 19, py + (5 if i < 2 else -5), f"({x},{y})", "small")
    text(ox + 185, oy - 10, f'{c["width"]} x {c["depth"]}')
    text(570, 190, "3.2 nominal carrier-compatible holes")
    text(570, 217, "60 x 26 centre pattern; 5 minimum edge distance")
    text(570, 244, "Dashed diameter 8 hardware projections")
    text(570, 271, "DXF axes: x mechanical, y = -mechanical y")
    text(570, 298, "Legacy native offset (+20,+20); physical top-left (+20,+18.5).", "small")
    text(570, 321, "Optional physical-local y = legacy y + 1.5; native parts fixed.", "small")

    text(35, 379, "Lower platform z14..16 / holder hole references pending", "head")
    ox, oy = 70, 420
    rect(ox, oy, scale * f["width"], scale * f["depth"], "#e2e8f0")
    # This panel uses the platform minimum rather than the cassette minimum.
    def fp(x, y):
        return ox + scale * (x - f["x"]), oy + scale * (y - f["y"])
    px, py = fp(cx - max_length / 2, cy - max_width / 2)
    rect(px, py, scale * max_length, scale * max_width, "#dcfce7", "#059669", "dash")
    for x, y, diameter in holder_holes:
        px, py = fp(x, y)
        circle(px, py, scale * diameter / 2, "#dc2626")
        circle(px, py, scale * h["recess_diameter"] / 2, "#dc2626", "dash")
        text(px - 49, oy + 130, f"({x:.2f},{y:g})", "small")
    text(ox + 145, oy - 10, f'{f["width"]} x {f["depth"]}')
    text(570, 433, "Maximum bare holder 78.20 x 21.40 x 21.81")
    text(570, 460, "10.68 from nominal left end; pitch 55.61")
    text(570, 487, "MPD general decimal tolerance +/-0.5")
    text(570, 514, "Red holes 3.20 / recess reference 5.08")
    text(570, 541, "Confirm actual part and 2-56 fastener before drilling.")

    text(35, 600, "Section reference / z down from carrier underside", "head")
    sx, sy, zscale = 70, 642, 5
    rect(sx, sy - 8, 350, 8, "#93c5fd", "#2563eb")
    rect(sx, sy + b["z"] * zscale, 350, b["thickness"] * zscale, "#cbd5e1")
    rect(sx + 29, sy + f["z"] * zscale, 293, f["thickness"] * zscale, "#cbd5e1")
    rect(sx + 54, sy + mounting_z * zscale, 243, max_height * zscale, "#dcfce7", "#059669", "dash")
    for dx in [16, 202]:
        rect(sx + dx, sy, 3, p["carrier_bolt_tip_nominal_z"] * zscale, "#9d174d", "#9d174d")
    svg.append(f'<path d="M{sx} {sy + p["fitted_loaded_limit_z"] * zscale}H{sx + 350}" stroke="#dc2626" stroke-width="2" class="dash"/>')
    rect(sx, sy + p["door"]["z"] * zscale, 350, p["door"]["thickness"] * zscale, "#cbd5e1")
    svg.append(f'<path d="M{sx - 10} {sy + p["support_surface_min_z"] * zscale}H{sx + 360}" stroke="#334155" stroke-width="2"/>')
    for y, label in [
        (644, "Carrier underside z0; board thickness 1.6 assumed"),
        (674, "Backplate z3..5; carrier bolt tips z9.9 nominal"),
        (710, "Platform z14..16; 4.1 nominal tip clearance"),
        (744, "Maximum bare body ends z37.81 (green)") ,
        (778, "Complete fitted/loaded limit z40 (red)") ,
        (812, "Door z42..44; closure and retainers pending"),
        (846, "Support surface >=47; 3 nominal to cassette")
    ]:
        text(470, y, label)
    text(35, 925, "No additional carrier or module holes. Platforms alone are not a retained enclosure.")
    text(35, 955, "CASSETTE_INTERFACES.md records sources, nominal tolerances, DXF layers and pending gates.")
    svg.append("</svg>")
    (args.out_dir / "cassette-interface-review.svg").write_text("\n".join(svg) + "\n")
    print("Wrote 2 review DXFs and 1 review SVG; nominal stack/clearance checks passed.")


if __name__ == "__main__":
    main()
