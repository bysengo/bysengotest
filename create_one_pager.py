#!/usr/bin/env python3
"""Generate Sengo one-pager PDF combining impact data and pitch narrative."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os

# Brand colors
TEAL = HexColor('#1B3533')
LIGHT_TEAL = HexColor('#244A47')
ORANGE = HexColor('#D57028')
CREAM = HexColor('#F3EDE7')
TAN = HexColor('#AF8145')
OLIVE = HexColor('#717E36')
WHITE = HexColor('#FFFFFF')
BROWN = HexColor('#67441A')

PAGE_W, PAGE_H = letter  # 8.5 x 11 portrait
MARGIN = 0.4 * inch
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(BASE_DIR, 'Sengo_One_Pager.pdf')


def rrect(c, x, y, w, h, r, fill_color):
    c.setFillColor(fill_color)
    c.roundRect(x, y, w, h, r, fill=1, stroke=0)


def wrap_text(c, text, x, y, max_width, font="Helvetica", size=7, color=CREAM, leading=9.5):
    """Word-wrap text. Returns y after last line."""
    c.setFont(font, size)
    c.setFillColor(color)
    words = text.split()
    lines, cur = [], ""
    for w in words:
        test = cur + (" " if cur else "") + w
        if c.stringWidth(test, font, size) <= max_width:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    for line in lines:
        c.drawString(x, y, line)
        y -= leading
    return y


def divider(c, y, usable_w):
    c.setFillColor(ORANGE)
    c.rect(MARGIN, y, usable_w, 1.5, fill=1, stroke=0)
    return y


def section_head(c, text, y):
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(ORANGE)
    c.drawString(MARGIN, y, text)
    return y


def build():
    c = canvas.Canvas(OUTPUT, pagesize=(PAGE_W, PAGE_H))
    c.setTitle("Sengo One Pager")

    uw = PAGE_W - 2 * MARGIN

    # ── BACKGROUND ──
    c.setFillColor(TEAL)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    # Orange top bar
    c.setFillColor(ORANGE)
    c.rect(0, PAGE_H - 3.5, PAGE_W, 3.5, fill=1, stroke=0)

    # ── HEADER ──
    logo_path = os.path.join(BASE_DIR, 'Sengo 2.PNG')
    logo_h = 55
    logo_w = logo_h * (3533 / 3089)  # preserve actual aspect ratio
    c.drawImage(ImageReader(logo_path),
                MARGIN, PAGE_H - 60,
                width=logo_w, height=logo_h, mask='auto')

    tx = MARGIN + logo_w + 8
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(ORANGE)
    c.drawString(tx, PAGE_H - 22, "REIMAGINING FUNDRAISING & INVESTING")
    c.setFont("Helvetica", 7)
    c.setFillColor(CREAM)
    c.drawString(tx, PAGE_H - 33, "Through community, education, and access")
    c.setFont("Helvetica", 6.5)
    c.setFillColor(TAN)
    c.drawString(tx, PAGE_H - 43, "Founded by Ila B Corcoran  |  bysengo.com")

    # Right: date badge
    bw, bh = 80, 20
    bx = PAGE_W - MARGIN - bw
    by = PAGE_H - 34
    rrect(c, bx, by, bw, bh, 5, ORANGE)
    c.setFont("Helvetica-Bold", 7.5)
    c.setFillColor(WHITE)
    c.drawCentredString(bx + bw / 2, by + 6, "February 2026")

    # ── DIVIDER ──
    y = PAGE_H - 68
    divider(c, y, uw)

    # ── THE PROBLEM ──
    y -= 13
    section_head(c, "THE PROBLEM", y)
    y -= 11
    y = wrap_text(c,
        "Despite 97% of the US population being technically eligible to invest in private "
        "assets\u2014the fastest-growing asset class\u2014less than 2% actually do. Meanwhile, "
        "less than 0.5% of Black founders received venture capital in Q2 2025.* A $14 trillion "
        "wealth gap is being fed from both sides: founders who can\u2019t access capital, and "
        "communities locked out of private investment.",
        MARGIN, y, uw, "Helvetica", 7, CREAM, 9.5)

    # Citation
    c.setFont("Helvetica", 5.5)
    c.setFillColor(TAN)
    c.drawString(MARGIN, y - 1, "*Source: HBCU VC \u2014 Q2 2025 Black Venture Funding Report (hbcu.vc)")
    y -= 12

    # ── THE SOLUTION ──
    section_head(c, "THE SOLUTION", y)
    y -= 11
    y = wrap_text(c,
        "Sengo is a platform reimagining fundraising and investing through community, education, "
        "and access. We help people make investments in private companies, and we help founders "
        "package themselves to receive them. Other platforms service transactions or provide "
        "one-sided support. Sengo builds economies\u2014transforming social capital into financial capital.",
        MARGIN, y, uw, "Helvetica", 7, CREAM, 9.5)

    # ── HEADLINE IMPACT ──
    y -= 6
    divider(c, y, uw)
    y -= 13
    section_head(c, "HEADLINE IMPACT", y)

    y -= 4
    stats = [
        ("600+", "Members"),
        ("9,500+", "Email\nSubscribers"),
        ("$32,150", "Grants\nDeployed"),
        ("$5M+", "Follow-on\nCapital"),
        ("19", "Founders\nFunded"),
        ("30+", "Events\nHosted"),
    ]
    stat_w = uw / len(stats)
    stat_h = 42
    # Draw boxes downward from current y
    box_top = y
    box_bot = box_top - stat_h
    for i, (num, label) in enumerate(stats):
        sx = MARGIN + i * stat_w
        rrect(c, sx + 2, box_bot, stat_w - 4, stat_h, 5, LIGHT_TEAL)
        c.setFont("Helvetica-Bold", 13)
        c.setFillColor(ORANGE)
        c.drawCentredString(sx + stat_w / 2, box_top - 16, num)
        c.setFont("Helvetica", 6)
        c.setFillColor(CREAM)
        lines = label.split('\n')
        sly = box_top - 28
        for line in lines:
            c.drawCentredString(sx + stat_w / 2, sly, line)
            sly -= 7.5
    y = box_bot

    # ── TWO-COLUMN SECTION ──
    y -= 8
    divider(c, y, uw)

    col_w = (uw - 14) / 2
    left_x = MARGIN
    right_x = MARGIN + col_w + 14
    col_top = y

    # LEFT: Traction + Market
    ly = col_top - 13
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(ORANGE)
    c.drawString(left_x, ly, "TRACTION")
    ly -= 11

    traction = [
        "9,500+ email list built organically (4x industry open rate)",
        "$32,150 in grants deployed to underrepresented founders",
        "167x multiplier: grants given \u2192 funds raised by winners",
        "$200K revenue milestone within 365 days of MVP launch",
        "90,678 emails delivered in 2025 with 46.5% open rate",
    ]
    for item in traction:
        c.setFillColor(ORANGE)
        c.setFont("Helvetica", 7)
        c.drawString(left_x + 3, ly, "\u2022")
        ly = wrap_text(c, item, left_x + 12, ly, col_w - 12, "Helvetica", 6.5, CREAM, 8.5)
        ly -= 2

    ly -= 5
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(ORANGE)
    c.drawString(left_x, ly, "MARKET OPPORTUNITY")
    ly -= 11

    market = [
        "Private markets projected to exceed $23T in next two years",
        "US crowdfunding & alt investing to exceed $10B annually",
        "49M Americans eligible to invest in private companies",
    ]
    for item in market:
        c.setFillColor(ORANGE)
        c.setFont("Helvetica", 7)
        c.drawString(left_x + 3, ly, "\u2022")
        ly = wrap_text(c, item, left_x + 12, ly, col_w - 12, "Helvetica", 6.5, CREAM, 8.5)
        ly -= 2

    # RIGHT: How It Works + Revenue
    ry = col_top - 13
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(ORANGE)
    c.drawString(right_x, ry, "HOW IT WORKS")
    ry -= 4

    pillars = [
        ("Readiness Technology", "Fundraise Readiness Score + Personalized Roadmap"),
        ("Human Support", "1:1 advisory at key inflection points"),
        ("Community Layer", "Education, events, peer learning, and access"),
        ("Grant Programs", "Non-dilutive capital to support founder readiness"),
    ]
    pill_h = 20
    for title, desc in pillars:
        pill_top = ry
        pill_bot = ry - pill_h
        rrect(c, right_x, pill_bot, col_w, pill_h, 4, LIGHT_TEAL)
        c.setFillColor(ORANGE)
        c.rect(right_x, pill_bot, 2, pill_h, fill=1, stroke=0)
        c.setFont("Helvetica-Bold", 6.5)
        c.setFillColor(WHITE)
        c.drawString(right_x + 7, pill_top - 9, title)
        c.setFont("Helvetica", 6)
        c.setFillColor(CREAM)
        c.drawString(right_x + 7, pill_top - 18, desc)
        ry -= pill_h + 4

    ry -= 5
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(ORANGE)
    c.drawString(right_x, ry, "REVENUE MODEL")
    ry -= 4

    revenue = [
        ("Subscriptions", "Monthly app access for founders & investors"),
        ("Monthly Retainers", "High-touch support for founders raising capital"),
        ("B2B Partners", "Institutions pay for deal flow & programming"),
    ]
    for title, desc in revenue:
        pill_top = ry
        pill_bot = ry - pill_h
        rrect(c, right_x, pill_bot, col_w, pill_h, 4, LIGHT_TEAL)
        c.setFillColor(ORANGE)
        c.rect(right_x, pill_bot, 2, pill_h, fill=1, stroke=0)
        c.setFont("Helvetica-Bold", 6.5)
        c.setFillColor(WHITE)
        c.drawString(right_x + 7, pill_top - 9, title)
        c.setFont("Helvetica", 6)
        c.setFillColor(CREAM)
        c.drawString(right_x + 7, pill_top - 18, desc)
        ry -= pill_h + 4

    # ── CASE STUDY SPOTLIGHT ──
    cs_y = min(ly, ry) - 6
    divider(c, cs_y, uw)
    cs_y -= 13
    section_head(c, "CASE STUDY SPOTLIGHT", cs_y)

    cs_y -= 4
    case_w = (uw - 10) / 2
    case_h = 56
    case_top = cs_y
    case_bot = cs_y - case_h

    photo_r = 18  # headshot circle radius
    text_indent = photo_r * 2 + 12  # text starts after photo circle

    # Satlyt — Rama Afullo
    rrect(c, MARGIN, case_bot, case_w, case_h, 5, LIGHT_TEAL)
    # Headshot circle
    rama_path = os.path.join(BASE_DIR, '1708410857908.jpg')
    photo_cx = MARGIN + 7 + photo_r
    photo_cy = case_top - photo_r - 4
    c.saveState()
    p = c.beginPath()
    p.circle(photo_cx, photo_cy, photo_r)
    p.close()
    c.clipPath(p, stroke=0)
    if os.path.exists(rama_path):
        c.drawImage(ImageReader(rama_path),
                     photo_cx - photo_r, photo_cy - photo_r,
                     width=photo_r * 2, height=photo_r * 2)
    c.restoreState()
    # Orange circle border
    c.setStrokeColor(ORANGE)
    c.setLineWidth(1.5)
    c.circle(photo_cx, photo_cy, photo_r, fill=0, stroke=1)

    tx1 = MARGIN + text_indent
    c.setFont("Helvetica-Bold", 7.5)
    c.setFillColor(ORANGE)
    c.drawString(tx1, case_top - 10, "Satlyt \u2014 Rama Afullo")
    c.setFont("Helvetica", 6)
    c.setFillColor(CREAM)
    c.drawString(tx1, case_top - 20, "Former SpaceX, Tesla & Google")
    c.drawString(tx1, case_top - 29, "Satellites \u2192 virtual data centers. $3K grant.")
    c.setFont("Helvetica-Bold", 6.5)
    c.setFillColor(ORANGE)
    c.drawString(MARGIN + 7, case_top - 46, "$3M raised post-Sengo  \u00b7  12 new hires  \u00b7  10 customers")

    # Versed Wellness — Jasmine Bowie
    rx2 = MARGIN + case_w + 10
    rrect(c, rx2, case_bot, case_w, case_h, 5, LIGHT_TEAL)
    # Headshot circle
    jasmine_path = os.path.join(BASE_DIR, 'Headshot 1.jpg')
    photo_cx2 = rx2 + 7 + photo_r
    photo_cy2 = case_top - photo_r - 4
    c.saveState()
    p2 = c.beginPath()
    p2.circle(photo_cx2, photo_cy2, photo_r)
    p2.close()
    c.clipPath(p2, stroke=0)
    if os.path.exists(jasmine_path):
        # Portrait photo (0.69:1) — fill circle width, let height overflow and clip
        img_draw_w = photo_r * 2
        img_draw_h = img_draw_w * (1542 / 1064)  # preserve aspect ratio
        # Center vertically, shift up slightly to show face
        img_y_offset = (img_draw_h - photo_r * 2) * 0.65
        c.drawImage(ImageReader(jasmine_path),
                     photo_cx2 - photo_r, photo_cy2 - photo_r - img_y_offset,
                     width=img_draw_w, height=img_draw_h)
    c.restoreState()
    c.setStrokeColor(ORANGE)
    c.setLineWidth(1.5)
    c.circle(photo_cx2, photo_cy2, photo_r, fill=0, stroke=1)

    tx2 = rx2 + text_indent
    c.setFont("Helvetica-Bold", 7.5)
    c.setFillColor(ORANGE)
    c.drawString(tx2, case_top - 10, "Versed Wellness \u2014 Jasmine Bowie")
    c.setFont("Helvetica", 6)
    c.setFillColor(CREAM)
    c.drawString(tx2, case_top - 20, "Concept to physical prototype. $500 Micro-Grant.")
    c.drawString(tx2, case_top - 29, "Chose not to raise prematurely\u2014readiness first.")
    c.setFont("Helvetica-Bold", 6.5)
    c.setFillColor(ORANGE)
    c.drawString(rx2 + 7, case_top - 46, "25 new customers  \u00b7  Revenue increased post-grant")
    cs_y = case_bot

    # ── PHOTOS ──
    img_y = cs_y - 10
    img_h = 90
    img_w = (uw - 10) / 2
    photo1_path = os.path.join(BASE_DIR, 'Conf-19.jpg')
    photo2_path = os.path.join(BASE_DIR, 'IMG_4246.JPG')

    if os.path.exists(photo1_path):
        c.drawImage(ImageReader(photo1_path),
                     MARGIN, img_y - img_h,
                     width=img_w, height=img_h,
                     preserveAspectRatio=True, mask='auto')
    if os.path.exists(photo2_path):
        c.drawImage(ImageReader(photo2_path),
                     MARGIN + img_w + 10, img_y - img_h,
                     width=img_w, height=img_h,
                     preserveAspectRatio=True, mask='auto')
    # ── FOOTER ──
    fy = img_y - img_h - 10
    c.setFont("Helvetica-Bold", 7.5)
    c.setFillColor(ORANGE)
    c.drawString(MARGIN, fy, "Get Involved:")
    c.setFont("Helvetica", 6.5)
    c.setFillColor(CREAM)
    c.drawString(MARGIN + 55, fy, "bysengo.com  \u00b7  hello@bysengo.com  \u00b7  Join the community  \u00b7  Invest  \u00b7  Partner with us")

    fy -= 12
    c.setFont("Helvetica", 5.5)
    c.setFillColor(TAN)
    c.drawCentredString(PAGE_W / 2, fy,
                        "Sengo  \u00b7  Founded by Ila B Corcoran  \u00b7  Capital access democratized.  \u00b7  Last updated February 2026")

    c.save()
    print(f"One-pager saved to {OUTPUT}")


if __name__ == '__main__':
    build()
