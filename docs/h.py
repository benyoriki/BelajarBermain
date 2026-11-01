import json,sys
from playwright.sync_api import sync_playwright
PORT=8811
import threading,http.server,functools,os
ROOT=os.environ.get('BBA_ROOT','/home/claude/work/Buku_anak')
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
def _serve():
    try:
        srv=http.server.ThreadingHTTPServer(('127.0.0.1',PORT),functools.partial(Q,directory=ROOT))
    except OSError: return
    threading.Thread(target=srv.serve_forever,daemon=True).start()
_serve()
URL=f'http://localhost:{PORT}/index.html'
SEED={"p":[{"id":"k1","name":"Dono","av":"🦕","age":1,"pts":120,"done":3,"ok":10,"bad":2,"best":4,"dc":0,"dcDay":"","bd":[],"hist":[],"days":{},"art":{},"played":2,"adj":0}],"cur":"k1","snd":0}
def page(b,vw=360,vh=740,touch=True,sw='block',seed=SEED,landscape=False,tv=False):
    if landscape: vw,vh=vh,vw
    ctx=b.new_context(viewport={'width':vw,'height':vh},service_workers=sw,has_touch=touch,is_mobile=touch and vw<900,device_scale_factor=1,timezone_id='Asia/Jakarta')
    pg=ctx.new_page(); pg.errs=[]
    pg.on('pageerror',lambda e:pg.errs.append(str(e)))
    pg.on('console',lambda m: pg.errs.append('console:'+m.text) if m.type=='error' and 'Failed to load resource' not in m.text else None)
    pg.route('https://**',lambda r:r.abort()); pg.route('http://**',lambda r: r.continue_() if f'localhost:{PORT}' in r.request.url else r.abort())
    if seed is not None:
        pg.add_init_script("if(!localStorage.getItem('bba1'))localStorage.setItem('bba1',%s);sessionStorage.setItem('bba_ld','1')"%json.dumps(json.dumps(seed)))
    pg.goto(URL); pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()"); pg.wait_for_timeout(250)
    return ctx,pg
def play(pg,gid):
    pg.evaluate(f"ACT.play('{gid}')"); pg.wait_for_timeout(250)
def go(pg):
    pg.click('#main [data-a=go]'); pg.wait_for_timeout(300)
