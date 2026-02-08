#!/usr/bin/env python3
"""
Generate branded social media graphics for Sengo 2025 Impact Report.
Creates Instagram (1080x1080), LinkedIn/Twitter (1200x628), and Story (1080x1920) formats.
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Brand colors
TEAL = (27, 53, 51)        # #1B3533
LIGHT_TEAL = (36, 74, 71)  # #244A47
ORANGE = (213, 112, 40)    # #D57028
CREAM = (243, 237, 231)    # #F3EDE7
OLIVE = (113, 126, 54)     # #717E36
TAN = (175, 129, 69)       # #AF8145
WHITE = (255, 255, 255)

# Try to load fonts, fall back to default if not available
def get_font(size, bold=False):
    font_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except:
                pass
    return ImageFont.load_default()

def draw_rounded_rect(draw, coords, radius, fill):
    """Draw a rounded rectangle."""
    x1, y1, x2, y2 = coords
    draw.rectangle([x1 + radius, y1, x2 - radius, y2], fill=fill)
    draw.rectangle([x1, y1 + radius, x2, y2 - radius], fill=fill)
    draw.ellipse([x1, y1, x1 + 2*radius, y1 + 2*radius], fill=fill)
    draw.ellipse([x2 - 2*radius, y1, x2, y1 + 2*radius], fill=fill)
    draw.ellipse([x1, y2 - 2*radius, x1 + 2*radius, y2], fill=fill)
    draw.ellipse([x2 - 2*radius, y2 - 2*radius, x2, y2], fill=fill)

def create_instagram_post():
    """Create 1080x1080 Instagram post with key stats."""
    width, height = 1080, 1080
    img = Image.new('RGB', (width, height), TEAL)
    draw = ImageDraw.Draw(img)

    # Orange accent bar at top
    draw.rectangle([0, 0, width, 8], fill=ORANGE)

    # Title
    title_font = get_font(42, bold=True)
    subtitle_font = get_font(24, bold=True)
    stat_font = get_font(72, bold=True)
    label_font = get_font(22)
    small_font = get_font(18)

    # Header
    draw.text((width//2, 80), "SENGO", font=get_font(36, bold=True), fill=ORANGE, anchor="mm")
    draw.text((width//2, 140), "2025 IMPACT REPORT", font=title_font, fill=WHITE, anchor="mm")

    # Orange accent line
    line_width = 120
    draw.rectangle([(width - line_width)//2, 175, (width + line_width)//2, 181], fill=ORANGE)

    # Stats grid - 2x3
    stats = [
        ("600+", "Members"),
        ("9,500+", "Subscribers"),
        ("$32,150", "Grants Deployed"),
        ("$5M+", "Follow-on Capital"),
        ("30+", "Events Hosted"),
        ("19", "Founders Funded"),
    ]

    cols, rows = 2, 3
    box_w, box_h = 420, 200
    start_x = (width - (cols * box_w + (cols-1) * 40)) // 2
    start_y = 230
    gap = 40

    for i, (num, label) in enumerate(stats):
        col = i % cols
        row = i // cols
        x = start_x + col * (box_w + gap)
        y = start_y + row * (box_h + 30)

        # Draw card background
        draw_rounded_rect(draw, [x, y, x + box_w, y + box_h], 16, LIGHT_TEAL)

        # Draw stat number
        draw.text((x + box_w//2, y + 75), num, font=stat_font, fill=ORANGE, anchor="mm")

        # Draw label
        draw.text((x + box_w//2, y + 150), label, font=label_font, fill=CREAM, anchor="mm")

    # Bottom tagline
    draw.text((width//2, 970), "Reimagining how communities fundraise & invest",
              font=small_font, fill=TAN, anchor="mm")
    draw.text((width//2, 1010), "bysengo.com", font=get_font(20, bold=True), fill=ORANGE, anchor="mm")

    return img

def create_linkedin_post():
    """Create 1200x628 LinkedIn/Twitter post."""
    width, height = 1200, 628
    img = Image.new('RGB', (width, height), TEAL)
    draw = ImageDraw.Draw(img)

    # Orange accent bar at top
    draw.rectangle([0, 0, width, 6], fill=ORANGE)

    # Fonts
    title_font = get_font(36, bold=True)
    stat_font = get_font(54, bold=True)
    label_font = get_font(18)
    small_font = get_font(16)

    # Left side - Title and tagline
    draw.text((60, 80), "SENGO", font=get_font(28, bold=True), fill=ORANGE)
    draw.text((60, 130), "2025 Impact Report", font=title_font, fill=WHITE)

    # Orange accent line
    draw.rectangle([60, 185, 180, 190], fill=ORANGE)

    draw.text((60, 220), "Reimagining how communities", font=get_font(20), fill=CREAM)
    draw.text((60, 250), "fundraise and invest.", font=get_font(20), fill=CREAM)

    # Key highlight stats on left
    highlight_stats = [
        ("$5M+", "Follow-on Capital"),
        ("167x", "Grant Multiplier"),
    ]

    y_pos = 320
    for num, label in highlight_stats:
        draw.text((60, y_pos), num, font=get_font(42, bold=True), fill=ORANGE)
        draw.text((60, y_pos + 50), label, font=label_font, fill=TAN)
        y_pos += 110

    # Right side - Stats grid
    stats = [
        ("600+", "Members"),
        ("9,500+", "Subscribers"),
        ("$32,150", "Grants"),
        ("19", "Founders"),
    ]

    box_w, box_h = 240, 130
    start_x = 550
    start_y = 100
    gap_x, gap_y = 30, 25

    for i, (num, label) in enumerate(stats):
        col = i % 2
        row = i // 2
        x = start_x + col * (box_w + gap_x)
        y = start_y + row * (box_h + gap_y)

        draw_rounded_rect(draw, [x, y, x + box_w, y + box_h], 12, LIGHT_TEAL)
        draw.text((x + box_w//2, y + 50), num, font=stat_font, fill=ORANGE, anchor="mm")
        draw.text((x + box_w//2, y + 100), label, font=label_font, fill=CREAM, anchor="mm")

    # Additional stats row
    extra_stats = [("30+", "Events"), ("46.5%", "Open Rate")]
    y = start_y + 2 * (box_h + gap_y)
    for i, (num, label) in enumerate(extra_stats):
        x = start_x + i * (box_w + gap_x)
        draw_rounded_rect(draw, [x, y, x + box_w, y + box_h], 12, LIGHT_TEAL)
        draw.text((x + box_w//2, y + 50), num, font=stat_font, fill=ORANGE, anchor="mm")
        draw.text((x + box_w//2, y + 100), label, font=label_font, fill=CREAM, anchor="mm")

    # Bottom
    draw.text((60, 570), "bysengo.com", font=get_font(18, bold=True), fill=ORANGE)

    return img

def create_story():
    """Create 1080x1920 Instagram/Facebook Story."""
    width, height = 1080, 1920
    img = Image.new('RGB', (width, height), TEAL)
    draw = ImageDraw.Draw(img)

    # Orange accent bar at top
    draw.rectangle([0, 0, width, 10], fill=ORANGE)

    # Fonts
    title_font = get_font(52, bold=True)
    stat_font = get_font(80, bold=True)
    label_font = get_font(26)
    small_font = get_font(22)

    # Header
    draw.text((width//2, 150), "SENGO", font=get_font(44, bold=True), fill=ORANGE, anchor="mm")
    draw.text((width//2, 230), "2025 IMPACT", font=title_font, fill=WHITE, anchor="mm")
    draw.text((width//2, 300), "REPORT", font=title_font, fill=WHITE, anchor="mm")

    # Orange accent line
    line_width = 150
    draw.rectangle([(width - line_width)//2, 350, (width + line_width)//2, 358], fill=ORANGE)

    # Stats - vertical stack
    stats = [
        ("600+", "Members Across Tiers"),
        ("9,500+", "Email Subscribers"),
        ("$32,150", "Grants Deployed"),
        ("$5M+", "Follow-on Capital"),
        ("30+", "Events Hosted"),
        ("19", "Founders Funded"),
        ("46.5%", "Email Open Rate"),
    ]

    box_w, box_h = 800, 150
    start_x = (width - box_w) // 2
    start_y = 420
    gap = 25

    for i, (num, label) in enumerate(stats):
        y = start_y + i * (box_h + gap)

        draw_rounded_rect(draw, [start_x, y, start_x + box_w, y + box_h], 16, LIGHT_TEAL)
        draw.text((start_x + 50, y + box_h//2), num, font=stat_font, fill=ORANGE, anchor="lm")
        draw.text((start_x + box_w - 50, y + box_h//2), label, font=label_font, fill=CREAM, anchor="rm")

    # Bottom tagline
    draw.text((width//2, 1780), "Reimagining how communities", font=small_font, fill=CREAM, anchor="mm")
    draw.text((width//2, 1815), "fundraise and invest.", font=small_font, fill=CREAM, anchor="mm")
    draw.text((width//2, 1870), "bysengo.com", font=get_font(26, bold=True), fill=ORANGE, anchor="mm")

    return img

def create_highlight_card(stat_num, stat_label, context=""):
    """Create a single-stat highlight card (1080x1080)."""
    width, height = 1080, 1080
    img = Image.new('RGB', (width, height), TEAL)
    draw = ImageDraw.Draw(img)

    # Orange accent bar at top
    draw.rectangle([0, 0, width, 8], fill=ORANGE)

    # Header
    draw.text((width//2, 120), "SENGO", font=get_font(36, bold=True), fill=ORANGE, anchor="mm")
    draw.text((width//2, 180), "2025 IMPACT", font=get_font(32, bold=True), fill=CREAM, anchor="mm")

    # Big stat in center
    draw.text((width//2, 480), stat_num, font=get_font(160, bold=True), fill=ORANGE, anchor="mm")
    draw.text((width//2, 620), stat_label, font=get_font(42, bold=True), fill=WHITE, anchor="mm")

    if context:
        draw.text((width//2, 720), context, font=get_font(24), fill=TAN, anchor="mm")

    # Bottom
    draw.text((width//2, 980), "bysengo.com", font=get_font(24, bold=True), fill=ORANGE, anchor="mm")

    return img

def main():
    output_dir = "/home/user/bysengotest"

    # Create main graphics
    print("Creating Instagram post (1080x1080)...")
    instagram = create_instagram_post()
    instagram.save(os.path.join(output_dir, "sengo_impact_instagram.png"), quality=95)

    print("Creating LinkedIn/Twitter post (1200x628)...")
    linkedin = create_linkedin_post()
    linkedin.save(os.path.join(output_dir, "sengo_impact_linkedin.png"), quality=95)

    print("Creating Story format (1080x1920)...")
    story = create_story()
    story.save(os.path.join(output_dir, "sengo_impact_story.png"), quality=95)

    # Create individual highlight cards
    highlights = [
        ("$5M+", "Follow-on Capital", "Influenced by supported founders"),
        ("167x", "Grant Multiplier", "$32,150 deployed → $5M+ raised"),
        ("19", "Founders Funded", "Building with intention"),
        ("46.5%", "Email Open Rate", "2x industry average"),
    ]

    print("Creating highlight cards...")
    for i, (num, label, context) in enumerate(highlights):
        card = create_highlight_card(num, label, context)
        filename = f"sengo_highlight_{i+1}_{label.lower().replace(' ', '_')}.png"
        card.save(os.path.join(output_dir, filename), quality=95)

    print(f"\nDone! Graphics saved to {output_dir}")
    print("Files created:")
    print("  - sengo_impact_instagram.png (1080x1080)")
    print("  - sengo_impact_linkedin.png (1200x628)")
    print("  - sengo_impact_story.png (1080x1920)")
    print("  - sengo_highlight_1_follow-on_capital.png")
    print("  - sengo_highlight_2_grant_multiplier.png")
    print("  - sengo_highlight_3_founders_funded.png")
    print("  - sengo_highlight_4_email_open_rate.png")

if __name__ == "__main__":
    main()
