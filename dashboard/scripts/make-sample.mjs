// Generates SAMPLE monthly data (clearly flagged sample:true) so the dashboard can be
// reviewed before real GA4 / Search Console credentials exist.
// Usage: node scripts/make-sample.mjs   (overwrites data/auto and data/manual)
import { writeFileSync, mkdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
mkdirSync(join(root, 'data/auto'), { recursive: true });
mkdirSync(join(root, 'data/manual'), { recursive: true });

let seed = 42;
const rnd = () => ((seed = (seed * 1664525 + 1013904223) % 4294967296) / 4294967296);
const jitter = (n, pct = 0.08) => Math.round(n * (1 + (rnd() - 0.5) * 2 * pct));

// Construction seasonality: peaks late spring/summer, trough in winter.
const season = [0.72, 0.75, 0.9, 1.05, 1.2, 1.25, 1.2, 1.15, 1.05, 0.98, 0.85, 0.72];

const months = [];
for (let y = 2024, m = 9; !(y === 2026 && m === 10); m++) {
  if (m === 13) { m = 1; y++; }
  months.push({ y, m, key: `${y}-${String(m).padStart(2, '0')}` });
}

months.forEach((mo, i) => {
  const growth = 1 + i * 0.022; // steady SEO/AEO improvement
  const s = season[mo.m - 1];
  const users = jitter(2400 * growth * s);
  const sessions = jitter(users * 1.28);
  const quoteRequests = jitter(users * (0.0155 + i * 0.00025));
  const phoneClicks = jitter(users * 0.021);
  const share = { 'Organic search': 0.46 + i * 0.004, 'Direct': 0.22, 'AI assistants': 0.003 + i * 0.0006, 'Referral': 0.1, 'Social': 0.07, 'Paid': 0.12 - i * 0.002 };
  const tot = Object.values(share).reduce((a, b) => a + b, 0);
  const bySrc = (n) => Object.fromEntries(Object.entries(share).map(([k, v]) => [k, Math.round(n * v / tot)]));
  const impressions = jitter(52000 * growth * s * (1 + i * 0.01));
  const clicks = jitter(impressions * (0.026 + i * 0.0006));
  const brandedClicks = Math.round(clicks * (0.55 - i * 0.008));
  const q = (query, c, imp, pos, prev) => ({ query, clicks: jitter(c * growth * s), impressions: jitter(imp * growth * s), position: +pos.toFixed(1), prevPosition: +prev.toFixed(1) });
  const pos = (base, slope) => Math.max(1.2, base - i * slope);

  const auto = {
    month: mo.key, sample: true,
    ga4: {
      users, sessions, engagementRate: +(0.58 + i * 0.002 + (rnd() - 0.5) * 0.02).toFixed(3),
      quoteRequests, phoneClicks, spamFiltered: jitter(quoteRequests * 0.18),
      formStarts: jitter(quoteRequests * 2.3),
      quoteRequestsBySource: bySrc(quoteRequests),
      sessionsBySource: bySrc(sessions),
      aiSessions: Math.round(sessions * share['AI assistants'] / tot),
      topLandingPages: [
        { page: '/', sessions: jitter(sessions * 0.28), quotes: jitter(quoteRequests * 0.22) },
        { page: '/steel-buildings/', sessions: jitter(sessions * 0.18), quotes: jitter(quoteRequests * 0.27) },
        { page: '/steel-garages/', sessions: jitter(sessions * 0.12), quotes: jitter(quoteRequests * 0.16) },
        { page: '/pricing/', sessions: jitter(sessions * 0.09), quotes: jitter(quoteRequests * 0.19) },
        { page: '/contact/', sessions: jitter(sessions * 0.06), quotes: jitter(quoteRequests * 0.1) },
      ],
      devices: { Mobile: 0.61, Desktop: 0.34, Tablet: 0.05 },
    },
    gsc: {
      clicks, impressions, avgPosition: +pos(18, 0.15).toFixed(1), brandedClicks, nonBrandedClicks: clicks - brandedClicks,
      keywords: [
        q('steel buildings near me', 210, 6200, pos(9.5, 0.2), pos(9.5, 0.2) + 0.2),
        q('metal garage kits', 140, 4100, pos(12, 0.22), pos(12, 0.22) + 0.3),
        q('steel building prices', 120, 5600, pos(14, 0.2), pos(14, 0.2) + 0.2),
        q('pole barn vs steel building', 60, 2300, pos(11, 0.25), pos(11, 0.25) + 0.4),
        q('brooks steel buildings', 700, 1500, 1.2, 1.2),
      ],
      strikingDistance: [
        { query: 'prefab steel garage cost', position: 11.4, impressions: jitter(1800 * s) },
        { query: 'steel workshop building kits', position: 13.2, impressions: jitter(1400 * s) },
        { query: 'metal building quote online', position: 9.1, impressions: jitter(900 * s) },
      ],
      lowCtrPages: [
        { page: '/steel-garages/', impressions: jitter(9000 * s), ctr: 0.012 },
        { page: '/pricing/', impressions: jitter(7200 * s), ctr: 0.017 },
      ],
    },
    gbp: { views: jitter(1800 * growth * s), calls: jitter(34 * growth * s), directions: jitter(22 * growth * s), websiteClicks: jitter(120 * growth * s) },
    tech: {
      lcpMobileSeconds: +Math.max(2.4, 14 - i * 0.45 + (rnd() - 0.5) * 0.4).toFixed(1), cls: 0.06, inpMs: 210 - i,
      perfScoreMobile: Math.min(92, 34 + i * 2), indexedPages: 84 + Math.floor(i / 2), notIndexedPages: Math.max(2, 14 - Math.floor(i / 2)),
      errors404: Math.max(0, 9 - Math.floor(i / 3)), referringDomains: 41 + i * 2, newLinks: jitter(5), lostLinks: jitter(2, 0.4),
      aiCrawlerHits: { GPTBot: jitter(120 * (1 + i * 0.05)), ClaudeBot: jitter(60 * (1 + i * 0.05)), PerplexityBot: jitter(40 * (1 + i * 0.05)) },
    },
  };

  const aiBase = Math.min(14, 2 + Math.round(i * 0.5));
  const manual = {
    month: mo.key, sample: true,
    aeo: {
      panelSize: 20,
      // number of the 20 fixed buyer questions where Brooks is cited/mentioned, per engine
      cited: { 'ChatGPT': Math.min(20, aiBase), 'Perplexity': Math.min(20, aiBase + 1), 'Gemini': Math.max(0, aiBase - 2), 'Google AI Overviews': Math.max(0, aiBase - 3) },
      citedInAny: Math.min(20, aiBase + 3),
      competitorsCited: [{ name: 'Competitor A', prompts: 12 }, { name: 'Competitor B', prompts: 9 }, { name: 'Competitor C', prompts: 6 }],
    },
    // Reported by Brooks each month. null until he reports.
    leads: i < months.length - 1
      ? { received: quoteRequests - auto.ga4.spamFiltered, qualified: Math.round(quoteRequests * 0.55), won: Math.max(1, Math.round(quoteRequests * 0.11)) }
      : null,
    narrative: {
      done: ['Sample: rewrote the steel garages page with FAQ schema', 'Sample: fixed 3 broken internal links'],
      moved: ['Sample: quote requests up vs. same month last year'],
      next: ['Sample: add customer project gallery with captions', 'Sample: expand AI-answer prompt panel'],
    },
  };

  writeFileSync(join(root, 'data/auto', `${mo.key}.json`), JSON.stringify(auto, null, 2));
  writeFileSync(join(root, 'data/manual', `${mo.key}.json`), JSON.stringify(manual, null, 2));
});
console.log(`Wrote ${months.length} months of SAMPLE data.`);
