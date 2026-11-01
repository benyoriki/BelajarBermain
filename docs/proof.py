import sys,json; sys.path.insert(0,'/home/claude/work/audit/tests')
import common
port=sys.argv[1]; common.URL=f'http://localhost:{port}/index.html'
from common import *
out={}
def fresh(b,**k):
    ctx,pg=mkpage(b,**k); mkprofile(pg); return ctx,pg
with sync_playwright() as p:
    b=p.chromium.launch()
    # 1 tanggal lokal (UTC+14): today() harus = tanggal lokal
    ctx=b.new_context(viewport={'width':412,'height':900},service_workers='block',timezone_id='Asia/Jakarta'); pg=ctx.new_page(); pg.errs=[]; pg.route('https://*/**',lambda r:r.abort())
    import datetime; ctx.clock.install(time=datetime.datetime(2026,10,30,20,0,0,tzinfo=datetime.timezone.utc))   # 03:00 WIB tanggal 31
    pg.goto(common.URL); pg.wait_for_timeout(300); mkprofile(pg)
    r=pg.evaluate("[today(), new Date().toLocaleDateString('sv-SE'), new Date().toISOString().slice(0,10)]")
    out['tanggal_lokal']=('OK' if r[0]==r[1] else f'SALAH (today={r[0]} lokal={r[1]} utc={r[2]})') ; ctx.close()
    # 2 Mewarnai: Reset harus tetap pada gambar yang sama
    ctx,pg=fresh(b); open_game(pg,'warna'); go(pg)
    try:
        a=pg.evaluate("G.dr.id"); pg.click('#main [data-a=rs]'); c=pg.evaluate("G.dr.id"); out['reset_warna_gambar_sama']='OK' if a==c else f'SALAH ({a}->{c})'
    except Exception as e: out['reset_warna_gambar_sama']='ERR '+str(e)[:50]
    ctx.close()
    # 3 Mewarnai: lembar tersimpan dari sesi lama (semua gambar sudah berwarna) -> Main Lagi lalu langsung Selesai
    ctx,pg=fresh(b); open_game(pg,'warna'); go(pg)
    pg.evaluate("(()=>{const a=P().art;BBA.DR.forEach(d=>d.s.forEach((s,i)=>a[d.id+'_'+i]='#ff5252'));save()})()")
    pg.evaluate("ACT.nav('home')"); open_game(pg,'warna'); go(pg)
    pg.evaluate("ACT.cdone()"); out['warna_tambang_poin']='SALAH (selesai tanpa mewarnai)' if on_fin(pg) else 'OK (ditolak)'
    ctx.close()
    # 4 Labirin: keluar tepat setelah babak selesai -> timer menimpa beranda?
    ctx,pg=fresh(b); open_game(pg,'labirin'); go(pg)
    pg.evaluate("(()=>{const z=G.mz;z.p=z.n*z.n-2;z.c[z.p].w&=~2;z.c[z.p+1].w&=~8})()"); pg.keyboard.press('ArrowRight')
    pg.evaluate("ACT.nav('home')"); pg.wait_for_timeout(1500)
    out['labirin_timer_bocor']='OK' if pg.query_selector('.hero') and not pg.errs else f"SALAH (home={bool(pg.query_selector('.hero'))}, errs={pg.errs[:1]})"; ctx.close()
    # 5 Simon: setelah salah, ketukan saat jeda 900ms harus diabaikan
    ctx,pg=fresh(b); open_game(pg,'urut'); go(pg); pg.wait_for_function("G.lock===0",timeout=15000)
    sq=pg.evaluate("G.sq"); w=(sq[0]+1)%4; pg.click(f'.sw2:nth-child({w+1})'); lk=pg.evaluate("G.lock")
    out['simon_kunci_setelah_salah']='OK' if lk==1 else 'SALAH (input masih diterima)'; ctx.close()
    # 6 Puzzle: main lagi pada puzzle yang sama tidak memberi +20 lagi (sesi baru)
    ctx,pg=fresh(b); open_game(pg,'puzzle'); go(pg); pg.click('[data-a=pzgo]'); pg.wait_for_selector('#pzb',timeout=6000)
    n=pg.evaluate("G.pz.n")
    for k in range(n): pg.click(f'.pzp2[data-v="{k}"]',force=True); pg.click(f'.pzs2[data-v="{k}"]',force=True)
    pg.wait_for_timeout(900); p1=pts(pg)
    pg.evaluate("ACT.nav('home')"); open_game(pg,'puzzle'); go(pg); pg.click('[data-a=pzgo]'); pg.wait_for_selector('#pzb',timeout=6000)
    for k in range(n): pg.click(f'.pzp2[data-v="{k}"]',force=True); pg.click(f'.pzs2[data-v="{k}"]',force=True)
    pg.wait_for_timeout(900); p2=pts(pg)
    out['puzzle_tambang_poin']='OK' if p2==p1 else f'SALAH (+{p2-p1} poin untuk puzzle yang sudah pernah selesai)'; ctx.close()
    # 7 Puzzle: keluar saat 'Menyiapkan puzzle…'
    ctx,pg=fresh(b); open_game(pg,'puzzle'); go(pg); pg.click('[data-a=pzgo]'); pg.evaluate("ACT.nav('home')"); pg.wait_for_timeout(2500)
    out['puzzle_timpa_beranda']='OK' if pg.query_selector('.hero') and not pg.errs else f"SALAH (home={bool(pg.query_selector('.hero'))} errs={pg.errs[:1]})"; ctx.close()
    # 8 Garis: resize
    ctx,pg=fresh(b); open_game(pg,'garis'); go(pg); pg.click('#l0'); pg.click('[data-a=R][data-v="0"]'); pg.set_viewport_size({'width':340,'height':700}); pg.wait_for_timeout(400)
    e=pg.evaluate("""(()=>{const c=document.getElementById('box').getBoundingClientRect(),l=document.querySelector('#sv line'),a=document.getElementById('l0').getBoundingClientRect();return Math.abs(+l.getAttribute('x1')-(a.left-c.left+a.width/2))+Math.abs(+l.getAttribute('y1')-(a.top-c.top+a.height/2))})()""")
    out['garis_resize']='OK' if e<2 else f'SALAH (garis bergeser {e:.0f}px)'; ctx.close()
    # 9 Data rusak: tidak boleh ditimpa diam-diam
    ctx=b.new_context(service_workers='block'); pg=ctx.new_page(); pg.route('https://*/**',lambda r:r.abort())
    pg.add_init_script("if(!sessionStorage.getItem('x')){sessionStorage.setItem('x','1');localStorage.setItem('bba1','{rusak:::')}")
    pg.goto(common.URL); pg.wait_for_timeout(400); pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()")
    pg.click('[data-a=new]'); pg.fill('#nm','Ani'); pg.click('[data-a=saveP]'); pg.wait_for_timeout(200)
    out['data_rusak_dicadangkan']='OK' if pg.evaluate("localStorage.getItem('bba1_rusak')")=='{rusak:::' else 'SALAH (data rusak ditimpa tanpa cadangan)'; ctx.close()
    # 10 Profil lama dengan kolom kurang (tanpa days/art/hist) tidak membuat crash
    old={'p':[{'id':'k1','name':'Lama','av':'🦕','age':1,'pts':250,'done':4,'ok':20,'bad':3,'best':6,'dc':1,'dcDay':'','bd':['Langkah Pertama']}],'cur':'k1','snd':1}
    ctx,pg=mkpage(b,seed=old); pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()")
    try:
        open_game(pg,'hitung'); go(pg); q=pg.evaluate("G.q"); pg.click(f'#main [data-a=ans][data-v="{q["a"]}"]'); pg.wait_for_timeout(100)
        res=pg.evaluate("[P().pts,P().done]"); out['profil_lama_tanpa_kolom']='OK pts=%s'%res[0] if res[0]==260 and not pg.errs else f'SALAH {res} errs={pg.errs[:1]}'
    except Exception as e: out['profil_lama_tanpa_kolom']='ERR '+str(e)[:60]+' errs='+str(pg.errs[:1])
    ctx.close(); b.close()
print(json.dumps(out,ensure_ascii=False,indent=1))
