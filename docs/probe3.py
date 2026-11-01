import sys; sys.path.insert(0,'/home/claude/work/audit/tests')
from common import *
with sync_playwright() as p:
    b=p.chromium.launch(); ctx,pg=mkpage(b,360,800,touch=True); mkprofile(pg); pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()")
    pg.evaluate("ACT.play('beda')"); pg.evaluate("document.querySelector('#main [data-a=go]').click()"); pg.wait_for_timeout(300)
    d=pg.evaluate("G.d[0]"); pg.locator(f'[data-a=bd][data-v="{d}"]').tap(); pg.wait_for_timeout(200)
    print(pg.evaluate("""(()=>{const e=document.querySelector('.gctl [data-a=rst]');if(!e)return 'TIDAK ADA';e.scrollIntoView({block:'center'});const r=e.getBoundingClientRect(),t=document.elementFromPoint(r.left+r.width/2,r.top+r.height/2);return {rect:[r.top,r.bottom],inner:innerHeight,hit:t.className+'|'+t.tagName+'|'+t.id,fb:(document.getElementById('fb')||{}).textContent}})()"""))
    pg.screenshot(path='shot_beda_reset.png',full_page=False)
    ctx.close(); b.close()
