"""Building-type page generator (template). Usage: python3 build_type_page.py <spec.json> <outdir>
Spec fields documented in snippets/type_commercial.json."""
import base64,urllib.parse,json,re,sys
spec=json.load(open(sys.argv[1])); out=sys.argv[2]
def enc(h): return base64.b64encode(urllib.parse.quote(h,safe='').encode()).decode()
src=open('snippets/build_about_page.py').read()
css=re.search(r'css="""(.*?)"""',src,re.S).group(1)
css+="""
.about-cards.four{display:grid !important;grid-template-columns:repeat(4,1fr);gap:20px}
.about-cards.four .about-card{min-width:0 !important;flex:none !important;padding:20px 16px;text-align:center}
.about-cards.six{display:grid !important;grid-template-columns:repeat(3,1fr);gap:20px}
.about-cards.six .about-card{min-width:0 !important;flex:none !important}
@media(max-width:900px){.about-cards.four{grid-template-columns:repeat(2,1fr)}.about-cards.six{grid-template-columns:repeat(2,1fr)}}
@media(max-width:560px){.about-cards.four,.about-cards.six{grid-template-columns:1fr}}
.hero-bg.type-hero{background-image:linear-gradient(rgba(20,30,45,.62),rgba(20,30,45,.62)),url(%s) !important}
.type-crumbs,.type-crumbs a{font-size:13px;color:#dfe6f1 !important}
.type-related{text-align:center;color:#444b55}
.type-related a{margin:0 10px;font-weight:700}
#main:has(.type-hero),#content:has(.type-hero){padding-top:0 !important;padding-bottom:0 !important;margin-top:0 !important;margin-bottom:0 !important}"""%spec['hero_image_url']
style=enc('<style>'+''.join(l.strip() for l in css.split('\n'))+'</style>')
def H(t,sub=''): return f"[ultimate_heading main_heading=\"{t}\" main_heading_style=\"font-weight:bold;\" sub_heading_font_size=\"desktop:18px;\" main_heading_margin=\"margin-bottom:10px;\"]{sub}[/ultimate_heading]"
def card(i,t,p): return f'<div class="about-card"><i class="{i}"></i><h3>{t}</h3><p>{p}</p></div>'
uses=''.join(card(*u) for u in spec['uses'])
why=''.join(card(*u) for u in spec['why'])
steps=''.join(f'<div><b>{i+1}. {t}</b><span>{d}</span></div>' for i,(t,d) in enumerate([('Design','We talk through your needs, site, and budget and plan the right building.'),('Engineering','Your building is engineered for local codes, with plans prepared for permitting.'),('Preparation','Your building package is prepared for accurate, efficient assembly.'),('Delivery','Your building package is delivered to your job site.'),('Construction','Build it yourself or hire a contractor.')]))
faq=spec['faq']
toggles=''.join(f'[vc_toggle title="{q}"]{a}[/vc_toggle]' for q,a in faq)
ld={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}
schema=enc('<script type="application/ld+json">'+json.dumps(ld)+'</script>')
d3=open('snippets/section-3d-builder.txt').read()
related=' '.join(f'<a href="{u}">{t}</a>' for t,u in spec['related'])
facts=''.join(f'[vc_column width="1/4"][vc_column_text]<div class="fact-num">{n}</div><div class="fact-label">{l}</div>[/vc_column_text][/vc_column]' for n,l in spec['facts'])
strip=f'[vc_row bg_type="bg_color" bg_override="ex-full" el_class="facts-strip" bg_color_value="#1a3153"]{facts}[/vc_row]'
look=''.join(card(*u) for u in spec['look'])
imgs=''.join(f'<img src="{u}" alt="{a}" loading="lazy" style="flex:1 1 240px;min-width:0;width:calc(33% - 11px);height:240px;object-fit:cover;border-radius:6px;">' for u,a in spec.get('photos',[]))
photos=f'<div style="display:flex;flex-wrap:wrap;gap:16px;margin-top:28px;">{imgs}</div>' if imgs else ''
lookrow=f'[vc_row el_class="about-alt" full_width="stretch_row"][vc_column][vc_empty_space height="40px"]{H(spec["look_h2"],spec["look_sub"])}[vc_empty_space height="20px"][vc_column_text]<div class="about-cards four">{look}</div><p style="text-align:center;margin-top:24px;">{spec["look_line"]}</p>{photos}[/vc_column_text][vc_empty_space height="40px"][/vc_column][/vc_row]'
c=(f'[vc_row el_class="hero-bg type-hero" full_width="stretch_row"][vc_column][vc_empty_space height="40px"]'
 f'[vc_column_text]<p class="type-crumbs"><a href="/steel-buildings/">Steel Buildings</a> &raquo; {spec["crumb"]}</p>[/vc_column_text]'
 f'[vc_column_text el_class="hero-eyebrow"]<p>{spec["eyebrow"]}</p>[/vc_column_text]'
 f'[ultimate_heading heading_tag="h1" main_heading="{spec["h1"]}" alignment="left" main_heading_color="#ffffff" main_heading_style="font-weight:bold;" sub_heading_color="#ffffff" sub_heading_font_size="desktop:20px;" main_heading_margin="margin-bottom:12px;"]{spec["answer"]}[/ultimate_heading]'
 f'[vc_empty_space height="10px"][vc_row_inner el_class="hero-btns"][vc_column_inner width="1/2"][dt_default_button link="url:%2Fquote%2F" el_class="btn-orange"]Get a Free Quote[/dt_default_button][/vc_column_inner][vc_column_inner width="1/2"][dt_default_button link="tel:8009084839" el_class="btn-outline-white"]Call 800-908-4839[/dt_default_button][/vc_column_inner][/vc_row_inner][vc_empty_space height="50px"][/vc_column][/vc_row]{strip}'
 f'[vc_row el_class="about-alt" full_width="stretch_row"][vc_column][vc_empty_space height="40px"]{H(spec["uses_h2"],spec["uses_sub"])}[vc_empty_space height="20px"][vc_column_text]<div class="about-cards four">{uses}</div>[/vc_column_text][vc_empty_space height="40px"][/vc_column][/vc_row]'
 f'[vc_row][vc_column][vc_empty_space height="40px"]{H(spec["why_h2"],spec["why_sub"])}[vc_empty_space height="20px"][vc_column_text]<div class="about-cards six">{why}</div><p style="text-align:center;margin-top:24px;">{spec["codes_line"]}</p>[/vc_column_text][vc_empty_space height="40px"][/vc_column][/vc_row]'
 f'{lookrow}[vc_row full_width="stretch_row"][vc_column][vc_empty_space height="40px"]{H("How Your Project Works","A simple process from first call to finished building.")}[vc_empty_space height="20px"][vc_column_text]<div class="about-steps">{steps}</div>[/vc_column_text][vc_empty_space height="40px"][/vc_column][/vc_row]'
 f'{d3}'
 f'[vc_row][vc_column][vc_empty_space height="40px"]{H(spec["faq_h2"])}[vc_empty_space height="20px"]{toggles}[vc_raw_html]{schema}[/vc_raw_html][vc_empty_space height="30px"][vc_column_text]<p class="type-related">Also see: {related} | <a href="/steel-buildings/">All steel building types</a></p>[/vc_column_text][vc_empty_space height="40px"][/vc_column][/vc_row]'
 f'[vc_row el_class="about-quote" full_width="stretch_row"][vc_column][vc_empty_space height="40px"]{H("Get Your Free Quote","Tell us about your project and we will provide a custom quote based on your needs.")}[vc_empty_space height="20px"][vc_raw_html]{style}[/vc_raw_html][gravityform id=\'2\' title=\'false\' description=\'false\' ajax=\'true\'][vc_column_text]<p style="text-align:center;">Prefer to talk? Call <a href="tel:8009084839">800-908-4839</a>.<br><small>By submitting this form, you agree to our <a href="/privacy-policy/">Privacy Policy</a>.</small></p>[/vc_column_text][vc_empty_space height="40px"][/vc_column][/vc_row]')
json.dump({"title":spec["draft_title"],"status":"draft","content":c},open(out+'/type_create.json','w'))
json.dump({"title":spec["live_title"],"content":c},open(out+'/type_publish.json','w'))
print(len(c))
