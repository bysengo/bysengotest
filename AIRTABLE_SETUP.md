# Airtable Setup Guide for ClubStack

## Quick Start

ClubStack works out of the box with sample data. To persist data in Airtable, follow these steps.

## 1. Create an Airtable Base

1. Go to [airtable.com](https://airtable.com) and sign in (or create a free account)
2. Click **Create a base** → name it **ClubStack**

## 2. Create the "Clubs" Table

Create a table called **Clubs** with these fields:

| Field Name          | Type            | Notes                              |
|---------------------|-----------------|------------------------------------|
| Name                | Single line text| Club name (primary field)          |
| Tagline             | Single line text| Short one-liner                    |
| Description         | Long text       | Full club description              |
| Investment Focus    | Single select   | stocks, real-estate, crypto, startups, esg, mixed |
| Strategy            | Single select   | Growth, Value, Income, Aggressive, Conservative, Balanced |
| Min Investment      | Number (integer)| Minimum monthly contribution ($)   |
| Max Investment      | Number (integer)| Maximum monthly contribution ($)   |
| Max Members         | Number (integer)| Member cap                         |
| Current Members     | Number (integer)| Current member count               |
| Meeting Frequency   | Single select   | Weekly, Bi-Weekly, Monthly, Quarterly |
| Format              | Single select   | Virtual, In-Person, Hybrid         |
| Location            | Single line text| City, state or "Remote"            |
| Decision Making     | Single select   | Majority Vote, Super Majority, Unanimous, Fund Manager Decides |
| Experience Level    | Single select   | Beginner Friendly, Intermediate, Advanced, Accredited Investors Only |
| Tags                | Single line text| Comma-separated (e.g. "tech, ai-ml, large-cap") |
| Founder Name        | Single line text| Club creator's name                |
| Founder Email       | Email           | Club creator's email               |
| Color               | Single line text| Hex color for branding (e.g. #6366f1) |
| Cover Image         | Attachment      | Optional cover photo               |
| Rules               | Long text       | Club rules / requirements          |

## 3. Create the "Interest" Table

Create a table called **Interest** with these fields:

| Field Name  | Type            | Notes                    |
|-------------|-----------------|--------------------------|
| Club Name   | Single line text| Which club they're interested in |
| Club ID     | Single line text| Airtable record ID of the club |
| Name        | Single line text| Investor's name          |
| Email       | Email           | Investor's email         |
| Message     | Long text       | Optional intro message   |
| Date        | Date            | When interest was expressed |

## 4. Create a Personal Access Token

1. Go to [airtable.com/create/tokens](https://airtable.com/create/tokens)
2. Click **Create new token**
3. Give it a name like "ClubStack"
4. Under **Scopes**, select:
   - `data.records:read`
   - `data.records:write`
5. Under **Access**, select your **ClubStack** base
6. Click **Create token** and copy it

## 5. Find Your Base ID

1. Open your ClubStack base in Airtable
2. Look at the URL: `https://airtable.com/appXXXXXXXXXXXXXX/...`
3. The Base ID is the part starting with `app` (e.g. `appABC123def456`)

## 6. Configure in ClubStack

1. Open the app and click the **Airtable Settings** gear icon in the footer
2. Paste your **Personal Access Token**
3. Paste your **Base ID**
4. Table names default to "Clubs" and "Interest" — change if you named them differently
5. Click **Save & Connect**

The app will test the connection and start loading clubs from your Airtable base.

## How It Works

- **Creating a club**: Data is sent to the Clubs table via the Airtable API
- **Expressing interest**: Investor info is sent to the Interest table
- **Browsing clubs**: Clubs are fetched from Airtable on page load
- **Offline fallback**: If Airtable is not connected, the app uses sample data and localStorage

## Field Mapping

The app is flexible with field names. It looks for these variations:

- Club name: `Name` or `Club Name`
- Focus: `Focus` or `Investment Focus`
- Min investment: `Min Investment` or `Min Monthly`
- Members: `Current Members`
- Image: `Image` or `Cover Image` (attachment)

## Tips

- Use Airtable's **Forms** feature to create an alternative club submission form
- Set up Airtable **Automations** to email founders when new interest comes in
- Use **Views** to filter clubs by focus area, sort by member count, etc.
- The **Interest** table gives you a CRM of potential members — use it!
