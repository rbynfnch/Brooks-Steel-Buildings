// Pulls one month of GA4 + Search Console data into data/auto/YYYY-MM.json.
// UNTESTED against live APIs (no credentials were available when written). Run it once with real
// credentials and compare the output against the GA4 and Search Console UIs before trusting it.
//
// Setup: npm i googleapis. Create a Google Cloud service account, enable the "Google Analytics Data API"
// and "Search Console API", then add the service account email as a Viewer on the GA4 property and as a
// user on the Search Console property. Never commit the key file.
//
// Usage: GOOGLE_APPLICATION_CREDENTIALS_JSON='<key json>' (or GOOGLE_APPLICATION_CREDENTIALS=/path/key.json) GA4_PROPERTY_ID=123456789 \
//        GSC_SITE=sc-domain:brookssteelbuildings.com QUOTE_EVENT=form_submit PHONE_EVENT=contact_link_click \
//        node scripts/pull-google.mjs 2026-09   (add --diagnose to list events and check what the quote/phone events really count)
import { google } from 'googleapis';
import { writeFileSync, mkdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const month = process.argv[2];
if (!/^\d{4}-\d{2}$/.test(month || '')) { console.error('Usage: node scripts/pull-google.mjs YYYY-MM'); process.exit(1); }
const { GA4_PROPERTY_ID = '542996053', GSC_SITE = 'sc-domain:brookssteelbuildings.com', QUOTE_EVENT = 'form_submit', PHONE_EVENT = 'contact_link_click' } = process.env;
if (!GA4_PROPERTY_ID || !GSC_SITE) { console.error('Set GA4_PROPERTY_ID and GSC_SITE'); process.exit(1); }

const [y, m] = month.split('-').map(Number);
const start = `${month}-01`;
const end = new Date(Date.UTC(y, m, 0)).toISOString().slice(0, 10); // last day of month

// Key comes from GOOGLE_APPLICATION_CREDENTIALS_JSON (the key file's contents, from the environment secret)
// or, failing that, from the file named by GOOGLE_APPLICATION_CREDENTIALS.
// GOOGLE_APPLICATION_CREDENTIALS_BASE64 (the same JSON, base64-encoded) is accepted for environments that mangle raw JSON.
const rawKey = process.env.GOOGLE_APPLICATION_CREDENTIALS_JSON || (process.env.GOOGLE_APPLICATION_CREDENTIALS_BASE64 && Buffer.from(process.env.GOOGLE_APPLICATION_CREDENTIALS_BASE64, 'base64').toString('utf8'));
let credentials;
try { credentials = rawKey ? JSON.parse(rawKey) : undefined; }
catch { // never print the parse error: Node echoes the whole input, which here is a private key
  console.error('Service-account key is not valid JSON (the secret was probably mangled: quotes stripped or \\n altered).\nSet GOOGLE_APPLICATION_CREDENTIALS_BASE64 to the base64 of the key file instead (base64 -w0 key.json).'); process.exit(1);
}
const auth = new google.auth.GoogleAuth({ credentials, scopes: ['https://www.googleapis.com/auth/analytics.readonly', 'https://www.googleapis.com/auth/webmasters.readonly'] });
const ga = google.analyticsdata({ version: 'v1beta', auth });
const sc = google.searchconsole({ version: 'v1', auth });
const property = `properties/${GA4_PROPERTY_ID}`;
const dateRanges = [{ startDate: start, endDate: end }];
const run = async (body) => (await ga.properties.runReport({ property, requestBody: { dateRanges, ...body } })).data.rows || [];
const num = (r, i) => Number(r.metricValues[i].value);
const eventFilter = (name) => ({ filter: { fieldName: 'eventName', stringFilter: { value: name } } });

if (process.argv.includes('--diagnose')) {
  // Verification aid: what events fired, where form_submit happened, and what contact_link_click clicked.
  const show = async (title, body) => { try { const r = await run(body); console.log('\n' + title); r.forEach((x) => console.log('  ', x.dimensionValues.map((d) => d.value).join(' | '), '=>', x.metricValues[0].value)); } catch (e) { console.log('\n' + title, 'FAILED:', e.message); } };
  await show('Events', { dimensions: [{ name: 'eventName' }], metrics: [{ name: 'eventCount' }], orderBys: [{ metric: { metricName: 'eventCount' }, desc: true }], limit: 30 });
  await show('form_submit by page', { dimensions: [{ name: 'pagePath' }], metrics: [{ name: 'eventCount' }], dimensionFilter: eventFilter(QUOTE_EVENT), orderBys: [{ metric: { metricName: 'eventCount' }, desc: true }], limit: 15 });
  await show(PHONE_EVENT + ' by link URL', { dimensions: [{ name: 'linkUrl' }], metrics: [{ name: 'eventCount' }], dimensionFilter: eventFilter(PHONE_EVENT), orderBys: [{ metric: { metricName: 'eventCount' }, desc: true }], limit: 15 });
  process.exit(0);
}

const [totals] = await run({ metrics: [{ name: 'activeUsers' }, { name: 'sessions' }, { name: 'engagementRate' }] });
const eventCount = async (name) => (await run({ metrics: [{ name: 'eventCount' }], dimensionFilter: eventFilter(name) }))[0];
const quotes = await eventCount(QUOTE_EVENT), phone = await eventCount(PHONE_EVENT);
const quoteBySource = await run({ dimensions: [{ name: 'sessionDefaultChannelGroup' }], metrics: [{ name: 'eventCount' }], dimensionFilter: eventFilter(QUOTE_EVENT) });
const sessionsBySource = await run({ dimensions: [{ name: 'sessionDefaultChannelGroup' }], metrics: [{ name: 'sessions' }] });
const aiRows = await run({ dimensions: [{ name: 'sessionSource' }], metrics: [{ name: 'sessions' }], dimensionFilter: { filter: { fieldName: 'sessionSource', stringFilter: { matchType: 'PARTIAL_REGEXP', value: 'chatgpt|openai|perplexity|gemini|copilot|claude' } } } });
const pages = await run({ dimensions: [{ name: 'landingPage' }], metrics: [{ name: 'sessions' }], orderBys: [{ metric: { metricName: 'sessions' }, desc: true }], limit: 5 });
const devices = await run({ dimensions: [{ name: 'deviceCategory' }], metrics: [{ name: 'sessions' }] });
const obj = (rows) => Object.fromEntries(rows.map((r) => [r.dimensionValues[0].value, num(r, 0)]));
const sessions = num(totals, 1);

const gscQuery = async (dimensions, rowLimit = 25) => (await sc.searchanalytics.query({ siteUrl: GSC_SITE, requestBody: { startDate: start, endDate: end, dimensions, rowLimit } })).data.rows || [];
const gscTotals = await gscQuery([], 1);
const queries = await gscQuery(['query'], 250);
const branded = queries.filter((r) => /brooks/i.test(r.keys[0])).reduce((a, r) => a + r.clicks, 0);
const clicks = gscTotals[0]?.clicks ?? 0;

const out = {
  month,
  ga4: {
    users: num(totals, 0), sessions, engagementRate: num(totals, 2),
    quoteRequests: quotes ? num(quotes, 0) : 0, phoneClicks: phone ? num(phone, 0) : 0,
    // TODO: GA4 cannot know spam. Subtract spam submissions (count them from Gravity Forms) or set manually.
    spamFiltered: 0, formStarts: 0,
    quoteRequestsBySource: obj(quoteBySource), sessionsBySource: obj(sessionsBySource),
    aiSessions: aiRows.reduce((a, r) => a + num(r, 0), 0),
    topLandingPages: pages.map((r) => ({ page: r.dimensionValues[0].value, sessions: num(r, 0), quotes: 0 })), // TODO: quotes per landing page
    devices: Object.fromEntries(Object.entries(obj(devices)).map(([k, v]) => [k, v / sessions])),
  },
  gsc: {
    clicks, impressions: gscTotals[0]?.impressions ?? 0, avgPosition: gscTotals[0]?.position ?? 0,
    brandedClicks: branded, nonBrandedClicks: clicks - branded,
    keywords: queries.slice(0, 5).map((r) => ({ query: r.keys[0], clicks: r.clicks, impressions: r.impressions, position: +r.position.toFixed(1) })),
    strikingDistance: queries.filter((r) => r.position >= 8 && r.position <= 20).sort((a, b) => b.impressions - a.impressions).slice(0, 5).map((r) => ({ query: r.keys[0], position: +r.position.toFixed(1), impressions: r.impressions })),
    lowCtrPages: (await gscQuery(['page'], 100)).filter((r) => r.impressions > 1000 && r.ctr < 0.02).slice(0, 5).map((r) => ({ page: new URL(r.keys[0]).pathname, impressions: r.impressions, ctr: r.ctr })),
  },
};
const dir = join(dirname(fileURLToPath(import.meta.url)), '../data/auto');
mkdirSync(dir, { recursive: true });
writeFileSync(join(dir, `${month}.json`), JSON.stringify(out, null, 2));
console.log(`Wrote data/auto/${month}.json. Now fill data/manual/${month}.json (see TEMPLATE.json) and run node scripts/build-data.mjs`);
