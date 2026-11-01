import sys,json; sys.path.insert(0,'/home/claude/work/audit/tests')
from common import *
RX=[]
def X(g,dim,sk,harap,fn):
    try: ok,ak=fn()
    except Exception as e: ok,ak=False,'PENGECUALIAN: '+str(e).split('\n')[0][:140]
    RX.append(dict(vp='hp-sentuh',game=g,dim=dim,skenario=sk,harapan=harap,aktual=str(ak)[:160],status='PASS' if ok else 'FAIL'))
def touch(cdp,pts):
    cdp.send('Input.dispatchTouchEvent',{'type':'touchStart','touchPoints':[{'x':pts[0][0],'y':pts[0][1]}]})
    for x,y in pts[1:]: cdp.send('Input.dispatchTouchEvent',{'type':'touchMove','touchPoints':[{'x':x,'y':y}]})
    cdp.send('Input.dispatchTouchEvent',{'type':'touchEnd','touchPoints':[]})
def center(pg,sel):
    b=pg.locator(sel).first.bounding_box(); return b['x']+b['width']/2,b['y']+b['height']/2
def line(a,b,n=8): return [(a[0]+(b[0]-a[0])*i/n,a[1]+(b[1]-a[1])*i/n) for i in range(n+1)]
with sync_playwright() as p:
    b=p.chromium.launch()
    ctx,pg=mkpage(b,360,520,touch=True); mkprofile(pg); pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()"); cdp=ctx.new_cdp_session(pg)
    # --- Labirin: usap sentuh ---
    pg.evaluate("ACT.play('labirin')"); pg.evaluate("document.querySelector('#main [data-a=go]').click()"); pg.wait_for_timeout(300)
    def swipe():
        z=pg.evaluate("({w:G.mz.c[0].w,sc:document.documentElement.scrollHeight>innerHeight})"); c=center(pg,'#mz')
        dirs=[(1,0,2,(60,0)),(2,0,4,(0,60)),(0,0,1,(0,-60)),(3,0,8,(-60,0))]
        for d,_,bit,(dx,dy) in dirs:
            if not z['w']&bit:
                y0=pg.evaluate("scrollY"); touch(cdp,line(c,(c[0]+dx,c[1]+dy),6)); pg.wait_for_timeout(120)
                mv=pg.evaluate("G.mz.mv"); y1=pg.evaluate("scrollY")
                return mv==1 and y0==y1, f'arah {d}: langkah={mv}, scrollY {y0}->{y1}, halaman_bisa_scroll={z["sc"]}'
        return False,'tidak ada arah terbuka'
    X('labirin','Input sentuh','Usap (swipe) jari menggerakkan karakter satu langkah dan halaman tidak ikut bergulir','langkah=1, scrollY tetap',swipe)
    # --- Garis: seret jari ---
    pg.evaluate("ACT.nav('home');ACT.play('garis')"); pg.evaluate("document.querySelector('#main [data-a=go]').click()"); pg.wait_for_timeout(300)
    def drag_garis():
        pg.evaluate("document.querySelector('#box').scrollIntoView({block:'start'})"); pg.wait_for_timeout(100)
        a=center(pg,'#l0'); r=center(pg,'[data-a=R][data-v="0"]'); y0=pg.evaluate("scrollY")
        touch(cdp,line(a,(r[0],r[1]),10)); pg.wait_for_timeout(200)
        ln=pg.evaluate("document.querySelectorAll('#sv line').length"); y1=pg.evaluate("scrollY")
        return ln==1 and pg.evaluate("G.m")==1 and y0==y1, f'garis={ln} cocok={pg.evaluate("G.m")} scrollY {y0}->{y1}'
    X('garis','Input sentuh','Seret jari dari gambar kiri ke pasangannya membentuk 1 garis; halaman tidak bergulir','1 garis, scrollY tetap',drag_garis)
    # --- Puzzle: seret jari (viewport 360x700 agar papan + keping sama-sama terlihat di atas navigasi bawah) ---
    pg.set_viewport_size({'width':360,'height':700})
    pg.evaluate("ACT.nav('home');ACT.play('puzzle')"); pg.evaluate("document.querySelector('#main [data-a=go]').click()"); pg.evaluate("document.querySelector('[data-a=pzgo]').click()"); pg.wait_for_selector('#pzb',timeout=6000); pg.wait_for_timeout(200)
    def drag_pz():
        pg.evaluate("document.querySelector('#pzb').scrollIntoView({block:'start'})"); pg.wait_for_timeout(100)
        a=center(pg,'.pzp2[data-v="0"]'); s_=center(pg,'.pzs2[data-v="0"]'); y0=pg.evaluate("scrollY")
        hit=pg.evaluate("(([x,y])=>{const t=document.elementFromPoint(x,y);return t.className+'|'+t.tagName})",a)
        touch(cdp,line(a,s_,10)); pg.wait_for_timeout(250); y1=pg.evaluate("scrollY")
        return pg.evaluate("G.pz.ok")==1 and abs(y0-y1)<2, f'terkunci={pg.evaluate("G.pz.ok")} scrollY {y0}->{y1} halaman_bisa_scroll={pg.evaluate("document.documentElement.scrollHeight>innerHeight")} titik_sentuh_mengenai={hit}'
    X('puzzle','Input sentuh','Seret keping dengan jari ke kotak benar → terkunci; halaman tidak bergulir','ok=1, scrollY tetap',drag_pz)
    ctx.close()
    # --- Penyimpanan gagal ---
    ctx,pg=mkpage(b,360,800,touch=True); mkprofile(pg); pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()")
    pg.evaluate("(()=>{const o=Storage.prototype.setItem;Storage.prototype.setItem=function(k){if(k==='bba1')throw new DOMException('Quota','QuotaExceededError');return o.apply(this,arguments)};return 0})()")
    def storfail():
        pg.evaluate("ACT.play('hitung')"); pg.evaluate("document.querySelector('#main [data-a=go]').click()"); q=pg.evaluate("G.q"); p0=pts(pg)
        pg.locator(f'#main [data-a=ans][data-v="{q["a"]}"]').tap(); pg.wait_for_timeout(1500)
        toast=pg.inner_text('#toast'); cont=bool(pg.query_selector('#main [data-a=nq]'))
        return (not pg.errs) and cont and pts(pg)>p0, f'error={pg.errs[:1]} lanjut={cont} poin_memori {p0}->{pts(pg)} toast="{toast[:60]}"'
    X('umum','Penyimpanan gagal (kuota penuh)','Tidak crash, permainan tetap bisa dilanjutkan, pesan ramah tampil sekali','tanpa error + pesan',storfail)
    pg.wait_for_timeout(300); msg=pg.evaluate("document.getElementById('toast').textContent")
    ctx.close()
    # --- Data lama: 14 permainan + idempotensi ---
    old={'p':[{'id':'k1','name':'Budi','av':'🦖','age':0,'pts':640,'done':12,'ok':50,'bad':9,'best':7,'dc':2,'dcDay':'2026-10-01','bd':['Langkah Pertama','100 Poin'],'hist':['x'],'days':{'2026-10-29':80},'art':{'a_0':'#fff'},'photo':'data:image/jpeg;base64,AAA','extra':{'kolom':'tak-dikenal'}},{'id':'k2','name':'Sari','av':'🐱','age':2,'pts':20,'done':1,'ok':2,'bad':0,'best':2,'dc':0,'dcDay':'','bd':[]}],'cur':'k1','snd':1,'sm':'sfx','mv':.3}
    ctx,pg=mkpage(b,412,900,seed=old); pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()")
    def idem():
        snaps=[]
        for i in range(3):
            snaps.append(pg.evaluate("localStorage.getItem('bba1')")); pg.reload(); pg.wait_for_timeout(300)
        return snaps[1]==snaps[2], 'JSON tersimpan identik setelah reload ke-2 dan ke-3 (migrasi idempoten)'
    X('umum','Migrasi data lama','Reload berulang tidak mengubah data lagi','idempoten',idem)
    pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()")
    GAMES=['warna','garis','pola','beda','hitung','spy','huruf','memori','bayangan','tambah','ganjil','labirin','urut','puzzle']
    def play14():
        errs=[]
        for g in GAMES:
            pg.evaluate(f"ACT.nav('home');ACT.play('{g}')"); pg.evaluate("document.querySelector('#main [data-a=go]').click()")
            if g=='puzzle': pg.evaluate("document.querySelector('[data-a=pzgo]').click()"); pg.wait_for_selector('#pzb',timeout=6000)
            pg.wait_for_timeout(250)
            if g in ['pola','hitung','huruf','tambah','ganjil','bayangan']: pg.evaluate("document.querySelector(`#main [data-a=ans][data-v='${G.q.a}']`).click()")
            if g in('beda','spy'): pg.evaluate("document.querySelector(`#main [data-a=bd][data-v='${G.d[0]}']`).click()")
        pg.evaluate("ACT.nav('home')"); pg.wait_for_timeout(500)
        S=pg.evaluate("JSON.parse(localStorage.getItem('bba1'))"); a=S['p'][0]; c=S['p'][1]
        keep=a['name']=='Budi' and a['av']=='🦖' and a['age']==0 and a['photo'].startswith('data:') and a['extra']=={'kolom':'tak-dikenal'} and set(['Langkah Pertama','100 Poin'])<=set(a['bd']) and a['pts']>=640 and a['done']>=12 and a['dc']==2
        other=c['name']=='Sari' and c['pts']==20 and c['age']==2
        sett=S['sm']=='sfx' and S['mv']==.3
        return keep and other and sett and not pg.errs, f"Budi utuh={keep} (poin {a['pts']}), Sari utuh={other}, pengaturan suara utuh={sett}, errs={pg.errs[:1]}"
    X('umum','Data lama × 14 permainan','Memainkan/membuka semua 14 permainan dengan profil lama: tak ada kolom hilang, tak ada error','semua utuh',play14)
    ctx.close(); b.close()
json.dump(RX,open('pg_sentuh_data.json','w'),ensure_ascii=False,indent=1)
for m in RX: print(m['status'],m['game'],'|',m['dim'],'|',m['aktual'][:150])
