#!/usr/bin/env python3
"""Generate Sengo one-pager PDF combining impact data and pitch narrative."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os
import io
import qrcode

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
MARGIN = 0.45 * inch
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(BASE_DIR, 'Sengo_One_Pager.pdf')


def rounded_rect(c, x, y, w, h, r, fill_color):
    c.setFillColor(fill_color)
    c.roundRect(x, y, w, h, r, fill=1, stroke=0)


def draw_text_wrapped(c, text, x, y, max_width, font="Helvetica", size=8, color=CREAM, leading=11):
    """Simple word-wrap text drawing. Returns final y position."""
    c.setFont(font, size)
    c.setFillColor(color)
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        test = current_line + (" " if current_line else "") + word
        if c.stringWidth(test, font, size) <= max_width:
            current_line = test
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    for line in lines:
        c.drawString(x, y, line)
        y -= leading
    return y


def build():
    c = canvas.Canvas(OUTPUT, pagesize=(PAGE_W, PAGE_H))
    c.setTitle("Sengo One Pager")

    usable_w = PAGE_W - 2 * MARGIN

    # ── BACKGROUND ──
    c.setFillColor(TEAL)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    # Orange top bar
    c.setFillColor(ORANGE)
    c.rect(0, PAGE_H - 4, PAGE_W, 4, fill=1, stroke=0)

    # ── HEADER: Logo + tagline ──
    logo_path = os.path.join(BASE_DIR, 'Sengo 2.PNG')
    logo_w, logo_h = 100, 67
    c.drawImage(ImageReader(logo_path),
                MARGIN, PAGE_H - 68,
                width=logo_w, height=logo_h, mask='auto')

    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(ORANGE)
    c.drawString(MARGIN + logo_w + 10, PAGE_H - 28, "REIMAGINING FUNDRAISING & INVESTING")
    c.setFont("Helvetica", 7.5)
    c.setFillColor(CREAM)
    c.drawString(MARGIN + logo_w + 10, PAGE_H - 40, "Through community, education, and access")
    c.setFont("Helvetica", 7)
    c.setFillColor(TAN)
    c.drawString(MARGIN + logo_w + 10, PAGE_H - 52, "Founded by Ila B Corcoran  |  bysengo.com")

    # Right side: year badge
    badge_w, badge_h = 65, 22
    badge_x = PAGE_W - MARGIN - badge_w
    badge_y = PAGE_H - 38
    rounded_rect(c, badge_x, badge_y, badge_w, badge_h, 6, ORANGE)
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(WHITE)
    c.drawCentredString(badge_x + badge_w / 2, badge_y + 7, "2025")

    # ── DIVIDER ──
    y = PAGE_H - 76
    c.setFillColor(ORANGE)
    c.rect(MARGIN, y, usable_w, 2, fill=1, stroke=0)

    # ── WHAT IS SENGO (origin story + mission) ──
    y -= 16
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(ORANGE)
    c.drawString(MARGIN, y, "THE PROBLEM")

    y -= 13
    y = draw_text_wrapped(c,
        "Despite 97% of the US population being technically eligible to invest in private assets\u2014"
        "the fastest-growing asset class\u2014less than 2% actually do. Meanwhile, less than 0.5% "
        "of Black founders received venture capital in Q2 2024. A $14 trillion wealth gap is being "
        "fed from both sides: founders who can\u2019t access capital, and communities locked out of "
        "private investment.",
        MARGIN, y, usable_w, "Helvetica", 7.5, CREAM, 10)

    y -= 8
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(ORANGE)
    c.drawString(MARGIN, y, "THE SOLUTION")

    y -= 13
    y = draw_text_wrapped(c,
        "Sengo is a platform reimagining fundraising and investing through community, education, "
        "and access. We help people make investments in private companies, and we help founders "
        "package themselves to receive them. Other platforms service transactions or provide "
        "one-sided support. Sengo builds economies\u2014transforming social capital into financial capital.",
        MARGIN, y, usable_w, "Helvetica", 7.5, CREAM, 10)

    # ── HEADLINE IMPACT STATS ──
    y -= 12
    c.setFillColor(ORANGE)
    c.rect(MARGIN, y, usable_w, 2, fill=1, stroke=0)
    y -= 14
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(ORANGE)
    c.drawString(MARGIN, y, "2025 HEADLINE IMPACT")

    y -= 18
    stats = [
        ("600+", "Members"),
        ("8,000+", "Email\nSubscribers"),
        ("$31,250", "Grants\nDeployed"),
        ("$5M+", "Follow-on\nCapital"),
        ("18", "Founders\nFunded"),
        ("29", "Events\nHosted"),
    ]
    stat_w = usable_w / len(stats)
    for i, (num, label) in enumerate(stats):
        sx = MARGIN + i * stat_w
        rounded_rect(c, sx + 2, y - 2, stat_w - 4, 48, 6, LIGHT_TEAL)
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(ORANGE)
        c.drawCentredString(sx + stat_w / 2, y + 26, num)
        c.setFont("Helvetica", 6.5)
        c.setFillColor(CREAM)
        lines = label.split('\n')
        ly = y + 12
        for line in lines:
            c.drawCentredString(sx + stat_w / 2, ly, line)
            ly -= 8

    # ── TWO-COLUMN SECTION ──
    y -= 62
    c.setFillColor(ORANGE)
    c.rect(MARGIN, y, usable_w, 2, fill=1, stroke=0)

    col_w = (usable_w - 16) / 2
    left_x = MARGIN
    right_x = MARGIN + col_w + 16

    # LEFT COLUMN: Traction + Market
    ly = y - 14
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(ORANGE)
    c.drawString(left_x, ly, "TRACTION")
    ly -= 12

    traction_items = [
        "8,000+ email list built organically (4x industry open rate)",
        "$30,000+ in grants deployed in 2025",
        "167x multiplier: grants given \u2192 funds raised by winners",
        "$200K revenue milestone within 365 days of MVP launch",
        "90,678 emails delivered with 46.5% open rate",
    ]
    for item in traction_items:
        c.setFillColor(ORANGE)
        c.drawString(left_x + 4, ly, "\u2022")
        ly = draw_text_wrapped(c, item, left_x + 14, ly, col_w - 14,
                               "Helvetica", 7, CREAM, 9.5)
        ly -= 2

    ly -= 6
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(ORANGE)
    c.drawString(left_x, ly, "MARKET OPPORTUNITY")
    ly -= 12

    market_items = [
        "Private markets projected to exceed $23T in next two years",
        "US crowdfunding & alternative investing to exceed $10B annually",
        "49M Americans eligible to invest in private companies",
    ]
    for item in market_items:
        c.setFillColor(ORANGE)
        c.drawString(left_x + 4, ly, "\u2022")
        ly = draw_text_wrapped(c, item, left_x + 14, ly, col_w - 14,
                               "Helvetica", 7, CREAM, 9.5)
        ly -= 2

    # RIGHT COLUMN: How It Works + Revenue Model
    ry = y - 14
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(ORANGE)
    c.drawString(right_x, ry, "HOW IT WORKS")
    ry -= 14

    pillars = [
        ("Readiness Technology", "Fundraise Readiness Score + Personalized Roadmap"),
        ("Human Support", "1:1 advisory at key inflection points"),
        ("Community Layer", "Education, events, peer learning, and access"),
        ("Grant Programs", "Non-dilutive capital to support founder readiness"),
    ]
    for title, desc in pillars:
        rounded_rect(c, right_x, ry - 2, col_w, 22, 4, LIGHT_TEAL)
        c.setFillColor(ORANGE)
        c.rect(right_x, ry - 2, 2, 22, fill=1, stroke=0)
        c.setFont("Helvetica-Bold", 7)
        c.setFillColor(WHITE)
        c.drawString(right_x + 8, ry + 8, title)
        c.setFont("Helvetica", 6.5)
        c.setFillColor(CREAM)
        c.drawString(right_x + 8, ry - 1, desc)
        ry -= 28

    ry -= 6
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(ORANGE)
    c.drawString(right_x, ry, "REVENUE MODEL")
    ry -= 14

    revenue = [
        ("Subscriptions", "Monthly app access for founders & investors"),
        ("Monthly Retainers", "High-touch support for founders raising capital"),
        ("B2B Partners", "Institutions pay for deal flow & programming"),
    ]
    for title, desc in revenue:
        rounded_rect(c, right_x, ry - 2, col_w, 22, 4, LIGHT_TEAL)
        c.setFillColor(ORANGE)
        c.rect(right_x, ry - 2, 2, 22, fill=1, stroke=0)
        c.setFont("Helvetica-Bold", 7)
        c.setFillColor(WHITE)
        c.drawString(right_x + 8, ry + 8, title)
        c.setFont("Helvetica", 6.5)
        c.setFillColor(CREAM)
        c.drawString(right_x + 8, ry - 1, desc)
        ry -= 28

    # ── CASE STUDY SPOTLIGHT ──
    cs_y = min(ly, ry) - 10
    c.setFillColor(ORANGE)
    c.rect(MARGIN, cs_y, usable_w, 2, fill=1, stroke=0)
    cs_y -= 14
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(ORANGE)
    c.drawString(MARGIN, cs_y, "CASE STUDY SPOTLIGHT")

    cs_y -= 10
    case_w = (usable_w - 12) / 2
    case_h = 62

    # Case 1: Satlyt
    rounded_rect(c, MARGIN, cs_y - case_h, case_w, case_h, 6, LIGHT_TEAL)
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(ORANGE)
    c.drawString(MARGIN + 8, cs_y - 12, "Satlyt \u2014 Rama Afullo")
    c.setFont("Helvetica", 6.5)
    c.setFillColor(CREAM)
    c.drawString(MARGIN + 8, cs_y - 23, "Former SpaceX, Tesla & Google \u2014 building software that turns")
    c.drawString(MARGIN + 8, cs_y - 32, "satellites into virtual data centers. $3,000 Standard Grant.")
    c.setFont("Helvetica-Bold", 7)
    c.setFillColor(ORANGE)
    c.drawString(MARGIN + 8, cs_y - 46, "$3M raised post-Sengo  \u00b7  12 new hires  \u00b7  10 new customers")

    # Case 2: Versed Wellness
    rounded_rect(c, MARGIN + case_w + 12, cs_y - case_h, case_w, case_h, 6, LIGHT_TEAL)
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(ORANGE)
    c.drawString(MARGIN + case_w + 20, cs_y - 12, "Versed Wellness \u2014 Jasmine Bowie")
    c.setFont("Helvetica", 6.5)
    c.setFillColor(CREAM)
    c.drawString(MARGIN + case_w + 20, cs_y - 23, "Concept to physical prototype. $500 Micro-Grant.")
    c.drawString(MARGIN + case_w + 20, cs_y - 32, "Chose not to raise capital prematurely\u2014readiness first.")
    c.setFont("Helvetica-Bold", 7)
    c.setFillColor(ORANGE)
    c.drawString(MARGIN + case_w + 20, cs_y - 46, "25 new customers  \u00b7  Revenue increased post-grant")

    # ── BOTTOM CALLOUT BAR ──
    bar_y = cs_y - case_h - 16
    rounded_rect(c, MARGIN, bar_y, usable_w, 24, 6, ORANGE)
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(WHITE)
    c.drawCentredString(PAGE_W / 2, bar_y + 8,
                        "\"You can\u2019t expect to hit the jackpot if you don\u2019t put a few nickels in the machine.\" \u2014 Flip Wilson")

    # ── FOOTER ──
    bar_y -= 20
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(ORANGE)
    c.drawString(MARGIN, bar_y, "Get Involved:")
    c.setFont("Helvetica", 7)
    c.setFillColor(CREAM)
    c.drawString(MARGIN + 62, bar_y, "bysengo.com  \u00b7  hello@bysengo.com  \u00b7  Join the community  \u00b7  Invest  \u00b7  Partner with us")

    c.setFont("Helvetica", 6)
    c.setFillColor(TAN)
    c.drawCentredString(PAGE_W / 2, bar_y - 14,
                        "Sengo  \u00b7  Founded by Ila B Corcoran  \u00b7  2025  \u00b7  Capital access democratized.")

    c.save()
    print(f"One-pager saved to {OUTPUT}")


if __name__ == '__main__':
    build()
