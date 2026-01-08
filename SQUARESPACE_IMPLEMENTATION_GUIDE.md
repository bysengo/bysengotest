# Squarespace Landing Page - Implementation Guide

## Overview
This custom code creates a beautiful landing page for Sengo with:
- Hero headline and image
- Animated logo slider featuring Forbes, NerdWallet, Nasdaq, Black Girl Ventures, and Business Insider
- Subtext section
- Interactive pathway selection (Founder/Funder/Both)
- Email capture integration

## How to Add to Squarespace

### Method 1: Code Block (Recommended for Single Page)

1. **Edit your page** in Squarespace
2. **Add a Code Block**:
   - Click an insert point (+ icon)
   - Select "Code" from the menu
3. **Paste the code**:
   - Open `squarespace-landing-page.html`
   - Copy ALL the content
   - Paste it into the Code Block
4. **Apply and Save**

### Method 2: Code Injection (For Site-Wide Header/Footer)

1. Go to **Settings > Advanced > Code Injection**
2. Paste the code into **Header** or **Footer** section
3. Click **Save**

## Customization Required

### 1. Replace Hero Image
Find this line in the code:
```html
<img src="YOUR_HERO_IMAGE_URL_HERE" alt="Sengo Hero" class="sengo-hero-image">
```

Replace `YOUR_HERO_IMAGE_URL_HERE` with your actual image URL:
- Upload image to Squarespace
- Right-click the image and select "Copy Image Address"
- Paste the URL in place of `YOUR_HERO_IMAGE_URL_HERE`

### 2. Customize Text Content

**Headline** (line ~165):
```html
<h1>Empowering the Next Generation of Founders</h1>
```

**Subtext** (line ~212):
```html
<p>Sengo is revolutionizing how founders and funders connect...</p>
```

**Thesis Section** (lines ~218-224):
Edit the heading and paragraph text to match your messaging.

### 3. Add Squarespace Form

1. In edit mode, **delete** the placeholder text that says `[Add your Squarespace Form Block here]`
2. Click the **+ icon** inside the email section
3. Select **Form** from the blocks menu
4. Configure your form fields:
   - Email (required)
   - Name (optional)
   - Any other fields you want
5. The form will automatically inherit the styling

## Logo Slider Notes

- The logos currently use publicly available images
- For **Black Girl Ventures**, you may need to replace with the official logo URL
- To replace any logo, find the corresponding `<img src="...">` tag and update the URL
- The slider automatically loops seamlessly
- Hover over logos to see them in color

## Customization Options

### Change Colors

The gradient background uses purple tones. To change:

Find this line (~90):
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

Replace with your brand colors:
```css
background: linear-gradient(135deg, #YOUR_COLOR_1 0%, #YOUR_COLOR_2 100%);
```

### Adjust Animation Speed

Logo slider speed (line ~71):
```css
animation: scroll 20s linear infinite;
```

Change `20s` to make it faster (lower number) or slower (higher number).

### Modify Button Styles

Find `.pathway-btn` styles (starting line ~103) to adjust:
- `padding`: Button size
- `font-size`: Text size
- `border-radius`: Corner roundness
- `border`: Border thickness and color

## Pathway Button Functionality

When users click a pathway button:
1. The button highlights with the "active" state
2. Their selection is saved to browser localStorage
3. You can track this with analytics (see code comments)

To add Google Analytics tracking, uncomment line ~256:
```javascript
gtag('event', 'pathway_selected', { pathway: pathway });
```

## Mobile Responsive

The design automatically adapts to mobile devices:
- Logo slider adjusts size
- Buttons stack vertically
- Text sizes reduce appropriately
- All elements remain centered and readable

## Browser Compatibility

Works in all modern browsers:
- Chrome, Firefox, Safari, Edge
- Mobile browsers (iOS Safari, Chrome Mobile)

## Troubleshooting

**Logos not appearing?**
- Check if the logo URLs are accessible
- Replace with your own uploaded images if needed

**Form not styled correctly?**
- Make sure the form block is inside the `.sengo-email-section` div
- Check that Squarespace form block is properly inserted

**Animation not smooth?**
- Clear browser cache
- Ensure JavaScript is enabled

**Buttons not working?**
- Check browser console for errors (F12)
- Ensure the script tag is included at the bottom

## Need Help?

If you encounter any issues or need customization:
1. Check the Squarespace help docs
2. Review the code comments
3. Test in a different browser
4. Contact Squarespace support for platform-specific issues

## Next Steps

After implementation:
1. Preview your page before publishing
2. Test on mobile devices
3. Test pathway button interactions
4. Submit a test form to ensure it works
5. Publish when ready!
