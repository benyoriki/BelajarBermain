# Offline + tata letak HP/PC + permainan lain tidak terganggu
import json
from common import *
OUT=[]
def T(n,ok,i=''):
    OUT.append(dict(uji=n,status='PASS' if ok else 'FAIL',bukti=str(i)));print(('PASS ' if ok else 'FAIL ')+n,'|',str(i)[:150])
with sync_playwright() as p:
    b=p.chromium.launch()
    # offline: SW aktif
    ctx=b.new_context(viewport={'width':412,'height':800},service_workers='allow',has_touch=True)
    pg=ctx.new_page();errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.route('https://*/**',lambda r:r.abort())
    pg.goto(URL);pg.wait_for_timeout(2500)
    pg.evaluate("navigator.serviceWorker.ready.then(()=>0);0");pg.wait_for_timeout(1500)
    keys=pg.evaluate("caches.keys().then(k=>k.join())");T('Cache bba-<hash> aktif',keys.startswith('bba-'),keys)
    cached=pg.evaluate("caches.open('%s')"%keys+".then(c=>c.keys()).then(r=>r.map(x=>new URL(x.url).pathname))")
    T('gambar-baru.js & warna.css masuk cache',any('gambar-baru.js' in x for x in cached) and any('warna.css' in x for x in cached))
    ctx.set_offline(True);pg.reload();pg.wait_for_timeout(800)
    pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()")
    mkprofile(pg,'Off',1);open_game(pg,'warna');go(pg);pg.wait_for_timeout(300)
    T('Offline: katalog 84 kartu',pg.evaluate("document.querySelectorAll('.wc').length")==84)
    pg.evaluate("ACT.wpick('gurita')");pg.wait_for_timeout(300)
    T('Offline: kanvas terbuka',pg.evaluate("document.querySelectorAll('.cv .f').length")==10)
    T('Offline: tanpa galat JS',not errs,errs[:2]);ctx.close()
    # tata letak
    for nm,vw,vh,tc in [('HP 360',360,740,True),('HP 320',320,640,True),('Tablet',820,1180,True),('PC',1366,768,False),('TV',1920,1080,False)]:
        ctx,pg=mkpage(b,vw,vh,touch=tc);mkprofile(pg,'L',1);open_game(pg,'warna');go(pg);pg.wait_for_timeout(300)
        h1=pg.evaluate("document.documentElement.scrollWidth<=innerWidth+1")
        pg.evaluate("ACT.wpick('kucing')");pg.wait_for_timeout(300)
        r=pg.evaluate("""(()=>{const c=document.querySelector('.cv').getBoundingClientRect(),p=document.querySelector('.wpal').getBoundingClientRect();
          const sw=[...document.querySelectorAll('.wpal .sw')].map(e=>e.getBoundingClientRect());
          return {noh:document.documentElement.scrollWidth<=innerWidth+1,sep:p.top>=c.bottom-1,minsw:Math.min(...sw.map(s=>Math.min(s.width,s.height))),cw:c.width}})()""")
        T(f'{nm}: tanpa scroll horizontal (katalog & kanvas)',h1 and r['noh'])
        T(f'{nm}: palet tidak menutupi gambar',r['sep'])
        T(f'{nm}: swatch >=44px',r['minsw']>=43,round(r['minsw']))
        pg.screenshot(path=f'/home/claude/lay_{nm.replace(" ","")}.png')
        T(f'{nm}: tanpa galat JS',not pg.errs,pg.errs[:2]);ctx.close()
    # permainan lain
    ctx,pg=mkpage(b,412,900,touch=True);mkprofile(pg,'G',1)
    for g in ['pola','hitung','huruf','tambah','ganjil','garis','beda','spy','memori','bayangan','labirin','urut','puzzle']:
        pg.evaluate(f"ACT.play('{g}')");pg.wait_for_timeout(150)
        try: pg.click('#main [data-a=go]',timeout=2000);pg.wait_for_timeout(250)
        except Exception: pass
        T(f'Permainan {g} tetap terbuka',pg.evaluate("document.querySelector('#main .gh, #main .card')!==null"))
    T('Permainan lain tanpa galat JS',not pg.errs,pg.errs[:3]);ctx.close();b.close()
json.dump(OUT,open('hasil_mewarnai_offline_layout.json','w'),ensure_ascii=False,indent=1)
print('PASS',sum(o['status']=='PASS' for o in OUT),'FAIL',sum(o['status']=='FAIL' for o in OUT))
