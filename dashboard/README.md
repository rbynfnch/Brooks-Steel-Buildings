# Monthly dashboard

Open `index.html` in a browser (no server needed). **Brooks report** is the client view; **Audit** is internal.
"Save report as PDF" prints only the Brooks view (choose "Save as PDF" in the print dialog).

## Each month
1. `node scripts/pull-google.mjs YYYY-MM` writes GA4 + Search Console data to `data/auto/`
   (needs credentials, see the header of that script; untested until first run with real credentials).
2. Copy `data/TEMPLATE.json` to `data/manual/YYYY-MM.json` and fill in: Google Business Profile numbers,
   PageSpeed/index/backlink numbers, the AI-answer prompt panel results, Brooks's lead outcomes
   (`"leads": {"received":0,"qualified":0,"won":0}`; leave `null` until he reports), and the narrative bullets.
3. `node scripts/build-data.mjs` then reload `index.html`.

## Sample data
`node scripts/make-sample.mjs` fills `data/` with clearly flagged sample data for layout review.
Remove it before real use (delete `data/auto/*` and `data/manual/*`); real months are not flagged `sample`.

## Privacy
This repo is public. `data/` is git-ignored so real client metrics and any credentials are never committed.
Never commit service-account keys.

## Metric split
Brooks sees outcomes (quote requests, calls, conversion, search clicks, AI answer visibility, Business Profile
actions, lead-to-customer) plus the narrative. The Audit view holds diagnostics (form funnel, spam, landing pages,
striking-distance keywords, technical health, AI crawler hits, competitor citations).
