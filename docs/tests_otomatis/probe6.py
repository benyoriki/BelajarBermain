import sys; sys.path.insert(0,'/home/claude/work/audit/tests')
from common import *
with sync_playwright() as p:
    b=p.chromium.launch(); ctx,pg=mkpage(b,360,800,touch=True); mkprofile(pg); pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()")
    pg.set_viewport_size({'width':800,'height':360}); pg.evaluate("ACT.play('labirin')"); pg.evaluate("document.querySelector('#main [data-a=go]').click()"); pg.wait_for_timeout(400)
    print(pg.evaluate("""[...document.querySelectorAll('#main *')].filter(e=>{const c=getComputedStyle(e);return (c.overflow==='hidden'||c.textOverflow==='ellipsis')&&e.clientWidth>0&&e.scrollWidth>e.clientWidth+2}).map(e=>[e.tagName,e.className,e.id,e.clientWidth,e.scrollWidth,e.textContent.trim().slice(0,30)])"""))
    pg.screenshot(path='shot_land_labirin.png'); ctx.close(); b.close()
