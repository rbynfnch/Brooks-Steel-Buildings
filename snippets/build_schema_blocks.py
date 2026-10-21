"""Builds JSON-LD edit payloads for /wpvibe/v1/content/edit (company + per-page Service data).
Usage (repo root): python3 snippets/build_schema_blocks.py
Writes snippets/schema_payloads/<post_id>.json = {target_type, post_id, field, old_content, new_content}.
Anchor: the Quick Quote shortcode in the quote band; the block is inserted right after it (page-level raw html, base64 like the FAQ schema).
"""
import json,base64,urllib.parse,os
BASE='https://brookssteelbuildings.com'
ANCHOR="[gravityform id='2' title='false' description='false' ajax='true']"
def enc(h): return base64.b64encode(urllib.parse.quote(h,safe='').encode()).decode()
LB_ID=BASE+'/#localbusiness'
LB={"@type":"LocalBusiness","@id":LB_ID,"name":"Brooks Steel Buildings","url":BASE+"/","telephone":"+1-800-908-4839",
 "image":BASE+"/wp-content/uploads/2020/06/Brooks-Steel-Buildings-Logo-1.jpg","logo":BASE+"/wp-content/uploads/2020/06/Brooks-Steel-Buildings-Logo-1.jpg",
 "description":"Custom pre-engineered steel buildings for Wyoming, Utah, and Idaho, supplied from Evanston, Wyoming.",
 "address":{"@type":"PostalAddress","streetAddress":"254 City View Dr.","addressLocality":"Evanston","addressRegion":"WY","postalCode":"82930","addressCountry":"US"},
 "areaServed":[{"@type":"State","name":n} for n in ("Wyoming","Utah","Idaho")],
 "sameAs":["https://www.facebook.com/brookssteelbuildings","https://www.instagram.com/brookssteelbuildings","https://www.linkedin.com/company/33190238"]}
STATES={"WY":"Wyoming","UT":"Utah","ID":"Idaho"}
def provider(): return {"@type":"LocalBusiness","@id":LB_ID,"name":LB["name"],"url":LB["url"],"telephone":LB["telephone"],"address":LB["address"]}
def service(url,name,desc,areas=None,stype="Pre-engineered steel buildings"):
    return {"@context":"https://schema.org","@type":"Service","@id":url+"#service","name":name,"serviceType":stype,"description":desc,"url":url,
      "provider":provider(),"areaServed":areas or LB["areaServed"]}
# (post_id, path, service name, description)
TYPES=[(1207,'steel-buildings/commercial/','Commercial and Retail Steel Buildings','Custom commercial and retail steel buildings for offices, warehouses, and storefronts in Wyoming, Utah, and Idaho. Clear-span options.'),
 (2597,'steel-buildings/flex-buildings/','Steel Flex Buildings','Custom steel flex buildings combining office, showroom, warehouse, and shop space in Wyoming, Utah, and Idaho.'),
 (2614,'steel-buildings/agricultural-steel-buildings/','Agricultural Steel Buildings and Barns','Custom hay barns and agricultural steel buildings for farms and ranches in Wyoming, Utah, and Idaho, engineered for your site’s snow loads.'),
 (2635,'steel-buildings/industrial/','Industrial and Warehouse Steel Buildings','Custom industrial and warehouse steel buildings with clear-span interiors and tall eaves for Wyoming, Utah, and Idaho.'),
 (1223,'steel-buildings/shops/','Steel Garages and Shop Buildings','Custom steel garages and shop buildings for RV storage, workshops, and home businesses in Wyoming, Utah, and Idaho.'),
 (2657,'steel-buildings/aircraft-hangars/','Steel Aircraft Hangars','Custom steel aircraft hangars for private and corporate aircraft in Wyoming, Utah, and Idaho. Clear-span, engineered for your site.'),
 (1233,'steel-buildings/recreational/','Steel Recreational Buildings and Gyms','Custom steel recreational buildings, gyms, and indoor sports facilities with clear spans and tall eaves in Wyoming, Utah, and Idaho.'),
 (2218,'steel-buildings/schools-and-gymnasiums/','Steel School and Gymnasium Buildings','Custom steel buildings for schools, gymnasiums, and churches in Wyoming, Utah, and Idaho. Clear-span, engineered for your site.'),
 (1288,'steel-buildings/storage-unit/','Steel Storage Unit Buildings','Custom steel storage unit buildings for mini storage, drive-up units, and RV storage in Wyoming, Utah, and Idaho.'),
 (2215,'steel-buildings/equestrian-riding-arenas/','Steel Riding Arenas and Horse Barns','Custom pre-engineered steel riding arenas and horse barns for Wyoming, Utah, and Idaho. Clear-span, engineered for your site.'),
 (2699,'steel-buildings/barndominiums/','Steel Barndominium Buildings','Custom pre-engineered steel barndominium and shop house building packages for Wyoming, Utah, and Idaho. Engineered for your site.')]
STATE_PAGES=[(2679,'wyoming-steel-buildings/','Steel Buildings in Wyoming','Custom pre-engineered steel buildings across Wyoming, from Evanston to Star Valley. Engineered for your snow and wind loads.',[{"@type":"State","name":"Wyoming"}]),
 (2682,'utah-steel-buildings/','Steel Buildings in Utah','Custom pre-engineered steel buildings throughout Utah, from the Wasatch Front to rural communities. Engineered for snow, wind, and seismic loads.',[{"@type":"State","name":"Utah"}]),
 (2670,'idaho-steel-buildings/','Steel Buildings in Idaho','Custom pre-engineered steel buildings in Idaho, including Idaho Falls, Rexburg, Driggs, and Pocatello. Engineered for your snow and wind loads.',[{"@type":"State","name":"Idaho"}]),
 (2297,'star-valley-wyoming-steel-buildings/','Steel Buildings in Star Valley, Wyoming','Custom pre-engineered steel buildings for Star Valley, Wyoming, including Afton, Alpine, and Thayne. Engineered for your snow and wind loads.',[{"@type":"Place","name":"Star Valley, Wyoming","containedInPlace":{"@type":"State","name":"Wyoming"}}])]
def write(pid,obj_list):
    html='<script type="application/ld+json">'+json.dumps(obj_list if len(obj_list)>1 else obj_list[0],ensure_ascii=False)+'</script>'
    json.loads(html[len('<script type="application/ld+json">'):-len('</script>')])  # validate
    new=ANCHOR+'[vc_raw_html]'+enc(html)+'[/vc_raw_html]'
    json.dump({"target_type":"post","post_id":pid,"field":"post_content","old_content":ANCHOR,"new_content":new},open('snippets/schema_payloads/%d.json'%pid,'w'))
    return len(new)
for pid,path,name,desc in TYPES: write(pid,[service(BASE+'/'+path,name,desc)])
for pid,path,name,desc,areas in STATE_PAGES: write(pid,[service(BASE+'/'+path,name,desc,areas,"Pre-engineered steel buildings")])
# Home: full LocalBusiness entity with @id; Hub: service catalog
write(2476,[dict({"@context":"https://schema.org"},**LB)])
cat={"@context":"https://schema.org","@type":"Service","@id":BASE+"/steel-buildings/#service","name":"Pre-engineered steel buildings","serviceType":"Pre-engineered steel buildings","url":BASE+"/steel-buildings/",
 "provider":provider(),"areaServed":LB["areaServed"],
 "hasOfferCatalog":{"@type":"OfferCatalog","name":"Steel building types","itemListElement":[{"@type":"Offer","itemOffered":{"@type":"Service","name":n,"url":BASE+'/'+p}} for _,p,n,_ in TYPES]}}
write(249,[cat])
print(sorted(os.listdir('snippets/schema_payloads')))
