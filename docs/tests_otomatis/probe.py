import sys; sys.path.insert(0,'/home/claude/work/audit/tests')
from common import *
with sync_playwright() as p:
    b=p.chromium.launch()
    ctx,pg=mkpage(b,360,800,touch=True); mkprofile(pg); pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()")
    print('dcard overflow children:',pg.evaluate("""(()=>{const c=document.querySelector('.dcard'),r=c.getBoundingClientRect();return [...c.querySelectorAll('*')].filter(e=>{const q=e.getBoundingClientRect();return q.right>r.right+1||q.left<r.left-1||q.bottom>r.bottom+1}).map(e=>e.className+' '+Math.round(e.getBoundingClientRect().right-r.right)).slice(0,5)})()"""))
    print('css gal:',pg.evaluate("getComputedStyle(document.querySelector('.gal')).overflowX"))
    print('#hd position:',pg.evaluate("[getComputedStyle(document.querySelector('#hd')).position,getComputedStyle(document.querySelector('#hd nav')).position]"))
    pg.set_viewport_size({'width':800,'height':360}); open_game(pg,'memori'); go(pg); pg.wait_for_timeout(200)
    print('landscape memori:',pg.evaluate("""(()=>{const hd=document.querySelector('#hd nav').getBoundingClientRect(),m=document.querySelector('#hd .me').getBoundingClientRect();const c=[...document.querySelectorAll('#main .opt')];const last=c[c.length-1].getBoundingClientRect();return {nav:[hd.top,hd.bottom,hd.left,hd.right],me:[m.top,m.bottom,m.left,m.right],last:[last.top,last.bottom,last.left,last.right],hdPos:getComputedStyle(document.querySelector('#hd')).position,navPos:getComputedStyle(document.querySelector('#hd nav')).position,pb:getComputedStyle(document.querySelector('#main')).paddingBottom,sh:document.documentElement.scrollHeight}})()"""))
    pg.screenshot(path='shot_land_memori.png'); ctx.close()
    ctx,pg=mkpage(b,320,568,touch=True); mkprofile(pg); pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()")
    print('sw css:',pg.evaluate("(open_=0,ACT.play('warna'),ACT.go(),getComputedStyle(document.querySelector('.sw')).width+' '+getComputedStyle(document.querySelector('.sw')).minWidth)"))
    b.close()
