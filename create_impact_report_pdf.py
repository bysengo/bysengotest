#!/usr/bin/env python3
"""Generate Sengo 2025 Impact Report as a PDF."""

from reportlab.lib.pagesizes import landscape
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import math
import os
import io
import qrcode
import cairosvg
from PIL import Image as PILImage
from reportlab.lib.utils import ImageReader

# Brand colors
TEAL = HexColor('#1B3533')
LIGHT_TEAL = HexColor('#244A47')
ORANGE = HexColor('#D57028')
CREAM = HexColor('#F3EDE7')
TAN = HexColor('#AF8145')
OLIVE = HexColor('#717E36')
WHITE = HexColor('#FFFFFF')
BROWN = HexColor('#67441A')

PAGE_W, PAGE_H = landscape((11 * inch, 8.5 * inch))
MARGIN = 0.6 * inch

OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Sengo_2025_Impact_Report.pdf')


class SlideDeck:
    def __init__(self, filename):
        self.filename = filename
        self.c = canvas.Canvas(filename, pagesize=(PAGE_W, PAGE_H))
        self.c.setTitle("Sengo 2025 Impact Report")
        self.page_num = 0

    def _bg(self, color):
        self.c.setFillColor(color)
        self.c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    def _orange_bar(self):
        self.c.setFillColor(ORANGE)
        self.c.rect(0, PAGE_H - 4, PAGE_W, 4, fill=1, stroke=0)

    def _accent_line(self, y):
        self.c.setFillColor(ORANGE)
        self.c.rect(PAGE_W / 2 - 40, y, 80, 3, fill=1, stroke=0)

    def _section_label(self, text, y, color=ORANGE):
        self.c.setFont("Helvetica-Bold", 10)
        self.c.setFillColor(color)
        self.c.drawCentredString(PAGE_W / 2, y, text.upper())

    def _title(self, text, y, size=30, color=WHITE):
        self.c.setFont("Helvetica-Bold", size)
        self.c.setFillColor(color)
        self.c.drawCentredString(PAGE_W / 2, y, text)

    def _body_center(self, text, y, size=12, color=CREAM, max_width=None):
        self.c.setFont("Helvetica", size)
        self.c.setFillColor(color)
        self.c.drawCentredString(PAGE_W / 2, y, text)

    def _rounded_rect(self, x, y, w, h, r, fill_color):
        self.c.setFillColor(fill_color)
        self.c.roundRect(x, y, w, h, r, fill=1, stroke=0)

    def _new_page(self):
        if self.page_num > 0:
            self.c.showPage()
        self.page_num += 1

    # ---- SLIDES ----

    def slide_hero(self):
        self._new_page()
        self._bg(TEAL)
        self._orange_bar()
        # Sengo logo from uploaded PNG
        logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'SENGO.PNG')
        logo_w, logo_h = 200, 134  # maintain aspect ratio (1685:1124 ≈ 1.5:1)
        self.c.drawImage(ImageReader(logo_path),
                         PAGE_W / 2 - logo_w / 2, PAGE_H - 210,
                         width=logo_w, height=logo_h, mask='auto')
        self.c.setFont("Helvetica-Bold", 44)
        self.c.setFillColor(WHITE)
        self.c.drawCentredString(PAGE_W / 2, PAGE_H - 240, "Impact Report 2025")
        self._accent_line(PAGE_H - 260)
        self.c.setFont("Helvetica", 16)
        self.c.setFillColor(CREAM)
        self.c.drawCentredString(PAGE_W / 2, PAGE_H - 295, "Reimagining fundraising and investing through education, community, and access.")
        self.c.setFont("Helvetica", 12)
        self.c.setFillColor(TAN)
        self.c.drawCentredString(PAGE_W / 2, PAGE_H - 320, "Building informed founders, prepared funders, and durable ecosystems")
        self.c.setFont("Helvetica", 9)
        self.c.setFillColor(TAN)
        self.c.drawCentredString(PAGE_W / 2, PAGE_H - 400, "Founded by Ila B Corcoran  |  2025 Year in Review")

    def slide_overview(self):
        self._new_page()
        self._bg(CREAM)
        self._orange_bar()
        self._section_label("Year in Review", PAGE_H - 80)
        self._title("From Experimentation to Infrastructure", PAGE_H - 120, size=28, color=TEAL)
        self._accent_line(PAGE_H - 135)

        items = [
            "2025 marked Sengo\u2019s official platform launch and first grant cycle",
            "Transitioned from research and pilots (2024) to repeatable, technology-enabled programs",
            "Introduced readiness tools that help founders assess, prepare, and decide if and when to raise",
            "Served founders, funders, and partners across the U.S. and internationally",
        ]
        y = PAGE_H - 175
        for item in items:
            self._rounded_rect(MARGIN + 40, y - 5, PAGE_W - 2 * MARGIN - 80, 28, 6, TEAL)
            self.c.setFillColor(ORANGE)
            self.c.rect(MARGIN + 40, y - 5, 3, 28, fill=1, stroke=0)
            self.c.setFont("Helvetica", 11)
            self.c.setFillColor(CREAM)
            self.c.drawString(MARGIN + 55, y + 5, item)
            y -= 38

        # Callout bar
        bw = PAGE_W - 2 * MARGIN - 80
        bx = (PAGE_W - bw) / 2
        self._rounded_rect(bx, y - 15, bw, 32, 6, ORANGE)
        self.c.setFont("Helvetica-Bold", 12)
        self.c.setFillColor(WHITE)
        self.c.drawCentredString(PAGE_W / 2, y - 3, 'Core shift: From "access to capital" \u2192 readiness for capital')

    def slide_headline_impact(self):
        self._new_page()
        self._bg(TEAL)
        self._orange_bar()
        self._section_label("Key Metrics", PAGE_H - 80)
        self._title("Headline Impact", PAGE_H - 120, size=28)
        self._accent_line(PAGE_H - 135)

        stats = [
            ("600+", "Members across Explorer,\nFounder, Funder &\nAll-Access tiers"),
            ("8,000+", "Email subscribers\n(from 157 in Jan 2025)"),
            ("$31,250", "Grants deployed to\nunderrepresented founders"),
            ("$5M+", "Follow-on capital\ninfluenced by\nsupported founders"),
            ("29", "Events hosted\nglobally"),
        ]
        card_w = 140
        gap = 14
        total_w = len(stats) * card_w + (len(stats) - 1) * gap
        sx = (PAGE_W - total_w) / 2
        y = PAGE_H - 280

        for i, (num, label) in enumerate(stats):
            x = sx + i * (card_w + gap)
            self._rounded_rect(x, y, card_w, 110, 8, LIGHT_TEAL)
            self.c.setFont("Helvetica-Bold", 24)
            self.c.setFillColor(ORANGE)
            self.c.drawCentredString(x + card_w / 2, y + 78, num)
            self.c.setFont("Helvetica", 9)
            self.c.setFillColor(CREAM)
            lines = label.split('\n')
            ly = y + 55
            for line in lines:
                self.c.drawCentredString(x + card_w / 2, ly, line)
                ly -= 12

    def slide_charts(self):
        self._new_page()
        self._bg(TEAL)
        self._orange_bar()
        self._section_label("Data & Trends", PAGE_H - 80)
        self._title("Charts & Breakdown", PAGE_H - 120, size=28)
        self._accent_line(PAGE_H - 135)

        # Donut chart (left)
        cx_donut = PAGE_W * 0.3
        cy_donut = PAGE_H - 280
        r_outer = 65
        r_inner = 33

        segments = [
            (0, 276.5, ORANGE, "Standard Grants 76.8%"),
            (276.5, 319.7, OLIVE, "Pitch Competition 12.0%"),
            (319.7, 360, TAN, "Micro/Mini Grants 11.2%"),
        ]
        for start_deg, end_deg, color, _ in segments:
            self.c.setFillColor(color)
            self.c.wedge(cx_donut - r_outer, cy_donut - r_outer, cx_donut + r_outer, cy_donut + r_outer,
                         90 - end_deg, end_deg - start_deg, fill=1, stroke=0)
        self.c.setFillColor(TEAL)
        self.c.circle(cx_donut, cy_donut, r_inner, fill=1, stroke=0)

        self.c.setFont("Helvetica-Bold", 12)
        self.c.setFillColor(WHITE)
        self.c.drawCentredString(cx_donut, PAGE_H - 185, "Grant Deployment Breakdown")

        # Legend
        ly = cy_donut - r_outer - 20
        for _, _, color, label in segments:
            self.c.setFillColor(color)
            self.c.rect(cx_donut - 70, ly - 2, 10, 10, fill=1, stroke=0)
            self.c.setFont("Helvetica", 9)
            self.c.setFillColor(CREAM)
            self.c.drawString(cx_donut - 55, ly, label)
            ly -= 16

        # Bar chart (right)
        bx_center = PAGE_W * 0.7
        self.c.setFont("Helvetica-Bold", 12)
        self.c.setFillColor(WHITE)
        self.c.drawCentredString(bx_center, PAGE_H - 185, "Programming Mix")

        bars = [("Virtual", 55.2, 120), ("In-Person", 44.8, 97)]
        bar_w = 70
        bar_gap = 40
        bx_start = bx_center - (2 * bar_w + bar_gap) / 2
        base_y = PAGE_H - 380

        for i, (label, val, h) in enumerate(bars):
            x = bx_start + i * (bar_w + bar_gap)
            self.c.setFillColor(ORANGE)
            self.c.roundRect(x, base_y, bar_w, h, 4, fill=1, stroke=0)
            self.c.setFont("Helvetica-Bold", 11)
            self.c.setFillColor(ORANGE)
            self.c.drawCentredString(x + bar_w / 2, base_y + h + 6, f"{val}%")
            self.c.setFont("Helvetica-Bold", 10)
            self.c.setFillColor(CREAM)
            self.c.drawCentredString(x + bar_w / 2, base_y - 16, label)

        # Engagement note
        self.c.setFont("Helvetica-Oblique", 9)
        self.c.setFillColor(CREAM)
        self.c.drawCentredString(PAGE_W / 2, PAGE_H - 430,
                                 "Strong engagement across programs")

    def slide_email_data(self):
        self._new_page()
        self._bg(TEAL)
        self._orange_bar()
        self._section_label("Data & Trends", PAGE_H - 80)
        self._title("Charts & Breakdown (Continued)", PAGE_H - 120, size=28)
        self._accent_line(PAGE_H - 135)

        self.c.setFont("Helvetica", 12)
        self.c.setFillColor(CREAM)
        self.c.drawCentredString(PAGE_W / 2, PAGE_H - 165, "Email engagement across 2025 campaigns")

        # Top row: 2 stats (delivered + opened)
        stats = [("90,678", "Emails Delivered"), ("42,150", "Emails Opened")]
        card_w = 200
        gap = 30
        total_w = 2 * card_w + gap
        sx = (PAGE_W - total_w) / 2
        y = PAGE_H - 280

        for i, (num, label) in enumerate(stats):
            x = sx + i * (card_w + gap)
            self._rounded_rect(x, y, card_w, 85, 8, LIGHT_TEAL)
            self.c.setFont("Helvetica-Bold", 28)
            self.c.setFillColor(ORANGE)
            self.c.drawCentredString(x + card_w / 2, y + 48, num)
            self.c.setFont("Helvetica", 11)
            self.c.setFillColor(CREAM)
            self.c.drawCentredString(x + card_w / 2, y + 22, label)

        # Open rate highlight
        ow = 200
        ox = (PAGE_W - ow) / 2
        oy = y - 80
        self._rounded_rect(ox, oy, ow, 60, 8, LIGHT_TEAL)
        self.c.setFont("Helvetica-Bold", 30)
        self.c.setFillColor(ORANGE)
        self.c.drawCentredString(PAGE_W / 2, oy + 28, "46.5%")
        self.c.setFont("Helvetica", 10)
        self.c.setFillColor(CREAM)
        self.c.drawCentredString(PAGE_W / 2, oy + 8, "Open Rate")

        self.c.setFont("Helvetica-Oblique", 9)
        self.c.setFillColor(CREAM)
        self.c.drawCentredString(PAGE_W / 2, oy - 22,
                                 "Open rate significantly above the industry average of ~21.33%*")

        # Citation
        self.c.setFont("Helvetica", 7)
        self.c.setFillColor(TAN)
        self.c.drawCentredString(PAGE_W / 2, oy - 40,
                                 "*Source: Mailchimp Email Marketing Benchmarks, 2024 \u2014 average open rate across all industries: 21.33%")

    def slide_events(self):
        self._new_page()
        self._bg(CREAM)
        self._orange_bar()
        self._section_label("29 Touchpoints", PAGE_H - 60)
        self._title("Events for Learning, Alignment & Trust", PAGE_H - 90, size=22, color=TEAL)
        self._accent_line(PAGE_H - 102)

        # (text, is_partner)
        virtual = [
            ("Welcome to Sengo Webinar \u2014 May 21", False),
            ("Debt vs. Bootstrapping with IFundWomen \u2014 Jun 3", True),
            ("Debt vs. Bootstrapping with IFundWomen \u2014 Jul 15", True),
            ("Founder Meetup: Social Enterprise \u2014 Jul 22", False),
            ("Ask an Angel with Mandy Bynum \u2014 Jul 31", False),
            ("Practice Your Pitch with Sarah Anto \u2014 Aug 12", False),
            ("Preparing to Raise Capital with Forecastr \u2014 Sep 4", False),
            ("Private Markets 101 (Part 1) \u2014 Sep 9", False),
            ("Founder Meetup: Angels & VCs \u2014 Sep 18", False),
            ("Virtual Pitch for $1,000 \u2014 Sep 25", False),
            ("Demystifying CDFI Funding with Isaiah Coleman \u2014 Oct 14", False),
            ("Pitch Prep with Amiah Shepherd \u2014 Oct 23", False),
            ("Virtual Pitch for $1,000 \u2014 Oct 30", False),
            ("Virtual Pitch for $1,000 (CPG Edition) \u2014 Nov 20", False),
            ("Building to Scale/Sell with Brianna Arps \u2014 Dec 4", False),
            ("Build 2026 Pitch Strategy with Dana Ammons \u2014 Dec 11", False),
        ]
        inperson = [
            "Dallas Galentine's Wine Club \u2014 Feb 21",
            "Barcelona, Spain Entrepreneurs Mixer \u2014 Mar 13",
            "Dallas Brunch Wine Club \u2014 Mar 15",
            "San Bernardino Founder/Funder Fireside \u2014 Mar 28",
            "Dallas Sip Into Spring \u2014 Mar 30",
            "Dallas Wine Club \u2014 Apr 9",
            "San Bernardino Funded & Fearless Workshop \u2014 Apr 26",
            "NYC GirlMath x Sengo at NY Tech Week \u2014 Jun 4",
            "Massaguel, France \u201cThe Village Retreat\u201d \u2014 Jun 10\u201315",
            "Los Angeles Fashion x Futures \u2014 Jun 28\u201329",
            "New York Fashion x Futures \u2014 Jul 26\u201327",
            "Los Angeles Spill the Tea: AI & Tech Week \u2014 Oct 14",
            "Los Angeles Fashion x Futures \u2014 Nov 8\u20139",
        ]

        col_x_left = MARGIN + 20
        col_x_right = PAGE_W / 2 + 10
        y_start = PAGE_H - 125

        self.c.setFont("Helvetica-Bold", 10)
        self.c.setFillColor(ORANGE)
        self.c.drawString(col_x_left, y_start, "Virtual Events (14 + 2 partner)")
        self.c.drawString(col_x_right, y_start, "In-Person Events (13)")

        # Virtual events (left column)
        y = y_start - 20
        for ev_text, is_partner in virtual:
            bg_color = OLIVE if is_partner else TEAL
            border_color = OLIVE if is_partner else ORANGE
            self._rounded_rect(col_x_left, y - 3, PAGE_W / 2 - MARGIN - 40, 15, 4, bg_color)
            self.c.setFillColor(border_color)
            self.c.rect(col_x_left, y - 3, 2, 15, fill=1, stroke=0)
            self.c.setFont("Helvetica", 6.5)
            self.c.setFillColor(WHITE if is_partner else CREAM)
            self.c.drawString(col_x_left + 8, y, ev_text)
            y -= 18

        # In-person events (right column)
        y = y_start - 20
        for ev in inperson:
            self._rounded_rect(col_x_right, y - 3, PAGE_W / 2 - MARGIN - 40, 15, 4, TEAL)
            self.c.setFillColor(ORANGE)
            self.c.rect(col_x_right, y - 3, 2, 15, fill=1, stroke=0)
            self.c.setFont("Helvetica", 6.5)
            self.c.setFillColor(CREAM)
            self.c.drawString(col_x_right + 8, y, ev)
            y -= 18

        # Partners section
        self.c.setFont("Helvetica-Bold", 10)
        self.c.setFillColor(ORANGE)
        self.c.drawCentredString(PAGE_W / 2, 62, "Thank You to Our 2025 Partners and Sponsors")
        self.c.setFont("Helvetica-Oblique", 8)
        self.c.setFillColor(BROWN)
        self.c.drawCentredString(PAGE_W / 2, 46, "+ more")

        # Callout
        bw = PAGE_W - 2 * MARGIN - 60
        bx = (PAGE_W - bw) / 2
        self._rounded_rect(bx, 20, bw, 20, 6, ORANGE)
        self.c.setFont("Helvetica-Bold", 7)
        self.c.setFillColor(WHITE)
        self.c.drawCentredString(PAGE_W / 2, 26,
                                 "Key Insight: Events are most effective when they lead into readiness tools and structured next steps.")

    def slide_case_studies(self):
        self._new_page()
        self._bg(TEAL)
        self._orange_bar()
        self._section_label("Success Stories", PAGE_H - 80)
        self._title("Case Studies", PAGE_H - 120, size=28)
        self._accent_line(PAGE_H - 135)

        cases = [
            {
                "name": "Versed Wellness",
                "meta": "Founder: Jasmine Bowie | Grant: $500 Micro-Grant",
                "bullets": [
                    "Concept \u2192 physical prototype",
                    "25 new customers acquired",
                    "Revenue increased post-grant",
                    "Founder chose not to raise capital prematurely",
                ],
                "why": "Why it matters: Readiness includes knowing when not to fundraise.",
            },
            {
                "name": "Satlyt",
                "meta": "Founder: Rama Afullo | Grant: $3,000 Standard Grant",
                "bullets": [
                    "10 new customers acquired",
                    "Operational capacity expanded",
                    "$3M raised post-Sengo",
                    "12 new hires",
                ],
                "why": "Why it matters: Prepared founders convert early support into scalable outcomes.",
            },
        ]

        card_w = (PAGE_W - 2 * MARGIN - 30) / 2
        for i, case in enumerate(cases):
            x = MARGIN + i * (card_w + 30)
            y_top = PAGE_H - 160
            self._rounded_rect(x, y_top - 180, card_w, 180, 8, LIGHT_TEAL)

            self.c.setFont("Helvetica-Bold", 15)
            self.c.setFillColor(ORANGE)
            self.c.drawString(x + 14, y_top - 20, case["name"])

            self.c.setFont("Helvetica", 8)
            self.c.setFillColor(CREAM)
            self.c.drawString(x + 14, y_top - 36, case["meta"])

            by = y_top - 60
            for bullet in case["bullets"]:
                self.c.setFillColor(ORANGE)
                self.c.drawString(x + 14, by, "\u2022")
                self.c.setFont("Helvetica", 9)
                self.c.setFillColor(CREAM)
                self.c.drawString(x + 28, by, bullet)
                by -= 16

            self._rounded_rect(x + 10, by - 10, card_w - 20, 26, 5, ORANGE)
            self.c.setFont("Helvetica-Bold", 8)
            self.c.setFillColor(WHITE)
            self.c.drawCentredString(x + card_w / 2, by - 1, case["why"])

        # --- TEASER OVERLAY (remove this block after live) ---
        # Solid overlay so case study content is not readable
        self.c.saveState()
        self.c.setFillColor(HexColor('#1B3533'))
        self.c.setFillAlpha(0.92)
        self.c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
        self.c.restoreState()

        # CTA text — positioned above QR code with spacing
        self.c.setFont("Helvetica-Bold", 28)
        self.c.setFillColor(WHITE)
        self.c.drawCentredString(PAGE_W / 2, PAGE_H / 2 + 120, "Join our email list")
        self.c.drawCentredString(PAGE_W / 2, PAGE_H / 2 + 85, "for full access")

        # QR code — centered in remaining space
        qr = qrcode.QRCode(version=1, box_size=10, border=2)
        qr.add_data("https://bysengo.com")
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="#D57028", back_color="#1B3533").convert("RGB")
        buf = io.BytesIO()
        qr_img.save(buf, format="PNG")
        buf.seek(0)
        qr_size = 160
        qr_y = PAGE_H / 2 - 50
        self.c.drawImage(ImageReader(buf),
                         PAGE_W / 2 - qr_size / 2, qr_y,
                         width=qr_size, height=qr_size)

        # Border around QR
        self.c.setStrokeColor(ORANGE)
        self.c.setLineWidth(2.5)
        self.c.roundRect(PAGE_W / 2 - qr_size / 2 - 3, qr_y - 3,
                         qr_size + 6, qr_size + 6, 6, fill=0, stroke=1)

        # URL label — below QR code
        self.c.setFont("Helvetica-Bold", 16)
        self.c.setFillColor(ORANGE)
        self.c.drawCentredString(PAGE_W / 2, qr_y - 28, "bysengo.com")
        # --- END TEASER OVERLAY ---

    def slide_media_press(self):
        self._new_page()
        self._bg(TEAL)
        self._orange_bar()
        self._section_label("In the News", PAGE_H - 80)
        self._title("Published Media & Press", PAGE_H - 120, size=28)
        self._accent_line(PAGE_H - 135)

        self.c.setFont("Helvetica", 12)
        self.c.setFillColor(CREAM)
        self.c.drawCentredString(PAGE_W / 2, PAGE_H - 170,
                                 "Sengo\u2019s work has been featured across media outlets and industry publications.")

        cards = [
            ("Press & Features", "Coverage and mentions to be listed here."),
            ("Speaking & Panels", "Conference appearances and panel discussions."),
            ("Publications", "Articles, thought leadership, and contributed pieces."),
        ]
        card_w = (PAGE_W - 2 * MARGIN - 40) / 3
        sx = MARGIN + 10
        y = PAGE_H - 300

        for i, (title, desc) in enumerate(cards):
            x = sx + i * (card_w + 20)
            self._rounded_rect(x, y, card_w, 100, 8, LIGHT_TEAL)
            self.c.setFont("Helvetica-Bold", 12)
            self.c.setFillColor(ORANGE)
            self.c.drawCentredString(x + card_w / 2, y + 72, title)
            self.c.setFont("Helvetica", 9)
            self.c.setFillColor(CREAM)
            self.c.drawCentredString(x + card_w / 2, y + 45, desc)

    def slide_model(self):
        self._new_page()
        self._bg(CREAM)
        self._orange_bar()
        self._section_label("How We Work", PAGE_H - 80)
        self._title("Readiness-First Capital Infrastructure", PAGE_H - 120, size=26, color=TEAL)
        self._accent_line(PAGE_H - 135)

        # Left column text
        lx = MARGIN + 20
        ly = PAGE_H - 180
        texts = [
            ("Helvetica-Bold", 11, TEAL, "Sengo is built around preparation before participation."),
            ("Helvetica", 10, BROWN, ""),
            ("Helvetica-Bold", 10, TEAL, "Technology:"),
            ("Helvetica", 10, BROWN, "Fundraise Readiness Score \u00b7 Personalized Fundraise Roadmap"),
            ("Helvetica", 10, BROWN, ""),
            ("Helvetica-Bold", 10, TEAL, "Human Support:"),
            ("Helvetica", 10, BROWN, "1:1 advisory for founders at key inflection points"),
            ("Helvetica", 10, BROWN, ""),
            ("Helvetica-Bold", 10, TEAL, "Community Layer:"),
            ("Helvetica", 10, BROWN, "Education, events, and peer learning"),
        ]
        for font, size, color, text in texts:
            self.c.setFont(font, size)
            self.c.setFillColor(color)
            if text:
                self.c.drawString(lx, ly, text)
            ly -= 18

        # Hub diagram (right)
        cx = PAGE_W * 0.72
        cy = PAGE_H - 300
        r = 50
        self.c.setStrokeColor(ORANGE)
        self.c.setLineWidth(2)
        self.c.setFillColor(TEAL)
        self.c.circle(cx, cy, r, fill=1, stroke=1)
        self.c.setFont("Helvetica-Bold", 16)
        self.c.setFillColor(ORANGE)
        self.c.drawCentredString(cx, cy - 5, "SENGO")

        nodes = [("Technology", 0, -85), ("Readiness", 85, 0), ("Advisory", 0, 85), ("Community", -85, 0)]
        for label, dx, dy in nodes:
            nx, ny = cx + dx, cy - dy
            self._rounded_rect(nx - 40, ny - 10, 80, 20, 10, ORANGE)
            self.c.setFont("Helvetica-Bold", 8)
            self.c.setFillColor(WHITE)
            self.c.drawCentredString(nx, ny - 3, label)

        # Callout
        bw = PAGE_W - 2 * MARGIN - 80
        bx = (PAGE_W - bw) / 2
        self._rounded_rect(bx, 60, bw, 30, 6, ORANGE)
        self.c.setFont("Helvetica-Bold", 11)
        self.c.setFillColor(WHITE)
        self.c.drawCentredString(PAGE_W / 2, 70,
                                 "Result: Better decisions, stronger outcomes, and healthier capital relationships.")

    def slide_theory_of_change(self):
        self._new_page()
        self._bg(TEAL)
        self._orange_bar()
        self._section_label("Why It Matters", PAGE_H - 80)
        self._title("How Readiness Drives Impact", PAGE_H - 120, size=28)
        self._accent_line(PAGE_H - 135)

        steps = [
            ("1", "Inputs", "Education \u00b7 Readiness\ntechnology \u00b7 Community\nspaces \u00b7 Grant capital"),
            ("2", "Activities", "Assessments \u00b7 Roadmaps\n\u00b7 Workshops \u00b7 Advisory\nsupport"),
            ("3", "Outputs", "Prepared founders \u00b7\nInformed funders \u00b7\nClear next steps"),
            ("4", "Outcomes", "Increased fundability\n\u00b7 Reduced premature\nfundraising \u00b7 Alignment"),
            ("5", "Long-Term\nImpact", "Communities that\nunderstand capital\nbefore seeking it"),
        ]

        step_w = 130
        arrow_w = 20
        total_w = len(steps) * step_w + (len(steps) - 1) * arrow_w
        sx = (PAGE_W - total_w) / 2
        y = PAGE_H - 310

        for i, (num, title, body) in enumerate(steps):
            x = sx + i * (step_w + arrow_w)
            self._rounded_rect(x, y, step_w, 140, 8, LIGHT_TEAL)

            # Circle number
            cx = x + step_w / 2
            cy_num = y + 120
            self.c.setFillColor(ORANGE)
            self.c.circle(cx, cy_num, 12, fill=1, stroke=0)
            self.c.setFont("Helvetica-Bold", 12)
            self.c.setFillColor(WHITE)
            self.c.drawCentredString(cx, cy_num - 4, num)

            # Title
            self.c.setFont("Helvetica-Bold", 10)
            self.c.setFillColor(ORANGE)
            title_lines = title.split('\n')
            ty = y + 95
            for tl in title_lines:
                self.c.drawCentredString(cx, ty, tl)
                ty -= 13

            # Body
            self.c.setFont("Helvetica", 8)
            self.c.setFillColor(CREAM)
            body_lines = body.split('\n')
            by = ty - 5
            for bl in body_lines:
                self.c.drawCentredString(cx, by, bl)
                by -= 11

            # Arrow
            if i < len(steps) - 1:
                ax = x + step_w + 2
                self.c.setFont("Helvetica-Bold", 18)
                self.c.setFillColor(ORANGE)
                self.c.drawCentredString(ax + arrow_w / 2, y + 70, "\u2192")

    def slide_core_programs(self):
        self._new_page()
        self._bg(CREAM)
        self._orange_bar()
        self._section_label("What We Run Today", PAGE_H - 80)
        self._title("Core Programs", PAGE_H - 120, size=28, color=TEAL)
        self._accent_line(PAGE_H - 135)

        programs = [
            ("01", "Fundraise Readiness Score", "A self-guided assessment to evaluate preparedness"),
            ("02", "Fundraise Roadmap (1:1 Clients)", "Customized plans based on stage, goals, and gaps"),
            ("03", "Membership Platform", "Education, tools, and community access"),
            ("04", "Events & Third Spaces", "Structured learning + relationship-building"),
            ("05", "Grant Programs", "Flexible, non-dilutive capital to support readiness"),
        ]

        card_w = (PAGE_W - 2 * MARGIN - 30) / 2
        card_h = 55
        y_start = PAGE_H - 180

        for i, (num, title, desc) in enumerate(programs):
            if i < 4:
                col = i % 2
                row = i // 2
                x = MARGIN + col * (card_w + 30)
                y = y_start - row * (card_h + 12)
            else:
                x = (PAGE_W - card_w) / 2
                y = y_start - 2 * (card_h + 12)

            self._rounded_rect(x, y, card_w, card_h, 8, TEAL)
            self.c.setFont("Helvetica-Bold", 22)
            self.c.setFillColor(ORANGE)
            self.c.drawString(x + 12, y + 20, num)
            self.c.setFont("Helvetica-Bold", 11)
            self.c.setFillColor(WHITE)
            self.c.drawString(x + 50, y + 30, title)
            self.c.setFont("Helvetica", 9)
            self.c.setFillColor(CREAM)
            self.c.drawString(x + 50, y + 12, desc)

    def slide_key_learnings(self):
        self._new_page()
        self._bg(TEAL)
        self._orange_bar()
        self._section_label("Reflections", PAGE_H - 80)
        self._title("What 2025 Taught Us", PAGE_H - 120, size=28)
        self._accent_line(PAGE_H - 135)

        learnings = [
            "Readiness beats access",
            "Events without follow-through create noise",
            "Founders value clarity over volume",
            "Pay-to-play limits discovery of strong builders",
            "Small capital, deployed intentionally, creates outsized outcomes",
        ]
        responses = [
            "Fewer, clearer programs",
            "Free readiness tools for members & non-members",
            "Deeper 1:1 support at critical moments",
        ]

        col_w = (PAGE_W - 2 * MARGIN - 40) / 2
        lx = MARGIN + 10
        rx = PAGE_W / 2 + 20
        y_start = PAGE_H - 175

        self.c.setFont("Helvetica-Bold", 12)
        self.c.setFillColor(ORANGE)
        self.c.drawString(lx, y_start + 15, "What We Learned")
        self.c.drawString(rx, y_start + 15, "Our Response")

        y = y_start - 10
        for i, item in enumerate(learnings):
            self._rounded_rect(lx, y - 4, col_w, 26, 5, LIGHT_TEAL)
            self.c.setFont("Helvetica-Bold", 12)
            self.c.setFillColor(ORANGE)
            num = f"0{i + 1}"
            self.c.drawString(lx + 8, y + 3, num)
            self.c.setFont("Helvetica", 9)
            self.c.setFillColor(CREAM)
            self.c.drawString(lx + 32, y + 3, item)
            y -= 34

        y = y_start - 10
        for resp in responses:
            self._rounded_rect(rx, y - 4, col_w, 26, 5, LIGHT_TEAL)
            self.c.setFont("Helvetica", 10)
            self.c.setFillColor(CREAM)
            self.c.drawString(rx + 10, y + 3, "\u2192  " + resp)
            y -= 34

    def slide_priorities(self):
        self._new_page()
        self._bg(CREAM)
        self._orange_bar()
        self._section_label("Looking Ahead", PAGE_H - 80)
        self._title("Deepening the Infrastructure", PAGE_H - 120, size=28, color=TEAL)
        self._accent_line(PAGE_H - 135)

        priorities = [
            "Expand readiness technology & impact tracking",
            "Increase investor participation through education",
            "Scale repeatable programs into new cities",
            "Strengthen longitudinal data on founder outcomes",
            "Continue prioritizing clarity, timing, and alignment",
        ]
        y = PAGE_H - 185
        item_w = PAGE_W - 2 * MARGIN - 100
        ix = (PAGE_W - item_w) / 2

        for i, p in enumerate(priorities):
            self._rounded_rect(ix, y - 5, item_w, 32, 8, TEAL)
            # Number circle
            cx = ix + 20
            cy = y + 6
            self.c.setFillColor(ORANGE)
            self.c.circle(cx, cy, 12, fill=1, stroke=0)
            self.c.setFont("Helvetica-Bold", 12)
            self.c.setFillColor(WHITE)
            self.c.drawCentredString(cx, cy - 4, str(i + 1))
            self.c.setFont("Helvetica", 11)
            self.c.setFillColor(CREAM)
            self.c.drawString(ix + 42, y + 2, p)
            y -= 42

    def slide_cta(self):
        self._new_page()
        self._bg(TEAL)
        self._orange_bar()
        self._section_label("Get Involved", PAGE_H - 140)
        self.c.setFont("Helvetica-Bold", 40)
        self.c.setFillColor(WHITE)
        self.c.drawCentredString(PAGE_W / 2, PAGE_H - 200, "Build With Us")
        self._accent_line(PAGE_H - 218)

        items = [
            "Join the Sengo community",
            "Partner on readiness, education, or grants",
            "Attend an event or workshop",
            "Support founders building with intention",
        ]
        y = PAGE_H - 260
        iw = 340
        ix = (PAGE_W - iw) / 2
        for item in items:
            self._rounded_rect(ix, y - 4, iw, 28, 8, LIGHT_TEAL)
            self.c.setFont("Helvetica", 12)
            self.c.setFillColor(CREAM)
            self.c.drawCentredString(PAGE_W / 2, y + 3, item)
            y -= 36

        self.c.setFont("Helvetica-Bold", 13)
        self.c.setFillColor(ORANGE)
        self.c.drawCentredString(PAGE_W / 2, y - 10,
                                 "Sengo is reimagining the way communities fundraise and invest by opening access.")

        self.c.setFont("Helvetica", 9)
        self.c.setFillColor(TAN)
        self.c.drawCentredString(PAGE_W / 2, y - 40, "SENGO  \u00b7  Founded by Ila B Corcoran  \u00b7  2025")

    def build(self):
        self.slide_hero()
        self.slide_overview()
        self.slide_headline_impact()
        self.slide_charts()
        self.slide_email_data()
        self.slide_events()
        self.slide_case_studies()
        self.slide_media_press()
        self.slide_model()
        self.slide_theory_of_change()
        self.slide_core_programs()
        self.slide_key_learnings()
        self.slide_priorities()
        self.slide_cta()
        self.c.save()
        print(f"PDF saved to {self.filename}")


if __name__ == '__main__':
    deck = SlideDeck(OUTPUT)
    deck.build()
