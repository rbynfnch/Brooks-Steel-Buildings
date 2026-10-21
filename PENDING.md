# Pending site changes (blocked by the WPVibe daily limit on 2026-10-21; resets about 6:40 PM UTC)

## URGENT: Star Valley page (ID 2297) is half-built and live
Part A of the rebuilt page was written; the visible text "[bsb_split]" shows near the bottom and the FAQ, 3D block, quote band and related links are missing. Finish with, in order:
1. `POST /wpvibe/v1/content/edit` {target_type:post, post_id:2297, field:post_content, old_content:"[bsb_split]", new_content: contents of snippets/state_sv_parts/B1.txt}  (expected result bytes 21719)
2. Same call with new_content = contents of snippets/state_sv_parts/B2.txt (expected result bytes 31417). Both parts end/begin as in the files; the first replaces the sentinel with B1 which ends in a new "[bsb_split]", the second replaces that one with B2.
3. Meta (WP-CLI, each with --force): `_dt_header_title disabled`, `_dt_sidebar_position disabled`, `_yoast_wpseo_title 'Star Valley, WY Steel Buildings | Brooks Steel Buildings'`, `_yoast_wpseo_metadesc 'Custom pre-engineered steel buildings for Star Valley, Wyoming, including Afton, Alpine, and Thayne. Engineered for your snow and wind loads. Free quote.'`, `_yoast_wpseo_focuskw 'star valley steel buildings'`. Then `post update 2297 --post_title='Star Valley, Wyoming Steel Buildings'`.
4. Verify with curl: one H1, FAQPage present, no "bsb_split", quote form present.

## Company data (Yoast Organization)
`option patch update wpseo_social instagram_url 'https://www.instagram.com/brookssteelbuildings'`; `... linkedin_url 'https://www.linkedin.com/company/33190238'`; confirm `facebook_site` and organization name in Yoast, Settings, Site representation (owner can do this in the UI).

## Service + LocalBusiness data per page
Run `python3 snippets/build_schema_blocks.py`, then for each file in snippets/schema_payloads/<post_id>.json POST its contents to /wpvibe/v1/content/edit (17 pages: 11 type pages, Wyoming, Utah, Idaho, Star Valley (after the rebuild), Home = full LocalBusiness, Steel Buildings hub = service catalog). If a page returns no_match (Home or hub may not use the same Quick Quote shortcode), search the page for `[gravityform` and adjust the anchor.
Validate afterward with a crawl for `"@type": "Service"` and Google's Rich Results test.

## Also queued
Demo content: DONE (58 items trashed). Titles/descriptions/Privacy H1: DONE.
