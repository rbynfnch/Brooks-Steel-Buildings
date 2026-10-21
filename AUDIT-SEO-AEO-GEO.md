# SEO / AEO / GEO audit of the active pages (2026-10-21)

Method: crawled the 21 live pages from outside (titles, descriptions, headings, schema, links, images, robots, sitemaps), tested AI/search crawler access, ran Google PageSpeed (mobile) on Home and Barndominiums. Nothing on the site was changed by this audit.

## Scorecard
| Area | Status |
|---|---|
| Indexability (robots, canonicals, noindex on Thank You) | Good |
| On-page basics (one H1, unique titles/descriptions, FAQ on 17 pages) | Good, with title/description length fixes |
| Internal links (20 checked) | No broken links |
| Lighthouse SEO score | 100/100 (Home, Barndominiums) |
| Structured data | FAQPage + Breadcrumb everywhere; Organization is thin; no Service schema |
| AI crawler access | GPTBot, ClaudeBot, PerplexityBot, OAI-SearchBot, Google-Extended, Googlebot, bingbot all 200; robots.txt allows all |
| llms.txt | Missing (404) |
| Speed (mobile) | 34 (Home) and 36 (Barndominiums) out of 100; LCP 20 s / 10 s; page weight 5.9 / 7.6 MB |
| Accessibility | 84 |
| Site quality signals | ~80 demo-content URLs are indexable and in the sitemap |

## Critical
1. Demo content is live and in the sitemap. 22 lorem-ipsum blog posts, 30 portfolio items (freight, trucks, "Mercedes truck", "Water freight"), 7 demo team members, 2 galleries, plus 6 categories and 10 tags: about 80 URLs next to 19 real pages. Hurts topical focus and trust for search and AI engines. Fix: trash or noindex all of it and remove from the sitemap (Yoast, Search appearance, Content types). Keep the Projects idea for real projects later.
2. Speed. Mobile 34-36. Biggest causes: oversized PNG/JPG images (Steel-Building-Design-on-Laptop-blue-bg.png 1.47 MB on every type page, design-concept.png 1.23 MB on Home, barndominium PNGs 0.67-0.70 MB each, mountain-bg 0.5 MB, hero JPGs 0.5-0.6 MB), about 1 MB of unused JavaScript, 135 KB unused CSS, CLS 0.23-0.35 (layout shift). Fix: ShortPixel bulk optimize + WebP/AVIF, resize the two 1+ MB images to display size, find the unused-JS plugins, check Cloudflare caching/minify, find the shifting element for CLS.
3. Placeholder images live. Shops page (7 placeholder references) and Equestrian page (3 photo spots + og:image = placehold.co). The social/AI preview image for both pages is a grey "Photo coming soon" box.

## High (SEO)
4. Title length. Over ~60 characters: Home 72, Equestrian 75, Barndominiums 68, Agricultural 65, Industrial 63, Recreational 60. Suggested: Home "Custom Steel Buildings in WY, UT & ID | Brooks Steel Buildings" (62); Equestrian "Steel Riding Arenas & Horse Barns | Brooks Steel Buildings" (58); Barndominiums "Steel Barndominium Buildings | Brooks Steel Buildings" (53); Flex title uses " - " instead of " | " (45 chars): "Steel Flex Buildings | Brooks Steel Buildings".
5. Meta descriptions over 160: Equestrian 167, Storage 163, Barndominiums 163. Star Valley has none.
6. Star Valley page (2297) is the old page: no meta description, no FAQ/schema, older wording, no og:image. Rebuild with the new template or fold into Wyoming and redirect.
7. No og:image on Home, Steel Buildings hub, About, Get a Quote, Star Valley. Set a default social image (Yoast, Settings, Social) and per-page images.
8. Privacy Policy has two H1s.
9. Barndominiums was missing from page-sitemap.xml when checked (Yoast sitemap cache; re-check).
10. Page titles for the state pages are short ("Wyoming Steel Buildings"); fine but could add an intent term ("Wyoming Steel Buildings | Custom Pre-Engineered Buildings | ...").

## AEO (answer engines, featured snippets)
Strengths: answer-first summary under every H1, 7-8 question FAQ with FAQPage schema on 17 pages, short direct answers, consistent facts (8 to 10 weeks, engineered for local loads).
Gaps and actions:
- No substantive guides. AI answers lean on long-form explainers. Add 6-8 evergreen articles (no invented numbers): what affects steel building cost, steel vs pole barn, snow load basics for Wyoming/Utah/Idaho, permitting steps by state, how to size a riding arena/hangar/shop, barndominium shell vs finished home and lender considerations, what is included in a building package.
- Cost question is only answered on the quote page; add a short "What affects price" section to each type page.
- Generic FAQs repeat on every type page (permit, how long, can I build it myself). Keep one or two; add type-specific questions to differentiate.
- No Service schema (type pages) or HowTo for the five-step process.

## GEO (generative engines, local entity)
- Organization schema is thin: only a Facebook sameAs; no phone or address; logo is a 887x890 JPG. A separate LocalBusiness exists only on About and is not linked to the Organization. Fix in Yoast (Organization name, square logo, FB/Instagram/LinkedIn) and publish one LocalBusiness with address, phone, areaServed (WY, UT, ID) site-wide, referenced by Service schema.
- No llms.txt. Optional; low effort. Crawlers are already allowed. Check whether Yoast's llms.txt feature is available in Settings and turn it on.
- Proof is thin: no reviews, testimonials or real project pages with locations/sizes. Add real projects (location, building type, size, year) and a few reviews; these are the strongest entity signals.
- Google Business Profile, Bing Places, directories and NAP consistency (800-908-4839, 254 City View Dr., Evanston WY 82930) not verified. Owner to confirm GBP is claimed with service areas, categories, photos.
- No author/reviewer or "last updated" on content pages.

## Accessibility (affects quality signals)
Color contrast, heading order, unnamed links, select without label (quote forms), `user-scalable=no` in the viewport tag (blocks zoom; theme setting), list items outside lists.

## Measurement
Confirm Google Search Console and Bing Webmaster Tools are set up with the sitemap submitted, and GA4 tracks form submits and the Thank You page as a conversion.

## Suggested order
1. Remove/noindex demo content (big, quick win). 2. Image compression + replace placeholders. 3. Fix titles/descriptions, privacy H1, default OG image. 4. Rebuild Star Valley. 5. Organization/LocalBusiness/Service schema. 6. Guides and real projects/reviews. 7. Accessibility fixes. 8. Search Console/GA4/GBP check.
