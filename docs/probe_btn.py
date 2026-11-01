import sys; sys.path.insert(0,'/home/claude/work/audit/tests')
from common import *
G=['warna','garis','pola','beda','hitung','spy','huruf','memori','bayangan','tambah','ganjil','labirin','urut','puzzle']
with sync_playwright() as p:
    b=p.chromium.launch(); ctx,pg=mkpage(b,360,800,touch=True); mkprofile(pg); pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()")
    for g in G:
        pg.evaluate(f"ACT.nav('home');ACT.play('{g}')"); pg.evaluate("document.querySelector('#main [data-a=go]').click()")
        if g=='puzzle': pg.evaluate("document.querySelector('[data-a=pzgo]').click()"); pg.wait_for_selector('#pzb',timeout=6000)
        pg.wait_for_timeout(300)
        bt=pg.evaluate("[...new Set([...document.querySelectorAll('#main button')].map(b=>b.dataset.a).filter(a=>!['ans','L','R','flip','bd','fill','col','sp','pzslot','pzpick','mv'].includes(a)))]")
        print(g.ljust(9),bt, '| header-nav:',pg.evaluate("[...document.querySelectorAll('#hd [data-a=nav]')].length"),'| gh:',pg.evaluate("(document.querySelector('#main .gh')||{}).textContent||''")[:40] if False else '')
    ctx.close(); b.close()
