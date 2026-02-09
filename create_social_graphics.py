#!/usr/bin/env python3
"""
Generate branded social media graphics for Sengo 2025 Impact Report.
Features: Sengo logo, gradient backgrounds, founder quotes.
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import requests
from io import BytesIO

# Brand colors
TEAL = (27, 53, 51)        # #1B3533
LIGHT_TEAL = (36, 74, 71)  # #244A47
ORANGE = (213, 112, 40)    # #D57028
CREAM = (243, 237, 231)    # #F3EDE7
OLIVE = (113, 126, 54)     # #717E36
TAN = (175, 129, 69)       # #AF8145
WHITE = (255, 255, 255)
DARK_TEAL = (18, 38, 36)   # Darker for gradients

# Founder quotes
QUOTES = [
    ("Sengo helped me understand when NOT to raise - that clarity was invaluable.", "Jasmine Bowie", "Versed Wellness"),
    ("The readiness tools and community gave me the foundation to raise $3M.", "Rama Afullo", "Satlyt"),
    ("Finally, a platform that prepares you before asking you to pitch.", "Sengo Founder", ""),
]

def get_font(size, bold=False):
    font_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except:
                pass
    return ImageFont.load_default()

def create_gradient(width, height, color1, color2, direction='vertical'):
    """Create a gradient image."""
    img = Image.new('RGB', (width, height))
    for i in range(height if direction == 'vertical' else width):
        ratio = i / (height if direction == 'vertical' else width)
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        if direction == 'vertical':
            ImageDraw.Draw(img).line([(0, i), (width, i)], fill=(r, g, b))
        else:
            ImageDraw.Draw(img).line([(i, 0), (i, height)], fill=(r, g, b))
    return img

def create_radial_gradient(width, height, center_color, edge_color):
    """Create a radial gradient from center."""
    img = Image.new('RGB', (width, height), edge_color)
    draw = ImageDraw.Draw(img)
    cx, cy = width // 2, height // 2
    max_radius = int((width**2 + height**2)**0.5 / 2)

    for r in range(max_radius, 0, -2):
        ratio = r / max_radius
        color = tuple(int(center_color[i] * (1-ratio) + edge_color[i] * ratio) for i in range(3))
        draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=color)
    return img

def draw_rounded_rect(draw, coords, radius, fill, outline=None, outline_width=0):
    """Draw a rounded rectangle with optional outline."""
    x1, y1, x2, y2 = coords
    draw.rectangle([x1 + radius, y1, x2 - radius, y2], fill=fill)
    draw.rectangle([x1, y1 + radius, x2, y2 - radius], fill=fill)
    draw.ellipse([x1, y1, x1 + 2*radius, y1 + 2*radius], fill=fill)
    draw.ellipse([x2 - 2*radius, y1, x2, y1 + 2*radius], fill=fill)
    draw.ellipse([x1, y2 - 2*radius, x1 + 2*radius, y2], fill=fill)
    draw.ellipse([x2 - 2*radius, y2 - 2*radius, x2, y2], fill=fill)

    if outline:
        # Draw outline arcs and lines
        draw.arc([x1, y1, x1 + 2*radius, y1 + 2*radius], 180, 270, fill=outline, width=outline_width)
        draw.arc([x2 - 2*radius, y1, x2, y1 + 2*radius], 270, 360, fill=outline, width=outline_width)
        draw.arc([x1, y2 - 2*radius, x1 + 2*radius, y2], 90, 180, fill=outline, width=outline_width)
        draw.arc([x2 - 2*radius, y2 - 2*radius, x2, y2], 0, 90, fill=outline, width=outline_width)
        draw.line([x1 + radius, y1, x2 - radius, y1], fill=outline, width=outline_width)
        draw.line([x1 + radius, y2, x2 - radius, y2], fill=outline, width=outline_width)
        draw.line([x1, y1 + radius, x1, y2 - radius], fill=outline, width=outline_width)
        draw.line([x2, y1 + radius, x2, y2 - radius], fill=outline, width=outline_width)

def load_logo():
    """Load Sengo logo from local file."""
    logo_path = "/home/user/bysengotest/Sengo 2.PNG"
    if os.path.exists(logo_path):
        return Image.open(logo_path).convert('RGBA')
    return None

def add_logo(img, logo, position, max_width):
    """Add logo to image at specified position."""
    if logo is None:
        return img

    # Resize logo maintaining aspect ratio
    ratio = max_width / logo.width
    new_size = (int(logo.width * ratio), int(logo.height * ratio))
    logo_resized = logo.resize(new_size, Image.LANCZOS)

    # Calculate position
    x, y = position
    if x == 'center':
        x = (img.width - logo_resized.width) // 2

    # Paste with transparency
    img.paste(logo_resized, (x, y), logo_resized)
    return img

def add_glow_effect(img, color, intensity=30):
    """Add subtle glow effect."""
    glow = Image.new('RGB', img.size, color)
    glow = glow.filter(ImageFilter.GaussianBlur(radius=intensity))
    return Image.blend(img, glow, 0.15)

def create_instagram_post(logo):
    """Create 1080x1080 Instagram post with gradient and logo."""
    width, height = 1080, 1080

    # Create gradient background
    img = create_gradient(width, height, LIGHT_TEAL, DARK_TEAL)

    # Add radial glow in center
    glow = create_radial_gradient(width, height, TEAL, DARK_TEAL)
    img = Image.blend(img, glow, 0.3)

    draw = ImageDraw.Draw(img)

    # Orange accent bar at top
    draw.rectangle([0, 0, width, 10], fill=ORANGE)

    # Add decorative corner accents
    draw.polygon([(0, 0), (80, 0), (0, 80)], fill=(*ORANGE, 50))
    draw.polygon([(width, 0), (width-80, 0), (width, 80)], fill=(*ORANGE, 50))

    # Add logo
    img = add_logo(img, logo, ('center', 50), 200)

    # Title below logo
    draw = ImageDraw.Draw(img)
    draw.text((width//2, 180), "2025 IMPACT REPORT", font=get_font(38, bold=True), fill=WHITE, anchor="mm")

    # Orange accent line
    line_width = 120
    draw.rectangle([(width - line_width)//2, 215, (width + line_width)//2, 221], fill=ORANGE)

    # Stats grid
    stats = [
        ("600+", "Members"),
        ("9,500+", "Subscribers"),
        ("$32,150", "Grants Deployed"),
        ("$5M+", "Follow-on Capital"),
        ("30+", "Events Hosted"),
        ("19", "Founders Funded"),
    ]

    cols, rows = 2, 3
    box_w, box_h = 420, 180
    start_x = (width - (cols * box_w + (cols-1) * 40)) // 2
    start_y = 270
    gap = 40

    for i, (num, label) in enumerate(stats):
        col = i % cols
        row = i // cols
        x = start_x + col * (box_w + gap)
        y = start_y + row * (box_h + 30)

        # Card with gradient effect
        draw_rounded_rect(draw, [x, y, x + box_w, y + box_h], 16, LIGHT_TEAL, ORANGE, 2)

        # Stat number with slight shadow
        draw.text((x + box_w//2 + 2, y + 65 + 2), num, font=get_font(64, bold=True), fill=DARK_TEAL, anchor="mm")
        draw.text((x + box_w//2, y + 65), num, font=get_font(64, bold=True), fill=ORANGE, anchor="mm")

        # Label
        draw.text((x + box_w//2, y + 135), label, font=get_font(22), fill=CREAM, anchor="mm")

    # Bottom tagline with quote styling
    draw.text((width//2, 920), '"Reimagining how communities fundraise & invest"',
              font=get_font(20), fill=CREAM, anchor="mm")
    draw.text((width//2, 980), "bysengo.com", font=get_font(24, bold=True), fill=ORANGE, anchor="mm")

    # Bottom accent
    draw.rectangle([0, height-10, width, height], fill=ORANGE)

    return img

def create_quote_card(logo, quote_data):
    """Create a quote card with founder testimonial."""
    width, height = 1080, 1080
    quote, name, company = quote_data

    # Gradient background
    img = create_gradient(width, height, TEAL, DARK_TEAL)
    draw = ImageDraw.Draw(img)

    # Orange accents
    draw.rectangle([0, 0, width, 8], fill=ORANGE)
    draw.rectangle([0, height-8, width, height], fill=ORANGE)

    # Decorative quote marks
    draw.text((100, 200), '"', font=get_font(200, bold=True), fill=(213, 112, 40))
    draw.text((width-200, height-450), '"', font=get_font(200, bold=True), fill=(213, 112, 40))

    # Add logo at top
    img = add_logo(img, logo, ('center', 60), 160)
    draw = ImageDraw.Draw(img)

    # Quote text - wrap manually
    words = quote.split()
    lines = []
    current_line = []
    max_chars = 30

    for word in words:
        current_line.append(word)
        if len(' '.join(current_line)) > max_chars:
            if len(current_line) > 1:
                current_line.pop()
                lines.append(' '.join(current_line))
                current_line = [word]
            else:
                lines.append(' '.join(current_line))
                current_line = []
    if current_line:
        lines.append(' '.join(current_line))

    # Draw quote
    y_pos = 400
    for line in lines:
        draw.text((width//2, y_pos), line, font=get_font(36, bold=True), fill=WHITE, anchor="mm")
        y_pos += 55

    # Attribution
    y_pos += 40
    draw.text((width//2, y_pos), f"— {name}", font=get_font(28, bold=True), fill=ORANGE, anchor="mm")
    if company:
        draw.text((width//2, y_pos + 40), company, font=get_font(22), fill=TAN, anchor="mm")

    # Bottom CTA
    draw.text((width//2, 920), "Join our community of founders & funders", font=get_font(20), fill=CREAM, anchor="mm")
    draw.text((width//2, 970), "bysengo.com", font=get_font(24, bold=True), fill=ORANGE, anchor="mm")

    return img

def create_story(logo):
    """Create 1080x1920 Story with gradient."""
    width, height = 1080, 1920

    # Gradient background
    img = create_gradient(width, height, LIGHT_TEAL, DARK_TEAL)
    draw = ImageDraw.Draw(img)

    # Orange accents
    draw.rectangle([0, 0, width, 12], fill=ORANGE)
    draw.rectangle([0, height-12, width, height], fill=ORANGE)

    # Side accent lines
    draw.rectangle([0, 200, 6, height-200], fill=ORANGE)
    draw.rectangle([width-6, 200, width, height-200], fill=ORANGE)

    # Add logo
    img = add_logo(img, logo, ('center', 80), 220)
    draw = ImageDraw.Draw(img)

    # Title
    draw.text((width//2, 240), "2025 IMPACT", font=get_font(48, bold=True), fill=WHITE, anchor="mm")
    draw.text((width//2, 300), "REPORT", font=get_font(48, bold=True), fill=WHITE, anchor="mm")

    # Accent line
    draw.rectangle([(width-150)//2, 350, (width+150)//2, 358], fill=ORANGE)

    # Stats
    stats = [
        ("600+", "Members Across Tiers"),
        ("9,500+", "Email Subscribers"),
        ("$32,150", "Grants Deployed"),
        ("$5M+", "Follow-on Capital"),
        ("30+", "Events Hosted"),
        ("19", "Founders Funded"),
        ("46.5%", "Email Open Rate"),
    ]

    box_w, box_h = 800, 140
    start_x = (width - box_w) // 2
    start_y = 420
    gap = 22

    for i, (num, label) in enumerate(stats):
        y = start_y + i * (box_h + gap)

        draw_rounded_rect(draw, [start_x, y, start_x + box_w, y + box_h], 16, LIGHT_TEAL, ORANGE, 2)

        # Shadow effect on numbers
        draw.text((start_x + 50 + 2, y + box_h//2 + 2), num, font=get_font(56, bold=True), fill=DARK_TEAL, anchor="lm")
        draw.text((start_x + 50, y + box_h//2), num, font=get_font(56, bold=True), fill=ORANGE, anchor="lm")
        draw.text((start_x + box_w - 50, y + box_h//2), label, font=get_font(22), fill=CREAM, anchor="rm")

    # Bottom quote
    draw.text((width//2, 1720), '"Readiness before access"', font=get_font(26, bold=True), fill=CREAM, anchor="mm")
    draw.text((width//2, 1780), "— Sengo 2025 Key Learning", font=get_font(18), fill=TAN, anchor="mm")
    draw.text((width//2, 1850), "bysengo.com", font=get_font(28, bold=True), fill=ORANGE, anchor="mm")

    return img

def create_linkedin_post(logo):
    """Create 1200x628 LinkedIn post."""
    width, height = 1200, 628

    img = create_gradient(width, height, TEAL, DARK_TEAL, 'horizontal')
    draw = ImageDraw.Draw(img)

    # Accent bars
    draw.rectangle([0, 0, width, 8], fill=ORANGE)
    draw.rectangle([0, height-8, width, height], fill=ORANGE)

    # Left side - Logo and tagline
    img = add_logo(img, logo, (50, 60), 140)
    draw = ImageDraw.Draw(img)

    draw.text((50, 160), "2025 Impact Report", font=get_font(32, bold=True), fill=WHITE)
    draw.rectangle([50, 205, 170, 211], fill=ORANGE)

    # Key message
    draw.text((50, 250), "Reimagining how", font=get_font(22), fill=CREAM)
    draw.text((50, 280), "communities fundraise", font=get_font(22), fill=CREAM)
    draw.text((50, 310), "and invest.", font=get_font(22), fill=CREAM)

    # Highlight stats
    draw.text((50, 380), "$5M+", font=get_font(48, bold=True), fill=ORANGE)
    draw.text((50, 440), "Follow-on Capital", font=get_font(18), fill=TAN)

    draw.text((50, 500), "167x", font=get_font(48, bold=True), fill=ORANGE)
    draw.text((50, 560), "Grant Multiplier", font=get_font(18), fill=TAN)

    # Right side - Stats grid
    stats = [
        ("600+", "Members"),
        ("9,500+", "Subscribers"),
        ("$32,150", "Grants"),
        ("19", "Founders"),
        ("30+", "Events"),
        ("46.5%", "Open Rate"),
    ]

    box_w, box_h = 200, 110
    start_x = 500
    start_y = 80
    gap_x, gap_y = 25, 20

    for i, (num, label) in enumerate(stats):
        col = i % 3
        row = i // 3
        x = start_x + col * (box_w + gap_x)
        y = start_y + row * (box_h + gap_y)

        draw_rounded_rect(draw, [x, y, x + box_w, y + box_h], 10, LIGHT_TEAL, ORANGE, 2)
        draw.text((x + box_w//2, y + 40), num, font=get_font(36, bold=True), fill=ORANGE, anchor="mm")
        draw.text((x + box_w//2, y + 85), label, font=get_font(16), fill=CREAM, anchor="mm")

    # Quote at bottom right
    draw.text((width - 50, height - 100), '"Readiness before access"', font=get_font(18, bold=True), fill=CREAM, anchor="rm")
    draw.text((width - 50, height - 70), "bysengo.com", font=get_font(20, bold=True), fill=ORANGE, anchor="rm")

    return img

def create_highlight_card(logo, stat_num, stat_label, context=""):
    """Create single-stat highlight with gradient."""
    width, height = 1080, 1080

    img = create_radial_gradient(width, height, LIGHT_TEAL, DARK_TEAL)
    draw = ImageDraw.Draw(img)

    # Accent bars
    draw.rectangle([0, 0, width, 10], fill=ORANGE)
    draw.rectangle([0, height-10, width, height], fill=ORANGE)

    # Corner accents
    for corner in [(0, 0, 100, 100), (width-100, 0, width, 100), (0, height-100, 100, height), (width-100, height-100, width, height)]:
        x1, y1, x2, y2 = corner
        draw.rectangle([x1, y1, x2, y2], outline=ORANGE, width=2)

    # Logo
    img = add_logo(img, logo, ('center', 80), 160)
    draw = ImageDraw.Draw(img)

    draw.text((width//2, 200), "2025 IMPACT", font=get_font(28, bold=True), fill=CREAM, anchor="mm")

    # Big stat with glow effect
    # Shadow
    draw.text((width//2 + 4, 500 + 4), stat_num, font=get_font(140, bold=True), fill=DARK_TEAL, anchor="mm")
    draw.text((width//2, 500), stat_num, font=get_font(140, bold=True), fill=ORANGE, anchor="mm")

    draw.text((width//2, 620), stat_label, font=get_font(40, bold=True), fill=WHITE, anchor="mm")

    if context:
        draw.text((width//2, 700), context, font=get_font(22), fill=TAN, anchor="mm")

    # Bottom
    draw.text((width//2, 950), "bysengo.com", font=get_font(26, bold=True), fill=ORANGE, anchor="mm")

    return img

def main():
    output_dir = "/home/user/bysengotest"

    # Load logo
    print("Loading Sengo logo...")
    logo = load_logo()
    if logo:
        print("✓ Logo loaded successfully")
    else:
        print("⚠ Logo not found, continuing without it")

    # Create main graphics
    print("\nCreating Instagram post (1080x1080)...")
    instagram = create_instagram_post(logo)
    instagram.save(os.path.join(output_dir, "sengo_impact_instagram.png"), quality=95)

    print("Creating LinkedIn/Twitter post (1200x628)...")
    linkedin = create_linkedin_post(logo)
    linkedin.save(os.path.join(output_dir, "sengo_impact_linkedin.png"), quality=95)

    print("Creating Story format (1080x1920)...")
    story = create_story(logo)
    story.save(os.path.join(output_dir, "sengo_impact_story.png"), quality=95)

    # Create quote cards
    print("Creating founder quote cards...")
    for i, quote_data in enumerate(QUOTES):
        card = create_quote_card(logo, quote_data)
        name_slug = quote_data[1].lower().replace(' ', '_').replace('.', '')
        filename = f"sengo_quote_{i+1}_{name_slug}.png"
        card.save(os.path.join(output_dir, filename), quality=95)

    # Create highlight cards
    highlights = [
        ("$5M+", "Follow-on Capital", "Influenced by supported founders"),
        ("167x", "Grant Multiplier", "$32,150 deployed → $5M+ raised"),
        ("19", "Founders Funded", "Building with intention"),
        ("46.5%", "Email Open Rate", "2x industry average"),
    ]

    print("Creating stat highlight cards...")
    for i, (num, label, context) in enumerate(highlights):
        card = create_highlight_card(logo, num, label, context)
        filename = f"sengo_highlight_{i+1}_{label.lower().replace(' ', '_').replace('-', '_')}.png"
        card.save(os.path.join(output_dir, filename), quality=95)

    print(f"\n✓ Done! Graphics saved to {output_dir}")
    print("\nFiles created:")
    print("  Main graphics:")
    print("    - sengo_impact_instagram.png (1080x1080)")
    print("    - sengo_impact_linkedin.png (1200x628)")
    print("    - sengo_impact_story.png (1080x1920)")
    print("  Quote cards:")
    print("    - sengo_quote_1_jasmine_bowie.png")
    print("    - sengo_quote_2_rama_afullo.png")
    print("    - sengo_quote_3_sengo_founder.png")
    print("  Highlight cards:")
    print("    - sengo_highlight_1_follow_on_capital.png")
    print("    - sengo_highlight_2_grant_multiplier.png")
    print("    - sengo_highlight_3_founders_funded.png")
    print("    - sengo_highlight_4_email_open_rate.png")

if __name__ == "__main__":
    main()
