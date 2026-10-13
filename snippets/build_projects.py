"""Build placeholder Portfolio (dt_portfolio) items + the Projects index page from snippets/project-template.txt.
Usage: python3 snippets/build_projects.py snippets/projects/placeholders.json <outdir>
Writes <outdir>/project_<slug>.json (POST /wp/v2/dt_portfolio body) and <outdir>/projects_index.json (POST /wp/v2/pages body)."""
import json, re, sys, base64, urllib.parse, os
specs=json.load(open(sys.argv[1])); out=sys.argv[2]; os.makedirs(out,exist_ok=True)
tpl=open('snippets/project-template.txt').read()
m=re.search(r'\[vc_raw_html\](.*?)\[/vc_raw_html\]\s*$',tpl,re.S)
css=urllib.parse.unquote(base64.b64decode(m.group(1)).decode()); body=tpl[:m.start()]
enc=lambda h:base64.b64encode(urllib.parse.quote(h,safe="!'()*-._~").encode()).decode()
for s in specs:
    b=body
    b=b.replace('PROJECT NAME',s['name'])
    b=b.replace('80 x 120 Commercial Warehouse in Rock Springs, WY',s['h1'])
    b=b.replace('One-sentence summary of the project, for example: A durable, efficient steel building for commercial storage in Rock Springs, WY.',s['summary'])
    b=b.replace('<i class="far fa-building"></i> Commercial<small>',f'<i class="{s["icon"]}"></i> {s["type"]}<small>')
    b=b.replace('<i class="fas fa-expand-arrows-alt"></i> 80 x 120<small>',f'<i class="fas fa-expand-arrows-alt"></i> {s["size"]}<small>')
    b=b.replace('<i class="fas fa-map-marker-alt"></i> Rock Springs, WY<small>',f'<i class="fas fa-map-marker-alt"></i> {s["location"]}<small>')
    b=b.replace('images=""',f'images="{",".join(map(str,s["gallery"]))}"')
    rows='\n'.join(f'<div class="proj-row"><i class="{i}"></i><div><b>{t}</b><span>{v}</span></div></div>' for i,t,v in s['details'])
    b=re.sub(r'(<h2>Project Details</h2>\n).*?(\[/vc_column_text\])',lambda mm:mm.group(1)+rows+'\n'+mm.group(2),b,count=1,flags=re.S)
    b=re.sub(r'(<h2>Why This Project Worked</h2><p>).*?(</p>)',lambda mm:mm.group(1)+s['why']+mm.group(2),b,count=1,flags=re.S)
    b=b.replace('[dt_default_button link="/#quote"]','[dt_default_button link="url:%2Fquote%2F" el_class="btn-orange"]').replace('link="/#quote"','link="url:%2Fquote%2F"')
    style='<style>'+css.replace('<style>','').replace('</style>','')+f'.proj-hero{{background-image:url({s["hero"]}) !important}}</style>'
    c=b+'[vc_raw_html]'+enc(style)+'[/vc_raw_html]'
    json.dump({'title':s['name'],'slug':s['slug'],'status':'draft','content':c},open(f'{out}/project_{s["slug"]}.json','w'))
    print(s['slug'],len(c))
# Projects index (static cards + small filter script)
types=[]; 
for s in specs:
    if s['type_slug'] not in [t[0] for t in types]: types.append((s['type_slug'],s['type']))
btns='<button class="pf-btn on" data-f="all">All</button>'+''.join(f'<button class="pf-btn" data-f="{k}">{v}</button>' for k,v in types)
cards=''.join(f'<a class="pf-card" data-t="{s["type_slug"]}" href="/project/{s["slug"]}/"><span class="pf-img" style="background-image:url({s["card"]})"></span><span class="pf-body"><b>{s["name"]}</b><em>{s["type"]} &middot; {s["location"]}</em><i>{s["size"]} ft</i></span></a>' for s in specs)
pcss='<style>.pf-filter{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin:0 0 24px}.pf-btn{background:#fff;border:2px solid #1a3153;color:#1a3153;border-radius:30px;padding:8px 18px;font-weight:700;cursor:pointer}.pf-btn.on{background:#1a3153;color:#fff}.pf-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}.pf-card{display:block;background:#f3f6fa;border-radius:6px;overflow:hidden;text-decoration:none;box-shadow:0 1px 4px rgba(26,49,83,.12)}.pf-card.hide{display:none}.pf-img{display:block;height:210px;background-size:cover;background-position:center}.pf-body{display:block;padding:14px 16px 16px}.pf-body b{display:block;color:#1a3153;font-size:18px;margin-bottom:4px}.pf-body em{display:block;color:#444b55;font-style:normal;font-size:14px}.pf-body i{display:block;color:#444b55;font-style:normal;font-size:14px;margin-top:2px}.pf-card:hover .pf-body b{color:#f68a31}@media(max-width:900px){.pf-grid{grid-template-columns:repeat(2,1fr)}}@media(max-width:560px){.pf-grid{grid-template-columns:1fr}}</style><script>document.addEventListener("click",function(e){var b=e.target.closest(".pf-btn");if(!b)return;document.querySelectorAll(".pf-btn").forEach(function(x){x.classList.remove("on")});b.classList.add("on");var f=b.getAttribute("data-f");document.querySelectorAll(".pf-card").forEach(function(c){c.classList.toggle("hide",f!=="all"&&c.getAttribute("data-t")!==f)})});</script>'
H=lambda t,sub='':f'[ultimate_heading main_heading="{t}" main_heading_style="font-weight:bold;" sub_heading_font_size="desktop:18px;" main_heading_margin="margin-bottom:10px;"]{sub}[/ultimate_heading]'
idx=('[vc_row el_class="hero-bg" full_width="stretch_row"][vc_column][vc_empty_space height="40px"][vc_column_text el_class="hero-eyebrow"]<p>OUR PROJECTS</p>[/vc_column_text]'
 '[ultimate_heading heading_tag="h1" main_heading="Steel Building Projects" alignment="left" main_heading_color="#ffffff" main_heading_style="font-weight:bold;" sub_heading_color="#ffffff" sub_heading_font_size="desktop:20px;" main_heading_margin="margin-bottom:12px;"]Browse custom steel buildings for commercial, agricultural, flex, and shop use across Wyoming, Utah, and Idaho.[/ultimate_heading][vc_empty_space height="50px"][/vc_column][/vc_row]'
 f'[vc_row][vc_column][vc_empty_space height="40px"][vc_column_text]<div class="pf-filter">{btns}</div><div class="pf-grid">{cards}</div>[/vc_column_text][vc_raw_html]{enc(pcss)}[/vc_raw_html][vc_empty_space height="40px"][/vc_column][/vc_row]'
 f'[vc_row el_class="about-quote" full_width="stretch_row"][vc_column][vc_empty_space height="40px"]{H("Planning a Similar Project?","Tell us about your building and we will provide a custom quote.")}[vc_empty_space height="20px"][dt_default_button link="url:%2Fquote%2F" button_alignment="btn_center" el_class="btn-orange"]Get a Free Quote[/dt_default_button][vc_empty_space height="40px"][/vc_column][/vc_row]')
json.dump({'title':'Projects (rebuild)','status':'draft','content':idx},open(f'{out}/projects_index.json','w')); print('index',len(idx))
