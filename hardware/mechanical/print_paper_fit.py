#!/usr/bin/env python3
"""Create a 1:1 two-page Letter paper fit; this is not machining CAD.

Requires ReportLab. Reads the existing mechanical SVG as a body-outline
reference; never reads or writes KiCad source. Output goes to output/pdf.
"""
from pathlib import Path
import xml.etree.ElementTree as ET

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path(__file__).with_name('paper-fit-template.svg')
OUTPUT = ROOT / 'output/pdf/make-music-paper-fit-letter.pdf'
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
svg = ET.parse(SOURCE).getroot()
assert svg.attrib['viewBox'] == '0 0 330 120'
page_w, page_h = letter
c = canvas.Canvas(str(OUTPUT), pagesize=letter, invariant=1)
c.setTitle('Make Music - full-size paper fit - two Letter pages')
c.setAuthor('Make Music project')


def label(x, y, text, size=8, bold=False, centered=False):
    c.setFillColor(colors.HexColor('#172b40'))
    c.setFont('Helvetica-Bold' if bold else 'Helvetica', size)
    if centered:
        c.drawCentredString(x * mm, page_h - y * mm, text)
    else:
        c.drawString(x * mm, page_h - y * mm, text)


for number, start in enumerate((0, 150), 1):
    label(15, 18, 'MAKE MUSIC / ACTUAL-SIZE PAPER FIT', 14, True)
    label(15, 26, f'Page {number} of 2 - board x={start} to {start + 180} mm', 10, True)
    label(15, 34, 'Print on US Letter at 100% / Actual Size. Turn off Fit or Shrink.', 9)
    label(15, 40, 'Check BOTH scale bars before judging reach. Paper checks comfort only.', 9)
    c.setStrokeColor(colors.HexColor('#172b40'))
    c.setLineWidth(.35 * mm)
    for y, length, caption in [(49, 101.6, '4 inches exactly - check with your tape measure'),
                                (61, 100, '100 mm exactly - optional metric check')]:
        c.line(15 * mm, page_h - y * mm, (15 + length) * mm, page_h - y * mm)
        for x in (15, 15 + length):
            c.line(x * mm, page_h - (y - 2) * mm, x * mm, page_h - (y + 2) * mm)
        label(15, y + 6, caption, 8)
    ox, oy = 15, 84
    c.saveState()
    clip = c.beginPath()
    clip.rect(ox * mm, page_h - (oy + 120) * mm, 180 * mm, 120 * mm)
    c.clipPath(clip, stroke=0)
    # Preserve actual SVG body coordinates in millimetres. Exclude the large
    # decorative background outside the board and reference text/dimensions.
    for element in svg:
        tag = element.tag.split('}')[-1]
        if tag == 'rect':
            x, y = float(element.get('x', '0')), float(element.get('y', '0'))
            w, h = float(element.get('width')), float(element.get('height'))
            if y < -1 or h > 120 or w > 330:
                continue
            fill = element.get('fill', 'none')
            c.setFillColor(colors.white if fill == 'white' else colors.HexColor(fill)
                           if fill.startswith('#') else colors.white)
            c.setStrokeColor(colors.HexColor('#64748b'))
            c.setLineWidth(.2 * mm)
            c.rect((ox + x - start) * mm, page_h - (oy + y + h) * mm,
                   w * mm, h * mm, stroke=1, fill=int(fill != 'none'))
        elif tag == 'circle':
            x, y, r = (float(element.get(key)) for key in ('cx', 'cy', 'r'))
            c.setStrokeColor(colors.HexColor('#64748b'))
            c.setFillColor(colors.white)
            c.setLineWidth(.2 * mm)
            c.circle((ox + x - start) * mm, page_h - (oy + y) * mm,
                     r * mm, stroke=1, fill=int(element.get('fill') == 'white'))
    bodies = [(24, 54, 'SEMITONE +'), (24, 94, 'OCTAVE +'),
              *[(70 + 34 * n, 94, note) for n, note in
                enumerate(('C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5'))],
              (60, 67.5, 'BUZZER 1'), (98, 67.5, 'BUZZER 2'),
              (120, 30, 'PICO H'), (180, 30, 'BATTERY BELOW')]
    for x, y, text in bodies:
        label(ox + x - start, oy + y, text, 7, True, True)
    c.restoreState()
    # Crosses in the 30 mm overlap have the same global coordinates on both
    # pages; cutting/taping does not require a ruler or an estimated join.
    for x in (160, 170):
        for y in (-3, 123):
            px, py = (ox + x - start) * mm, page_h - (oy + y) * mm
            c.setStrokeColor(colors.HexColor('#be123c'))
            c.setLineWidth(.3 * mm)
            c.line(px - 2 * mm, py, px + 2 * mm, py)
            c.line(px, py - 2 * mm, px, py + 2 * mm)
    label(15, 219, 'JOIN: overlap the repeated section and align all four red crosses.', 9, True)
    label(15, 227, 'Hold the joined 330 x 120 mm outline; try the keys with both hands.', 9)
    label(15, 233, 'Notes: 24 mm bodies, 34 mm centres, 10 mm clear gaps. Modifiers on left.', 9)
    label(15, 245, 'Record: comfortable reach? key gap? overall size? room for USB/removal?', 9)
    label(15, 254, 'Body sizes and mounts still need actual-part fit. DO NOT use this to drill.', 9, True)
    c.showPage()
c.save()
print(OUTPUT)
