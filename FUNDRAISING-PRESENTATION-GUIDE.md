# Sengo Fundraising Presentation - Integration Guide

## Overview

This interactive presentation provides European startups with essential guidance on fundraising from U.S. investors. The presentation covers:

1. **Sengo Overview** - Who we are and our mission
2. **When is the Best Time to Have Investors?** - Timing strategies for fundraising
3. **How to Pitch to an Investor?** - Essential elements of winning pitches
4. **The Danger of Having Investors Too Early** - Risks of premature funding
5. **Can European Startups Receive U.S. Funding?** - Transatlantic funding strategies

## Features

✅ **Fully Responsive** - Works perfectly on desktop, tablet, and mobile
✅ **Smooth Animations** - Professional slide transitions and content reveals
✅ **Multiple Navigation Options** - Buttons, keyboard arrows, touch gestures, and dot navigation
✅ **Progress Indicator** - Visual progress bar shows current position
✅ **Brand Consistent** - Matches Sengo's color palette and typography
✅ **Self-Contained** - No external dependencies except Google Fonts

## File Structure

```
/fundraising-presentation.html         → Full standalone HTML version
/fundraising-presentation-embed.html   → Optimized embed code for Squarespace/Kajabi
```

---

## Integration Instructions

### Option 1: Kajabi Embedding

Kajabi allows custom HTML/CSS/JavaScript through its Custom Code blocks.

#### Steps:

1. **Log into Kajabi** and navigate to the page where you want to add the presentation
2. **Add a Custom Code Block:**
   - Click "+ Add Section" or "+ Add Element"
   - Choose "Custom Code" or "HTML/CSS/JavaScript"
3. **Copy the code:**
   - Open `fundraising-presentation-embed.html`
   - Copy the ENTIRE contents (including the HTML comment at the top)
4. **Paste into Kajabi:**
   - Paste the code into the Custom Code block
5. **Save and Publish** your page

**Kajabi-Specific Tips:**
- The presentation is wrapped in a scoped container (`.sengo-presentation`) to prevent CSS conflicts
- All JavaScript is wrapped in an IIFE to avoid namespace conflicts
- The presentation will automatically center on the page with responsive padding

---

### Option 2: Squarespace Embedding

#### Method A: Code Block (Recommended)

1. **Edit your Squarespace page**
2. **Add a Code Block:**
   - Click an insert point (+)
   - Select "Code" from the menu
3. **Copy and paste:**
   - Open `fundraising-presentation-embed.html`
   - Copy ALL the code
   - Paste it into the Code Block
4. **Click "Apply"**
5. **Save your page**

#### Method B: Code Injection (Site-Wide)

If you want the presentation available across multiple pages:

1. Go to **Settings** → **Advanced** → **Code Injection**
2. Paste the code from `fundraising-presentation-embed.html` into the **Footer** section
3. On any page where you want to display it, add an HTML element with:
   ```html
   <div id="sengo-fundraising-presentation"></div>
   ```

---

### Option 3: Standalone Webpage

Use `fundraising-presentation.html` as a standalone page:

1. **Upload to your web server** or hosting platform
2. **Link to it** from your main site
3. **Embed it in an iframe:**
   ```html
   <iframe src="fundraising-presentation.html"
           width="100%"
           height="675"
           frameborder="0"
           allowfullscreen>
   </iframe>
   ```

---

## Navigation Controls

### Desktop Users:
- **← → Arrow Keys** - Navigate between slides
- **Mouse Click** - Use arrow buttons or dots
- **Dot Indicators** - Click any dot to jump to that slide

### Mobile Users:
- **Swipe Left/Right** - Navigate between slides
- **Tap Buttons** - Use the arrow buttons
- **Tap Dots** - Jump to any slide

### Features:
- **Progress Bar** - Orange bar at top shows progress through presentation
- **Disabled States** - Previous button disabled on first slide, Next button disabled on last slide
- **Smooth Transitions** - 0.6s cubic-bezier animation between slides
- **Content Animation** - Elements fade in sequentially for professional effect

---

## Customization Options

### Changing Content

Edit the HTML slides in either file. Each slide is wrapped in:

```html
<div class="sengo-slide">
    <h2>Slide Title</h2>
    <ul>
        <li><strong>Point:</strong> Description</li>
    </ul>
    <div class="sengo-highlight-box">
        <p><strong>Callout:</strong> Important message</p>
    </div>
</div>
```

### Changing Colors

The presentation uses Sengo's brand colors:

```css
#1B3533 - Dark green (primary background)
#67441A - Brown (secondary)
#F3EDE7 - Cream (text/backgrounds)
#D57028 - Orange (accents/CTAs)
```

To change colors, find and replace the hex codes in the `<style>` section.

### Adding More Slides

1. Copy an existing `<div class="sengo-slide">...</div>` block
2. Paste it before the closing `</div>` of `.sengo-slides-wrapper`
3. Update the content
4. The navigation will automatically update (no JavaScript changes needed)

### Changing Fonts

Currently uses Google Fonts - Montserrat. To change:

1. Update the Google Fonts import link
2. Change `font-family: 'Montserrat'` in the CSS

---

## Technical Specifications

### Browser Compatibility:
- ✅ Chrome/Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

### Performance:
- **Page Weight:** ~35KB (compressed)
- **External Resources:** Only Google Fonts
- **Load Time:** < 1 second on typical connections

### Accessibility:
- Keyboard navigation support
- Semantic HTML structure
- High contrast text (WCAG AA compliant)
- Touch-friendly tap targets (50px minimum)

---

## Troubleshooting

### Presentation Not Showing

**Issue:** Code block appears blank
**Solution:**
- Ensure you copied the ENTIRE code including `<style>` and `<script>` tags
- Check that Squarespace/Kajabi hasn't stripped the code
- Try saving and refreshing the page

### Styling Conflicts

**Issue:** Presentation looks broken or fonts don't match
**Solution:**
- The embed version uses namespaced classes (`.sengo-` prefix)
- Check for CSS conflicts with page theme
- Try using `!important` on critical styles if needed

### Navigation Not Working

**Issue:** Buttons or swipes don't work
**Solution:**
- Check browser console for JavaScript errors
- Ensure the `<script>` tag wasn't removed
- Verify no other scripts are interfering

### Mobile Responsiveness

**Issue:** Presentation too large/small on mobile
**Solution:**
- The presentation is responsive by default
- Check that viewport meta tag is present: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
- Adjust padding in CSS media queries if needed

---

## Support & Customization

For custom modifications or integration support, contact your development team or refer to:

- **Squarespace Developer Docs:** https://developers.squarespace.com/
- **Kajabi Support:** https://help.kajabi.com/

---

## Version History

**v1.0** (January 2026)
- Initial release
- 5 slides covering fundraising fundamentals
- Full responsive design
- Keyboard, mouse, and touch navigation
- Optimized for Squarespace and Kajabi

---

## License & Usage

This presentation is proprietary to Sengo. All content and code are for Sengo's exclusive use. Do not redistribute without permission.

**© 2026 Sengo - Reimagining Fundraising & Investing**
