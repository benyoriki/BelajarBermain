# QA ilustrasi: lembar kontak + luas area terlihat per bentuk (piksel di skala 4x). Pakai: python3 tools/qa_gambar.py [id1 id2 ...]
import json,sys,subprocess
from playwright.sync_api import sync_playwright
ids=sys.argv[1:]
js=open('gambar-baru.js').read()
CSS='.f{stroke:#333;stroke-width:3;stroke-linejoin:round;stroke-linecap:round}.ey{fill:#222}.hl{fill:#fff}.o2{fill:none;stroke:#222;stroke-width:3;stroke-linecap:round}.o3{fill:none;stroke:#222;stroke-width:2}'
HTML='<html><body style="margin:0;background:#eee"><script>'+js+'</script><script>window.ART=BBA_ART</script></body></html>'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1500,'height':900}); pg.set_content(HTML)
    res=pg.evaluate("""async(args)=>{const [ids,CSS]=args;const A=ART.filter(a=>!ids.length||ids.includes(a.id));const out={};let h='<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;padding:8px;font:14px sans-serif">';
    const ns='http://www.w3.org/2000/svg';
    for(const a of A){h+=`<div style="background:#fff;border-radius:10px;padding:4px"><b>${a.id} (${a.s.length})</b><svg viewBox="0 0 300 200" width="100%"><style>${CSS}</style><rect width="300" height="200" fill="#eaf8ff"/>${a.s.map(s=>`<${s} class="f" style="fill:#fff"/>`).join('')}${a.d}</svg></div>`;
      // luas area terlihat
      const cols=a.s.map((_,i)=>'rgb('+[(i*37+20)%256,(i*91+60)%256,(i*53+100)%256]+')');
      const svg=`<svg xmlns="${ns}" viewBox="0 0 300 200" width="1200" height="800"><rect width="300" height="200" fill="#fff"/>${a.s.map((s,i)=>`<${s} fill="${cols[i]}" stroke="none"/>`).join('')}</svg>`;
      const img=new Image();img.src='data:image/svg+xml;charset=utf-8,'+encodeURIComponent(svg);await img.decode();
      const c=document.createElement('canvas');c.width=1200;c.height=800;const x=c.getContext('2d');x.drawImage(img,0,0);const d=x.getImageData(0,0,1200,800).data;
      const cnt=a.s.map(()=>0);const map={};cols.forEach((k,i)=>map[k]=i);
      for(let i=0;i<d.length;i+=4){const k='rgb('+d[i]+','+d[i+1]+','+d[i+2]+')';if(k in map)cnt[map[k]]++}
      out[a.id]=cnt.map(n=>Math.round(n/16));
      // keluar kanvas?
    }
    h+='</div>';document.body.innerHTML=h;return out}""",[ids,CSS])
    pg.set_viewport_size({'width':1500,'height':900})
    pg.screenshot(path='/home/claude/qa_sheet.png',full_page=True)
    b.close()
bad={}
for k,v in res.items():
    s=[(i,n) for i,n in enumerate(v) if n<380]
    if s: bad[k]=s
print('area kecil (<380 unit^2, indeks,luas):',json.dumps(bad))
json.dump(res,open('/home/claude/qa_area.json','w'))
