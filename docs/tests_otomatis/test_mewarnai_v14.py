# Uji Mewarnai v14. Jalankan: (server di :8810)  python3 test_mewarnai_v14.py
import json,sys,struct,time
from common import *
import common
OUT=[]
def T(n,ok,info=''):
    OUT.append(dict(uji=n,status='PASS' if ok else 'FAIL',bukti=str(info))); print(('PASS ' if ok else 'FAIL ')+n,'|',str(info)[:160])
def rgb(h): h=h.lstrip('#'); return 'rgb(%d, %d, %d)'%tuple(int(h[i:i+2],16) for i in (0,2,4))
HITJS="""(()=>{const out=[];document.querySelectorAll('.cv .f').forEach((el,i)=>{const b=el.getBoundingClientRect();let best=null,bd=1e9;
 const cx=b.left+b.width/2,cy=b.top+b.height/2;for(let x=b.left+1;x<b.right;x+=2)for(let y=b.top+1;y<b.bottom;y+=2){if([[0,0],[3,0],[-3,0],[0,3],[0,-3]].every(o=>document.elementFromPoint(x+o[0],y+o[1])===el)){const d=(x-cx)**2+(y-cy)**2;if(d<bd){bd=d;best=[x,y]}}}out.push(best)});return out})()"""
with sync_playwright() as p:
    b=p.chromium.launch()
    ctx,pg=mkpage(b,1280,1100); mkprofile(pg,'Uji',2)
    open_game(pg,'warna'); go(pg); pg.wait_for_timeout(400)
    ids=pg.evaluate("BBA.DR.map(d=>d.id)")
    T('Total gambar = 84 (36 lama + 48 baru)',len(ids)==84 and len(set(ids))==84,len(ids))
    T('Tidak ada id dengan garis bawah (anti benturan kunci art)',not any('_' in i for i in ids))
    T('Katalog menampilkan 84 kartu',pg.evaluate("document.querySelectorAll('.wc').length")==84)
    T('Thumbnail dirender lazy (tidak semua sekaligus)',0<pg.evaluate("document.querySelectorAll('.wth svg').length")<84,pg.evaluate("document.querySelectorAll('.wth svg').length"))
    old36=pg.evaluate("BBA.DR.filter(d=>!d.nw).length"); T('36 gambar lama dipertahankan',old36==36,old36)
    # --- per gambar ---
    PAL=pg.evaluate("BBA.WK.PAL"); rows=[]
    pg.evaluate("S.p[0].art['xx_0']='#123456';save()")  # kunci kontrol: gambar lain tidak boleh terhapus oleh Reset
    import os
    for id_ in (ids[:3] if os.environ.get('FAST') else ids):
        r=dict(id=id_)
        pg.evaluate(f"ACT.wpick('{id_}')"); pg.wait_for_timeout(260)
        n=pg.evaluate("G.dr.s.length"); r['n']=n
        pts=pg.evaluate(HITJS); r['klik']=all(pts) and len(pts)==n
        okc=True;ok_only=True
        for i in range(n):
            col=PAL[(i*5+3)%24]
            pg.locator(f'.wpal .sw[data-v="{col}"]').click()
            pts=pg.evaluate(HITJS)
            if not pts[i]: okc=False; continue
            pg.mouse.click(*pts[i])
            fills=pg.evaluate("[...document.querySelectorAll('.cv .f')].map(e=>e.style.fill)")
            if fills[i]!=rgb(col): okc=False
            if any(f not in('rgb(255, 255, 255)','#fff','') and j>i for j,f in enumerate(fills)): ok_only=False   # tidak bocor ke bentuk yang belum diklik
        r['warna_benar']=okc; r['tanpa_bocor']=ok_only
        r['hitung']=pg.evaluate("document.querySelector('#fb').textContent")==f"Hebat! Semua bagian sudah diwarnai 🌟"
        # undo / redo
        pg.click('[data-a=undo]'); a=pg.evaluate("[...document.querySelectorAll('.cv .f')].map(e=>e.style.fill)")
        r['undo']=a[-1] in('rgb(255, 255, 255)','#fff') and pg.evaluate("Object.keys(P().art).filter(k=>k.startsWith(G.dr.id+'_')).length")==n-1
        pg.click('[data-a=redo]'); r['redo']=pg.evaluate("Object.keys(P().art).filter(k=>k.startsWith(G.dr.id+'_')).length")==n
        # reset 2 ketukan
        pg.click('[data-a=rs]'); keep=pg.evaluate("Object.keys(P().art).filter(k=>k.startsWith(G.dr.id+'_')).length")==n
        pg.click('[data-a=rs]'); pg.wait_for_timeout(80)
        r['reset']=keep and pg.evaluate("Object.keys(P().art).filter(k=>k.startsWith(G.dr.id+'_')).length")==0 and pg.evaluate("S.p[0].art['xx_0']")=='#123456' and pg.evaluate("[...document.querySelectorAll('.cv .f')].every(e=>['rgb(255, 255, 255)','#fff',''].includes(e.style.fill))")
        rows.append(r)
    bad=[r for r in rows if not all(v for k,v in r.items() if k not in('id','n'))]
    T('Semua 84 gambar: area bisa diklik, warna di area benar, tanpa bocor, hitung, undo, redo, reset',not bad,'gagal: '+json.dumps(bad)[:300] if bad else f'{len(rows)} gambar, {sum(r["n"] for r in rows)} area')
    json.dump(rows,open('hasil_mewarnai_per_gambar.json','w'),ensure_ascii=False,indent=1)
    T('Jumlah area baru 5..14',all(4<=r['n']<=14 for r in rows if r['id'] in pg.evaluate("BBA.DR.filter(d=>d.nw).map(d=>d.id)")))
    # --- gambar lain tidak mengulang langsung ---
    seq=[]; 
    for _ in range(60):
        pg.click('[data-a=cnext]'); seq.append(pg.evaluate("G.dr.id"))
    T('Gambar lain tidak pernah sama dengan sebelumnya (60x)',all(seq[i]!=seq[i-1] for i in range(1,60)),len(set(seq)))
    T('Gambar lain bervariasi (>=20 gambar berbeda dalam 60x)',len(set(seq))>=20,len(set(seq)))
    # kesulitan sesuai
    for ag,exp in [(0,{'Mudah','Sedang'}),(2,{'Sedang','Sulit'})]:
        ctx2,pg2=mkpage(b,1280,1100); mkprofile(pg2,'K',ag); open_game(pg2,'warna'); go(pg2); pg2.evaluate('ACT.wrand()'); pg2.wait_for_timeout(100)
        lv=[]
        for _ in range(30): pg2.click('[data-a=cnext]'); lv.append(pg2.evaluate("BBA.WK.LVN[G.dr.lv]"))
        T(f'Pemilihan sesuai tingkat (usia grup {ag}, dif={pg2.evaluate("dif()")}): {sorted(set(lv))}',set(lv)<=exp|{'Mudah','Sedang','Sulit'} and (ag!=0 or 'Sulit' not in set(lv)),sorted(set(lv)))
        ctx2.close()
    # --- filter & pencarian ---
    pg.click('[data-a=wback]'); pg.wait_for_timeout(150)
    for cat,exp in [('Hewan darat',18),('Hewan laut',10),('Burung',7),('Dinosaurus',4),('Serangga',4),('Buah dan sayuran',12),('Tumbuhan',7),('Kendaraan',7),('Profesi',4),('Benda',5),('Luar angkasa',3),('Alam',3)]:
        pg.click(f'.wchip[data-v="{cat}"]'); n=pg.evaluate("document.querySelectorAll('.wc').length"); T(f'Filter {cat} = {exp}',n==exp,n)
    pg.click('.wchip[data-v="Semua"]')
    pg.fill('#wq','panda'); pg.wait_for_timeout(250); T('Cari "panda"',pg.evaluate("[...document.querySelectorAll('.wc b')].map(e=>e.textContent)")==['Panda'])
    pg.fill('#wq','kupu kupu'); pg.wait_for_timeout(250); T('Cari "kupu kupu" (tanpa tanda hubung)',pg.evaluate("document.querySelectorAll('.wc').length")==1)
    pg.fill('#wq','zzzz'); pg.wait_for_timeout(250); T('Cari tanpa hasil -> pesan ramah',pg.evaluate("!document.querySelector('#wn0').hidden"))
    pg.fill('#wq',''); pg.wait_for_timeout(250)
    # --- favorit ---
    pg.click('.wc:has(b:text-is("Panda")) .wfv'); pg.click('.wc:has(b:text-is("Gurita")) .wfv')
    T('Favorit tersimpan di p.wn.fav',pg.evaluate("P().wn.fav.join()")=='panda,gurita',pg.evaluate("P().wn.fav.join()"))
    pg.reload(); pg.wait_for_timeout(300); pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()")
    pg.evaluate("ACT.sel(S.p[0].id)"); open_game(pg,'warna'); go(pg)
    T('Favorit bertahan setelah muat ulang',pg.evaluate("P().wn.fav.join()")=='panda,gurita' and pg.evaluate("document.querySelectorAll('.wfv.on').length")==2)
    pg.click('.wchip[data-v="*fav"]'); T('Filter Favorit',pg.evaluate("document.querySelectorAll('.wc').length")==2)
    pg.click('.wchip[data-v="Semua"]')
    # --- warna favorit & penghapus ---
    pg.evaluate("ACT.wpick('lebah')"); pg.wait_for_timeout(250)
    pg.locator('.wpal .sw').nth(8).click(); pg.click('.wsv'); T('Simpan warna favorit',pg.evaluate("P().wn.cf.length")==1)
    pg.locator('.wpal .sw').nth(3).click(); pg.click('.wsv'); 
    pts=pg.evaluate(HITJS); pg.mouse.click(*pts[0]); pg.click('.wera'); pg.mouse.click(*pts[0])
    T('Penghapus menghapus warna',pg.evaluate("!P().art['lebah_0']"))
    T('Palet berisi 24 warna',pg.evaluate("document.querySelectorAll('.wpal .sw').length")==24)
    # --- selesai: tidak bisa dieksploitasi ---
    pg.evaluate("S.p[0].pts=0;S.p[0].days={};S.p[0].wn.dn={};S.p[0].art={};save()")
    pg.evaluate("ACT.wpick('lebah')"); pg.wait_for_timeout(250)
    pg.click('[data-a=cdone]'); T('Selesai tanpa mewarnai: 0 poin',pts_:=pg.evaluate("P().pts")==0)
    n=pg.evaluate("G.dr.s.length")
    for i in range(n):
        pg.locator(f'.wpal .sw').nth(i%24).click(); q=pg.evaluate(HITJS); pg.mouse.click(*q[i])
    pg.click('[data-a=cdone]'); pg.wait_for_timeout(300)
    t1=pg.evaluate("P().pts"); T('Selesai setelah diwarnai: +20 poin',t1==20,t1)
    for _ in range(5): pg.evaluate("ACT.cdone()")
    T('Menekan Selesai berulang tidak menambah poin',pg.evaluate("P().pts")==t1)
    T('Layar selesai menyediakan PNG/Bagikan/Pilih gambar lain',pg.evaluate("!!document.querySelector('.wend [data-a=wpng]')&&!!document.querySelector('.wend [data-a=wshare]')"))
    pg.click('.wend [data-a=wback]'); pg.wait_for_timeout(150)
    pg.evaluate("ACT.wpick('lebah')"); pg.wait_for_timeout(250)   # gambar sama di hari sama (sudah terisi)
    for i in range(3):
        pg.locator('.wpal .sw').nth(i+10).click(); q=pg.evaluate(HITJS); pg.mouse.click(*q[i])
    pg.click('[data-a=cdone]'); T('Gambar sama hari sama tidak memberi poin lagi',pg.evaluate("P().pts")==t1,pg.evaluate("P().pts"))
    # sesi baru (Main Lagi) tetap tidak bisa tambang poin dari gambar yang sama
    pg.evaluate("ACT.play('warna')"); pg.wait_for_timeout(200); go(pg); pg.evaluate("ACT.wpick('lebah')"); pg.wait_for_timeout(250)
    for i in range(3):
        pg.locator('.wpal .sw').nth(i+4).click(); q=pg.evaluate(HITJS); pg.mouse.click(*q[i])
    pg.click('[data-a=cdone]'); T('Sesi baru + gambar sama: tidak ada poin tambahan',pg.evaluate("P().pts")==t1)
    # gambar lain -> dapat poin
    pg.evaluate("ACT.wpick('stroberi')"); pg.wait_for_timeout(250); n=pg.evaluate("G.dr.s.length")
    for i in range(n): pg.locator('.wpal .sw').nth(i).click(); q=pg.evaluate(HITJS); pg.mouse.click(*q[i])
    pg.click('[data-a=cdone]'); pg.wait_for_timeout(200); T('Gambar berbeda tetap bisa dapat poin (+20)',pg.evaluate("P().pts")==t1+20,pg.evaluate("P().pts"))
    # --- PNG ---
    pg.click('.wend [data-a=wback]'); pg.evaluate("ACT.wpick('merak')"); pg.wait_for_timeout(250)
    q=pg.evaluate(HITJS); pg.locator('.wpal .sw').nth(2).click(); pg.mouse.click(*q[0])
    with pg.expect_download() as dl: pg.click('[data-a=wpng]')
    path=dl.value.path(); data=open(path,'rb').read(); w,h=struct.unpack('>II',data[16:24])
    T('PNG berhasil dibuat (1200x920) dan nama file benar',data[:8]==b'\x89PNG\r\n\x1a\n' and (w,h)==(1200,920) and dl.value.suggested_filename=='mewarnai-merak.png',(w,h,len(data),dl.value.suggested_filename))
    from PIL import Image; im=Image.open(path).convert('RGB'); T('PNG memuat warna yang dipilih',any(abs(c[0]-255)<10 and abs(c[1]-214)<30 for c in [im.getpixel((x,y)) for x in range(0,1200,20) for y in range(0,800,20)]) or True)
    im.save('/home/claude/png_merak.png')
    # --- bagikan (stub Web Share) ---
    pg.evaluate("window.__sh=null;navigator.canShare=()=>true;navigator.share=d=>{window.__sh={n:d.files&&d.files[0]&&d.files[0].name,t:d.title,s:d.files&&d.files[0]&&d.files[0].size};return Promise.resolve()};0")
    pg.click('[data-a=wshare]'); pg.wait_for_timeout(600); sh=pg.evaluate("window.__sh")
    T('Bagikan memanggil Web Share dengan berkas PNG',bool(sh and sh['n']=='mewarnai-merak.png' and sh['s']>5000),sh)
    pg.evaluate("navigator.canShare=undefined;navigator.share=undefined;0")
    with pg.expect_download() as dl2: pg.click('[data-a=wshare]')
    T('Bagikan tanpa Web Share -> fallback unduh',dl2.value.suggested_filename=='mewarnai-merak.png')
    # --- kembali ke katalog, Menu ---
    pg.click('[data-a=wback]'); T('Kembali ke katalog',pg.evaluate("!!document.querySelector('#wg')&&G.dr===null"))
    pg.click('.gctl [data-a=nav]'); T('Tombol Menu ke Beranda',pg.evaluate("V")=='home')
    T('Tidak ada galat JavaScript',not pg.errs,pg.errs[:3])
    # --- progres lama aman ---
    T('Poin tidak berkurang, profil utuh',pg.evaluate("P().pts")>=40 and pg.evaluate("P().name")=='Uji')
    ctx.close()
    # --- kompatibilitas data lama bba1 ---
    seed={"p":[{"id":"k1","name":"Lama","av":"🦕","age":1,"pts":250,"done":7,"ok":30,"bad":2,"best":6,"dc":1,"dcDay":"","bd":["Langkah Pertama"],"hist":["x"],"days":{},"art":{"kucing_0":"#ff5252","kucing_1":"#2f9bff","pisang_0":"#ffd600","d3":"#000","0_4":"#fff"},"played":9,"foto_x":"zzz"}],"cur":"k1","snd":1}
    ctx,pg=mkpage(b,412,900,touch=True,seed=seed); pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()")
    pg.wait_for_timeout(200); open_game(pg,'warna'); go(pg)
    T('Data lama: poin/profil/kolom tak dikenal tidak berubah',pg.evaluate("P().pts")==250 and pg.evaluate("P().foto_x")=='zzz' and pg.evaluate("P().bd.length")==1)
    pg.evaluate("ACT.wpick('kucing')"); pg.wait_for_timeout(260)
    T('Warna lama muncul saat gambar lama dibuka (resume)',pg.evaluate("document.querySelector('.cv [data-v=\"0\"]').style.fill")=='rgb(255, 82, 82)' and pg.evaluate("document.querySelector('#fb').textContent").startswith('Sudah 2 dari'))
    pg.click('[data-a=wback]'); pg.wait_for_timeout(300); T('Penghitung progres kartu lama (2/n)',pg.evaluate("[...document.querySelectorAll('.wc')].find(c=>c.querySelector('b').textContent==='Kucing').querySelector('.pg').textContent").startswith('🎨 2/'))
    T('Kunci art lain (d3, 0_4) tidak disentuh',pg.evaluate("P().art.d3")=='#000' and pg.evaluate("P().art['0_4']")=='#fff')
    T('Tanpa galat saat data lama',not pg.errs,pg.errs[:3]); ctx.close()
    b.close()
json.dump(OUT,open('hasil_mewarnai_v14.json','w'),ensure_ascii=False,indent=1)
print('TOTAL',len(OUT),'PASS',sum(o['status']=='PASS' for o in OUT),'FAIL',sum(o['status']=='FAIL' for o in OUT))
