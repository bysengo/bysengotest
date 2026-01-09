# Investor Questionnaire Block - Implementation Guide

## Overview
This is a styled questionnaire block designed for the investor checkout/payment page at `app.bysengo.com/investor-enrollment`. The block embeds an external form while maintaining the Sengo brand styling.

## File
- `investor-questionnaire-block.html` - Complete standalone HTML file with embedded questionnaire

## Features
- **Branded Styling**: Matches the main Sengo website design system
  - Colors: Dark Green (#1B3533), Brown (#67441A), Orange (#D57028), Cream (#F3EDE7)
  - Fonts: Arimo (headings), Montserrat (body)
  - Smooth animations and transitions
- **Embedded Form**: Uses the external form embed script from `app.bysengo.com`
- **Responsive Design**: Mobile-friendly with breakpoints at 768px
- **Professional UI**: Impact badge, styled container, fade-in animations

## Usage

### Option 1: Standalone Page
Simply host the `investor-questionnaire-block.html` file and link to it from your checkout flow.

### Option 2: Embed in Existing Page
Copy the contents of the file and insert into your checkout page where you want the questionnaire to appear.

### Option 3: Extract Just the Block
Copy the following sections from the file:
1. The `<style>` block (lines 10-225)
2. The `.questionnaire-container` div (lines 227-283)
3. The `<script>` block (lines 287-321)

Then insert into your payment page HTML.

## Customization

### Change the Heading
Edit line 274-276:
```html
<h2>Tell Us About Your Investment Goals</h2>
<p class="subtitle">
  Your custom subtitle text here...
</p>
```

### Change the Badge Text
Edit line 273:
```html
<span class="impact-badge">Investment Profile</span>
```

### Adjust Colors
The main colors are defined in the styles:
- Primary Dark: `#1B3533`
- Brown Accent: `#67441A`
- Orange Highlight: `#D57028`
- Light Background: `#F3EDE7`

### Update Embed Code
If you need to change the embedded form, update line 281:
```html
<script src="https://app.bysengo.com/forms/[YOUR_FORM_ID]/embed.js"></script>
```

## Integration Notes

1. **Font Loading**: The file uses Google Fonts (Arimo and Montserrat). These are loaded via CDN at the top of the file.

2. **Responsive Behavior**:
   - Desktop: Full 800px width container
   - Mobile (≤768px): Adjusted padding and font sizes

3. **Animation**: The section fades in on page load for a professional appearance

4. **Form Styling**: JavaScript applies Montserrat font family to embedded form elements to ensure brand consistency

## Browser Support
- Modern browsers (Chrome, Firefox, Safari, Edge)
- Mobile browsers (iOS Safari, Chrome Mobile)
- IE11+ (with potential minor styling differences)

## Questions?
Contact the Sengo development team or refer to the main landing page files for additional styling examples.
