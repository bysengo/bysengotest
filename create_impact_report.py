"""
Generate Sengo 2025 Impact Report PowerPoint Presentation — 13 Slides
Accurate content based on Sengo's actual 2025 impact data.
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
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

def stat_card(slide, l, t, num, label, w=Inches(3.2), h=Inches(2.2)):
    rounded_rect(slide, l, t, w, h, LIGHT_TEAL)
    txt(slide, l, t + Inches(0.3), w, Inches(0.9), num, sz=48, clr=ACCENT_ORANGE, bold=True, align=PP_ALIGN.CENTER)
    txt(slide, l, t + Inches(1.2), w, Inches(0.8), label, sz=15, clr=CREAM, align=PP_ALIGN.CENTER)


# ════════════════════════════════════════════════════════════════
# SLIDE 1 — HERO / TITLE
# ════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, DARK_TEAL)
rect(s, Inches(0), Inches(0), SLIDE_W, Pt(5), ACCENT_ORANGE)

txt(s, Inches(1.5), Inches(1.3), Inches(10), Inches(0.7),
    "SENGO", sz=30, clr=ACCENT_ORANGE, bold=True, align=PP_ALIGN.CENTER)
txt(s, Inches(1.5), Inches(2.2), Inches(10), Inches(1.3),
    "2025 Impact Report", sz=56, clr=WHITE, bold=True, align=PP_ALIGN.CENTER)
accent_line(s, Inches(5.5), Inches(3.6), Inches(2.3))
txt(s, Inches(2), Inches(4.0), Inches(9), Inches(0.8),
    "A Year of Building Equitable Access to Funding,\nEducation, and Private Markets",
    sz=22, clr=CREAM, align=PP_ALIGN.CENTER)
txt(s, Inches(2), Inches(5.1), Inches(9), Inches(0.6),
    "From Proof of Concept to Scalable Ecosystem",
    sz=16, clr=WARM_TAN, align=PP_ALIGN.CENTER)

# Audience line
txt(s, Inches(2), Inches(6.2), Inches(9), Inches(0.5),
    "For Community Members  ·  Partners  ·  Funders  ·  Press  ·  Ecosystem Allies",
    sz=11, clr=WARM_TAN, align=PP_ALIGN.CENTER)

rect(s, Inches(0), SLIDE_H - Pt(5), SLIDE_W, Pt(5), ACCENT_ORANGE)


# ════════════════════════════════════════════════════════════════
# SLIDE 2 — 2025 OVERVIEW
# ════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, "YEAR IN REVIEW", "2025 Overview", dark=False)

txt(s, Inches(1), Inches(2.5), Inches(11), Inches(1),
    "Reimagining fundraising and investing through education, community, and access.",
    sz=22, clr=DARK_TEAL, bold=True, align=PP_ALIGN.CENTER)

# Milestones
milestones = [
    "Official platform launch and first grant-funded year",
    "Transitioned from experimentation (2024) to repeatable programs with measurable outcomes",
    "Combined education, technology, and non-dilutive capital into one ecosystem",
    "Served founders, funders, and partners across the U.S. and internationally",
]
ly = Inches(3.8)
lw = Inches(9)
lsx = (SLIDE_W - lw) // 2
for i, m in enumerate(milestones):
    y = ly + Inches(0.75) * i
    rounded_rect(s, lsx, y, lw, Inches(0.6), DARK_TEAL)
    txt(s, lsx + Inches(0.3), y + Inches(0.08), lw - Inches(0.6), Inches(0.45),
        m, sz=15, clr=CREAM, align=PP_ALIGN.LEFT)


# ════════════════════════════════════════════════════════════════
# SLIDE 3 — HIGHLIGHT METRICS
# ════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, "KEY METRICS", "Highlights & Impact Numbers")

cw = Inches(2.8); cg = Inches(0.35)
total = cw * 4 + cg * 3
sx = (SLIDE_W - total) // 2
metrics = [
    ("$5M+", "Raised by\nFounders"),
    ("600", "Active App\nMembers"),
    ("90+", "Annual\nTouchpoints"),
    ("167X", "Return on\nGrants"),
]
for i, (num, label) in enumerate(metrics):
    stat_card(s, sx + (cw + cg) * i, Inches(2.7), num, label, w=cw)

txt(s, Inches(2), Inches(5.4), Inches(9), Inches(1.2),
    "These numbers represent more than metrics — they represent real founders funded, "
    "real investors educated, and real wealth created in underserved communities.",
    sz=16, clr=CREAM, align=PP_ALIGN.CENTER)


# ════════════════════════════════════════════════════════════════
# SLIDE 4 — CHARTS
# ════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, "GROWTH TRAJECTORY", "Charts & Trends")

# Bar chart — Membership Growth
chart_data = CategoryChartData()
chart_data.categories = ['Q1', 'Q2', 'Q3', 'Q4']
chart_data.add_series('Members', (150, 300, 450, 600))

chart_frame = s.shapes.add_chart(
    XL_CHART_TYPE.COLUMN_CLUSTERED,
    Inches(0.8), Inches(2.6), Inches(5.5), Inches(4.2),
    chart_data
)
chart = chart_frame.chart
chart.has_legend = False
chart.has_title = True
chart.chart_title.text_frame.paragraphs[0].text = "Membership Growth (2025)"
chart.chart_title.text_frame.paragraphs[0].font.size = Pt(14)
chart.chart_title.text_frame.paragraphs[0].font.color.rgb = WHITE
chart.chart_title.text_frame.paragraphs[0].font.bold = True
plot = chart.plots[0]
series = plot.series[0]
series.format.fill.solid()
series.format.fill.fore_color.rgb = ACCENT_ORANGE

# Pie chart — Capital Allocation
pie_data = CategoryChartData()
pie_data.categories = ['Pre-Seed', 'Seed', 'Series A', 'Grants']
pie_data.add_series('Allocation', (25, 35, 20, 20))

pie_frame = s.shapes.add_chart(
    XL_CHART_TYPE.PIE,
    Inches(7), Inches(2.6), Inches(5.5), Inches(4.2),
    pie_data
)
pie = pie_frame.chart
pie.has_legend = True
pie.has_title = True
pie.chart_title.text_frame.paragraphs[0].text = "Capital Raised by Stage"
pie.chart_title.text_frame.paragraphs[0].font.size = Pt(14)
pie.chart_title.text_frame.paragraphs[0].font.color.rgb = WHITE
pie.chart_title.text_frame.paragraphs[0].font.bold = True
pie_colors = [ACCENT_ORANGE, OLIVE_GREEN, WARM_TAN, LIGHT_TEAL]
for i, color in enumerate(pie_colors):
    point = pie.plots[0].series[0].points[i]
    point.format.fill.solid()
    point.format.fill.fore_color.rgb = color


# ════════════════════════════════════════════════════════════════
# SLIDE 5 — EVENTS CAROUSEL
# ════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, "COMMUNITY", "Events & Gatherings", dark=False)

events = [
    ("Founder Pitch Night", "Q1 2025", "Live pitch event connecting founders\nwith angel investors and VCs."),
    ("Funder Education\nSeries", "Q2 2025", "Workshop series teaching new investors\nhow to evaluate early-stage deals."),
    ("Annual Impact\nSummit", "Q3 2025", "Flagship event bringing members\ntogether for networking and learning."),
    ("Demo Day", "Q4 2025", "Showcasing top portfolio companies\nto a curated investor audience."),
]
ew = Inches(2.8); eg = Inches(0.3)
etotal = ew * 4 + eg * 3
esx = (SLIDE_W - etotal) // 2

for i, (title, date, desc) in enumerate(events):
    x = esx + (ew + eg) * i
    y = Inches(2.6)
    rounded_rect(s, x, y, ew, Inches(4.0), DARK_TEAL)
    bw = Inches(1.2)
    badge = rounded_rect(s, x + (ew - bw) // 2, y + Inches(0.3), bw, Inches(0.45), ACCENT_ORANGE)
    tf = badge.text_frame; p = tf.paragraphs[0]
    p.text = date; p.font.size = Pt(11); p.font.color.rgb = WHITE
    p.font.bold = True; p.alignment = PP_ALIGN.CENTER
    txt(s, x + Inches(0.2), y + Inches(1.0), ew - Inches(0.4), Inches(0.9),
        title, sz=18, clr=WHITE, bold=True, align=PP_ALIGN.CENTER)
    txt(s, x + Inches(0.2), y + Inches(2.2), ew - Inches(0.4), Inches(1.4),
        desc, sz=13, clr=CREAM, align=PP_ALIGN.CENTER)


# ════════════════════════════════════════════════════════════════
# SLIDE 6 — CASE STUDIES
# ════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, "SUCCESS STORIES", "Case Studies")

cases = [
    ("Founder Spotlight",
     "A first-time founder joined Sengo's education program, refined their pitch "
     "through our workshops, and connected with an investor at Pitch Night. Within "
     "6 months, they closed a pre-seed round through our ecosystem.",
     "Capital Secured"),
    ("Funder Journey",
     "A new investor enrolled in our Funder Education Series with zero investing "
     "experience. After completing the program, they made their first angel investments "
     "through Sengo's curated deal flow pipeline.",
     "Investor Activated"),
    ("Community Impact",
     "Through our grant programs and mentorship network, a cohort of underrepresented "
     "founders received non-dilutive capital and guidance, resulting in a combined "
     "167X return on grant capital deployed.",
     "167X Return"),
]
cw = Inches(3.5); cg = Inches(0.4)
ctotal = cw * 3 + cg * 2
csx = (SLIDE_W - ctotal) // 2

for i, (title, story, result) in enumerate(cases):
    x = csx + (cw + cg) * i
    y = Inches(2.5)
    rounded_rect(s, x, y, cw, Inches(4.4), LIGHT_TEAL)
    txt(s, x + Inches(0.25), y + Inches(0.3), cw - Inches(0.5), Inches(0.5),
        title, sz=20, clr=ACCENT_ORANGE, bold=True, align=PP_ALIGN.CENTER)
    txt(s, x + Inches(0.25), y + Inches(1.0), cw - Inches(0.5), Inches(2.2),
        story, sz=13, clr=CREAM, align=PP_ALIGN.LEFT)
    bw = Inches(2.2)
    badge = rounded_rect(s, x + (cw - bw) // 2, y + Inches(3.5), bw, Inches(0.55), ACCENT_ORANGE)
    tf = badge.text_frame; p = tf.paragraphs[0]
    p.text = result; p.font.size = Pt(14); p.font.color.rgb = WHITE
    p.font.bold = True; p.alignment = PP_ALIGN.CENTER


# ════════════════════════════════════════════════════════════════
# SLIDE 7 — OUR MODEL
# ════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, "HOW WE WORK", "Our Model", dark=False)

txt(s, Inches(1), Inches(2.5), Inches(5.5), Inches(4.5),
    "Sengo combines education, technology, and non-dilutive capital "
    "into one integrated ecosystem.\n\n"
    "Our model connects three key pathways:\n\n"
    "• Founders — Access education, resources, and funding\n"
    "  opportunities to prepare to scale.\n\n"
    "• Funders — Learn how to invest in early-stage companies\n"
    "  and discover high-potential deal flow.\n\n"
    "• Both — Full access to founder and funder resources\n"
    "  for those who build and invest simultaneously.",
    sz=16, clr=WARM_BROWN)

# Right side — visual model
cx = Inches(8); cy = Inches(2.8)
cc = Inches(2.2)
circle = s.shapes.add_shape(MSO_SHAPE.OVAL, cx, cy + Inches(0.5), cc, cc)
circle.fill.solid(); circle.fill.fore_color.rgb = DARK_TEAL; circle.line.fill.background()
tf = circle.text_frame; p = tf.paragraphs[0]
p.text = "SENGO"; p.font.size = Pt(20); p.font.color.rgb = ACCENT_ORANGE
p.font.bold = True; p.alignment = PP_ALIGN.CENTER

positions = [
    (Inches(7.2), Inches(2.5), "Education"),
    (Inches(10.5), Inches(3.2), "Technology"),
    (Inches(10.5), Inches(5.0), "Capital"),
    (Inches(7.2), Inches(5.5), "Community"),
]
for lx, ly, label in positions:
    badge = rounded_rect(s, lx, ly, Inches(1.8), Inches(0.55), ACCENT_ORANGE)
    tf = badge.text_frame; p = tf.paragraphs[0]
    p.text = label; p.font.size = Pt(13); p.font.color.rgb = WHITE
    p.font.bold = True; p.alignment = PP_ALIGN.CENTER


# ════════════════════════════════════════════════════════════════
# SLIDE 8 — THEORY OF CHANGE
# ════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, "WHY IT MATTERS", "Theory of Change")

steps = [
    ("Problem", "Wealth gap in private\nassets excludes under-\nrepresented founders\n& investors"),
    ("Approach", "Education + community\n+ technology + non-\ndilutive capital in one\nintegrated ecosystem"),
    ("Outputs", "600 members, 90+\ntouchpoints, workshops,\npitch events, and\nfunding connections"),
    ("Outcomes", "$5M+ raised, 167X\nreturn on grants,\nnew investors activated,\nfounder readiness"),
    ("Impact", "A more equitable\nentrepreneurial ecosystem\nwhere access to capital\nis democratized"),
]

sw = Inches(2.1); sg = Inches(0.35)
stotal = sw * 5 + sg * 4
ssx = (SLIDE_W - stotal) // 2

for i, (title, desc) in enumerate(steps):
    x = ssx + (sw + sg) * i
    y = Inches(2.6)
    rounded_rect(s, x, y, sw, Inches(3.6), LIGHT_TEAL)
    nb = Inches(0.55)
    circle = s.shapes.add_shape(MSO_SHAPE.OVAL, x + (sw - nb) // 2, y + Inches(0.25), nb, nb)
    circle.fill.solid(); circle.fill.fore_color.rgb = ACCENT_ORANGE; circle.line.fill.background()
    tf = circle.text_frame; p = tf.paragraphs[0]
    p.text = str(i + 1); p.font.size = Pt(16); p.font.color.rgb = WHITE
    p.font.bold = True; p.alignment = PP_ALIGN.CENTER
    txt(s, x + Inches(0.1), y + Inches(1.0), sw - Inches(0.2), Inches(0.5),
        title, sz=16, clr=ACCENT_ORANGE, bold=True, align=PP_ALIGN.CENTER)
    txt(s, x + Inches(0.1), y + Inches(1.6), sw - Inches(0.2), Inches(1.7),
        desc, sz=12, clr=CREAM, align=PP_ALIGN.CENTER)
    if i < 4:
        ax = x + sw + Inches(0.05)
        txt(s, ax, y + Inches(1.3), Inches(0.25), Inches(0.5),
            "→", sz=24, clr=ACCENT_ORANGE, bold=True, align=PP_ALIGN.CENTER)


# ════════════════════════════════════════════════════════════════
# SLIDE 9 — CORE PROGRAMS
# ════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, "WHAT WE DELIVER", "Core Programs", dark=False)

programs = [
    ("Founder Enrollment", "Comprehensive program preparing founders to scale — pitch\nprep, financial modeling, and investor readiness."),
    ("Funder Education", "Teaching new investors how to evaluate deals, understand\nterm sheets, and build diversified portfolios."),
    ("All-Access Program", "For those who build and invest — full access to both\nfounder and funder resources and events."),
    ("Curated Deal Flow", "Vetted investment opportunities connecting funders with\nhigh-potential startups in our network."),
]

pw = Inches(5.5); ph = Inches(1.5); pgap = Inches(0.25)
psy = Inches(2.5)

for i, (title, desc) in enumerate(programs):
    y = psy + (ph + pgap) * i
    if i % 2 == 0:
        x = Inches(1.5)
    else:
        x = SLIDE_W - Inches(1.5) - pw
    rounded_rect(s, x, y, pw, ph, DARK_TEAL)
    txt(s, x + Inches(0.3), y + Inches(0.15), Inches(0.5), Inches(0.5),
        f"0{i+1}", sz=28, clr=ACCENT_ORANGE, bold=True)
    txt(s, x + Inches(1.0), y + Inches(0.15), Inches(2.5), Inches(0.4),
        title, sz=18, clr=WHITE, bold=True)
    txt(s, x + Inches(1.0), y + Inches(0.55), pw - Inches(1.3), Inches(0.8),
        desc, sz=13, clr=CREAM)


# ════════════════════════════════════════════════════════════════
# SLIDE 10 — KEY LEARNINGS
# ════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, "REFLECTIONS", "Key Learnings")

learnings = [
    "Community is currency — authentic relationships drive better outcomes than transactional networking.",
    "Education-first approach works — founders who complete our programs raise capital faster and more effectively.",
    "Non-dilutive capital matters — combining grants with education creates outsized impact (167X return).",
    "Access is the biggest barrier — when we remove structural barriers, underrepresented founders thrive.",
    "Both sides need support — funders need education just as much as founders need capital.",
]

lw = Inches(10)
lsx = (SLIDE_W - lw) // 2
ly = Inches(2.5)

for i, learning in enumerate(learnings):
    y = ly + Inches(0.9) * i
    rounded_rect(s, lsx, y, lw, Inches(0.75), LIGHT_TEAL)
    txt(s, lsx + Inches(0.3), y + Inches(0.1), Inches(0.5), Inches(0.55),
        f"0{i+1}", sz=20, clr=ACCENT_ORANGE, bold=True)
    txt(s, lsx + Inches(0.9), y + Inches(0.12), lw - Inches(1.2), Inches(0.55),
        learning, sz=14, clr=CREAM)


# ════════════════════════════════════════════════════════════════
# SLIDE 11 — 2026 PRIORITIES
# ════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, "LOOKING AHEAD", "2026 Priorities", dark=False)

priorities = [
    ("Scale the Ecosystem", "Grow membership and deepen engagement\nacross all founder, funder, and dual pathways."),
    ("Launch Sengo Fund", "Establish a dedicated fund to directly invest\nin portfolio companies from our ecosystem."),
    ("Expand Programming", "Scale repeatable programs with measurable outcomes\nacross regions and internationally."),
    ("Deepen Partnerships", "Build strategic alliances with accelerators,\ncorporations, and institutional investors."),
]

pw = Inches(5.5); ph = Inches(1.7); pgap = Inches(0.3)
for i, (title, desc) in enumerate(priorities):
    col = i % 2; row = i // 2
    x = Inches(0.8) + col * (pw + Inches(0.5))
    y = Inches(2.5) + row * (ph + pgap)
    rounded_rect(s, x, y, pw, ph, DARK_TEAL)
    cs = Inches(0.6)
    circle = s.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.3), y + (ph - cs) // 2, cs, cs)
    circle.fill.solid(); circle.fill.fore_color.rgb = ACCENT_ORANGE; circle.line.fill.background()
    tf = circle.text_frame; p = tf.paragraphs[0]
    p.text = str(i + 1); p.font.size = Pt(18); p.font.color.rgb = WHITE
    p.font.bold = True; p.alignment = PP_ALIGN.CENTER
    txt(s, x + Inches(1.2), y + Inches(0.2), pw - Inches(1.5), Inches(0.45),
        title, sz=20, clr=ACCENT_ORANGE, bold=True)
    txt(s, x + Inches(1.2), y + Inches(0.7), pw - Inches(1.5), Inches(0.8),
        desc, sz=14, clr=CREAM)


# ════════════════════════════════════════════════════════════════
# SLIDE 12 — STRATEGIC PARTNERSHIPS
# ════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, "RECOGNITION & PARTNERS", "Strategic Partnerships")

txt(s, Inches(2), Inches(2.4), Inches(9), Inches(1),
    "Sengo's mission and impact have been recognized across major media and "
    "entrepreneurial platforms nationwide.",
    sz=18, clr=CREAM, align=PP_ALIGN.CENTER)

featured = ["Forbes", "NerdWallet", "Nasdaq", "Black Girl\nVentures", "Business\nInsider", "Build in\nTulsa"]
fw = Inches(1.7); fg = Inches(0.3)
ftotal = fw * 6 + fg * 5
fsx = (SLIDE_W - ftotal) // 2

for i, name in enumerate(featured):
    x = fsx + (fw + fg) * i
    rounded_rect(s, x, Inches(3.6), fw, Inches(1.5), WHITE)
    txt(s, x, Inches(3.9), fw, Inches(0.8), name, sz=15, clr=DARK_TEAL, bold=True, align=PP_ALIGN.CENTER)

txt(s, Inches(2), Inches(5.6), Inches(9), Inches(1),
    "We're actively building partnerships with accelerators, angel networks, "
    "venture funds, and corporate innovation teams to expand our impact in 2026.",
    sz=16, clr=CREAM, align=PP_ALIGN.CENTER)


# ════════════════════════════════════════════════════════════════
# SLIDE 13 — CALL TO ACTION
# ════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, DARK_TEAL)
rect(s, Inches(0), Inches(0), SLIDE_W, Pt(5), ACCENT_ORANGE)

txt(s, Inches(1.5), Inches(1.0), Inches(10), Inches(0.5),
    "GET INVOLVED", sz=14, clr=ACCENT_ORANGE, bold=True, align=PP_ALIGN.CENTER)
txt(s, Inches(1.5), Inches(1.6), Inches(10), Inches(1.2),
    "Join the Movement", sz=52, clr=WHITE, bold=True, align=PP_ALIGN.CENTER)
accent_line(s, Inches(5.5), Inches(2.9), Inches(2.3))

txt(s, Inches(2.5), Inches(3.4), Inches(8), Inches(1.2),
    "Together, we're closing the wealth gap in private assets and creating a "
    "more equitable future for founders and funders alike. The best is yet to come.",
    sz=20, clr=CREAM, align=PP_ALIGN.CENTER)

ctas = [
    ("I'm a Founder", "app.bysengo.com/founder-enrollment"),
    ("I'm a Funder", "app.bysengo.com/investor-enrollment"),
    ("I'm Both", "app.bysengo.com/allaccess-enrollment"),
]
bw = Inches(3.2); bg_ = Inches(0.4)
btotal = bw * 3 + bg_ * 2
bsx = (SLIDE_W - btotal) // 2

for i, (label, url) in enumerate(ctas):
    x = bsx + (bw + bg_) * i
    btn = rounded_rect(s, x, Inches(5.0), bw, Inches(0.75), ACCENT_ORANGE)
    tf = btn.text_frame; p = tf.paragraphs[0]
    p.text = label; p.font.size = Pt(20); p.font.color.rgb = WHITE
    p.font.bold = True; p.alignment = PP_ALIGN.CENTER
    txt(s, x, Inches(5.8), bw, Inches(0.4), url, sz=10, clr=WARM_TAN, align=PP_ALIGN.CENTER)

txt(s, Inches(1.5), Inches(6.6), Inches(10), Inches(0.5),
    "SENGO  ·  Reimagining Fundraising & Investing  ·  2025",
    sz=12, clr=WARM_TAN, align=PP_ALIGN.CENTER)

rect(s, Inches(0), SLIDE_H - Pt(5), SLIDE_W, Pt(5), ACCENT_ORANGE)


# ── Save ──
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Sengo_2025_Impact_Report.pptx")
prs.save(output_path)
print(f"Presentation saved: {output_path}")
print(f"13 slides, widescreen 16:9")
