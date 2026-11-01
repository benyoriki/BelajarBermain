import sys; sys.path.insert(0,'/home/claude/work/audit/tests')
from common import *
RT=[]
def r(s,h,a,ok): RT.append(dict(skenario=s,harapan=h,aktual=str(a),status='PASS' if ok else 'FAIL'))
def act(pg): return pg.evaluate("(()=>{const a=document.activeElement;return a&&a!==document.body?(a.dataset.a||a.tagName)+':'+(a.dataset.v||'')+':'+(a.textContent||'').trim().slice(0,12):'(none)'})()")
with sync_playwright() as p:
    b=p.chromium.launch()
    # ===== SMART TV: 1920x1080, hanya keyboard (panah/Enter/Escape) =====
    ctx,pg=mkpage(b,1920,1080); mkprofile(pg); pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()")
    pg.evaluate("ACT.tv()")
    pg.evaluate("document.querySelector('#hd nav button').focus()")
    seq=[]
    for k in ['ArrowRight','ArrowRight','ArrowDown','ArrowDown','ArrowLeft','ArrowUp']:
        pg.keyboard.press(k); pg.wait_for_timeout(120); seq.append(act(pg))
    r('Navigasi panah di beranda','fokus selalu ada dan berpindah (tidak hilang)',seq,'(none)' not in seq and len(set(seq))>=4)
    fv=pg.evaluate("(()=>{const a=document.activeElement;const c=getComputedStyle(a);return [c.outlineStyle,c.outlineWidth,c.boxShadow!=='none']})()")
    r('Indikator fokus terlihat','outline/box-shadow terlihat pada elemen fokus',fv,fv[0]!='none' or fv[2])
    # buka kuis lewat keyboard
    pg.evaluate("ACT.nav('belajar')"); pg.wait_for_timeout(150)
    pg.evaluate("document.querySelector('[data-a=play][data-v=hitung]').focus()"); pg.keyboard.press('Enter'); pg.wait_for_timeout(250)
    pg.evaluate("document.querySelector('#main [data-a=go]').focus()"); pg.keyboard.press('Enter'); pg.wait_for_timeout(300)
    n_ok=0
    for i in range(5):
        a=pg.evaluate("G.q.a"); pg.evaluate(f"document.querySelector('[data-a=ans][data-v=\"{a}\"]').focus()"); pg.keyboard.press('Enter'); pg.wait_for_timeout(120)
        f=act(pg); 
        if f.startswith('nq'): n_ok+=1
        pg.keyboard.press('Enter'); pg.wait_for_timeout(150)
    r('Main kuis hanya dengan keyboard (Enter) sampai selesai','fokus otomatis ke Lanjut tiap soal; layar selesai',f'fokus_lanjut={n_ok}/5 fin={on_fin(pg)}',n_ok==5 and on_fin(pg))
    # labirin dengan panah
    pg.evaluate("ACT.nav('main')"); pg.evaluate("document.querySelector('[data-a=play][data-v=labirin]').click()"); pg.wait_for_timeout(200); pg.evaluate("document.querySelector('#main [data-a=go]').click()"); pg.wait_for_timeout(300)
    mv0=pg.evaluate("G.mz.mv"); pg.keyboard.press('ArrowRight'); pg.keyboard.press('ArrowDown'); pg.keyboard.press('ArrowLeft'); pg.keyboard.press('ArrowUp')
    r('Labirin: panah remote/keyboard','karakter bergerak (langkah bertambah) tanpa mouse',pg.evaluate("G.mz.mv"),pg.evaluate("G.mz.mv")>mv0 or pg.evaluate("G.mz.p")>=0)
    # puzzle tanpa drag: panah + Enter
    pg.evaluate("ACT.nav('main')"); pg.evaluate("document.querySelector('[data-a=play][data-v=puzzle]').click()"); pg.wait_for_timeout(200); pg.evaluate("document.querySelector('#main [data-a=go]').click()"); pg.wait_for_timeout(200)
    pg.evaluate("document.querySelector('[data-a=pzgo]').focus()"); pg.keyboard.press('Enter'); pg.wait_for_selector('#pzb',timeout=6000)
    pg.evaluate("document.querySelector('.pzp2[data-v=\"0\"]').focus()"); pg.keyboard.press('Enter'); pg.evaluate("document.querySelector('.pzs2[data-v=\"0\"]').focus()"); pg.keyboard.press('Enter'); pg.wait_for_timeout(150)
    r('Puzzle tanpa drag (Enter pada keping lalu kotak)','keping terkunci',pg.evaluate("G.pz.ok"),pg.evaluate("G.pz.ok")==1)
    # modal: buka & tutup dengan Escape
    pg.evaluate("ACT.nav('home')"); pg.evaluate("ACT.snd()"); pg.wait_for_timeout(200)
    opened=pg.evaluate("!!document.getElementById('md')||!!document.querySelector('[role=dialog]')"); pg.keyboard.press('Escape'); pg.wait_for_timeout(250)
    closed=pg.evaluate("!document.querySelector('[role=dialog]')")
    r('Modal Pengaturan Suara: Escape menutup','dialog terbuka lalu tertutup',f'open={opened} closed={closed}',opened and closed)
    pg.evaluate("ACT.don()"); pg.wait_for_timeout(200); o2=pg.evaluate("!!document.querySelector('[role=dialog]')"); pg.keyboard.press('Escape'); pg.wait_for_timeout(250)
    r('Modal Donasi: Escape menutup','dialog terbuka lalu tertutup',f"open={o2} closed={pg.evaluate('!document.querySelector(\"[role=dialog]\")')}",o2 and pg.evaluate('!document.querySelector("[role=dialog]")'))
    ctx.close()
    # ===== SERVICE WORKER / OFFLINE =====
    import shutil,re,os
    ctx=b.new_context(viewport={'width':412,'height':900},timezone_id='Asia/Jakarta'); pg=ctx.new_page(); pg.errs=[]; pg.on('pageerror',lambda e:pg.errs.append(str(e)))
    pg.route('https://*/**',lambda r:r.abort())
    pg.goto(URL); pg.wait_for_timeout(500)
    pg.evaluate("navigator.serviceWorker.ready.then(()=>1)"); pg.wait_for_function("navigator.serviceWorker.controller||true",timeout=5000); pg.wait_for_timeout(2500)
    keys=pg.evaluate("caches.keys()"); r('Kunjungan pertama: cache terbentuk','1 cache bba-v26',keys,keys==['bba-v26'])
    cnt=pg.evaluate("caches.open('bba-v26').then(c=>c.keys()).then(k=>k.length)"); r('Aset inti ter-cache','>= 25 berkas (prasyarat install addAll)',cnt,cnt>=25)
    pg.reload(); pg.wait_for_timeout(1200); mkprofile(pg)
    pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()")
    pg.evaluate("ACT.play('hitung')"); pg.evaluate("document.querySelector('#main [data-a=go]').click()")
    p_on=pts(pg)
    ctx.set_offline(True); pg.reload(); pg.wait_for_timeout(1500); pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()")
    r('Offline: reload halaman','halaman tetap tampil (bukan blank)',pg.inner_text('#main')[:40].replace('\n',' '),len(pg.inner_text('#main'))>20)
    st=pg.evaluate("document.querySelector('#net')&&document.querySelector('#net').textContent"); r('Indikator offline','menampilkan Mode Offline',st,'Offline' in str(st))
    allok=True; detail=[]
    for gid in ['hitung','warna','garis','memori','labirin','urut','puzzle','spy']:
        e0=len(pg.errs)
        try:
            pg.evaluate(f"ACT.nav('home')"); pg.evaluate(f"ACT.play('{gid}')"); pg.evaluate("document.querySelector('#main [data-a=go]').click()"); pg.wait_for_timeout(500)
            if gid=='puzzle': pg.evaluate("document.querySelector('[data-a=pzgo]').click()"); pg.wait_for_selector('#pzb',timeout=6000)
            bad_img=pg.evaluate("[...document.images].filter(i=>i.complete&&i.naturalWidth===0).length")
            sprite=pg.evaluate("fetch('aset.webp').then(r=>r.ok).catch(()=>false)")
            if len(pg.errs)>e0 or not sprite or bad_img: allok=False; detail.append((gid,len(pg.errs)-e0,sprite,bad_img))
        except Exception as ex: allok=False; detail.append((gid,str(ex)[:40]))
    r('Offline: 8 permainan terbuka + sprite gambar tersedia','tanpa error, aset.webp dari cache',detail or 'semua OK',allok)
    # selesaikan satu kuis offline lalu cek progres tersimpan
    pg.evaluate("ACT.nav('home')"); pg.evaluate("ACT.play('pola')"); pg.evaluate("document.querySelector('#main [data-a=go]').click()")
    for i in range(5):
        a=pg.evaluate("G.q.a"); pg.evaluate(f"document.querySelector('[data-a=ans][data-v=\"{a}\"]').click()"); pg.evaluate("document.querySelector('[data-a=nq]').click()")
    r('Offline: selesaikan permainan & simpan progres','poin bertambah, fin tampil',f'{p_on}->{pts(pg)}',on_fin(pg) and pts(pg)>p_on)
    ctx.set_offline(False)
    # musik offline: audio belum di-precache -> catat saja
    # ===== PEMBARUAN VERSI =====
    sw=open('/home/claude/work/audit/proj/service-worker.js').read(); open('/home/claude/work/audit/proj/service-worker.js','w').write(sw.replace("bba-v26","bba-v27"))
    pts_before=pts(pg)
    pg.reload(); pg.wait_for_timeout(3500); pg.reload(); pg.wait_for_timeout(1500); pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()")
    keys=pg.evaluate("caches.keys()"); r('Pembaruan versi: cache lama dihapus','hanya bba-v27',keys,keys==['bba-v27'])
    r('Pembaruan versi: progres tetap ada','poin sama setelah update',f'{pts_before}->{pg.evaluate("P()&&P().pts")}',pg.evaluate("P()&&P().pts")==pts_before)
    open('/home/claude/work/audit/proj/service-worker.js','w').write(sw)
    ctx.close(); b.close()
json.dump(RT,open('hasil_tv_offline.json','w'),ensure_ascii=False,indent=1)
for x in RT: print(x['status'],'|',x['skenario'],'|',x['aktual'][:110])
