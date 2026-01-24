# EU Capital Pathways Navigator - Kajabi Setup Guide

## Overview
The EU Capital Pathways Navigator is a comprehensive assessment tool that helps EU founders understand their viable capital raising paths based on their specific situation.

## How to Add to Kajabi

### Method 1: Direct Page Embed (Recommended)

1. **Create a New Page in Kajabi**
   - Go to Website > Pages
   - Click "New Page"
   - Choose "Blank" template

2. **Add the HTML**
   - In the page editor, add a "Custom Code" section
   - Copy the entire contents of `eu-capital-navigator.html`
   - Paste into the Custom Code section
   - Save and publish

### Method 2: Embed in Course/Product

1. **Inside a Kajabi Product**
   - Open your Product (Course, Membership, etc.)
   - Add a new "Post" or "Lesson"
   - In the content editor, add a "Code" block
   - Paste the HTML from `eu-capital-navigator.html`
   - Save

### Method 3: Popup/Modal

1. **Create a Popup**
   - Go to Marketing > Popups
   - Create new popup
   - Use "Custom Code" block
   - Paste the HTML
   - Set display triggers (e.g., button click, time delay)

## Important Notes

### ✅ What Works
- Fully self-contained HTML (no external dependencies)
- All styling is embedded (no external CSS files)
- Pure vanilla JavaScript (no jQuery or frameworks)
- Mobile responsive design
- Works in iframes

### ⚠️ Kajabi Limitations to Consider

1. **Code Block Height**
   - Kajabi code blocks might have height restrictions
   - If content is cut off, wrap in: `<div style="min-height: 3000px;">[content]</div>`

2. **Print Functionality**
   - The "Save This Report" button uses `window.print()`
   - This works in most browsers but test in your Kajabi environment

3. **Links/Navigation**
   - Update the CTA button URLs to point to your actual Kajabi pages:
   ```javascript
   // Line ~1950 in the HTML
   onclick="window.location.href='YOUR-KAJABI-URL/founders'"
   ```

## Customization for Your Brand

### Colors
Update these CSS variables in the `<style>` section:

```css
/* Primary Brand Colors */
#1B3533  /* Dark green - main headings */
#67441A  /* Brown - secondary text */
#D57028  /* Orange - CTAs and accents */
#F3EDE7  /* Cream - backgrounds */
#717E36  /* Olive - badges */
```

### Call-to-Action URLs
The main CTA is already configured to link to the fundraising strategy call booking:

```javascript
<button class="btn btn-primary" onclick="window.location.href='https://calendly.com/ila-bysengo/fundraising'">
  Book Your Strategy Call
</button>
```

**Current pricing displayed:** €425 - €1,700 for 1:1 fundraising strategy sessions

To update the Calendly link or pricing, find the CTA section (around line 1199) and modify as needed.

### Footer Email Capture
Replace the CTA buttons with Kajabi form:

1. Create a Form in Kajabi (Marketing > Forms)
2. Copy the embed code
3. Replace the `<div class="cta-buttons">` section with your form embed

## Integration with Existing Sengo Kajabi Site

### Recommended Flow

1. **Landing Page** → Introduce the tool
2. **Navigator Tool** → Assessment (this page)
3. **Results** → Show pathways (embedded in tool)
4. **CTA** → Book strategy call / Join membership

### Gating Options

**Option A: Free Lead Magnet**
- Make tool publicly accessible
- Gate the results PDF or detailed report
- Capture email before showing results

**Option B: Member-Only**
- Require login to access tool
- Add to existing membership/course
- Use as value-add for paid community

**Option C: Email-Gated**
```html
<!-- Add before the questionnaire starts -->
<div id="emailGate" style="max-width: 600px; margin: 60px auto; text-align: center;">
  <h2>Get Your Free Capital Pathways Report</h2>
  <p>Enter your email to access the EU Capital Pathways Navigator</p>
  <!-- Insert Kajabi Form Embed Here -->
  <button onclick="startAssessment()">Continue to Assessment</button>
</div>

<div id="assessmentContent" style="display: none;">
  <!-- Move all existing content here -->
</div>

<script>
function startAssessment() {
  document.getElementById('emailGate').style.display = 'none';
  document.getElementById('assessmentContent').style.display = 'block';
}
</script>
```

## Tracking & Analytics

### Add Google Analytics Events
Insert this code in the results generation section:

```javascript
// After line 1095 (in generateResults function)
if (typeof gtag !== 'undefined') {
  gtag('event', 'capital_navigator_completed', {
    'incorporation': data.incorporation,
    'check_size': data.checkSize,
    'target_geo': data.targetGeo.join(',')
  });
}
```

### Kajabi Built-in Analytics
- Kajabi will automatically track page views
- Use Kajabi's conversion tracking for form submissions
- Monitor completion rates via Kajabi dashboard

## Testing Checklist

Before going live:

- [ ] Test on desktop browsers (Chrome, Firefox, Safari)
- [ ] Test on mobile devices (iOS, Android)
- [ ] Verify all 7 questions display correctly
- [ ] Complete full assessment flow
- [ ] Check results display for different scenarios
- [ ] Verify CTA buttons link to correct pages
- [ ] Test "Start Over" functionality
- [ ] Print/save functionality works
- [ ] Forms submit correctly (if added)
- [ ] No console errors (check browser developer tools)

## Support & Troubleshooting

### Common Issues

**Issue: Content is cut off**
- Add `style="min-height: 3500px; overflow: visible;"` to main container

**Issue: JavaScript not working**
- Ensure code is in "HTML" mode, not "Visual" editor
- Check Kajabi doesn't strip `<script>` tags
- Try wrapping in `<![CDATA[ ... ]]>` if needed

**Issue: Styling looks wrong**
- Kajabi might inject its own CSS
- Add `!important` to critical styles if needed
- Wrap in iframe for complete isolation

**Issue: Can't track completions**
- Use Kajabi webhooks to track form submissions
- Add custom events to JavaScript
- Integrate with Zapier for advanced tracking

## Advanced: Database Integration

If you want to store assessment results:

1. **Use Kajabi Forms** to capture data after completion
2. **Zapier Integration**: Send results to:
   - Google Sheets
   - Airtable
   - Your CRM (HubSpot, Salesforce, etc.)
3. **Custom Backend**: Send results to your own API endpoint

Example API integration:
```javascript
// Add to generateResults function
fetch('https://your-api.com/save-assessment', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(formData)
});
```

## Monetization Strategies

### 1. **Freemium Model**
- Free: Basic compatibility map
- Paid ($97): Full report + 1:1 strategy session

### 2. **Membership Upgrade**
- Free tier: Access to tool
- Premium tier ($49/mo): Monthly capital strategy updates, investor intros

### 3. **Lead Magnet → Course**
- Free tool → Capture leads
- Upsell: "EU Fundraising Masterclass" ($497)

### 4. **Consultation Funnel**
- Free tool → Show complexity
- CTA: "Book Strategy Call" ($200-$500)

## Need Help?

For technical support with Kajabi integration:
- Kajabi Support: support@kajabi.com
- Kajabi Community: community.kajabi.com
- Developer docs: developers.kajabi.com

---

**Tool Version:** 1.0
**Last Updated:** January 2026
**Compatibility:** All modern browsers, mobile responsive
