import sys; sys.path.insert(0,'/home/claude/work/audit/tests')
from common import *
with sync_playwright() as p:
    b=p.chromium.launch(); ctx,pg=mkpage(b,360,800,touch=True); mkprofile(pg); pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()")
    pg.evaluate("Storage.prototype.setItem=function(){throw new DOMException('Quota','QuotaExceededError')}")
    for step in ["ACT.play('hitung')","document.querySelector('#main [data-a=go]').click()","document.querySelector(`#main [data-a=ans][data-v='${G.q.a}']`).click()"]:
        try: pg.evaluate(step); print('ok  ',step[:50])
        except Exception as e: print('GAGAL',step[:50],'->',str(e).split('\n')[0][:100], '\n',str(e)[:600].split('Call log')[0][-400:])
    print(pg.errs[:3]); b.close()
