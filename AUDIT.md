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
