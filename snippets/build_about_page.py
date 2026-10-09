import base64,urllib.parse,json
SP='/tmp/claude-0/-home-user-Brooks-Steel-Buildings/16b9ac92-3fc0-5869-ab7b-4f92b9081108/scratchpad'
def enc(h): return base64.b64encode(urllib.parse.quote(h,safe='').encode()).decode()
css=""".about-alt{background:#f7f9fc}
.about-wrap{max-width:1000px;margin:0 auto}
.about-cards{display:flex;flex-wrap:wrap;gap:20px}
.about-card{flex:1 1 calc(33.333% - 20px);min-width:240px;background:#f3f6fa;border-radius:6px;padding:22px}
.about-alt .about-card{background:#fff}
.about-card i{font-size:28px;color:#1a3153;margin-bottom:10px;display:block}
.about-card h3{font-size:19px;margin:0 0 6px;color:#1a3153}
.about-card p{margin:0;color:#444b55}
.about-states{display:flex;flex-wrap:wrap;gap:30px}
.about-states>div{flex:1 1 220px}
.about-states h3{color:#1a3153;margin:0 0 8px}
.about-states ul{list-style:none;margin:0 0 8px;padding:0}
.about-states li{padding:3px 0;color:#444b55}
.about-steps{display:flex;flex-wrap:wrap;gap:16px}
.about-steps>div{flex:1 1 170px;text-align:center;padding:16px;background:#fff;border-radius:6px;border-top:4px solid #f68a31}
.about-steps b{display:block;color:#1a3153;font-size:18px;margin-bottom:6px}
.about-steps span{color:#444b55;font-size:15px}
.about-quote{background:#1a3153;box-shadow:0 0 0 100vmax #1a3153;clip-path:inset(0 -100vmax)}
.about-quote h2,.about-quote .uvc-sub-heading,.about-quote .gfield_label,.about-quote p,.about-quote p a{color:#fff!important}
.about-quote .gform-field-label--type-sub,.about-quote .gfield_required{color:#dfe6f1!important}
.about-quote .gform_wrapper{max-width:900px;margin:0 auto}
.about-quote .gform_wrapper form{display:flex;flex-wrap:wrap;align-items:flex-end;gap:10px 14px}
.about-quote .gform_wrapper .gform_body{flex:1 1 100%}
.about-quote .gform_wrapper ul.gform_fields{display:flex;flex-wrap:wrap;gap:8px 14px;margin:0;padding:0;list-style:none}
.about-quote .gform_wrapper li.gfield{flex:1 1 100%;margin:0;padding:0;width:auto}
.about-quote .gform_wrapper li[id^="field_2_8"],.about-quote .gform_wrapper li[id^="field_2_9"],.about-quote .gform_wrapper li[id^="field_2_10"]{flex:1 1 calc(33.333% - 10px)}
.about-quote .gform_wrapper li[id^="field_2_14"],.about-quote .gform_wrapper li[id^="field_2_7"]{flex:1 1 calc(50% - 7px)}
.about-quote .gform_wrapper input[type=text],.about-quote .gform_wrapper input[type=tel],.about-quote .gform_wrapper input[type=email],.about-quote .gform_wrapper textarea{width:100%;box-sizing:border-box;padding:8px 10px;font-size:15px}
.about-quote .gform_wrapper textarea{height:44px;min-height:44px}
.about-quote .gform_wrapper .gfield_label{font-size:13px;margin-bottom:2px;padding:0}
.about-quote .gform_wrapper .ginput_complex span{display:inline-block;width:calc(50% - 6px);padding:0}
.about-quote .gform_wrapper .gform_footer{margin:0;padding:0}
@media(max-width:778px){.about-quote .gform_wrapper li.gfield{flex:1 1 100%!important}}"""
style=enc('<style>'+''.join(l.strip() for l in css.split('\n'))+'</style>')
faq=[("Where is Brooks Steel Buildings located?","We are based at 254 City View Dr., Evanston, Wyoming 82930. You can reach us at 800-908-4839."),
("What areas do you serve?","We supply custom steel buildings across Wyoming, Utah, and Idaho."),
("How long has Brooks Steel Buildings been in business?","The company is led by an owner with more than 30 years of experience in the steel building industry."),
("What kinds of buildings do you offer?","Commercial and retail, agricultural, industrial and warehouse, storage, recreational, shops and garages, schools and gymnasiums, equestrian riding arenas, aircraft hangars, and barndominiums.")]
ld={"@context":"https://schema.org","@graph":[
{"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]},
{"@type":"LocalBusiness","name":"Brooks Steel Buildings","url":"https://brookssteelbuildings.com/","telephone":"+1-800-908-4839","address":{"@type":"PostalAddress","streetAddress":"254 City View Dr.","addressLocality":"Evanston","addressRegion":"WY","postalCode":"82930","addressCountry":"US"},"areaServed":[{"@type":"State","name":"Wyoming"},{"@type":"State","name":"Utah"},{"@type":"State","name":"Idaho"}],"sameAs":["https://www.facebook.com/brookssteelbuildings","https://www.instagram.com/brookssteelbuildings","https://www.linkedin.com/company/33190238"]}]}
schema=enc('<script type="application/ld+json">'+json.dumps(ld)+'</script>')
def card(i,t,p): return f'<div class="about-card"><i class="{i}"></i><h3>{t}</h3><p>{p}</p></div>'
cards=''.join([card('fas fa-drafting-compass','Custom Designed','Your building is designed for how you will use it, whether that is commercial, agricultural, equestrian, or residential.'),
card('fas fa-snowflake','Built for Snow and Wind','We design for the snow loads, wind, and temperature swings common across Wyoming, Utah, and Idaho.'),
card('fas fa-clock','Faster Construction','Steel buildings go up faster than many traditional methods, which can reduce labor time and delays.'),
card('fas fa-expand-arrows-alt','Open Interiors','Clear-span designs are available for open space with no interior support columns.'),
card('fas fa-map-marked-alt','Regional Know-How','We know the codes and conditions in the three states we serve.'),
card('fas fa-clipboard-check','Permitting Support','Buildings are designed with local codes and structural requirements in mind, and engineered plans are prepared for permitting. Requirements vary by location.')])
def col(h,l,towns): return f'<div><h3>{h}</h3><ul>'+''.join(f'<li>{t}</li>' for t in towns)+f'</ul>{l}</div>'
states=col('Wyoming','<p><a href="/wyoming-steel-buildings/">Wyoming Steel Buildings</a></p>',['Evanston','Rock Springs','Pinedale','Afton','Star Valley','Lyman','Jackson'])+col('Utah','<p><a href="/utah-steel-buildings/">Utah Steel Buildings</a></p>',['Salt Lake','Ogden','Provo / Orem','Spanish Fork','Payson','Mapleton','Heber','Coalville','St. George'])+col('Idaho','',['Idaho Falls','Rexburg','Driggs','Swan Valley','Pocatello','Preston','Montpelier'])
steps=''.join(f'<div><b>{i+1}. {t}</b><span>{d}</span></div>' for i,(t,d) in enumerate([('Design','We talk through your needs, site, and budget and plan the right building.'),('Engineering','Your building is engineered for local codes, with plans prepared for permitting.'),('Preparation','Your building package is prepared for accurate, efficient assembly.'),('Delivery','Your building package is delivered to your job site.'),('Construction','Build it yourself or hire a contractor.')]))
def H(t,sub=''): return f"[ultimate_heading heading_tag='h2' main_heading='{t}' main_heading_style='font-weight:bold;' sub_heading_font_size='desktop:18px;' main_heading_margin='margin-bottom:10px;']{sub}[/ultimate_heading]"
toggles=''.join(f"[vc_toggle title='{q}']{a}[/vc_toggle]" for q,a in faq)
c=f"""[vc_row el_class="hero-bg" full_width="stretch_row"][vc_column][vc_empty_space height="50px"][vc_column_text el_class="hero-eyebrow"]<p>ABOUT US</p>[/vc_column_text][ultimate_heading heading_tag="h1" main_heading="Steel Building Experts in Wyoming, Utah &amp; Idaho" alignment="left" main_heading_color="#ffffff" main_heading_style="font-weight:bold;" sub_heading_color="#ffffff" sub_heading_font_size="desktop:20px;" main_heading_margin="margin-bottom:12px;"]Brooks Steel Buildings is a custom steel building supplier based in Evanston, Wyoming, with 30+ years of experience serving customers across Wyoming, Utah, and Idaho.[/ultimate_heading][vc_empty_space height="10px"][vc_row_inner el_class="hero-btns"][vc_column_inner width="1/2"][dt_default_button link="/#quote" el_class="btn-orange"]Get a Free Quote[/dt_default_button][/vc_column_inner][vc_column_inner width="1/2"][dt_default_button link="tel:8009084839" el_class="btn-outline-white"]Call 800-908-4839[/dt_default_button][/vc_column_inner][/vc_row_inner][vc_empty_space height="50px"][/vc_column][/vc_row]
[vc_row][vc_column][vc_empty_space height="40px"]{H('Who We Are')}[vc_column_text el_class="about-wrap"]<p>Brooks Steel Buildings supplies custom pre-engineered steel buildings for commercial, agricultural, equestrian, shop, and residential use. Every building is designed around your site, your use, and your budget.</p><p>The company is owned and operated by Brooks Walk, who has spent more than 30 years in the steel building industry. That experience helps guide you through each step, from design and engineering plans to delivery and construction.</p>[/vc_column_text][vc_empty_space height="30px"][/vc_column][/vc_row]
[vc_row el_class="about-alt" full_width="stretch_row"][vc_column][vc_empty_space height="40px"]{H('Why Customers Choose Brooks Steel Buildings','Every building is custom designed for your project, location, and use.')}[vc_empty_space height="20px"][vc_column_text]<div class="about-cards">{cards}</div>[/vc_column_text][vc_empty_space height="40px"][/vc_column][/vc_row]
[vc_row][vc_column][vc_empty_space height="40px"]{H('Serving Wyoming, Utah &amp; Idaho','From small towns to growing cities, we supply steel buildings engineered for local snow loads, wind, and building conditions.')}[vc_empty_space height="20px"][vc_column_text]<div class="about-states">{states}</div>[/vc_column_text][vc_empty_space height="40px"][/vc_column][/vc_row]
[vc_row el_class="about-alt" full_width="stretch_row"][vc_column][vc_empty_space height="40px"]{H('How Your Project Works','A simple process from first call to finished building.')}[vc_empty_space height="20px"][vc_column_text]<div class="about-steps">{steps}</div>[/vc_column_text][vc_empty_space height="40px"][/vc_column][/vc_row]
[vc_row][vc_column][vc_empty_space height="40px"]{H('Common Questions')}[vc_empty_space height="20px"]{toggles}[vc_raw_html]{schema}[/vc_raw_html][vc_empty_space height="40px"][/vc_column][/vc_row]
[vc_row el_class="about-quote"][vc_column][vc_empty_space height="40px"]{H('Get Your Free Quote','Tell us about your project and we will provide a custom quote based on your needs.')}[vc_empty_space height="20px"][vc_raw_html]{style}[/vc_raw_html][gravityform id='2' title='false' description='false' ajax='true'][vc_column_text]<p style="text-align:center;">Prefer to talk? Call <a href="tel:8009084839">800-908-4839</a>.</p>[/vc_column_text][vc_empty_space height="40px"][/vc_column][/vc_row]""".replace('\n','')
open(SP+'/about_content.txt','w').write(c)
json.dump({"title":"About Us (rebuild)","status":"draft","content":c},open(SP+'/about_create.json','w'))
print(len(c))
