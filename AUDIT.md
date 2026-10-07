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
- 20 active plugins, including two page builders (Elementor + WPBakery) plus Ultimate VC Addons, Revolution Slider, LayerSlider, and four form plugins (Contact Form 7, Gravity Forms, Ninja Forms, WPForms Lite). Likely heavy and partly unused.
- "Search Engine Visibility" plugin is active: confirm it is not discouraging indexing.
- Sucuri appears to block some admin REST saves (widgets/page settings); WPVibe saves work.

## Task list (priority order)

### A. Quick wins (SEO / housekeeping)
1. Confirm indexing is on (Settings → Reading, "Discourage search engines" unchecked; check the Search Engine Visibility plugin).
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
20. Remove unused plugins one at a time after backup (extra form plugins, second page builder, unused sliders, `wp-contact-slider`).
21. Ask Sucuri/GoDaddy to allow `/wp-json/wp/v2/` for logged-in admins so normal saves work.
22. Move custom CSS/PHP into the child theme and set up GitHub → GoDaddy deployment.
23. Create the 3 missing pages (Barndominiums, Custom Steel Buildings, Design Your Own) and link the home cards.
