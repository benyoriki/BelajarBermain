import sys; sys.path.insert(0,'/home/claude/work/audit/tests')
from common import *
G=['warna','garis','pola','beda','hitung','spy','huruf','memori','bayangan','tambah','ganjil','labirin','urut','puzzle']
D="(()=>{const c={};document.querySelectorAll('[id]').forEach(e=>c[e.id]=(c[e.id]||0)+1);return Object.entries(c).filter(x=>x[1]>1)})()"
with sync_playwright() as p:
    b=p.chromium.launch(); ctx,pg=mkpage(b); mkprofile(pg); pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()")
    dups={}; 
    dups['beranda']=pg.evaluate(D)
    for g in G:
        pg.evaluate(f"ACT.nav('home');ACT.play('{g}')"); dups[g+'/intro']=pg.evaluate(D); pg.evaluate("document.querySelector('#main [data-a=go]').click()")
        if g=='puzzle': pg.evaluate("document.querySelector('[data-a=pzgo]').click()"); pg.wait_for_selector('#pzb',timeout=6000)
        pg.wait_for_timeout(150); dups[g]=pg.evaluate(D)
    for t in ['belajar','main','rank','prof']:
        pg.evaluate(f"ACT.nav('{t}')"); dups[t]=pg.evaluate(D)
    print({k:v for k,v in dups.items() if v} or 'tidak ada ID ganda di 33 layar')
    # listener ganda: jumlah klik pada tombol utama menghasilkan 1 efek
    pg.evaluate("ACT.nav('home');ACT.play('hitung')"); pg.evaluate("document.querySelector('#main [data-a=go]').click()")
    for i in range(3): pg.evaluate("ACT.nav('home');ACT.play('hitung')"); pg.evaluate("document.querySelector('#main [data-a=go]').click()")
    q=pg.evaluate("G.q"); p0=pts(pg); pg.click(f'#main [data-a=ans][data-v="{q["a"]}"]'); print('poin satu jawaban benar setelah 4x buka-tutup:',pts(pg)-p0)
    print('errs',pg.errs); ctx.close(); b.close()
