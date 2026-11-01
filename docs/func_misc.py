from h import *
import json,sys
from func_games import rec,R,pts
with sync_playwright() as p:
    b=p.chromium.launch()
    # navigasi lima menu
    ctx,pg=page(b,360,740)
    for v,lab in [('belajar','Belajar'),('main','Bermain'),('rank','Peringkat'),('prof','Profil'),('home','Beranda')]:
        pg.click(f'nav [data-v={v}]'); pg.wait_for_timeout(150)
        rec('navigasi',f'menu {lab}',pg.evaluate("V")==v and pg.locator(f'nav [data-v={v}][aria-current=page]').count()==1)
    nh=pg.evaluate("document.querySelector('nav').getBoundingClientRect().height")
    rec('navigasi','navigasi bawah pendek (≤ 4.2rem=67px)',nh<=67,round(nh))
    hh=pg.evaluate("document.querySelector('header').getBoundingClientRect().height")
    rec('header','header ringkas (≤ 62px di HP)',hh<=62,round(hh))
    pg.evaluate("ACT.play('hitung')");pg.wait_for_timeout(200)
    rec('navigasi','intro permainan: tombol ← Kembali ada',pg.locator('#main .intro [data-a=nav]').count()==1)
    pg.click('#main [data-a=go]');pg.wait_for_timeout(200)
    rec('navigasi','HP: navigasi global disembunyikan saat bermain, tombol ← tersedia',pg.evaluate("getComputedStyle(document.querySelector('nav')).display")=='none' and pg.locator('#main .gback').count()==1)
    pg.click('#main .gback'); pg.wait_for_timeout(150); rec('navigasi','← kembali ke menu Belajar & navigasi tampil lagi',pg.evaluate("V")=='belajar' and pg.evaluate("getComputedStyle(document.querySelector('nav')).display")!='none')
    # kartu permainan: 14 total
    pg.click('nav [data-v=belajar]');n1=pg.locator('#main .gc').count();pg.click('nav [data-v=main]');n2=pg.locator('#main .gc').count()
    rec('permainan','14 permainan tersedia (6 Belajar + 8 Bermain)',n1==6 and n2==8,(n1,n2))
    # data lama & bba1
    raw=pg.evaluate("localStorage.getItem('bba1')"); o=json.loads(raw)
    rec('data','kunci localStorage bba1 dipakai, profil lama utuh',o['cur']=='k1' and o['p'][0]['name']=='Dono' and o['p'][0]['pts']>=120,o['p'][0]['pts'])
    pg.reload(); pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()"); pg.wait_for_timeout(300)
    rec('data','refresh: profil & poin tetap',pg.evaluate("P().name")=='Dono' and pg.evaluate("P().pts")>=120)
    pg.evaluate("ACT.play('pola')");pg.wait_for_timeout(150);pg.click('#main [data-a=go]');pg.wait_for_timeout(200);pg.reload();pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()");pg.wait_for_timeout(300)
    rec('data','refresh di tengah permainan: kembali aman ke Beranda, poin tetap, tanpa error',pg.evaluate("P().pts")>=120 and not pg.errs,pg.errs[:1])
    # keyboard
    pg.keyboard.press('Tab');pg.keyboard.press('Tab');pg.wait_for_timeout(100)
    fo=pg.evaluate("(()=>{const s=getComputedStyle(document.activeElement);return [s.outlineStyle,s.outlineWidth]})()")
    rec('keyboard','fokus Tab terlihat (outline)',fo[0]!='none' and fo[1]!='0px',fo)
    ctx.close()
    # Mode TV + remote
    ctx,pg=page(b,1280,720,touch=False)
    pg.evaluate("ACT.tv()");pg.wait_for_timeout(100)
    pg.keyboard.press('Tab');pg.wait_for_timeout(100)
    fo=pg.evaluate("(()=>{const s=getComputedStyle(document.activeElement);return [s.outlineStyle,s.outlineWidth]})()")
    rec('TV','Mode TV: ring fokus tebal (5px) terlihat',fo[1]=='5px',fo)
    # panah remote berpindah fokus antar tombol
    pg.focus('nav [data-v=home]');pg.keyboard.press('ArrowRight');pg.wait_for_timeout(300)
    rec('TV','panah kanan memindahkan fokus ke menu berikutnya',pg.evaluate("document.activeElement.dataset.v")=='belajar',pg.evaluate("document.activeElement.dataset.v"))
    pg.keyboard.press('Enter');pg.wait_for_timeout(200);rec('TV','OK/Enter membuka menu',pg.evaluate("V")=='belajar')
    rec('TV','PC/TV: navigasi tetap di header saat bermain',(pg.evaluate("ACT.play('urut')") or True) and pg.evaluate("getComputedStyle(document.querySelector('nav')).display")!='none')
    ctx.close()
    # offline + SW
    ctx,pg=page(b,360,740,sw='allow')
    pg.wait_for_timeout(2500)
    rec('offline','Service Worker aktif',pg.evaluate("navigator.serviceWorker.getRegistration().then(r=>!!(r&&r.active))"))
    ctx.set_offline(True); pg.reload(); pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()"); pg.wait_for_timeout(500)
    rec('offline','offline: halaman tetap termuat dari cache',pg.evaluate("!!document.querySelector('#main .hero,#main .wl')"))
    for g in ['puzzle','labirin','warna']:
        pg.evaluate(f"ACT.play('{g}')");pg.wait_for_timeout(150);pg.evaluate("ACT.go()");pg.wait_for_timeout(300)
        rec('offline',f'offline: {g} berjalan',pg.locator('#main .card').count()>=1 and not pg.errs,pg.errs[:1])
    ctx.close(); b.close()
json.dump(R,open('/home/claude/tests/res_misc.json','w'),ensure_ascii=False,indent=1)
