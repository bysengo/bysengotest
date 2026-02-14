#!/usr/bin/env python3
"""Generate a banner-style GIF that swipes through Fashion x Futures brands."""

import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import os

# Brand data: name, logo URL, dark background (True = grey bg for white logos)
brands = [
    ("FAR FROM PRIVACY", "https://images.squarespace-cdn.com/content/v1/64bef9c843c01a1201d98873/44939674-65e3-4d6d-878f-7a1a62b6a5e0/FFP_DESIGN2_NY-BLK.png?format=750w", False),
    ("A Grimm Company", "https://images.squarespace-cdn.com/content/v1/64bef9c843c01a1201d98873/354f6120-c6ee-4c61-a02f-d5e6e5001f50/AGCtransparent-blk.png?format=750w", False),
    ("ar*ky*ved", "https://images.squarespace-cdn.com/content/v1/64bef9c843c01a1201d98873/8e860dbb-53c3-4e9e-8c48-84ba1e55533f/arkyvedlogo-blk.png?format=750w", False),
    ("Aworan", "https://images.squarespace-cdn.com/content/v1/64bef9c843c01a1201d98873/829c358f-c5db-4257-ad36-57f297eb38a0/Aworan+logo+blk.png?format=750w", False),
    ("Favelo World Wide", "https://images.squarespace-cdn.com/content/v1/64bef9c843c01a1201d98873/e03754e1-8509-4603-9836-e88858053dd9/favelo+logo.png?format=750w", False),
    ("Hause of Oninku", "https://images.squarespace-cdn.com/content/v1/64bef9c843c01a1201d98873/006761f3-ccde-478e-9db6-1f4c1b08eb87/oninku-logo-blk.png?format=750w", False),
    ("Hoop York City", "https://images.squarespace-cdn.com/content/v1/64bef9c843c01a1201d98873/ab8887f4-49c0-4c4c-b2a6-54ebe05a7644/HYC_Graphic.png?format=750w", False),
    ("J.Lew Atelier", "https://images.squarespace-cdn.com/content/v1/64bef9c843c01a1201d98873/1baab940-2994-40c8-995f-27d318ef4cdc/LewLogo.png?format=750w", False),
    ("Justin Mensinger", "https://images.squarespace-cdn.com/content/v1/64bef9c843c01a1201d98873/316ba488-b8c0-44c8-99e4-a92ad4518e8b/Untitled+design.png?format=750w", False),
    ("Maddy Kelly", "https://images.squarespace-cdn.com/content/v1/64bef9c843c01a1201d98873/a86da67a-7a9e-466b-9b4a-a7b78eb42abc/Maddy+Kelly+transparent+logo.png?format=750w", False),
    ("Maison Ravi", "https://images.squarespace-cdn.com/content/v1/64bef9c843c01a1201d98873/39c321aa-516c-40ea-bb0b-1b51c3c75a23/MaisonRavi.png?format=750w", False),
    ("Maya Winston", "https://images.squarespace-cdn.com/content/v1/64bef9c843c01a1201d98873/cfc10aae-db7d-4b24-9fb3-c5b262889e8a/MAYA-WINSTON-logo-blk.png?format=750w", False),
    ("Michael Wright", "https://images.squarespace-cdn.com/content/v1/64bef9c843c01a1201d98873/8cbf6e6b-9b02-4d9b-aeb0-d177829ae39a/MIchael+Wright+logo+blk.png?format=750w", False),
    ("Mingo by Domingo", "https://images.squarespace-cdn.com/content/v1/64bef9c843c01a1201d98873/9516c573-83f2-48b6-a7b6-9cac60ef0e8d/Mingo+logo+blk.png?format=750w", False),
    ("SHOP NIKITA", "https://images.squarespace-cdn.com/content/v1/64bef9c843c01a1201d98873/afffa300-7d37-4e5a-8652-faaac9f37a91/SHOP+NIKITA+brand+logo.png?format=750w", False),
    ("Oberon Asscher", "https://images.squarespace-cdn.com/content/v1/64bef9c843c01a1201d98873/5014ed46-23eb-48be-bb44-a5099dd11b97/oa-logo-blk.png?format=750w", False),
    ("SoulMaison", "https://images.squarespace-cdn.com/content/v1/64bef9c843c01a1201d98873/b45be828-6785-42db-b2fa-a79fb73160cf/SoulMaison_MainLogo_Normal.png?format=750w", False),
    ("Starfish Mrkt", "https://images.squarespace-cdn.com/content/v1/64bef9c843c01a1201d98873/2d49da5f-293e-4ca7-89bf-7660030d2daf/STARFISH-MRKT-LOGO-logo-blk.png?format=750w", False),
    ("Studio Tanaïs", "https://images.squarespace-cdn.com/content/v1/64bef9c843c01a1201d98873/d80e6fbc-58b3-413c-bbdf-c2ea29f62a6e/Untitled+design+%281%29.png?format=750w", False),
    ("Verdictstillout", "https://images.squarespace-cdn.com/content/v1/64bef9c843c01a1201d98873/33fbdd4e-b6cc-4cf2-a43a-500c8c45061e/VERDICT4.png?format=750w", False),
    ("Wildly Black", "https://images.squarespace-cdn.com/content/v1/64bef9c843c01a1201d98873/1564fe8e-cd81-4b83-9f91-d1e5495b5b6e/wildlyblack-black+%284%29.png?format=750w", False),
    ("Ru by Rupal", "https://images.squarespace-cdn.com/content/v1/64bef9c843c01a1201d98873/668c945a-a178-49e1-8a0e-3f6f2b144fad/ru-logo-upward.png?format=750w", True),
]

# Banner dimensions (email-friendly)
BANNER_W = 600
BANNER_H = 250
BG_COLOR = (45, 48, 47)        # #2d302f grey
ACCENT_COLOR = (213, 112, 40)  # #D57028 orange
TEXT_COLOR = (243, 237, 231)    # #F3EDE7 cream
LOGO_AREA_H = 170
LOGO_MAX = 140
FRAME_DURATION = 1800  # ms per brand
TRANSITION_FRAMES = 6
TRANSITION_MS = 50

def download_logo(url):
    """Download and return a PIL Image."""
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers, timeout=15)
        r.raise_for_status()
        img = Image.open(BytesIO(r.content)).convert("RGBA")
        return img
    except Exception as e:
        print(f"  Failed to download: {e}")
        return None

def fit_logo(logo, max_w, max_h):
    """Resize logo to fit within bounds, maintaining aspect ratio."""
    w, h = logo.size
    ratio = min(max_w / w, max_h / h)
    new_w = int(w * ratio)
    new_h = int(h * ratio)
    return logo.resize((new_w, new_h), Image.LANCZOS)

def create_brand_frame(logo_img, brand_name, is_dark_bg=False):
    """Create a single banner frame for a brand."""
    frame = Image.new("RGBA", (BANNER_W, BANNER_H), BG_COLOR + (255,))
    draw = ImageDraw.Draw(frame)

    # Top accent line
    draw.rectangle([(0, 0), (BANNER_W, 3)], fill=ACCENT_COLOR)

    # Logo area
    if logo_img:
        fitted = fit_logo(logo_img, LOGO_MAX, LOGO_MAX)
        # White card behind logo
        card_w = fitted.width + 40
        card_h = fitted.height + 30
        card_x = (BANNER_W - card_w) // 2
        card_y = 20
        if is_dark_bg:
            draw.rounded_rectangle(
                [(card_x, card_y), (card_x + card_w, card_y + card_h)],
                radius=12, fill=(45, 48, 47, 255)
            )
        else:
            draw.rounded_rectangle(
                [(card_x, card_y), (card_x + card_w, card_y + card_h)],
                radius=12, fill=(255, 255, 255, 255)
            )
        logo_x = (BANNER_W - fitted.width) // 2
        logo_y = card_y + (card_h - fitted.height) // 2
        frame.paste(fitted, (logo_x, logo_y), fitted)

    # Brand name at bottom
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
    except:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), brand_name, font=font)
    tw = bbox[2] - bbox[0]
    tx = (BANNER_W - tw) // 2
    ty = BANNER_H - 45
    draw.text((tx, ty), brand_name, fill=TEXT_COLOR, font=font)

    # Subtitle
    try:
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
    except:
        small_font = ImageFont.load_default()

    sub = "Fashion x Futures  •  22 Brands"
    bbox2 = draw.textbbox((0, 0), sub, font=small_font)
    sw = bbox2[2] - bbox2[0]
    sx = (BANNER_W - sw) // 2
    sy = BANNER_H - 22
    draw.text((sx, sy), sub, fill=ACCENT_COLOR, font=small_font)

    # Bottom accent line
    draw.rectangle([(0, BANNER_H - 3), (BANNER_W, BANNER_H)], fill=ACCENT_COLOR)

    return frame.convert("RGBA")

def create_slide_transition(frame_from, frame_to, steps=6):
    """Create transition frames sliding left."""
    frames = []
    for i in range(1, steps + 1):
        progress = i / steps
        offset = int(BANNER_W * progress)
        combined = Image.new("RGBA", (BANNER_W, BANNER_H), BG_COLOR + (255,))
        # Old frame sliding left
        combined.paste(frame_from, (-offset, 0))
        # New frame entering from right
        combined.paste(frame_to, (BANNER_W - offset, 0))
        frames.append(combined.convert("P", palette=Image.ADAPTIVE, colors=256))
    return frames

def main():
    print("Downloading logos...")
    logos = []
    for i, (name, url, dark) in enumerate(brands):
        print(f"  [{i+1}/22] {name}")
        logo = download_logo(url)
        logos.append(logo)

    print("\nGenerating frames...")
    brand_frames = []
    for i, (name, url, dark) in enumerate(brands):
        frame = create_brand_frame(logos[i], name, dark)
        brand_frames.append(frame)

    print("Building GIF with transitions...")
    gif_frames = []
    durations = []

    for i in range(len(brand_frames)):
        # Static frame (hold)
        static = brand_frames[i].convert("P", palette=Image.ADAPTIVE, colors=256)
        gif_frames.append(static)
        durations.append(FRAME_DURATION)

        # Transition to next
        next_i = (i + 1) % len(brand_frames)
        trans = create_slide_transition(brand_frames[i], brand_frames[next_i], TRANSITION_FRAMES)
        gif_frames.extend(trans)
        durations.extend([TRANSITION_MS] * TRANSITION_FRAMES)

    output = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fxf-brand-banner.gif")
    print(f"Saving GIF to {output}...")

    gif_frames[0].save(
        output,
        save_all=True,
        append_images=gif_frames[1:],
        duration=durations,
        loop=0,
        optimize=False,
    )

    size_kb = os.path.getsize(output) / 1024
    print(f"\nDone! Created {output}")
    print(f"Size: {size_kb:.0f} KB")
    print(f"Dimensions: {BANNER_W}x{BANNER_H}")
    print(f"Brands: {len(brands)}")

if __name__ == "__main__":
    main()
