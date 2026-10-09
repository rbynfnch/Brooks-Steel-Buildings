import base64,urllib.parse,json,re,sys
SP=sys.argv[1]
def enc(h): return base64.b64encode(urllib.parse.quote(h,safe='').encode()).decode()
src=open('snippets/build_about_page.py').read()
css=re.search(r'css="""(.*?)"""',src,re.S).group(1)
css+="""
.bsb-type-grid{display:flex;flex-wrap:wrap;justify-content:center}
.bsb-type-grid>.wpb_column{float:none}
.bsb-type-grid .ult-new-ib .ult-new-ib-title{font-size:24px!important}
.bsb-type-grid .ult-new-ib .ult-new-ib-content{font-size:17px!important}
.about-cards.four .about-card{flex:1 1 calc(25% - 20px);min-width:200px;text-align:center}
.bsb-navy{background:#1a3153;box-shadow:0 0 0 100vmax #1a3153;clip-path:inset(0 -100vmax)}
.bsb-navy h2,.bsb-navy .uvc-sub-heading{color:#fff!important}
@media(max-width:778px){.bsb-type-grid>.wpb_column{width:100%}}"""
style=enc('<style>'+''.join(l.strip() for l in css.split('\n'))+'</style>')
faq=[("Are steel buildings and metal buildings the same thing?","Yes. People use the two terms interchangeably. Our buildings are pre-engineered steel buildings that are custom designed for your project."),
("What types of steel buildings do you offer?","Commercial and retail, agricultural, industrial and warehouse, storage, recreational, shops and garages, schools and gymnasiums, equestrian riding arenas, aircraft hangars, and barndominiums."),
("How much does a steel building cost?","The cost depends on the size, design, options, location, and current steel pricing. Share your location, building type, and approximate size and we will provide a custom quote."),
("How long does it take to get a steel building?","Our current turnaround is 8 to 10 weeks. Timelines can vary with project size, options, and demand, so contact us for the latest estimate."),
("Do you serve my area?","We supply steel buildings across Wyoming, Utah, and Idaho. Contact us with your project location.")]
ld={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}
schema=enc('<script type="application/ld+json">'+json.dumps(ld)+'</script>')
U='https://brookssteelbuildings.com/wp-content/uploads/'
cards=[
("Commercial and Retail Steel Buildings","Retail stores, offices, warehouses, and distribution centers.",2074,U+"2020/06/IMG_1721-scaled.jpg","Commercial steel building","/steel-buildings/commercial/"),
("Agricultural Steel Buildings","Barns, equipment and hay storage, and shelters for livestock.",2072,U+"2020/06/agricultural-steel-building.jpg","Agricultural steel building","/steel-buildings/agricultural-steel-buildings/"),
("Shops and Garages","Workshops, auto and welding shops, and large garages.",2066,U+"2020/06/garage.jpg","Steel shop and garage building","/steel-buildings/shops/"),
("Equestrian Riding Arenas","Clear-span riding arenas, horse barns, and run-in shelters.",2073,U+"2020/06/steel-building-arena.jpg","Steel equestrian riding arena","/steel-buildings/equestrian-riding-arenas/"),
("Industrial and Warehouse Steel Buildings","Warehouses, fabrication shops, and manufacturing space.",2071,U+"2020/06/warehouse.jpg","Steel warehouse building","/steel-buildings/industrial/"),
("Storage Units","Mini storage, RV and boat storage, and equipment storage.",2070,U+"2020/06/storage-units.jpg","Steel storage units","/steel-buildings/storage-unit/"),
("Aircraft Hangars","Clear-span hangars designed for multiple door styles.",2067,U+"2020/06/hangar-steel-buildings.jpg","Steel aircraft hangar","/quote/"),
("Barndominiums","Shop-house and living-space buildings for residential use.",2291,U+"2023/09/metal-building-shop-house-3.jpg","Steel barndominium shop house","/quote/"),
("Recreational Steel Buildings","Gyms, indoor sports facilities, and fitness centers.",2068,U+"2020/06/recreational-steel-buildings.jpg","Steel recreational building","/steel-buildings/recreational/"),
("Schools and Gymnasiums","Schools, churches, and gymnasiums.",2065,U+"2020/06/commercial-steel-buildings.jpg","Steel school or gymnasium building","/steel-buildings/schools-and-gymnasiums/")]
def card(t,d,i,u,a,l):
    return (f'[vc_column width="1/3"][interactive_banner_2 banner_title="{t}" heading_tag="h3" banner_desc="{d}" '
            f'banner_image="id^{i}|url^{u}|caption^null|alt^{a}|title^{a}|description^null" '
            f'banner_link="url:{urllib.parse.quote(l,safe="")}" banner_style="style1" image_opacity="1" image_opacity_on_hover="1"][/vc_column]')
cardrow='[vc_row el_class="home-type-cards bsb-type-grid"]'+''.join(card(*c) for c in cards)+'[/vc_row]'
def H(t,sub=''): return f"[ultimate_heading main_heading=\"{t}\" main_heading_style=\"font-weight:bold;\" sub_heading_font_size=\"desktop:18px;\" main_heading_margin=\"margin-bottom:10px;\"]{sub}[/ultimate_heading]"
def icard(i,t,p): return f'<div class="about-card"><i class="{i}"></i><h3>{t}</h3><p>{p}</p></div>'
inc=''.join([icard('fas fa-drafting-compass','Custom Designed','Sized and laid out for your use, site, and budget.'),icard('fas fa-snowflake','Snow and Wind Engineered','Designed for the loads at your location.'),icard('fas fa-expand-arrows-alt','Open Interiors','Clear-span designs available on all building types.'),icard('fas fa-clipboard-check','Permitting Support','Engineered plans prepared for permitting. Requirements vary by location.')])
toggles=''.join(f'[vc_toggle title="{q}"]{a}[/vc_toggle]' for q,a in faq)
c=(f'[vc_row el_class="hero-bg" full_width="stretch_row"][vc_column][vc_empty_space height="50px"][vc_column_text el_class="hero-eyebrow"]<p>STEEL BUILDINGS</p>[/vc_column_text]'
 f'[ultimate_heading heading_tag="h1" main_heading="Custom Steel &amp; Metal Buildings in Wyoming, Utah &amp; Idaho" alignment="left" main_heading_color="#ffffff" main_heading_style="font-weight:bold;" sub_heading_color="#ffffff" sub_heading_font_size="desktop:20px;" main_heading_margin="margin-bottom:12px;"]Brooks Steel Buildings supplies custom pre-engineered steel buildings for commercial, agricultural, equestrian, shop, storage, and recreational use. Choose a building type below to see what fits your project.[/ultimate_heading]'
 f'[vc_empty_space height="10px"][vc_row_inner el_class="hero-btns"][vc_column_inner width="1/2"][dt_default_button link="url:%2Fquote%2F" el_class="btn-orange"]Get a Free Quote[/dt_default_button][/vc_column_inner][vc_column_inner width="1/2"][dt_default_button link="tel:8009084839" el_class="btn-outline-white"]Call 800-908-4839[/dt_default_button][/vc_column_inner][/vc_row_inner][vc_empty_space height="50px"][/vc_column][/vc_row]'
 f'[vc_row][vc_column][vc_empty_space height="40px"]{H("Find the Right Building for Your Project","Steel buildings, also called metal buildings, work for almost any use, from a farm shop to a commercial warehouse. Every building we supply is custom designed for your site and engineered for local snow and wind conditions. Pick the type closest to your project, or contact us if yours is something different.")}[vc_empty_space height="20px"][/vc_column][/vc_row]'
 f'{cardrow}[vc_row][vc_column][vc_empty_space height="40px"][/vc_column][/vc_row]'
 f'[vc_row el_class="about-alt" full_width="stretch_row"][vc_column][vc_empty_space height="40px"]{H("Built Around Your Project")}[vc_empty_space height="20px"][vc_column_text]<div class="about-cards four">{inc}</div>[/vc_column_text][vc_empty_space height="40px"][/vc_column][/vc_row]'
 f'[vc_row el_class="bsb-navy" full_width="stretch_row"][vc_column][vc_empty_space height="40px"]{H("See Your Building Before You Order","Explore sizes, styles, colors, and options with our interactive 3D building designer.")}[vc_empty_space height="10px"][dt_default_button link="url:https%3A%2F%2Fbrooks-steel-buildings-llc.actbuildingsystems.com%2F%3Fshareid%3D97435377-73fe-4732-b906-1437a03b2e04|title:Design%20Your%20Building" size="medium" button_alignment="btn_center" el_class="btn-orange"]Design Your Building[/dt_default_button][vc_empty_space height="40px"][/vc_column][/vc_row]'
 f'[vc_row][vc_column][vc_empty_space height="40px"]{H("Steel Building Questions")}[vc_empty_space height="20px"]{toggles}[vc_raw_html]{schema}[/vc_raw_html][vc_empty_space height="40px"][/vc_column][/vc_row]'
 f'[vc_row el_class="about-quote" full_width="stretch_row"][vc_column][vc_empty_space height="40px"]{H("Get Your Free Quote","Tell us about your project and we will provide a custom quote based on your needs.")}[vc_empty_space height="20px"][vc_raw_html]{style}[/vc_raw_html][gravityform id=\'2\' title=\'false\' description=\'false\' ajax=\'true\'][vc_column_text]<p style="text-align:center;">Prefer to talk? Call <a href="tel:8009084839">800-908-4839</a>.<br><small>By submitting this form, you agree to our <a href="/privacy-policy/">Privacy Policy</a>.</small></p>[/vc_column_text][vc_empty_space height="40px"][/vc_column][/vc_row]')
json.dump({"title":"Steel Buildings (rebuild)","status":"draft","content":c},open(SP+'/sb_create.json','w'))
print(len(c))
