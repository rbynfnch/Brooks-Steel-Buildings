"""Get a Quote page + Thank You page generator. Usage: python3 snippets/build_quote_page.py <outdir>  (run from repo root)"""
import base64,urllib.parse,json,re,sys
out=sys.argv[1]
def enc(h): return base64.b64encode(urllib.parse.quote(h,safe='').encode()).decode()
HERO='https://brookssteelbuildings.com/wp-content/uploads/2023/09/metal-building-shop-house-2-scaled.jpg'
css="""
.about-alt{background:#f7f9fc}
.about-cards{display:flex;flex-wrap:wrap;gap:20px}
.about-card{flex:1 1 calc(33.333% - 20px);min-width:240px;background:#f3f6fa;border-radius:6px;padding:22px}
.about-alt .about-card{background:#fff}
.about-card i{font-size:28px;color:#1a3153;margin-bottom:10px;display:block}
.about-card h3{font-size:19px;margin:0 0 6px;color:#1a3153;line-height:1.25 !important}
.about-card p{margin:0;color:#444b55}
.about-cards.four{display:grid !important;grid-template-columns:repeat(4,1fr);gap:20px}
.about-cards.four .about-card{min-width:0 !important;flex:none !important;padding:20px 16px;text-align:center}
@media(max-width:900px){.about-cards.four{grid-template-columns:repeat(2,1fr)}}
@media(max-width:560px){.about-cards.four{grid-template-columns:1fr}}
.hero-bg.type-hero{background-image:linear-gradient(rgba(20,30,45,.62),rgba(20,30,45,.62)),url(HEROURL) !important;background-position:center 55% !important}
.type-crumbs,.type-crumbs a{font-size:13px;color:#dfe6f1 !important}
.type-related{text-align:center;color:#444b55}
.type-related a{margin:0 10px;font-weight:700}
.quote-side{background:#1a3153;color:#fff;border-radius:6px;padding:26px}
.quote-side h3,.quote-side p,.quote-side a:not(.dt-btn){color:#fff !important}
.quote-side h3{margin:0 0 14px;font-size:22px}
.quote-side ol{list-style:none;margin:0 0 18px;padding:0;counter-reset:s}
.quote-side li{counter-increment:s;position:relative;padding:0 0 14px 42px;color:#fff}
.quote-side li:before{content:counter(s);position:absolute;left:0;top:0;width:30px;height:30px;border-radius:50%;background:#f68a31;color:#fff;font-weight:700;text-align:center;line-height:30px}
.quote-side li b{display:block;font-size:17px}
.quote-side li span{color:#dfe6f1;font-size:15px}
.quote-side .btn-wrap{margin-top:8px}
#main:has(.type-hero),#content:has(.type-hero){padding-top:0 !important;padding-bottom:0 !important;margin-top:0 !important;margin-bottom:0 !important}""".replace("HEROURL",HERO)
style=enc('<style>'+''.join(l.strip() for l in css.split('\n'))+'</style>')
def H(t,sub='',tag='h2'): return f'[ultimate_heading main_heading="{t}" main_heading_style="font-weight:bold;" sub_heading_font_size="desktop:18px;" main_heading_margin="margin-bottom:10px;"]{sub}[/ultimate_heading]'
def card(i,t,p): return f'<div class="about-card"><i class="{i}" aria-hidden="true">&#8203;</i><h3>{t}</h3><p>{p}</p></div>'
DESIGN='url:https%3A%2F%2Fbrooks-steel-buildings-llc.actbuildingsystems.com%2F%3Fshareid%3D97435377-73fe-4732-b906-1437a03b2e04|title:Design%20Your%20Building'
facts=[("30+","Years in the steel building industry"),("8–10 Weeks","Current turnaround"),("Engineered","For your site’s snow and wind loads"),("WY · UT · ID","Where we supply buildings")]
strip='[vc_row bg_type="bg_color" bg_override="ex-full" el_class="facts-strip" bg_color_value="#1a3153"]'+''.join(f'[vc_column width="1/4"][vc_column_text]<div class="fact-num">{n}</div><div class="fact-label">{l}</div>[/vc_column_text][/vc_column]' for n,l in facts)+'[/vc_row]'
def hero(crumb,eyebrow,h1,sub,btns):
    return (f'[vc_row el_class="hero-bg type-hero" full_width="stretch_row"][vc_column][vc_empty_space height="40px"]'
     f'[vc_column_text]<p class="type-crumbs"><a href="/steel-buildings/">Steel Buildings</a> &raquo; {crumb}</p>[/vc_column_text]'
     f'[vc_column_text el_class="hero-eyebrow"]<p>{eyebrow}</p>[/vc_column_text]'
     f'[ultimate_heading heading_tag="h1" main_heading="{h1}" alignment="left" main_heading_color="#ffffff" main_heading_style="font-weight:bold;" sub_heading_color="#ffffff" sub_heading_font_size="desktop:20px;" main_heading_margin="margin-bottom:12px;"]{sub}[/ultimate_heading]'
     f'[vc_empty_space height="10px"][vc_row_inner el_class="hero-btns"]{btns}[/vc_row_inner][vc_empty_space height="50px"][/vc_column][/vc_row]')
btns_q=(f'[vc_column_inner width="1/2"][dt_default_button link="tel:8009084839" el_class="btn-orange"]Call 800-908-4839[/dt_default_button][/vc_column_inner]'
        f'[vc_column_inner width="1/2"][dt_default_button link="{DESIGN}" el_class="btn-outline-white"]Design It in 3D[/dt_default_button][/vc_column_inner]')
faq=[("How much does a steel building cost?","Every building is custom, so the price depends on its size, height, location, and options. Send us your details and we will price your building. We do not publish one-size-fits-all prices."),
("Do I need exact dimensions to ask for a quote?","No. Share what you know, such as the use, location, and rough size. We will help you work out the width, length, and eave height."),
("What happens after I send the form?","We review your details and follow up with you directly to confirm the size, openings, and options. Then we prepare your custom quote. Tell us your timeline in the form so we can plan around it."),
("How long does it take to get a building?","Our current turnaround is 8 to 10 weeks. Timelines can vary with project size, options, and demand."),
("Do you supply overhead doors and windows?","No. We design the building and its openings for the overhead doors and windows you choose, and they are installed by others. We supply commercial walk doors (man doors)."),
("Can I build it myself?","Yes. Many owners build their own buildings or hire a local contractor. Your building package is prepared for accurate, efficient assembly."),
("Where do you supply buildings?","We supply buildings in Wyoming, Utah, and Idaho, and we are based in Evanston, Wyoming.")]
ld={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}
schema=enc('<script type="application/ld+json">'+json.dumps(ld)+'</script>')
toggles=''.join(f'[vc_toggle title="{q}"]{a}[/vc_toggle]' for q,a in faq)
side=('<div class="quote-side"><h3>What Happens Next</h3><ol>'
 '<li><b>We review your details</b><span>We look at your use, your site, and the building you have in mind.</span></li>'
 '<li><b>We talk it through</b><span>We confirm the size, openings, and options with you.</span></li>'
 '<li><b>You get a custom quote</b><span>Priced for your building, engineered for your site’s loads.</span></li></ol>'
 '<p>Prefer to talk? Call <a href="tel:8009084839"><b>800-908-4839</b></a>.</p></div>')
helpful=''.join(card(*c) for c in [("fas fa-map-marker-alt","Your Location","City and state, so we can plan for local snow and wind loads."),("fas fa-bullseye","How You Will Use It","Shop, barn, storage, hangar, or something else."),("fas fa-ruler-combined","A Rough Size","Width, length, and height if you have them. If not, we will help."),("fas fa-door-open","Door and Window Ideas","We design for the overhead doors and windows you choose, installed by others. We supply commercial walk doors (man doors).")])
related=('<a href="/steel-buildings/">All steel building types</a> <a href="/wyoming-steel-buildings/">Wyoming</a> <a href="/utah-steel-buildings/">Utah</a> <a href="/idaho-steel-buildings/">Idaho</a>')
quote=(hero("Get a Quote","FREE CUSTOM QUOTE","Get a Free Steel Building Quote","Tell us about your project and we will prepare a custom quote. Not sure of the size yet? Send what you know and we will help you plan the rest.",btns_q)
 +strip
 +'[vc_row][vc_column width="2/3"][vc_empty_space height="40px"]'+H("Tell Us About Your Project","Fields marked * are required.")+'[vc_empty_space height="20px"][gravityform id=\'2\' title=\'false\' description=\'false\' ajax=\'true\'][vc_column_text]<p><small>By submitting this form, you agree to our <a href="/privacy-policy/">Privacy Policy</a>.</small></p>[/vc_column_text][vc_empty_space height="40px"][/vc_column]'
 +'[vc_column width="1/3"][vc_empty_space height="40px"][vc_column_text]'+side+'[/vc_column_text][vc_empty_space height="20px"][dt_default_button link="'+DESIGN+'" size="medium" button_alignment="btn_left" el_class="btn-orange"]Start With the 3D Designer[/dt_default_button][vc_empty_space height="40px"][/vc_column][/vc_row]'
 +'[vc_row el_class="about-alt" full_width="stretch_row"][vc_column][vc_empty_space height="40px"]'+H("Helpful to Include, But Not Required","The more you tell us, the faster we can price your building.")+'[vc_empty_space height="20px"][vc_column_text]<div class="about-cards four">'+helpful+'</div>[/vc_column_text][vc_empty_space height="40px"][/vc_column][/vc_row]'
 +'[vc_row][vc_column][vc_empty_space height="40px"]'+H("Quote Questions")+'[vc_empty_space height="20px"]'+toggles+'[vc_raw_html]'+schema+'[/vc_raw_html][vc_empty_space height="30px"][vc_column_text]<p class="type-related">'+related+'</p>[/vc_column_text][vc_empty_space height="40px"][vc_raw_html]'+style+'[/vc_raw_html][/vc_column][/vc_row]')
tys=hero("Thank You","REQUEST RECEIVED","Thank You, We Have Your Request","Your quote request has been sent. We will review your details and follow up with you directly.",
 f'[vc_column_inner width="1/2"][dt_default_button link="{DESIGN}" el_class="btn-orange"]Design It in 3D[/dt_default_button][/vc_column_inner][vc_column_inner width="1/2"][dt_default_button link="tel:8009084839" el_class="btn-outline-white"]Call 800-908-4839[/dt_default_button][/vc_column_inner]')
tysteps=''.join(card(*c) for c in [("fas fa-search","We Review Your Details","We look at your use, your site, and the building you have in mind."),("fas fa-comments","We Follow Up","We confirm the size, openings, and options with you."),("fas fa-file-invoice-dollar","You Get a Custom Quote","Priced for your building and engineered for your site’s loads.")])
tys+=('[vc_row][vc_column][vc_empty_space height="40px"]'+H("What Happens Next","In the meantime, you can explore our building types or design your building in 3D.")+'[vc_empty_space height="20px"][vc_column_text]<div class="about-cards">'+tysteps+'</div>[/vc_column_text][vc_empty_space height="30px"][vc_column_text]<p class="type-related"><a href="/steel-buildings/">Steel Building Types</a> <a href="/wyoming-steel-buildings/">Wyoming</a> <a href="/utah-steel-buildings/">Utah</a> <a href="/idaho-steel-buildings/">Idaho</a></p>[/vc_column_text][vc_empty_space height="40px"][vc_raw_html]'+style+'[/vc_raw_html][/vc_column][/vc_row]')
json.dump({"title":"Get a Quote (rebuild)","status":"draft","slug":"get-a-quote-rebuild","parent":0,"content":quote},open(out+'/quote_create.json','w'))
json.dump({"title":"Thank You","status":"draft","slug":"thank-you","parent":0,"content":tys},open(out+'/thanks_create.json','w'))
print(len(quote),len(tys))
