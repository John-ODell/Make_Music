"""Render quote-only logical cable drawings; no native KiCad mutations."""
from pathlib import Path
import argparse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.colors import HexColor, white
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle

ROOT = Path(__file__).resolve().parents[3]
PINS = [('J3','C4',16,'Touch OUT/DI'),('J4','D4',17,'Touch OUT/DI'),
        ('J5','E4',18,'Touch OUT/DI'),('J6','F4',19,'Touch OUT/DI'),
        ('J7','G4',20,'Touch OUT/DI'),('J8','A4',21,'Touch OUT/DI'),
        ('J9','B4',22,'Touch OUT/DI'),('J10','C5',26,'Touch OUT/DI'),
        ('J11','Semitone modifier',27,'Touch OUT/DI'),('J12','Octave modifier',28,'Touch OUT/DI'),
        ('J13','Buzzer 1',13,'Passive module I/O'),('J14','Buzzer 2',12,'Passive module I/O')]
CIRCUITS = [(1,'WHITE','SIGNAL','OUT/DI or I/O'),
            (2,'RED','regulated 3V3','VCC'),(3,'BLACK','GND','GND')]
W, H = landscape(A4)
INK = HexColor('#172D3D')
MUTED = HexColor('#526674')
RULE = HexColor('#CAD5DC')
WARN = HexColor('#A32822')
STYLE = ParagraphStyle('body', fontName='Helvetica', fontSize=9, leading=12,
                       textColor=INK, spaceAfter=0)

def label(c, x, y, text, size=10, bold=False, color=INK):
    c.setFillColor(color)
    c.setFont('Helvetica-Bold' if bold else 'Helvetica', size)
    c.drawString(x, y, text)

def para(c, x, y, text, width, size=9):
    style = ParagraphStyle('p', parent=STYLE, fontSize=size, leading=size+3)
    p = Paragraph(text, style)
    aw, ah = p.wrap(width, 1000)
    p.drawOn(c, x, y-ah)
    return y-ah

def start(c, number, title, code):
    label(c,36,H-37,'MAKE MUSIC P1  |  CABLE DRAWINGS',18,True)
    label(c,36,H-58,title,11,True)
    label(c,36,H-79,'QUOTE / ENGINEERING REVIEW ONLY - NOT A RELEASED CABLE MANUFACTURING DRAWING',9,True,WARN)
    c.setStrokeColor(RULE); c.line(36,H-90,W-36,H-90)
    label(c,36,34,f'{code}  /  REV A  /  2026-10-19  /  Sheet {number} of 3',8,False,MUTED)
    label(c,415,34,'Logical connections only. Not to scale. No physical connector view is implied.',8,False,MUTED)

def box(c,x,y,w,h):
    c.setFillColor(HexColor('#F4F7F9'));c.setStrokeColor(RULE)
    c.roundRect(x,y,w,h,7,stroke=1,fill=1)

def wire(c,x1,y,x2,name,color):
    c.setStrokeColor(color); c.setLineWidth(2)
    c.line(x1,y,x2,y)
    for x in (x1,x2):
        c.setFillColor(color);c.circle(x,y,3,stroke=0,fill=1)
    c.setLineWidth(1)
    c.setFillColor(white);c.rect((x1+x2)/2-102,y+5,204,14,stroke=0,fill=1)
    label(c,(x1+x2)/2-99,y+8,name,9,True)

def dimension(c,x1,x2,y,text):
    c.setStrokeColor(MUTED);c.setLineWidth(.7);c.setDash(3,3)
    c.line(x1,y,x2,y);c.setDash()
    for x,sign in ((x1,1),(x2,-1)):
        c.line(x,y,x+sign*6,y+3);c.line(x,y,x+sign*6,y-3)
    c.setFont('Helvetica',8);c.setFillColor(MUTED)
    c.drawCentredString((x1+x2)/2,y-14,text)

def table(c,data,x,top,widths,row_height=23):
    converted=[[Paragraph(str(v),ParagraphStyle('cell',parent=STYLE,fontSize=9,
                 leading=11,textColor=white if i==0 else INK)) for v in row]
               for i,row in enumerate(data)]
    t=Table(converted,colWidths=widths,rowHeights=[row_height]*len(data))
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),INK),
                          ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                          ('LEFTPADDING',(0,0),(-1,-1),8),
                          ('LINEBELOW',(0,0),(-1,0),.7,RULE),
                          ('ROWBACKGROUNDS',(0,1),(-1,-1),[white,HexColor('#F3F6F8')])]))
    tw,th=t.wrap(1000,1000);t.drawOn(c,x,top-th)
    return top-th

def validate_source():
    source=(Path(__file__).parent/'WIRE_SPEC.md').read_text()
    for header,function,gpio,destination in PINS:
        assert f'| {header} | {function} | GP{gpio} |' in source
    for cavity,color,function,terminal in CIRCUITS:
        assert f'Carrier cavity {cavity}' in source
    assert len(PINS)==12 and 12*2==24 and 24*3==72
    assert '7.2 m' in source and '100 mm' in source
    for token in ('M20-1060300','M20-1180046','AWG26','AWG24','PHR-2','SPH-002T-P0.5S','150 +/-5'):
        assert token in source

def build(path):
    validate_source()
    path.parent.mkdir(parents=True,exist_ok=True)
    c=canvas.Canvas(str(path),pagesize=(W,H),pageCompression=1)
    c.setTitle('Make Music P1 - Cable Connection Drawings - Quote Only - Rev A')
    c.setAuthor('Make Music project')

    start(c,1,'A. Typical touch / passive buzzer module harness','MM-CAB-001')
    label(c,44,477,'12 per complete instrument / 24 total for two complete instruments',11,True)
    label(c,44,458,'Carrier-side circuit numbers are fixed. Module-end physical positions and mating parts are NOT yet defined.',9)
    box(c,44,252,205,177);box(c,587,252,210,177)
    label(c,57,410,'CARRIER-END PLUG',11,True)
    label(c,57,393,'Harwin M20-1060300 housing',9)
    label(c,57,377,'3 x M20-1180046 contacts',9)
    label(c,600,410,'MODULE-END FUNCTIONS',11,True)
    label(c,600,393,'Actual connector / pad view TBD',9)
    for (pin,color,signal,target),y in zip(CIRCUITS,(350,310,270)):
        label(c,58,y-3,f'Cavity {pin}: {signal}',10,True)
        wire(c,249,y,587,f'{color} - stranded AWG26',
             {'WHITE':HexColor('#738695'),'RED':HexColor('#C33730'),'BLACK':INK}[color])
        label(c,602,y-3,target,10,True)
    dimension(c,264,574,233,'100 mm per conductor = INITIAL COSTING ALLOWANCE ONLY')
    para(c,44,197,'<b>Length:</b> factory to propose finished dressed length and tolerance after measuring the actual module, mounting fixture and routing. Do not cut wires to 100 mm without an approved final drawing.',750)
    para(c,44,157,'<b>Crimp:</b> insulation OD 0.9-1.6 mm; strip 3-4 mm for the specified Harwin contact. Qualify tooling, sample pull/retention and insulation support. The grey line represents the specified WHITE wire, not a fourth conductor.',750)
    para(c,44,116,'<b>Orientation:</b> mark carrier plug cavity 1 and align to the carrier square pad/pin1 mark. The unkeyed plug must not reverse or shift by one pin. Map module SIGNAL / VCC / GND by its actual labels; do not assume straight-through pin order. Regulated 3.3V only, never raw battery voltage.',750)
    c.showPage()

    start(c,2,'B. Harness identification, quantities and module-end drawing request','MM-CAB-001')
    rows=[['Harness ID / carrier','Function','Pico GPIO','Module signal terminal','Quantity for two']]
    rows += [[f'MH-{h} / {h}',f, f'GP{g}', d,2] for h,f,g,d in PINS]
    bottom=table(c,rows,44,478,[145,110,100,245,153],21)
    para(c,44,bottom-15,'Every harness also connects carrier cavity 2 to verified module VCC and cavity 3 to verified module GND. GPIO numbers are not physical Pico pin numbers. Total: 24 housings, 72 contacts and 72 AWG26 conductors (7.2 m before scrap at the initial allowance).',750)
    para(c,44,bottom-63,'<b>Supplier to return before cable release:</b> exact module maker/revision and photo; mating-face AND wire-entry connector views with cavity numbers; module-end connector/contact MPNs or approved pad-termination drawing; pin-to-pin continuity map; installed length, slack and tolerance; retention and strain-relief details.',750)
    para(c,44,bottom-122,'Generic modules are allowed for quotation. Their header pitch, pin order, engagement, electrical polarity and mounting clearances must be confirmed on delivered parts. Existing ST0238 and generic module pin order must not be treated as identical.',750)
    c.showPage()

    start(c,3,'C. Protected removable 18650 battery-holder harness','MM-CAB-002')
    label(c,44,477,'1 per complete instrument / 2 completed battery harnesses total',11,True)
    label(c,44,458,'Diagram shows circuit function only; terminal location and connector-face orientation are NOT depicted.',9)
    box(c,44,273,220,159);box(c,591,273,206,159)
    label(c,57,413,'MPD BH-18650-W',11,True)
    label(c,57,396,'Holder with factory-installed leads',9)
    label(c,604,413,'JST PHR-2 PLUG',11,True)
    label(c,604,396,'2 x SPH-002T-P0.5S contacts',9)
    label(c,57,358,'Measured holder POSITIVE (+)',9,True)
    label(c,57,295,'Measured holder NEGATIVE (-)',9,True)
    wire(c,264,356,591,'AWG24 factory lead - positive',HexColor('#C33730'))
    wire(c,264,293,591,'AWG24 factory lead - ground',INK)
    label(c,604,356,'Circuit 1 -> H1.1',10,True)
    label(c,604,339,'BAT_PROT_PLUS',9)
    label(c,604,293,'Circuit 2 -> H1.2',10,True)
    label(c,604,276,'GND',9)
    dimension(c,276,579,253,'Factory supplied leads: 150 +/-5 mm EACH; final finished length TBD')
    para(c,44,215,'<b>Parts / quantity for two:</b> 2 wired holders, 2 PHR-2 housings and 4 SPH-002T-P0.5S contacts. Holder leads are included; do not add a duplicate wire set. The bottom-mounted carrier H1 connector is already in the 47-part carrier BOM.',750)
    para(c,44,172,'<b>Process:</b> supplied AWG24 TR64 lead insulation OD must fit the exact JST contact/tool range of 0.8-1.5 mm. Re-prepare and crimp per the qualified JST process. The holder supplier\'s pre-stripped end is not a JST strip instruction. Identify polarity by continuity, not color; diagram colors show functions only.',750)
    para(c,44,116,'<b>Cold acceptance:</b> with cell, USB and electronics disconnected, trace holder (+) to PHR-2 circuit 1 / H1.1 and holder (-) to circuit 2 / H1.2. Verify no cross-short, insulated joints, strain relief and removal slack. Final dressed length, connector views, cell/holder fit, contact capability and cell/charger qualification remain held.',750)
    c.showPage();c.save()

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=ROOT/'output/pdf/MakeMusic_Cable_Drawings_RevA_QUOTE_ONLY.pdf')
    build(parser.parse_args().output)
