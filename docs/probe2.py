import sys; sys.path.insert(0,'/home/claude/work/audit/tests')
from common import *
with sync_playwright() as p:
    b=p.chromium.launch()
    ctx,pg=mkpage(b,800,360,touch=True); mkprofile(pg); pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()")
    open_game(pg,'memori'); go(pg); pg.wait_for_timeout(200)
    pg.evaluate("window.scrollTo(0,document.documentElement.scrollHeight)"); pg.wait_for_timeout(200)
    print(pg.evaluate("""(()=>{const c=[...document.querySelectorAll('#main .opt')];const l=c[c.length-1],r=l.getBoundingClientRect();const t=document.elementFromPoint(r.left+r.width/2,Math.min(r.top+r.height/2,innerHeight-1));return {last:[r.top,r.bottom],inner:innerHeight,hit:t.className+'|'+t.tagName+'|'+(t.closest('#hd')?'dalam-hd':'luar')}})()"""))
    pg.screenshot(path='shot_land_memori_bottom.png'); ctx.close(); b.close()
