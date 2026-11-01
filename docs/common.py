import json,time
from playwright.sync_api import sync_playwright
URL='http://localhost:8810/index.html'
R=[]  # hasil
def rec(game,skenario,harap,aktual,ok,catatan=''):
    R.append(dict(game=game,skenario=skenario,harapan=harap,aktual=str(aktual),status='PASS' if ok else 'FAIL',catatan=catatan))
def mkpage(b,vw=412,vh=900,sw='block',touch=False,tz='Asia/Jakarta',seed=None):
    ctx=b.new_context(viewport={'width':vw,'height':vh},service_workers=sw,has_touch=touch,timezone_id=tz)
    pg=ctx.new_page(); pg.errs=[]
    pg.on('pageerror',lambda e:pg.errs.append(str(e)))
    pg.on('console',lambda m: pg.errs.append('console:'+m.text) if m.type=='error' and 'Failed to load resource' not in m.text else None)
    pg.route('https://*/**',lambda r:r.abort())
    if seed is not None:
        pg.add_init_script("if(!localStorage.getItem('bba1'))localStorage.setItem('bba1',%s)"%json.dumps(json.dumps(seed)))
    pg.goto(URL); pg.wait_for_timeout(300)
    return ctx,pg
def mkprofile(pg,name='Dono',age=1):
    pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()")
    pg.click('[data-a=new]'); pg.fill('#nm',name)
    pg.click(f'[data-a=age][data-v="{age}"]'); pg.click('[data-a=saveP]'); pg.wait_for_timeout(250)
def P(pg): return pg.evaluate("(()=>{const p=P();return p?JSON.parse(JSON.stringify(p)):null})()")
def pts(pg): return pg.evaluate("P().pts")
def open_game(pg,gid):
    pg.evaluate(f"ACT.play('{gid}')"); pg.wait_for_timeout(250)
def go(pg):
    pg.click('#main [data-a=go]'); pg.wait_for_timeout(350)
def on_fin(pg):
    t=pg.inner_text('#main'); return 'Aktivitas selesai' in t or 'Puzzle Selesai' in t
