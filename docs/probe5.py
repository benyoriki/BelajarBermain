import sys; sys.path.insert(0,'/home/claude/work/audit/tests')
from common import *
with sync_playwright() as p:
    b=p.chromium.launch(); ctx,pg=mkpage(b,360,520,touch=True); mkprofile(pg); pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()"); cdp=ctx.new_cdp_session(pg)
    pg.evaluate("ACT.play('puzzle')"); pg.evaluate("document.querySelector('#main [data-a=go]').click()"); pg.evaluate("document.querySelector('[data-a=pzgo]').click()"); pg.wait_for_selector('#pzb',timeout=6000); pg.wait_for_timeout(200)
    pg.evaluate("window.__ev=[];['pointerdown','pointermove','pointerup','pointercancel','touchstart','touchmove','touchend','click'].forEach(t=>document.addEventListener(t,e=>window.__ev.push(t+':'+(e.target.className||e.target.tagName).toString().slice(0,10)),true))")
    pg.evaluate("document.querySelector('#pzb').scrollIntoView({block:'start'})"); pg.wait_for_timeout(100)
    def c(sel): b=pg.locator(sel).first.bounding_box(); return b['x']+b['width']/2,b['y']+b['height']/2
    a=c('.pzp2[data-v="0"]'); s=c('.pzs2[data-v="0"]'); print('piece',a,'slot',s,'inner',pg.evaluate('[innerWidth,innerHeight]'))
    print('touch-action piece:',pg.evaluate("getComputedStyle(document.querySelector('.pzp2')).touchAction"),'| tray:',pg.evaluate("getComputedStyle(document.querySelector('.pzy')).touchAction"),pg.evaluate("getComputedStyle(document.querySelector('.pzy')).overflowX"))
    send=lambda t,pts: cdp.send('Input.dispatchTouchEvent',{'type':t,'touchPoints':pts})
    send('touchStart',[{'x':a[0],'y':a[1]}])
    for i in range(1,11): send('touchMove',[{'x':a[0]+(s[0]-a[0])*i/10,'y':a[1]+(s[1]-a[1])*i/10}])
    send('touchEnd',[]); pg.wait_for_timeout(300)
    print(pg.evaluate("window.__ev").__len__(),pg.evaluate("[...new Set(window.__ev)].slice(0,14)"), 'ok=',pg.evaluate("G.pz.ok"))
    b.close()
