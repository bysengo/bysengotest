// ═══════════════════════════════════════════════════════
// Sengo Dashboard Configuration
// ═══════════════════════════════════════════════════════
// Fill in your Airtable token below, then upload this
// file alongside airtable-dashboard.html.
//
// The dashboard auto-connects on page load — no setup
// screen needed. Your token stays in this file only.
//
// HOW TO GET YOUR TOKEN:
// 1. Go to https://airtable.com/create/tokens
// 2. Create a token with scopes:
//    - data.records:read
//    - schema.bases:read
// 3. Under "Access", add your base(s)
// 4. Paste the token below
// ═══════════════════════════════════════════════════════

window.SENGO_CONFIG = {
  // REQUIRED: Your Airtable Personal Access Token
  token: "patpBQcRI6cpGUQFz.1d2542f8b9d4c28b9dfa3ec69a8d21bfe162ec542f71ed445f7ce0555dd5fb10",

  // OPTIONAL: Pre-select a specific base (leave empty to auto-pick)
  // If your token only has access to one base, it's auto-selected
  baseId: "",

  // OPTIONAL: Pre-select a specific table (leave empty to auto-pick)
  // If the base only has one table, it's auto-selected
  tableId: ""
};
