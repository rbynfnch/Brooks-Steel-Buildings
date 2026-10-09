# Site audit and task list – brookssteelbuildings.com

Date: 2026-10-07. Source: one WPVibe database read (all pages/posts + Yoast meta), `site_info`, the home-page PDF and screenshots you supplied.
**Not yet verified (public site was unreachable from this environment):** rendered titles, schema/JSON-LD, page speed, link/CTA targets, form behavior, mobile layout.

## What the data shows

**Content inventory**
- 18 published pages, 22 published posts, 19 draft pages.
- All 22 posts are theme demo content ("Lorem ipsum…", "Hello world!") and are published, so they can be indexed and show in blog widgets.
- Draft pages that look needed: Contact (23), Projects (251), Gallery (1007), Testimonials (258), Team (256), Privacy Policy (3), About us (2355). Several others are leftovers: Home (OLD), three "Landing page" drafts, Sample Page, "CUSTOM DESIGN" (slug `storage`).
- Two published pages still carry demo URLs: "BUILDING TYPES" at `/logistic-services/` (16) and "STEEL BUILDING PROJECTS" at `/vehicle-fleet/` (14). Home is at slug `home-2`.
- Equestrian Riding Arenas exists twice: published (2215, ~4.8k chars) and a richer draft (2428, ~17k chars, has a meta description).

**SEO metadata (Yoast)**
- 1 of 18 published pages has a meta description (Aircraft Hangars). 0 have a custom SEO title or a focus keyword.
- The 9 building-type pages, 3 location pages, About, Get a Quote and Home have none.
- About page title says "Idaho, Utah & Wyoming"; the home page and footer say Wyoming/Utah. Addresses disagree too (Afton WY, Star Valley WY, Stansbury Park UT).

**Site health**
- 20 plugins installed: 12 active, 8 inactive.
  - Active: CoBlocks, Gravity Forms, Ninja Forms, Search Engine Visibility, Site Kit, Slider Revolution, The7 Elements, Ultimate Addons for WPBakery, WPBakery, WPVibe, Yoast Duplicate Post, Yoast SEO.
  - Inactive: Akismet, Contact Form 7, Elementor, PRO Elements, Sucuri (plugin), LayerSlider, WP Contact Slider, WPForms Lite.
- The site is built with **WPBakery**, not Elementor (Elementor is inactive). Pages 14 and 16 (and the demo posts) were built in Elementor and are published; check how they render.
- Indexing is ON (`blog_public = 1`).
- Updates available: Gravity Forms (2.7.17), Contact Form 7, WPForms Lite. Update after a backup.
- GoDaddy's network firewall (Sucuri rules, not the plugin) blocks some admin REST saves and some long SQL reads (`SQLi17`) from WPVibe. Simple reads and WP-CLI commands work.

## Task list (priority order)

### A. Quick wins (SEO / housekeeping)
1. ~~Confirm indexing is on~~ Done: indexing is ON.
2. Move the 22 demo posts to Trash or draft; remove blog widgets that point at them.
3. Write unique SEO title + meta description + focus keyword for every published page (start with Home, Steel Buildings, 9 building types, 3 location pages, About, Get a Quote).
4. Fix demo slugs with 301 redirects: `/logistic-services/`, `/vehicle-fleet/`, `/home-2/`.
5. Decide on duplicate Equestrian pages: publish the richer draft's content to the live URL, then retire the draft.
6. Make name/address/phone identical everywhere (header, footer, About, location pages, Google Business Profile). Decide whether Idaho is a real service area.
7. Publish Contact and Privacy Policy pages (forms collect personal data).
8. Delete or archive leftover drafts (Home OLD, Landing pages, Sample Page).

### B. AEO / structured data
9. Add LocalBusiness (or HomeAndConstructionBusiness) schema with consistent NAP, service area, and hours.
10. Add 5–8 question-and-answer FAQs per building-type page (cost range, size, lead time, permitting, snow load, financing) with FAQPage schema. Put a 40–60 word direct answer first.
11. Add Service schema per building type; BreadcrumbList on child pages.
12. Strengthen location pages (Utah, Wyoming, Star Valley): local project examples, snow-load/code notes, FAQs. Consider an Idaho page only if you serve it.
13. Image alt text and descriptive file names on all building photos.

### C. Lead funnel / UX
14. Review the funnel end to end: Home → building-type page → Get a Quote → thank-you. Test every form submission and confirm notification emails arrive.
15. One primary CTA per page ("Get a Quote"); demote "Design a Building" or explain what it is. Make the phone number click-to-call on mobile.
16. Expand the quote form: building type, approximate size, timeline, and a short project note. Add a visible thank-you page and conversion tracking (Google Site Kit / GA4 events).
17. Add proof: publish Projects/Gallery and Testimonials, add 3–5 photos with locations.
18. Add a quote CTA and short form on every building-type page (not only the home page).
19. Improve card "Details" buttons (contrast) and shorten the home page (it prints to 12 pages).

### D. Performance / maintenance
20. Plugin cleanup after backup: delete the 8 inactive plugins; confirm which of Gravity Forms / Ninja Forms is the live quote form and remove the other; confirm Slider Revolution is used by the hero; confirm CoBlocks is used; update Gravity Forms.
21. Ask Sucuri/GoDaddy to allow `/wp-json/wp/v2/` for logged-in admins so normal saves work.
22. Move custom CSS/PHP into the child theme and set up GitHub → GoDaddy deployment.
23. Create the 3 missing pages (Barndominiums, Custom Steel Buildings, Design Your Own) and link the home cards.

## Progress log
- 2026-10-07: Child theme `dt-the7-child` active; Theme Options copied from parent; menus intact.
- 2026-10-07: Sidebar disabled on all 10 pages under Steel Buildings (via WPVibe, `_dt_sidebar_position = disabled`).
- 2026-10-07: Owner deleted Contact Form 7, Ninja Forms, WPForms Lite. Gravity Forms is the only form plugin. **Quote form test still pending.**
- 2026-10-07: Owner trashed pages 14, 16 (also 18 News, 251 Projects, 258 Testimonials are in Trash). Main menu has no links to them.
- Keep: Slider Revolution (powers the home page hero). Still to decide: CoBlocks.
- Next: delete inactive plugins (Akismet, Elementor, PRO Elements, Sucuri, LayerSlider, WP Contact Slider) after a fresh backup; update Gravity Forms; trash the 22 demo posts.

## Decisions (NAP and service area)
- Business address (confirmed by owner): **254 City View Dr., Evanston, WY 82930**. Replaces 389 Crossfire Trail (Afton WY) and 5454 Windsor Way (Stansbury Park UT) everywhere.
- Phone: 800-908-4839 appears on the site everywhere (header, footer, PDF capture); owner to confirm it is the official number.
- Service area: Wyoming, Utah, Idaho. Drop Colorado, North Dakota, South Dakota, "Mountain West" and "nationwide / nation-wide / nationally" claims. Order: Wyoming, Utah, Idaho (HQ first) unless owner says Utah is the larger market (then Utah, Wyoming, Idaho). Use one order everywhere.

### Where the old references live (dry-run scan, 2026-10-08)
- Published pages containing old addresses or out-of-area states: Home (5), About (247), Aircraft Hangars (732), Get a Quote (1940), Utah (2275), Wyoming (2283), Star Valley (2297).
- Draft pages also containing them: Home (OLD) 2351, About us 2355, Landing page Barndo. 2320, new draft Home 2476.
- Options: 2 rows contain "Stansbury" (footer contact widget / Theme Options), 2 rows contain "Crossfire" (top bar address in `the7` AND the child copy `the7childbrookssteelbuildings`). Update the child copy first, parent copy second.
- Gravity Forms entries also contain old text (leave as historical data).
- Leftover Ninja Forms tables (`nf3_*`) remain in the database after the plugin was deleted; clean up later.
- Counts including revisions/drafts: Colorado 33, North Dakota 20, South Dakota 20, Mountain West 31, Stansbury 17, Crossfire 2, Idaho 72 (mostly page titles).

### Owner answers (2026-10-08)
- Phone 800-908-4839 confirmed.
- Remove all "nationwide / nation-wide / nationally" claims; use Wyoming, Utah and Idaho wording.
- Idaho towns to list: Swan Valley, Driggs, Rexburg, Idaho Falls, Pocatello, Preston, Montpelier.
- Star Valley page (2297): keep as is for now; improve later as a landing page.
- Apply the address/service-area changes when the WPVibe call window reopens. Plan: edit the 7 published pages and the options (child copy of Theme Options first, then parent) with targeted edits, not a global search-replace; skip drafts and old form entries; read each change back.

### Applied 2026-10-08 (service area / NAP)
- Street `5454 Windsor Way` -> `254 City View Dr.` via search-replace (posts + options), approved by owner.
- Targeted edits (WPVibe `content/edit`, revisions kept, no approval needed) on published pages: Get a Quote (1940), Home (5), About (247 incl. title), Utah (2275), Wyoming (2283). Removed Colorado / ND / SD / Mountain West / Northern Plains / nationwide wording; order is Wyoming, Utah, Idaho; "27 years" -> "30+ years"; Idaho towns list now Preston, Swan Valley, Idaho Falls, Pocatello, Driggs, Rexburg, Montpelier.
- Read-back check: no published page still contains the old terms. Drafts still do (Home OLD 2351, About us 2355, Landing page Barndo. 2320).
- Left as is by owner request: Star Valley page (2297) still says "Located in Afton, Wyoming".
- Pending owner approval (settings, not pages): top-bar address `389 Crossfire Trail, Afton, WY 83110` (2 option rows), footer widget city/zip `Stansbury Park, UT 84074`, footer accordion "services nationally" text.
- Lesson: prefer `content/edit` (targeted, keeps revisions, no approval) over database-wide search-replace for page text. Use search-replace only for serialized options.
- Open: staging links (`k9q.9e0.myftpupload.com`) in Home buttons and the Proofpoint link; owner will replace during the home page rebuild.

### Completed 2026-10-08
- Settings approved and applied: top-bar address (the7 and child options) -> 254 City View Dr., Evanston, WY 82930; footer contact widget -> same address; footer accordion "nationally" -> "in Wyoming, Utah, and Idaho".
- Verified: 0 remaining matches for Crossfire / Stansbury / nationally in the options table; none in published pages.
- Owner note: wp-admin saves (widgets, page settings) fail with "not a valid JSON response" = firewall blocking REST. Ask GoDaddy/Sucuri to allow it. WPVibe edits work.
- Task "Confirm service area + NAP" is DONE. Remaining: flush GoDaddy cache and visually confirm footer/top bar; drafts (Home OLD, About us, Landing Barndo.) still contain old text; Star Valley page (2297) left as is.

### Save problem (2026-10-08)
- wp-admin widget saves failed with "not a valid JSON response" (firewall blocking REST). GoDaddy support had owner install the **Classic Widgets** plugin; widget/sidebar saves now work. Site Health says REST API is available (read check only).
- Still to confirm: page saves (block editor / page settings) and Gravity Forms edits. If they fail, options are the Classic Editor plugin or a proper Sucuri exception for `/wp-json/` and `?rest_route=`.
- Plugin added: Classic Widgets (keep unless the firewall exception makes it unnecessary).

### Home page rebuild (draft 2476) – v1 written 2026-10-08
- Draft Home (2476) rewritten via REST (status stays draft; old content kept as revision 2513). Live Home (5) untouched.
- Sections: static-image hero (one H1, Get a Quote + Design Your Building), "What are you building?" (3 interactive banners + View All Building Types), Design It in 3D + Ready for Pricing, 5-step process (vc_section with parallax image 2484), closing CTA band with Get a Quote + Call 800-908-4839.
- Decisions: static hero (no Slider Revolution); 3 cards + link to Steel Buildings hub (249). Left out until confirmed: Featured Projects, trust badges/logos, "Trusted Since 1971", "Financially strong".
- Placeholder images by media ID: hero 2315, cards 2257/2265/2253, 3D 2370, CTA band 2086, process bg 2484. Owner to swap.
- Shortcodes use single-quoted attributes; open once in WPBakery and click Update to normalize and generate styles. Draft preview is not visible to WPVibe (404 when logged out); owner reviews via Preview.
- Publishing plan: copy final content into live Home (5) (keeps front-page setting) rather than swapping page IDs.
- Slider Revolution is no longer needed for Home once published; candidate for removal later (check other pages first).

### Home draft cards (2026-10-08)
- "What are you building?" now: Commercial and Industrial (img 2074 -> /steel-buildings/commercial/), Equestrian Riding Arenas (2073 -> /steel-buildings/equestrian-riding-arenas/), Shops and Garages (2066 -> /steel-buildings/shops/). Row has el_class `home-type-cards`.
- Page-scoped CSS stored in post meta `_wpb_post_custom_css` on draft 2476 (equal 300px card height, object-fit cover, blue gradient 0% -> 50% over the image, always-visible white text). **When publishing, copy this meta to live Home (5)** or paste into WPBakery Page Settings > Custom CSS.
- Brand blue used: rgba(26,49,83) (#1a3153).
- 2026-10-08: card CSS (meta `_wpb_post_custom_css` on 2476) updated: gradient 0% -> 80% navy, title 28px / text 20px, card height 320px, text locked in place on hover (no shift). Note: another open editor tab overwrote the draft once; keep other tabs closed while Claude edits.

### Global button radius (2026-10-08)
- The7 Theme Options (child copy `the7childbrookssteelbuildings`): `buttons-l_border_radius`, `buttons-m_border_radius`, `buttons-s_border_radius`, `header-elements-button-1-border_radius` changed from `100px` (pill) to `7px`. Fill/stroke unchanged. Owner said "7mm"; interpreted as 7px (7mm = ~26px). Easy to change.
- Not changed: header-elements-soc_icons_border_radius and microwidgets-search (100px), button-2 (already 0px), inputs (1px).
- Set `the7_force_regen_css` = 1 to rebuild The7's dynamic CSS. If buttons still look round, open The7 > Theme Options and click Save, then flush GoDaddy cache.
- Parent copy (`the7`) not changed (rollback copy).

### Home draft "reverted" investigation (2026-10-08)
- DB check: rebuild draft **2476** was intact (hero, 3 cards, class, 80% gradient CSS in `_wpb_post_custom_css`); last saved 20:20:39; no newer revisions or autosaves.
- Root cause of the second report: a separate draft **2512** titled "Home" (copy of the original live Home, 26,297 chars, created 19:41) was probably being opened instead. Rebuild renamed to "Home REBUILD (new design)". 2512 is unused; trash it when ready.
- Earlier overwrite at 20:17:46 (revision 2518) restored the v1 content; something saved an older copy once. If it recurs: only edit 2476 in one place at a time.
- Live Home (5) untouched since 18:57 (address/service-area edits).

### Button variants (2026-10-08) – PENDING (WPVibe daily limit reached)
- CSS written to `snippets/button-variants.css` (btn-orange #f68a31, btn-outline-white). Existing The7 global Custom CSS (`general-custom_css`) backed up to `backups/the7-general-custom_css-before-2026-10-08.css`; it also contains an older `.orange-button` (#ff751f) left untouched.
- To apply: append the snippet to The7 > Theme Options > Advanced > Custom CSS (or via `option patch update ... general-custom_css`), then add `el_class` to buttons on draft 2476:
  - Hero (dark): Get a Quote -> btn-orange; Design Your Building -> btn-outline-white
  - View All Building Types, Start Designing, Ready for Pricing "Get a Quote" (light) -> default blue
  - Closing band (dark): Get a Quote -> btn-orange; Call 800-908-4839 -> btn-outline-white

### Button variants APPLIED (2026-10-08)
- Banked WPVibe reset used (owner approved). `general-custom_css` in the7childbrookssteelbuildings now = original rules + `snippets/button-variants.css` (minified).
- Draft 2476: Hero Get a Quote = btn-orange; Hero Design Your Building = btn-outline-white; Closing Get a Quote = btn-orange; Closing Call 800-908-4839 = btn-outline-white. Verified in rendered output: el_class lands on the `<a class="... dt-btn ... btn-orange">`.
- Blue default kept for View All Building Types, Start Designing, Ready for Pricing Get a Quote.
- WPVibe banked resets remaining: 0. Free cap 100 calls / rolling 24h.
- Open: confirm visual result in preview (hover colors, size match with blue buttons). Old `.orange-button` (#ff751f) still in Custom CSS; remove if unused.

### Hero/CTA spacing (2026-10-08)
- Hero H1 now two lines via `<br>` (renders as `<br />` inside the single H1): "Built for Your Project." / "Engineered for the Long Haul."
- H1 margin-bottom 20px -> 32px; body text margin-bottom 40px (sub_heading_margin).
- Hero and CTA button rows tagged `hero-btns` / `cta-btns`: page-scoped CSS (meta `_wpb_post_custom_css` on 2476) makes them flex with a 20px gap; CTA row centered. Remember to copy this CSS when publishing to live Home (5).

### Styles moved to global CSS (2026-10-08)
- Card, button-row and "no gap under nav" CSS added to The7 `general-custom_css` (also in `snippets/home-rebuild.css`) because page-level `_wpb_post_custom_css` did not apply reliably in the owner's preview. DB check showed draft 2476 content + meta intact (no autosave override).
- `.page-id-2476 #main/#content {padding-top:0}` removes the gap below the header. When publishing to live Home (page 5) add `.page-id-5` selectors (do NOT add earlier: it would change the live home page now).
- Page meta CSS left in place (harmless duplicate).

### Logo update (2026-10-08) - previous values (for rollback)
- header-logo_regular: /wp-content/uploads/2020/06/BSB-Logo-57c.png (id 1752); header-logo_hd: BSB-Logo-114c.png (1756)
- header-style-mobile-logo_regular: BSB-Logo-44c.png (1748); _hd: BSB-Logo-88c.png (1754)
- bottom_bar-logo_regular: BSB-Logo-28.png (1745); bottom_bar-logo_hd: BSB-Logo-56.png (1749)
- New files (996x522 PNG): ids 2536 Black, 2537 Black_on_White, 2538 Navy, 2539 Navy_on_White, 2540 White, 2541 White_on_Black.
- Plan: header + mobile = Navy (2538); footer bottom bar (dark #373d45) = White (2540). Sized with CSS (header 68px, mobile 48px, footer 56px tall).
- Menu fix: "Home" menu item now points to live page 2476 (old item 1946 -> page 5 draft removed).
- Logos APPLIED: header-logo_regular/hd + header-style-mobile-logo_regular/hd = Navy (2538); bottom_bar-logo_regular/hd = White (2540). Verified in live HTML (`.branding img`, `#branding-bottom img`, both 996px natural width). Sizing CSS added to The7 `general-custom_css` (also appended to `snippets/home-rebuild.css`): header 68px, mobile 48px, footer 56px tall. Live Home is now page 2476 (front page); `.page-id-2476` no-gap rule applies to it.
- Pending owner check: logo proportions/placement in header (menu spacing), mobile header, footer bar; GoDaddy cache flush.

### Home: "Built With a Proven System" section added (2026-10-08, live Home 2476)
- Inserted after the building cards: H2 "Built to Industry Standards. Backed by Proven Manufacturing." + intro, 4 text/icon cards (IAS AC472 Accredited Manufacturing; MBMA Member Manufacturing; UL Classified Systems; ENERGY STAR(R) Cool Roof Options) + qualifying footnote. Light grey band (#f2f2f2).
- Owner rules (compliance): do NOT name the manufacturer; do NOT say BSB itself is IAS accredited; MBMA is membership, not certification; say "UL Classified" (never "UL Certified"), not every building/component; ENERGY STAR only "where applicable", no tax-credit promises (owner's tax-incentive sentence was cut off, so no tax wording was added). No logos used (trademarks need permission). Do not publish hours, contact email, testimonials, manufacturer name or warranty/certification details lifted from the manufacturer site (owner decision).
- Heading changed from "ENERGY STAR(R) Partner" to "ENERGY STAR(R) Cool Roof Options" to avoid implying BSB is an ENERGY STAR partner. Owner may revert.
- Home plan still open: eyebrow line + facts strip, Serving WY/UT/ID section, FAQ with schema, inline quote form, Featured Projects (future), SEO title/description.

### MANDATORY content accuracy rules (owner, 2026-10-08) - apply to ALL public copy
1. NEVER name the manufacturer anywhere in public-facing website copy.
2. NEVER link customers directly to the manufacturer's website.
3. NEVER use manufacturer logos.
4. NEVER use wording that encourages customers to contact the manufacturer directly.
5. Do not claim BSB itself holds IAS AC472 accreditation.
6. Do not call MBMA membership a certification.
7. Do not change "UL Classified" to "UL Certified."
8. Do not imply every BSB building automatically has every listed certification or warranty.
9. Do not describe a 30-year Kynar warranty as a 30-year building warranty (it is a FINISH warranty).
10. Do not guarantee tax-credit eligibility.
11. Do not publish TDI claims unless separately verified and specifically approved for public use.
12. Do not invent certification numbers, approval numbers or warranty terms.
13. Preserve the distinction between manufacturing credentials and project-specific approvals.
14. Keep warranty language subject to the applicable warranty documents and project specifications.
Also: no hours, no contact email, no testimonials (none yet), do not list certification/warranty details taken from the manufacturer website beyond the owner-approved copy.

### Home: tax footnote + Warranty section added (live Home 2476)
- Footnote under credentials now also includes the owner-approved tax wording ("Certain qualifying building components may be eligible ... Consult your tax professional for current eligibility.").
- New section "Warranty Options for Long-Term Performance": intro + 6 cards (1-Year Material & Workmanship; 20-Year Panel Material; 20-Year Finish (acrylic-coated Galvalume); 25-Year SMP Finish; 30-Year Kynar 500 Finish - labeled as a finish warranty, not a building warranty; 20-Year Weathertightness options) + disclaimer line. Placed after credentials, before "Design It in 3D".
- Check run: no manufacturer name, no manufacturer site link, no "UL Certified", no "BSB is IAS", no TDI in page content.
- 2026-10-08: "What Happens After You Contact Us?" section (vc_section el_class `process-section`, bg image 2543 mountain-bg-md) now has a white gradient overlay 50% (top) to 70% (bottom) via global CSS (`snippets/home-rebuild.css`). If the overlay doesn't show, the parallax inner element may sit above ::before; raise the overlay z-index or move it onto the parallax element.
- 2026-10-08: Parallax removed from `process-section` (vc_section no longer has parallax/parallax_image). Background + white gradient (50% -> 70%) now one CSS background in global CSS using mountain-bg-md.jpg (id 2543). The earlier ::before overlay approach was replaced.
- 2026-10-08 Mobile logo: mobile header uses the same `.branding` element ("same-logo", since desktop and mobile logos are both Navy 2538), so the desktop 68px rule also applied on phones (header bar only 60px; tablet 70px). Added media queries to global CSS: <=1100px centered (absolute, left 50%) at 52px tall; <=778px 44px tall. Removed the unused `.mobile-branding` rule. Mobile header breakpoints from Theme Options: first switch 1100px (height 70), second switch 778px (height 60).
- BUG FOUND: header top-bar social icons link to relative paths ("/brookssteelbuildings/", "company/brooks-steel-buildings/") instead of full URLs (facebook.com/..., instagram.com/..., linkedin.com/...). Fix in The7 Theme Options > Header > Top bar/microwidgets > Social icons (header-elements-soc_icons). Footer/widget socials use correct URLs.
- 2026-10-08: Phone (<=778px) header logo reduced 50%: 44px -> 22px tall (still centered). Tablet (<=1100px) stays 52px. Owner can raise the phone header height (Theme Options > Header > Mobile, now 60px) if a larger logo is wanted later.
- 2026-10-08 Header social links fixed (The7 option `header-elements-soc_icons` in the7childbrookssteelbuildings): Facebook https://www.facebook.com/brookssteelbuildings ; Instagram https://www.instagram.com/brookssteelbuildings ; LinkedIn https://www.linkedin.com/company/33190238 (numeric company ID supplied by owner). Verified in live HTML. Social icons only show on desktop (top bar).
- Mobile header logo still unresolved after cache flush: CSS is saved and live but not changing what owner sees on phone. Need a phone screenshot + device/width; consider The7 native mobile header settings (layout/height) instead of CSS workaround. Theme files readable via read_file scope=wp-content (themes/dt-the7/...).
- 2026-10-08 Mobile logo, round 3: owner's phone screenshot (5:23pm) showed the logo at ~full size (~730px wide, ~380px tall) with the hamburger overlapping it, i.e. earlier CSS was NOT applied on the phone. Rewrote logo CSS with `html body .masthead ...` specificity + `!important`, tablet 54px / phone 44px, centered (absolute, left 50%). The earlier test (22px halving) was applied in vain. Also removed unused rules. Pending owner re-check on the phone after cache flush. If still wrong, inspect with a phone-width screenshot or use The7 native mobile header options (header-mobile-second_switch-layout/height).

### Home: eyebrow + facts strip (2026-10-08, live Home 2476)
- NOTE: owner re-saved Home in the WPBakery editor (23:36), which normalized shortcodes to DOUBLE quotes and turned the H1 <br> into a newline. Anchor future content/edit calls with double-quoted attributes; all sections were verified intact afterward.
- Eyebrow (orange #f68a31, 14px, letter-spaced, el_class `hero-eyebrow`) above the H1: "CUSTOM STEEL BUILDINGS · WYOMING · UTAH · IDAHO".
- Facts strip (navy #1a3153 band, el_class `facts-strip`, 4 columns, 2x2 on phones) under the hero: "30+ / Years in the steel building industry"; "8-10 Weeks / Current turnaround"; "Engineered / For your site's snow and wind loads"; "Custom / Designed for your exact needs". CSS in global Custom CSS and snippets/home-rebuild.css.
- CONSISTENCY ISSUE: owner says current turnaround is 8-10 weeks, but published pages still say "5 to 6 weeks": Utah (2275), Wyoming (2283), Star Valley (2297, owner asked to leave that page for now). Decide whether to update 2275/2283 (and 2297 later) and any building-type pages.

### Hero image lost after editor save (2026-10-08) - FIXED
- Cause: owner re-saved Home in the WPBakery editor; the editor DROPPED `bg_image_new` (and bg size/position attrs) from both Ultimate image rows (hero + closing band) and DROPPED `heading_tag="h1"` from the H1 ultimate_heading (SEO regression). Hero text is white, so it vanished on the white page.
- Fix: rows now `el_class="hero-bg"` / `el_class="cta-bg"` (bg_type/overlay attrs removed). Photos + 60% navy-dark overlay are CSS backgrounds in global CSS (hero = BSB-25.jpg 2026/03; closing = li-brookssteelbuildings-2.jpg 2020/06). H1 restored via heading_tag="h1".
- LESSON: the WPBakery editor drops attrs it does not know. After any editor save, re-verify: image rows, `heading_tag` on the hero H1, el_class values. To change the hero/closing photos, edit the URLs in `.hero-bg` / `.cta-bg` in The7 Custom CSS (not in the row settings).
- Other headings lost explicit `heading_tag="h2"` in the editor; default tag is h2, so structure is still OK. Banner titles kept h3.
- 2026-10-08 Hero/closing photos not full width: Ultimate `bg_override="ex-full"` only works with the editor image setting. Switched `hero-bg` and `cta-bg` rows to native `full_width="stretch_row"`. Verified in live HTML: row has data-vc-full-width="true" and class hero-bg; H1 present (ultimate-heading ... h1). The page builder JS stretches the row after load; owner to confirm edge-to-edge look (desktop + phone).

## 2026-10-08 — Home: quote form, FAQ, SEO
- Page 2476: added `quote-section` row (Gravity Form 1 inline + "helpful to have ready" + phone) and `faq-section` row (8 `vc_toggle` FAQs, 8–10 week turnaround) with FAQPage JSON-LD (vc_raw_html), inserted before the closing band.
- Yoast (2476): title "Custom Steel Buildings in Wyoming, Utah & Idaho | Brooks Steel Buildings"; meta description (155 chars); focus keyword "custom steel buildings". Verified live in `<head>`.
- Open: "5 to 6 weeks" wording on Utah/Wyoming/Star Valley pages vs 8–10 weeks on Home.
- Home quote section reworked: now uses Gravity Form 2 "Quick Quote" (Name/Phone/Email, Project Location city+state, conditional project textarea). Removed "Helpful to have ready" list; single centered column (heading, one sentence, form, phone line). Compact two-row layout via inline `<style>` in a vc_raw_html (copy in snippets/quick-quote-form.css); stacks to one column under 778px.
- APPLIED 2026-10-09: global CSS (outline blue buttons, darker process text, navy Home quote section, Quick Quote form alignment + white outline submit) appended to general-custom_css; the7_force_regen_css set. Source: snippets/outline-buttons-and-quote-bg.css.
- Privacy Policy published: https://brookssteelbuildings.com/privacy-policy/ (to link from footer and near quote form submit; not yet linked).
- Footer column copy drafted in snippets/footer-widget-copy.md; awaiting approval and quota to apply (3rd footer widget).
- Project page template shortcode written: snippets/project-template.txt (hero w/ facts, gallery + details, why-it-worked, CTA band, inline style block). Paste via WPBakery Classic Mode. Hero photo set per page in Design Options > Background image. Related-projects carousel to be added when Portfolio is enabled. Buttons link to /#quote (needs id="quote" on Home quote row).
- About page draft copy: snippets/about-page-copy.md (awaiting approval).
- About draft: Utah town spelled Coleville (confirmed by owner).
- Owner confirmed Coalville (not Coleville) for the Utah town; About draft updated. (Earlier note saying Coleville was correct is superseded.)
- About page rebuilt as DRAFT page 2570 "About Us (rebuild)" (live About stays page 247 /about-us/ until approved). Sections: hero, who we are, 6 why-cards, three-state service area (Coalville), 5-step process, 4-question FAQ + FAQPage/LocalBusiness JSON-LD, navy quote band with Gravity Form 2. Yoast set on 2570 (title, description, focus keyword). Generator script: snippets/build_about_page.py. To publish: swap content into 247 (keeps URL) or set 2570 slug to about-us after renaming 247. Open: photo for Who We Are; "#quote" id on Home quote row; global CSS (outline buttons etc.) still pending.
- Owner confirmed: keep Brooks Walk named; clear-span available on all building types. (Message about 30+ years was cut off after '30-'; awaiting rest.)
- Owner confirmed: 30+ years wording correct; 'Preparation' step wording approved. All About [CONFIRM] items resolved; awaiting preview check/publish go-ahead.
- About draft 2570: _dt_sidebar_position=disabled, _dt_header_title=disabled (page title hidden), and an inline style block zeroing #main/#content top/bottom padding (selector .page-id-2570; change to .page-id-247 if content is swapped into 247 at publish).
- 2026-10-09: About page PUBLISHED into page 247 (/about-us/): content from draft 2570 with .page-id-247 padding fix; sidebar + title bar disabled; Yoast title/desc/focus kw set. Verified live: title, meta description, one H1, cards, steps, FAQPage + LocalBusiness JSON-LD, Quick Quote form. Draft 2570 left as draft (can be trashed). Previous About content is in 247's revisions.
- 2026-10-09: Privacy Policy links added: footer bottom bar text (`bottom_bar-text` in the7childbrookssteelbuildings and the7) now "... All rights reserved. | Privacy Policy" -> /privacy-policy/; "By submitting this form, you agree to our Privacy Policy" added under the quote form on Home (2476) and About (247). Footer copy was already applied by owner (live footer shows new service area/about/types text).
- "5 to 6 weeks" still present as "five to six weeks" in the "Faster Design and Construction Time" block on published Utah (2275), Wyoming (2283), Star Valley (2297) pages (+ drafts 5, 2320, 2355 and trashed 2351, 2512). Home/FAQ say 8-10 weeks. Decision pending from owner.
- Steel Buildings page (249) review: 9 cards, no meta description, bland title, "mini strorage" typo, 3 cards link to staging domain k9q.9e0.myftpupload.com, no portfolio/blog. Keyword note: "metal buildings" is searched interchangeably with "steel buildings"; use naturally in intro/H2/meta/FAQ.
- Steel Buildings page draft copy: snippets/steel-buildings-page-copy.md (awaiting approval).
- 2026-10-09: Owner confirmed 8-10 week wording everywhere incl. Star Valley: replaced "normally delivered within five to six weeks after receiving the order" with "have a current turnaround of 8 to 10 weeks, which can vary with project size, options, and demand" on Utah 2275, Wyoming 2283, Star Valley 2297. Old drafts still contain 5-6 wording (ignore).
- Steel Buildings rebuilt as DRAFT page 2575 (live page stays 249). Hangars (732) is TRASHED (post_name aircraft-hangars__trashed); Hangars and Barndominiums cards link to /quote/ until those pages are built. Barndo card image: attachment 2291. Yoast set on 2575; sidebar/title bar disabled. Generator: snippets/build_steel_buildings_page.py. To publish: PUT content into 249, swap padding style id to .page-id-249, set meta on 249.
- 2026-10-09: STANDARD 3D BUILDER SECTION: snippets/section-3d-builder.txt (shortcode; could not create a WPBakery saved template via WPVibe, post type vc4_templates is not creatable; owner can save row as template in the editor). Layout: navy full-width band, 3D screenshot (media 2370) left, "Design It in 3D" + one line + orange "Design Your Building" button right; self-contained style block (.bsb-3d). Applied to Steel Buildings draft 2575. Home still has its older "Design It in 3D" row (candidate to swap). "Built Around Your Project" row forced to 4 columns (grid; 2 cols <=900px, 1 col <=560px).
- 2026-10-09: 3D section on Steel Buildings draft 2575 now uses background image 'Steel Building Design on Laptop blue bg' (media 2582) across the whole band; left 3D screenshot removed, left column empty (220px spacer), text + orange CTA in right column; mobile adds navy overlay. Standard-section snippet (snippets/section-3d-builder.txt) still the older 2-column image version; update after owner approves look. CSS for this lives in an inline style block in the page.
- APPLIED 2026-10-09 to Steel Buildings draft 2575: taller 3D band (280px spacer; 20px on phones). Snippets/section-3d-builder.txt matches. Optional white-outline Get a Quote variant for pages without a quote form below: agreed, add per page when needed.
- 2026-10-09: STEEL BUILDINGS PUBLISHED into page 249 (/steel-buildings/): content from draft 2575 (2575 left as draft, can be trashed), .page-id-249 padding fix, sidebar + title off, Yoast title/description/focus kw. First PUT was blocked by GoDaddy firewall rule PTA158 (nothing written); one retry with identical content succeeded. Verified live: title, description, 1 H1, cards, 4-col icons, 3D band, FAQPage JSON-LD, Quick Quote form, Privacy line; no staging links or typo.
- Building type TEMPLATE: draft copy in snippets/building-type-template-commercial-copy.md for Commercial and Retail (page 1207). Existing page had unsourced stats (71%, 30-50% faster) removed in draft.
- 2026-10-09: Owner supplied source list for claims (AISC, MBMA, SteelConstruction.info, AISI). Added Claims and Sources section + sourced benefit cards to snippets/building-type-template-commercial-copy.md. Sources used from owner summary; exact URLs not yet verified; stats (71%, 30-50%) stay out.
- Source URLs recorded in building-type template copy. Could not fetch them (WebFetch DNS fail, curl proxy 403 CONNECT); claims remain unverified against the pages. Note MBMA retail page is a gallery.
- 2026-10-09: Commercial and Retail DRAFT page 2588 created via generator (snippets/build_type_page.py + type_commercial.json); fixed a typo in the inline style (type-hero selector); sidebar/title off. Live Commercial page stays 1207. Yoast and padding handled at publish (:has(.type-hero) rule, no page id needed). Competitor notes in snippets/competitor-notes-commercial.md. Pending owner approval of additions (appearance section, trust strip).
- 2026-10-09: Commercial draft 2588 updated: trust strip under hero (30+ yrs, 8-10 weeks, engineered for snow/wind, WY·UT·ID; Home facts-strip style), new 'Built to Look Like Your Business' section (colors/finishes, doors/entries, windows/storefront openings; no canopy claim), outcome wording on clear-span card. Hero photo stays IMG_1721 (owner: best image). Other images owner listed (commercial-steel-buildings, IMG_1723, IMG_1153, delivery800x500, IMG_3713, rock-tops) not placed yet; owner did not want a media-library query run, awaiting direction. NOTE: these edits are in the draft only; mirror in snippets/type_commercial.json/build_type_page.py when generalizing the template.
- 2026-10-09: COMMERCIAL AND RETAIL PUBLISHED into page 1207 (/steel-buildings/commercial/): hero (IMG_1721), trust strip, uses, why steel (sourced general wording), "Built to Look Like Your Business", steps, standard 3D band, FAQ + FAQPage JSON-LD, related links, quote band. Yoast: "Commercial Steel Buildings | Brooks Steel Buildings", description, focus kw "commercial steel buildings"; title bar off; sidebar already off. Verified live (title, description, 1 H1, sections, no 71% stat). Padding fix uses #main:has(.type-hero) so no page id needed. Draft 2588 left as draft. Generator + spec updated (snippets/build_type_page.py, type_commercial.json) = TEMPLATE for other types. Open: other 5 owner-listed images unplaced; Hangars (732 trashed) and Barndominiums pages to build; competitor notes in snippets/competitor-notes-commercial.md.
- 2026-10-09: Commercial (1207) live edits: added "Canopies and Overhangs" card (owner OK; 4-card row) and a 3-photo strip IMG_3713, IMG_1723, IMG_1153 (media 2144, 2173, 2161; alt "Commercial steel building project"; generic alt, refine once photos reviewed). SEO already set on 1207 earlier. Generator/spec synced (type_commercial.json now has facts, look, photos). Other listed images (commercial-steel-buildings, delivery800x500, rock-tops) still unplaced.
- 2026-10-09: NEW TYPE: Steel Flex Buildings. Draft copy snippets/flex-buildings-page-copy.md + spec snippets/type_flex.json; generator now supports optional intro section. Not yet created on site (WPVibe at ~95/100 calls today). URL /steel-buildings/flex-buildings/. No ACT naming, no insulation claims until owner confirms.
- 2026-10-09: Flex copy updated per owner: insulation supplied, insulated panels, parapets/canopies, investor build-to-lease angle; Flex to be #1 card on Steel Buildings. Awaiting go-ahead to create draft page.
- 2026-10-09: Reviewed second ChatGPT flex brainstorm: added layout sentence, multi-tenant planning, 2 FAQs (8 total); kept separate Flex page per owner; plan a Flex teaser section on Commercial + cross-links; vendor name and Utah market claims excluded.
- 2026-10-09: STEEL FLEX BUILDINGS DRAFT created: page 2597, child of Steel Buildings (parent 249), slug flex-buildings (URL /steel-buildings/flex-buildings/ once published). Content verified identical to generator output (snippets/type_flex.json). Sidebar + title bar disabled. Yoast NOT yet set: title "Steel Flex Buildings | Office & Warehouse Combinations"; description "Explore custom steel flex buildings combining office, showroom, warehouse, and shop space. Design a commercial building around your business needs."; focus kw "steel flex buildings". Hero placeholder IMG_1723; owner sourcing hero + 3 photos. Owner notes: no R-values (location dependent); BSB does not supply plumbing/electrical. To do when live: Flex card #1 on Steel Buildings (11 cards), footer type list, menu, Flex teaser + link on Commercial page.
- 2026-10-09: Flex page 2597 PUBLISHED by owner (menu item added by owner). Owner added Yoast; live title had " - Brooks Steel Buildings" suffix (78 chars), fixed by setting _yoast_wpseo_title via WP-CLI to the bare 53-char title. Hero image set to Flex-Building-Industrial-Warehouses (media 2601) via override style; photo strip added (2602 warehouse, 2603 retail strip, 2604 Flex-Building) under "Who Uses Flex Buildings?"; alt text generic. Steel Buildings (249): Flex card added as #1 (11 cards). Commercial (1207): Flex teaser section + button added before the 3D band. Open: footer type list; Flex related link on Commercial related row (teaser covers it); refine alt text after photos reviewed; Hangars/Barndos pages.
