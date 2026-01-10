# Wix About Page Implementation Guide

## Overview
A sleek, modern About Me page featuring large headings, minimal text, photo sections, social links, and a contact form.

## File
`wix-about-page.html` - Complete HTML/CSS page ready for Wix

## How to Add to Wix

### Option 1: Embed Code (Recommended)
1. In Wix Editor, click the **+** button to add elements
2. Select **Embed** → **Custom Embeds** → **Embed a Widget**
3. Click **HTML iframe**
4. Copy the entire content from `wix-about-page.html`
5. Paste it into the code window
6. Adjust the frame size to fit your page

### Option 2: Custom Page Code
1. Go to **Settings** → **Custom Code**
2. Click **+ Add Custom Code**
3. Paste the HTML in the code section
4. Set to load on specific page (your About page)
5. Save and publish

## Customization Checklist

### 1. Add Your Links
Replace these placeholder URLs in the HTML:

- **Line 324**: `YOUR_SUBSTACK_URL` - Add your Substack profile URL
- **Line 333**: `YOUR_BUSINESS_URL` - Add your business website URL
- **Line 342**: `YOUR_THREADS_URL` - Add your Threads profile URL
- **Line 351**: `YOUR_LINKEDIN_URL` - Add your LinkedIn profile URL

### 2. Add Your Photos
Replace the photo placeholders (Lines 282-292):

```html
<div class="photo-placeholder">
    [Insert Photo 1]
</div>
```

Change to:

```html
<div class="photo-placeholder">
    <img src="YOUR_IMAGE_URL" alt="Description" style="width: 100%; height: 100%; object-fit: cover; border-radius: 12px;">
</div>
```

**How to get image URLs in Wix:**
1. Upload images to Wix Media Manager
2. Right-click on image → Copy Image URL
3. Use that URL in the `src` attribute

### 3. Connect Contact Form
The form at line 363 needs to be connected to Wix's form handler:

**Option A - Use Wix Form (Easier):**
1. Delete the HTML form section (lines 363-378)
2. Add a Wix Contact Form element in that space instead
3. Style it to match (dark background, white text)

**Option B - Custom Form Handler:**
Update the form action attribute:
```html
<form action="https://your-wix-form-handler" method="POST">
```

## Design Features

✨ **Large, Bold Typography** - Massive headings that command attention
📱 **Fully Responsive** - Looks great on mobile, tablet, and desktop
🎨 **Modern Gradients** - Subtle gradients for visual depth
🖼️ **Photo Grid** - Clean 3-column grid (1 column on mobile)
🔗 **Social Links** - Stylish link cards with hover effects
📝 **Contact Form** - Integrated contact form with premium styling
⚡ **Smooth Animations** - Subtle hover effects and transitions

## Color Scheme
- **Primary Background**: White (#fff)
- **Dark Section**: Near-black (#1a1a1a)
- **Accent**: Light gray gradients (#f8f9fa)
- **Text**: Dark gray (#1a1a1a, #4a4a4a)

## Quick Edits

### Change Hero Title
Line 261: Edit "About Me" to your preferred title

### Change Subtitle
Line 262: Edit "Building at the intersection of what matters most"

### Update Footer Year
Line 395: Update copyright year if needed

## Testing
1. Preview in Wix before publishing
2. Test all social links
3. Test contact form submission
4. Check mobile responsiveness
5. Verify photos display correctly

## Support
If you need help customizing:
1. Specific color changes
2. Layout adjustments
3. Additional sections
4. Animation tweaks

Just let me know what you'd like to modify!
