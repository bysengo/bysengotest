"""
Generate Sengo 2025 Impact Report PowerPoint Presentation — 12 Slides
Accurate content based on Sengo's actual 2025 impact data.
Founded by Ila B. Corcoran.
"""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.chart import XL_CHART_TYPE
from pptx.chart.data import CategoryChartData
import os

# ── Brand Colors ──
DARK_TEAL = RGBColor(0x1B, 0x35, 0x33)
WARM_BROWN = RGBColor(0x67, 0x44, 0x1A)
ACCENT_ORANGE = RGBColor(0xD5, 0x70, 0x28)
CREAM = RGBColor(0xF3, 0xED, 0xE7)
OLIVE_GREEN = RGBColor(0x71, 0x7E, 0x36)
WARM_TAN = RGBColor(0xAF, 0x81, 0x45)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_TEAL = RGBColor(0x24, 0x4A, 0x47)

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)


# ── Helpers ──
def add_bg(slide, color):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color

def rect(slide, l, t, w, h, color):
    s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, l, t, w, h)
    s.fill.solid(); s.fill.fore_color.rgb = color; s.line.fill.background()
    return s

def rounded_rect(slide, l, t, w, h, color):
    s = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, l, t, w, h)
    s.fill.solid(); s.fill.fore_color.rgb = color; s.line.fill.background()
    return s

def txt(slide, l, t, w, h, text, sz=18, clr=WHITE, bold=False, align=PP_ALIGN.LEFT, font="Arial"):
    tb = slide.shapes.add_textbox(l, t, w, h)
    tb.text_frame.word_wrap = True
    p = tb.text_frame.paragraphs[0]
    p.text = text; p.font.size = Pt(sz); p.font.color.rgb = clr
    p.font.bold = bold; p.font.name = font; p.alignment = align
    return tb

def accent_line(slide, l, t, w):
    return rect(slide, l, t, w, Pt(4), ACCENT_ORANGE)

def section_header(slide, label, title, dark=True):
    bg_clr = DARK_TEAL if dark else CREAM
    title_clr = WHITE if dark else DARK_TEAL
    add_bg(slide, bg_clr)
    rect(slide, Inches(0), Inches(0), SLIDE_W, Pt(5), ACCENT_ORANGE)
    txt(slide, Inches(1), Inches(0.5), Inches(11), Inches(0.5),
        label, sz=13, clr=ACCENT_ORANGE, bold=True, align=PP_ALIGN.CENTER)
    txt(slide, Inches(1), Inches(1.0), Inches(11), Inches(1),
        title, sz=40, clr=title_clr, bold=True, align=PP_ALIGN.CENTER)
    accent_line(slide, Inches(5.5), Inches(2.0), Inches(2.3))

def stat_card(slide, l, t, num, label, w=Inches(2.3), h=Inches(2.0)):
    rounded_rect(slide, l, t, w, h, LIGHT_TEAL)
    txt(slide, l, t + Inches(0.2), w, Inches(0.8), num, sz=42, clr=ACCENT_ORANGE, bold=True, align=PP_ALIGN.CENTER)
    txt(slide, l, t + Inches(1.0), w, Inches(0.8), label, sz=13, clr=CREAM, align=PP_ALIGN.CENTER)


# ════════════════════════════════════════════════════════════════
# SLIDE 1 — HERO / TITLE
# ════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, DARK_TEAL)
rect(s, Inches(0), Inches(0), SLIDE_W, Pt(5), ACCENT_ORANGE)

txt(s, Inches(1.5), Inches(1.3), Inches(10), Inches(0.7),
    "SENGO", sz=30, clr=ACCENT_ORANGE, bold=True, align=PP_ALIGN.CENTER)
txt(s, Inches(1.5), Inches(2.1), Inches(10), Inches(1.3),
    "Impact Report 2025", sz=54, clr=WHITE, bold=True, align=PP_ALIGN.CENTER)
accent_line(s, Inches(5.5), Inches(3.5), Inches(2.3))
txt(s, Inches(2), Inches(3.9), Inches(9), Inches(0.8),
    "Turning Community Into Capital — Through Readiness",
    sz=24, clr=CREAM, bold=True, align=PP_ALIGN.CENTER)
txt(s, Inches(2), Inches(4.8), Inches(9), Inches(0.7),
    "Building informed founders, prepared funders, and durable ecosystems",
    sz=16, clr=WARM_TAN, align=PP_ALIGN.CENTER)
txt(s, Inches(2), Inches(6.2), Inches(9), Inches(0.5),
    "Founded by Ila B. Corcoran  |  2025 Year in Review",
    sz=12, clr=WARM_TAN, align=PP_ALIGN.CENTER)
rect(s, Inches(0), SLIDE_H - Pt(5), SLIDE_W, Pt(5), ACCENT_ORANGE)


# ════════════════════════════════════════════════════════════════
# SLIDE 2 — 2025 OVERVIEW
# ════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, "YEAR IN REVIEW", "From Experimentation to Infrastructure", dark=False)

milestones = [
    "2025 marked Sengo's official platform launch and first grant-funded year",
    "Transitioned from research and pilots (2024) to repeatable, technology-enabled programs",
    "Introduced readiness tools that help founders assess, prepare, and decide if and when to raise",
    "Served founders, funders, and partners across the U.S. and internationally",
]
ly = Inches(2.6)
lw = Inches(10)
lsx = (SLIDE_W - lw) // 2
for i, m in enumerate(milestones):
    y = ly + Inches(0.75) * i
    rounded_rect(s, lsx, y, lw, Inches(0.6), DARK_TEAL)
    txt(s, lsx + Inches(0.3), y + Inches(0.08), lw - Inches(0.6), Inches(0.45),
        m, sz=15, clr=CREAM, align=PP_ALIGN.LEFT)

# Core shift callout
rounded_rect(s, lsx, Inches(5.8), lw, Inches(0.7), ACCENT_ORANGE)
txt(s, lsx + Inches(0.3), Inches(5.9), lw - Inches(0.6), Inches(0.5),
    'Core shift:  From "access to capital" → readiness for capital',
    sz=17, clr=WHITE, bold=True, align=PP_ALIGN.CENTER)


# ════════════════════════════════════════════════════════════════
# SLIDE 3 — HEADLINE IMPACT
# ════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, "KEY METRICS", "Headline Impact")

cw = Inches(2.3); cg = Inches(0.25)
total = cw * 5 + cg * 4
sx = (SLIDE_W - total) // 2
metrics = [
    ("600+", "Members across\nExplorer, Founder,\nFunder & All-Access"),
    ("8,000+", "Email Subscribers\n(from 157 in\nJan 2025)"),
    ("$31,250", "Grants Deployed to\nUnderrepresented\nFounders"),
    ("$5M+", "Follow-on Capital\nInfluenced by\nSupported Founders"),
    ("27", "Events Hosted\nGlobally"),
]
for i, (num, label) in enumerate(metrics):
    stat_card(s, sx + (cw + cg) * i, Inches(2.6), num, label, w=cw)

txt(s, Inches(2), Inches(5.2), Inches(9), Inches(1),
    "Real founders funded. Real investors educated. Real wealth created in underserved communities.",
    sz=15, clr=CREAM, align=PP_ALIGN.CENTER)


# ════════════════════════════════════════════════════════════════
# SLIDE 4 — CHARTS
# ════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, "DATA & TRENDS", "Charts & Breakdown")

# Pie chart — Grant Deployment Breakdown
pie_data = CategoryChartData()
pie_data.categories = ['Standard Grants (76.8%)', 'Pitch Competition Awards (12.0%)', 'Micro / Mini Grants (11.2%)']
pie_data.add_series('Grant Deployment', (76.8, 12.0, 11.2))

pie_frame = s.shapes.add_chart(
    XL_CHART_TYPE.PIE,
    Inches(0.6), Inches(2.5), Inches(5.8), Inches(4.3),
    pie_data
)
pie = pie_frame.chart
pie.has_legend = True
pie.has_title = True
pie.chart_title.text_frame.paragraphs[0].text = "Grant Deployment Breakdown"
pie.chart_title.text_frame.paragraphs[0].font.size = Pt(14)
pie.chart_title.text_frame.paragraphs[0].font.color.rgb = WHITE
pie.chart_title.text_frame.paragraphs[0].font.bold = True
pie_colors = [ACCENT_ORANGE, OLIVE_GREEN, WARM_TAN]
for i, color in enumerate(pie_colors):
    point = pie.plots[0].series[0].points[i]
    point.format.fill.solid()
    point.format.fill.fore_color.rgb = color

# Bar chart — Programming Mix
bar_data = CategoryChartData()
bar_data.categories = ['In-Person', 'Virtual']
bar_data.add_series('Programming Mix', (51.85, 48.15))

bar_frame = s.shapes.add_chart(
    XL_CHART_TYPE.COLUMN_CLUSTERED,
    Inches(7), Inches(2.5), Inches(5.5), Inches(4.3),
    bar_data
)
chart = bar_frame.chart
chart.has_legend = False
chart.has_title = True
chart.chart_title.text_frame.paragraphs[0].text = "Programming Mix (%)"
chart.chart_title.text_frame.paragraphs[0].font.size = Pt(14)
chart.chart_title.text_frame.paragraphs[0].font.color.rgb = WHITE
chart.chart_title.text_frame.paragraphs[0].font.bold = True
series = chart.plots[0].series[0]
series.format.fill.solid()
series.format.fill.fore_color.rgb = ACCENT_ORANGE


# ════════════════════════════════════════════════════════════════
# SLIDE 5 — EVENTS (two sub-slides: Virtual + In-Person)
# ════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, "27 TOUCHPOINTS", "Events — Virtual (13)", dark=False)

virtual_events = [
    "Virtual Pitch for $1,000 — Sep 25",
    "Virtual Pitch for $1,000 — Oct 30",
    "Virtual Pitch Competition (CPG) — Nov 20",
    "Pitch Prep with Amiah — Oct 23",
    "Practice Your Pitch with Sarah Anto — Aug 12",
    "Build Your 2026 Pitch Strategy (Dana Ammons) — Dec 11",
    "Private Markets 101 (Part 1) — Sep 9",
    "Demystifying CDFI Funding with Coleman — Oct 14",
    "Ask an Angel — Jul 31",
    "Preparing to Raise Capital with Confidence — Sep 4",
    "Welcome to Sengo Webinar — May 21",
    "Sengo Founder Meetup: Angels & VCs — Sep 18",
    "Sengo Founder Meetup: Social Enterprise & EdTech — Jul 22",
]

lw = Inches(5.5)
col1_x = Inches(0.6)
col2_x = Inches(6.8)
ly = Inches(2.5)

for i, ev in enumerate(virtual_events):
    col = 0 if i < 7 else 1
    row = i if i < 7 else i - 7
    x = col1_x if col == 0 else col2_x
    y = ly + Inches(0.58) * row
    rounded_rect(s, x, y, lw, Inches(0.48), DARK_TEAL)
    txt(s, x + Inches(0.2), y + Inches(0.06), lw - Inches(0.4), Inches(0.38),
        ev, sz=12, clr=CREAM, align=PP_ALIGN.LEFT)

# + IFundWomen
rounded_rect(s, col2_x, ly + Inches(0.58) * 6, lw, Inches(0.48), DARK_TEAL)
txt(s, col2_x + Inches(0.2), ly + Inches(0.58) * 6 + Inches(0.06), lw - Inches(0.4), Inches(0.38),
    "IFundWomen Webinar — Jun 3", sz=12, clr=CREAM, align=PP_ALIGN.LEFT)


# SLIDE 5b — In-Person Events
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, "27 TOUCHPOINTS", "Events — In-Person (14)", dark=False)

in_person = [
    "Fashion x Futures — LA (Jun 28)",
    "Fashion x Futures — NY (Jul 26)",
    "Fashion x Futures — LA Holiday Pop-Up (Nov 8–9)",
    "Galentine's Wine Club — Dallas (Feb 21)",
    "Brunch Wine Club — Dallas (Mar 15)",
    "Sip Into Spring — Dallas (Mar 30)",
    "Wine Club — Dallas (Apr 9)",
    "GirlMath x Sengo: Wed Night Write-Off (NY Tech Week, Jun 4)",
    "Spill the Tea: AI & Tech (LA Tech Week, Oct 14)",
    "NY Tech Week Mixer (Sengo x Little More, Jun 4)",
    "BBOP Center x Sengo Founder Workshop (Mar 28)",
    "Funded & Fearless Workshop (Apr 26)",
    "Barcelona Black Women Entrepreneurs Mixer (Mar 13)",
    "The Village Retreat — France (Jun 10–15)",
]

for i, ev in enumerate(in_person):
    col = 0 if i < 7 else 1
    row = i if i < 7 else i - 7
    x = col1_x if col == 0 else col2_x
    y = ly + Inches(0.58) * row
    rounded_rect(s, x, y, lw, Inches(0.48), DARK_TEAL)
    txt(s, x + Inches(0.2), y + Inches(0.06), lw - Inches(0.4), Inches(0.38),
        ev, sz=12, clr=CREAM, align=PP_ALIGN.LEFT)

# Key Insight
rounded_rect(s, Inches(1.5), Inches(6.6), Inches(10), Inches(0.6), ACCENT_ORANGE)
txt(s, Inches(1.8), Inches(6.68), Inches(9.4), Inches(0.45),
    "Key Insight: Events are most effective when they lead into readiness tools and structured next steps.",
    sz=13, clr=WHITE, bold=True, align=PP_ALIGN.CENTER)


# ════════════════════════════════════════════════════════════════
# SLIDE 6 — CASE STUDIES
# ════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, "SUCCESS STORIES", "Case Studies")

# Versed Wellness
vx = Inches(0.8); vy = Inches(2.5)
vw = Inches(5.5); vh = Inches(4.5)
rounded_rect(s, vx, vy, vw, vh, LIGHT_TEAL)
txt(s, vx + Inches(0.3), vy + Inches(0.2), vw - Inches(0.6), Inches(0.4),
    "Versed Wellness", sz=22, clr=ACCENT_ORANGE, bold=True)
txt(s, vx + Inches(0.3), vy + Inches(0.65), vw - Inches(0.6), Inches(0.35),
    "Founder: Jasmine Bowie  |  Grant: $500 Micro-Grant", sz=13, clr=CREAM)
txt(s, vx + Inches(0.3), vy + Inches(1.2), vw - Inches(0.6), Inches(1.8),
    "Impact:\n"
    "• Concept → physical prototype\n"
    "• 25 new customers acquired\n"
    "• Revenue increased post-grant\n"
    "• Founder chose not to raise capital prematurely",
    sz=14, clr=CREAM)
rounded_rect(s, vx + Inches(0.3), vy + Inches(3.4), Inches(4.5), Inches(0.7), ACCENT_ORANGE)
txt(s, vx + Inches(0.4), vy + Inches(3.5), Inches(4.3), Inches(0.5),
    "Why it matters: Readiness includes knowing when not to fundraise.",
    sz=13, clr=WHITE, bold=True, align=PP_ALIGN.LEFT)

# Satlyt
sx2 = Inches(7); sy = Inches(2.5)
rounded_rect(s, sx2, sy, vw, vh, LIGHT_TEAL)
txt(s, sx2 + Inches(0.3), sy + Inches(0.2), vw - Inches(0.6), Inches(0.4),
    "Satlyt", sz=22, clr=ACCENT_ORANGE, bold=True)
txt(s, sx2 + Inches(0.3), sy + Inches(0.65), vw - Inches(0.6), Inches(0.35),
    "Founder: Rama Afullo  |  Grant: $3,000 Standard Grant", sz=13, clr=CREAM)
txt(s, sx2 + Inches(0.3), sy + Inches(1.2), vw - Inches(0.6), Inches(1.8),
    "Impact:\n"
    "• 10 new customers acquired\n"
    "• Operational capacity expanded\n"
    "• $3M raised post-Sengo\n"
    "• 12 new hires",
    sz=14, clr=CREAM)
rounded_rect(s, sx2 + Inches(0.3), sy + Inches(3.4), Inches(4.5), Inches(0.7), ACCENT_ORANGE)
txt(s, sx2 + Inches(0.4), sy + Inches(3.5), Inches(4.3), Inches(0.5),
    "Why it matters: Prepared founders convert early support into scalable outcomes.",
    sz=13, clr=WHITE, bold=True, align=PP_ALIGN.LEFT)


# ════════════════════════════════════════════════════════════════
# SLIDE 7 — OUR MODEL
# ════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, "HOW WE WORK", "Readiness-First Capital Infrastructure", dark=False)

txt(s, Inches(1), Inches(2.5), Inches(6), Inches(0.5),
    "Sengo is built around preparation before participation.",
    sz=18, clr=DARK_TEAL, bold=True)

txt(s, Inches(1), Inches(3.2), Inches(5.5), Inches(3.5),
    "Technology:\n"
    "  • Fundraise Readiness Score\n"
    "  • Personalized Fundraise Roadmap\n\n"
    "Human Support:\n"
    "  • 1:1 advisory for founders at key inflection points\n\n"
    "Community Layer:\n"
    "  • Education, events, and peer learning",
    sz=15, clr=WARM_BROWN)

# Right side — visual model
cx = Inches(8); cy = Inches(2.8)
cc = Inches(2.2)
circle = s.shapes.add_shape(MSO_SHAPE.OVAL, cx, cy + Inches(0.5), cc, cc)
circle.fill.solid(); circle.fill.fore_color.rgb = DARK_TEAL; circle.line.fill.background()
tf = circle.text_frame; p = tf.paragraphs[0]
p.text = "SENGO"; p.font.size = Pt(20); p.font.color.rgb = ACCENT_ORANGE
p.font.bold = True; p.alignment = PP_ALIGN.CENTER

positions = [
    (Inches(7.2), Inches(2.5), "Technology"),
    (Inches(10.5), Inches(3.2), "Readiness"),
    (Inches(10.5), Inches(5.0), "Advisory"),
    (Inches(7.2), Inches(5.5), "Community"),
]
for lx, ly, label in positions:
    badge = rounded_rect(s, lx, ly, Inches(1.8), Inches(0.55), ACCENT_ORANGE)
    tf = badge.text_frame; p = tf.paragraphs[0]
    p.text = label; p.font.size = Pt(13); p.font.color.rgb = WHITE
    p.font.bold = True; p.alignment = PP_ALIGN.CENTER

# Result callout
rounded_rect(s, Inches(1), Inches(6.4), Inches(11), Inches(0.7), ACCENT_ORANGE)
txt(s, Inches(1.3), Inches(6.5), Inches(10.4), Inches(0.5),
    "Result: Better decisions, stronger outcomes, and healthier capital relationships.",
    sz=15, clr=WHITE, bold=True, align=PP_ALIGN.CENTER)


# ════════════════════════════════════════════════════════════════
# SLIDE 8 — THEORY OF CHANGE
# ════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, "WHY IT MATTERS", "How Readiness Drives Impact")

steps = [
    ("Inputs", "Education\nReadiness technology\nCommunity spaces\nGrant capital"),
    ("Activities", "Assessments\nRoadmaps\nWorkshops\nAdvisory support"),
    ("Outputs", "Prepared founders\nInformed funders\nClear next steps"),
    ("Outcomes", "Increased fundability\nwhen appropriate\nReduced premature\nfundraising\nStronger alignment"),
    ("Long-Term\nImpact", "Communities that\nunderstand capital\nbefore seeking it"),
]

sw = Inches(2.1); sg = Inches(0.35)
stotal = sw * 5 + sg * 4
ssx = (SLIDE_W - stotal) // 2

for i, (title, desc) in enumerate(steps):
    x = ssx + (sw + sg) * i
    y = Inches(2.6)
    rounded_rect(s, x, y, sw, Inches(4.0), LIGHT_TEAL)
    nb = Inches(0.55)
    circle = s.shapes.add_shape(MSO_SHAPE.OVAL, x + (sw - nb) // 2, y + Inches(0.25), nb, nb)
    circle.fill.solid(); circle.fill.fore_color.rgb = ACCENT_ORANGE; circle.line.fill.background()
    tf = circle.text_frame; p = tf.paragraphs[0]
    p.text = str(i + 1); p.font.size = Pt(16); p.font.color.rgb = WHITE
    p.font.bold = True; p.alignment = PP_ALIGN.CENTER
    txt(s, x + Inches(0.1), y + Inches(1.0), sw - Inches(0.2), Inches(0.7),
        title, sz=15, clr=ACCENT_ORANGE, bold=True, align=PP_ALIGN.CENTER)
    txt(s, x + Inches(0.1), y + Inches(1.8), sw - Inches(0.2), Inches(1.8),
        desc, sz=12, clr=CREAM, align=PP_ALIGN.CENTER)
    if i < 4:
        ax = x + sw + Inches(0.05)
        txt(s, ax, y + Inches(1.5), Inches(0.25), Inches(0.5),
            "→", sz=24, clr=ACCENT_ORANGE, bold=True, align=PP_ALIGN.CENTER)


# ════════════════════════════════════════════════════════════════
# SLIDE 9 — CORE PROGRAMS
# ════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, "WHAT WE RUN TODAY", "Core Programs", dark=False)

programs = [
    ("Fundraise Readiness Score", "A self-guided assessment to evaluate preparedness"),
    ("Fundraise Roadmap (1:1)", "Customized plans based on stage, goals, and gaps"),
    ("Membership Platform", "Education, tools, and community access"),
    ("Events & Third Spaces", "Structured learning + relationship-building"),
    ("Grant Programs", "Flexible, non-dilutive capital to support readiness"),
]

pw = Inches(5.5); ph = Inches(0.9); pgap = Inches(0.15)
psy = Inches(2.5)

for i, (title, desc) in enumerate(programs):
    y = psy + (ph + pgap) * i
    if i % 2 == 0:
        x = Inches(1.5)
    else:
        x = SLIDE_W - Inches(1.5) - pw
    rounded_rect(s, x, y, pw, ph, DARK_TEAL)
    txt(s, x + Inches(0.3), y + Inches(0.08), Inches(0.5), Inches(0.4),
        f"0{i+1}", sz=24, clr=ACCENT_ORANGE, bold=True)
    txt(s, x + Inches(1.0), y + Inches(0.08), Inches(2.8), Inches(0.35),
        title, sz=16, clr=WHITE, bold=True)
    txt(s, x + Inches(1.0), y + Inches(0.45), pw - Inches(1.3), Inches(0.4),
        desc, sz=12, clr=CREAM)


# ════════════════════════════════════════════════════════════════
# SLIDE 10 — KEY LEARNINGS
# ════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, "REFLECTIONS", "What 2025 Taught Us")

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

# Left column — learnings
txt(s, Inches(0.8), Inches(2.5), Inches(5.5), Inches(0.4),
    "What We Learned:", sz=18, clr=ACCENT_ORANGE, bold=True)

lw2 = Inches(5.5)
for i, learning in enumerate(learnings):
    y = Inches(3.1) + Inches(0.65) * i
    rounded_rect(s, Inches(0.8), y, lw2, Inches(0.55), LIGHT_TEAL)
    txt(s, Inches(1.1), y + Inches(0.08), Inches(0.4), Inches(0.4),
        f"0{i+1}", sz=18, clr=ACCENT_ORANGE, bold=True)
    txt(s, Inches(1.6), y + Inches(0.1), lw2 - Inches(1.0), Inches(0.4),
        learning, sz=13, clr=CREAM)

# Right column — response
txt(s, Inches(7), Inches(2.5), Inches(5.5), Inches(0.4),
    "Our Response:", sz=18, clr=ACCENT_ORANGE, bold=True)

for i, resp in enumerate(responses):
    y = Inches(3.1) + Inches(0.65) * i
    rounded_rect(s, Inches(7), y, lw2, Inches(0.55), LIGHT_TEAL)
    txt(s, Inches(7.3), y + Inches(0.1), lw2 - Inches(0.6), Inches(0.4),
        f"→ {resp}", sz=13, clr=CREAM)


# ════════════════════════════════════════════════════════════════
# SLIDE 11 — 2026 PRIORITIES
# ════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, "LOOKING AHEAD", "Deepening the Infrastructure", dark=False)

priorities = [
    "Expand readiness technology & impact tracking",
    "Increase investor participation through education",
    "Scale repeatable programs into new cities",
    "Strengthen longitudinal data on founder outcomes",
    "Continue prioritizing clarity, timing, and alignment",
]

pw2 = Inches(10)
psx = (SLIDE_W - pw2) // 2

for i, pri in enumerate(priorities):
    y = Inches(2.6) + Inches(0.8) * i
    rounded_rect(s, psx, y, pw2, Inches(0.65), DARK_TEAL)
    cs = Inches(0.5)
    circle = s.shapes.add_shape(MSO_SHAPE.OVAL, psx + Inches(0.2), y + Inches(0.075), cs, cs)
    circle.fill.solid(); circle.fill.fore_color.rgb = ACCENT_ORANGE; circle.line.fill.background()
    tf = circle.text_frame; p = tf.paragraphs[0]
    p.text = str(i + 1); p.font.size = Pt(16); p.font.color.rgb = WHITE
    p.font.bold = True; p.alignment = PP_ALIGN.CENTER
    txt(s, psx + Inches(1.0), y + Inches(0.1), pw2 - Inches(1.3), Inches(0.45),
        pri, sz=16, clr=CREAM)


# ════════════════════════════════════════════════════════════════
# SLIDE 12 — CALL TO ACTION
# ════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, DARK_TEAL)
rect(s, Inches(0), Inches(0), SLIDE_W, Pt(5), ACCENT_ORANGE)

txt(s, Inches(1.5), Inches(1.0), Inches(10), Inches(0.5),
    "GET INVOLVED", sz=14, clr=ACCENT_ORANGE, bold=True, align=PP_ALIGN.CENTER)
txt(s, Inches(1.5), Inches(1.6), Inches(10), Inches(1.2),
    "Build With Us", sz=52, clr=WHITE, bold=True, align=PP_ALIGN.CENTER)
accent_line(s, Inches(5.5), Inches(2.9), Inches(2.3))

ctas = [
    "Join the Sengo community",
    "Partner on readiness, education, or grants",
    "Attend an event or workshop",
    "Support founders building with intention",
]

cta_w = Inches(5)
cta_x = (SLIDE_W - cta_w) // 2
for i, cta in enumerate(ctas):
    y = Inches(3.5) + Inches(0.55) * i
    rounded_rect(s, cta_x, y, cta_w, Inches(0.45), LIGHT_TEAL)
    txt(s, cta_x + Inches(0.3), y + Inches(0.06), cta_w - Inches(0.6), Inches(0.35),
        cta, sz=15, clr=CREAM, align=PP_ALIGN.CENTER)

txt(s, Inches(2), Inches(5.8), Inches(9), Inches(0.6),
    "Sengo believes capital should meet preparedness — not pressure.",
    sz=18, clr=ACCENT_ORANGE, bold=True, align=PP_ALIGN.CENTER)

txt(s, Inches(1.5), Inches(6.6), Inches(10), Inches(0.5),
    "SENGO  ·  Founded by Ila B. Corcoran  ·  2025",
    sz=12, clr=WARM_TAN, align=PP_ALIGN.CENTER)

rect(s, Inches(0), SLIDE_H - Pt(5), SLIDE_W, Pt(5), ACCENT_ORANGE)


# ── Save ──
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Sengo_2025_Impact_Report.pptx")
prs.save(output_path)
print(f"Presentation saved: {output_path}")
print(f"12 slides (events split into Virtual + In-Person), widescreen 16:9")
