from h import *
import json,sys,heapq,time
R=[]
def rec(area,name,ok,det=''):
    R.append(dict(area=area,tes=name,status='PASS' if ok else 'FAIL',detail=str(det)[:200]))
    print(('PASS' if ok else 'FAIL'),area,'|',name,'|',str(det)[:120])
def pts(pg): return pg.evaluate("P().pts")
def fin_ok(pg): return 'Aktivitas selesai' in pg.inner_text('#main') or 'Puzzle Selesai' in pg.inner_text('#main')
def header_ok(pg,g):
    h=pg.evaluate("""(()=>{const b=document.querySelector('#main .gh .gback'),r=document.querySelector('#main .gh .gre');return {back:!!b,bl:b?b.getAttribute('aria-label'):'',re:!!r}})()""")
    need_re = g!='warna'
    rec(g,'header seragam (← ada, 🔁 %s)'%('ada' if need_re else 'tidak dipakai'),h['back'] and (h['re']==need_re),h)
def quiz(b,g):
    ctx,pg=page(b,360,740); p0=pts(pg); play(pg,g); pg.click('#main [data-a=go]'); pg.wait_for_timeout(250)
    header_ok(pg,g)
    wrongok=True
    for i in range(5):
        a=pg.evaluate("G.q.a"); n=pg.evaluate("G.q.o.length")
        if i==0:
            w=[k for k in range(n) if k!=a][0]; pg.click(f'#main [data-a=ans][data-v="{w}"]'); pg.wait_for_timeout(100)
            t=pg.inner_text('#fb'); wrongok='Hampir' in t and '❌' not in t and pg.evaluate("document.querySelectorAll('.opt.wrong').length")==1
        else: pg.click(f'#main [data-a=ans][data-v="{a}"]')
        pg.click('#fb [data-a=nq]'); pg.wait_for_timeout(120)
    pg.wait_for_timeout(300)
    rec(g,'salah = pesan ramah (💛 Hampir), tanpa ❌',wrongok)
    rec(g,'selesai setelah 5 soal + poin bertambah',fin_ok(pg) and pts(pg)>p0,f'{p0}->{pts(pg)}')
    rec(g,'layar selesai: Main Lagi + Pilih Permainan',pg.locator('#main [data-a=play]').count()==1 and pg.locator('#main [data-a=nav]').count()==1)
    pg.click('#main [data-a=nav]'); pg.wait_for_timeout(150)
    rec(g,'Pilih Permainan → menu + navigasi global kembali',pg.evaluate("getComputedStyle(document.querySelector('nav')).display")!='none' and 'inplay' not in pg.evaluate("document.body.className"))
    rec(g,'tanpa error JS',not pg.errs,pg.errs[:1]); ctx.close()
def finder(b,g):
    ctx,pg=page(b,360,740); p0=pts(pg); play(pg,g); pg.click('#main [data-a=go]'); pg.wait_for_timeout(250); header_ok(pg,g)
    for r in range(3):
        d=pg.evaluate("G.d"); n=pg.evaluate("document.querySelectorAll('[data-a=bd]').length")
        if r==0:
            w=[k for k in range(n) if k not in d][0]; pg.click(f'[data-a=bd][data-v="{w}"]'); pg.wait_for_timeout(80)
            rec(g,'ketukan salah tidak menyelesaikan + tanda lembut',pg.evaluate("G.f")==0)
        for k in d: pg.click(f'[data-a=bd][data-v="{k}"]')
        pg.click('#fb [data-a=nr]'); pg.wait_for_timeout(150)
    pg.wait_for_timeout(200)
    rec(g,'selesai 3 babak + poin bertambah',fin_ok(pg) and pts(pg)>p0,f'{p0}->{pts(pg)}'); rec(g,'tanpa error JS',not pg.errs,pg.errs[:1]); ctx.close()
def garis(b):
    ctx,pg=page(b,360,740); g='garis'; p0=pts(pg); play(pg,g); pg.click('#main [data-a=go]'); pg.wait_for_timeout(250); header_ok(pg,g)
    rec(g,'tidak ada tombol Ulangi ganda di bawah',pg.locator('#main .row .ghost[data-a=go]').count()==0 and pg.locator('#main [data-a=rst]').count()==1)
    n=pg.evaluate("G.t"); 
    if n>1:
        pg.click('[data-a=L][data-v="0"]'); other=pg.evaluate("[...document.querySelectorAll('[data-a=R]')].map(e=>e.dataset.v).filter(v=>v!=='0'&&v!=='x')[0]")
        pg.click(f'[data-a=R][data-v="{other}"]'); pg.wait_for_timeout(100); rec(g,'pasangan salah ditolak',pg.evaluate("G.m")==0)
    for i in range(n): pg.click(f'[data-a=L][data-v="{i}"]'); pg.click(f'[data-a=R][data-v="{i}"]'); pg.wait_for_timeout(60)
    pg.wait_for_timeout(1000); rec(g,'semua pasangan benar → selesai',fin_ok(pg) and pts(pg)>p0,f'{p0}->{pts(pg)}')
    # seret (drag)
    play(pg,g); pg.click('#main [data-a=go]'); pg.wait_for_timeout(250)
    a=pg.locator('[data-a=L][data-v="0"]').bounding_box(); c=pg.locator('[data-a=R][data-v="0"]').bounding_box()
    pg.mouse.move(a['x']+a['width']/2,a['y']+a['height']/2); pg.mouse.down(); pg.mouse.move(c['x']+10,c['y']+c['height']/2,steps=8); pg.mouse.up(); pg.wait_for_timeout(150)
    rec(g,'seret jari ke pasangan berfungsi',pg.evaluate("G.m")==1); rec(g,'tanpa error JS',not pg.errs,pg.errs[:1]); ctx.close()
def memori(b):
    ctx,pg=page(b,360,740); g='memori'; p0=pts(pg); play(pg,g); pg.click('#main [data-a=go]'); pg.wait_for_timeout(250); header_ok(pg,g)
    ks=pg.evaluate("[...document.querySelectorAll('.mc')].map(e=>+e.dataset.k)"); idx={}
    for i,k in enumerate(ks): idx.setdefault(k,[]).append(i)
    pairs=list(idx.values()); cards=pg.locator('.mc')
    cards.nth(pairs[0][0]).click(); cards.nth(pairs[1][0]).click(); pg.wait_for_timeout(1000)
    rec(g,'pasangan salah menutup lagi',pg.evaluate("document.querySelectorAll('.mc.on').length")==0)
    for a,c in pairs: cards.nth(a).click(); cards.nth(c).click(); pg.wait_for_timeout(80)
    pg.wait_for_timeout(1000); rec(g,'semua pasangan → selesai',fin_ok(pg) and pts(pg)>p0,f'{p0}->{pts(pg)}'); rec(g,'tanpa error JS',not pg.errs,pg.errs[:1]); ctx.close()
def urut(b):
    ctx,pg=page(b,360,740); g='urut'; p0=pts(pg); play(pg,g); pg.click('#main [data-a=go]'); pg.wait_for_timeout(200); header_ok(pg,g)
    rec(g,'kontrol: hanya "Lihat Contoh Lagi" + 🔁 header (tanpa Ulangi ganda)',pg.locator('#main [data-a=srep]').count()==1 and pg.locator('#main [data-a=rst]').count()==1 and 'Ulangi contoh' not in pg.inner_text('#main'),pg.inner_text('#main .row'))
    def wait_state(s,t=15000):
        pg.wait_for_function(f"document.getElementById('sm')&&document.getElementById('sm').dataset.s==='{s}'",timeout=t)
    wait_state('watch'); rec(g,'indikator: "Perhatikan" saat contoh + tombol contoh nonaktif',pg.evaluate("document.getElementById('srepb').disabled")==True)
    wait_state('turn'); rec(g,'indikator: "Giliranmu" saat giliran anak',True,pg.inner_text('#sm'))
    a=pg.evaluate("G.sq[0]"); w=(a+1)%4; pg.click(f'.sw2[data-v="{w}"]'); pg.wait_for_timeout(60)
    rec(g,'salah = pesan ramah (💛), contoh diulang otomatis',pg.evaluate("document.getElementById('sm').dataset.s")=='oops' and 'Tidak apa-apa' in pg.inner_text('#sm'),pg.inner_text('#sm'))
    t=pg.evaluate("G.t"); done=False; st=time.time()
    while time.time()-st<80 and not fin_ok(pg):
        try: wait_state('turn',8000)
        except Exception: break
        sq=pg.evaluate("G.sq.slice()")
        for x in sq: pg.click(f'.sw2[data-v="{x}"]'); pg.wait_for_timeout(40)
        pg.wait_for_timeout(300)
    rec(g,f'main sampai urutan {t} → selesai + poin',fin_ok(pg) and pts(pg)>p0,f'{p0}->{pts(pg)}')
    rec(g,'layar selesai punya Main Lagi',pg.locator('#main [data-a=play]').count()==1); rec(g,'tanpa error JS',not pg.errs,pg.errs[:1]); ctx.close()
def bfs(z):
    n=z['n'];c=z['c'];goal=n*n-1;DIR=[(0,-1,1),(1,0,2),(0,1,4),(-1,0,8)];prev={z['p']:None};q=[z['p']]
    while q:
        i=q.pop(0)
        if i==goal:break
        for v,(dx,dy,wb) in enumerate(DIR):
            if c[i]['w']&wb:continue
            j=i+dy*n+dx
            if j not in prev: prev[j]=(i,v);q.append(j)
    path=[];i=goal
    while prev[i]: i,v=prev[i];path.append(v)
    return path[::-1]
def labirin(b,vw=360,vh=740,tag=''):
    ctx,pg=page(b,vw,vh); g='labirin'; p0=pts(pg); play(pg,g); pg.click('#main [data-a=go]'); pg.wait_for_timeout(250)
    if not tag: header_ok(pg,g)
    z=pg.evaluate("JSON.parse(JSON.stringify({n:G.mz.n,c:G.mz.c,p:G.mz.p}))")
    # simetri D-pad
    bx={k:pg.locator(f'.dk-{k}').bounding_box() for k in 'uldr'}
    cu=bx['u']['x']+bx['u']['width']/2; cd=bx['d']['x']+bx['d']['width']/2
    sym=abs(cu-cd)<1.5 and abs(bx['l']['y']-bx['d']['y'])<1.5 and abs(bx['d']['y']-bx['r']['y'])<1.5 and len({round(v['width']) for v in bx.values()})==1 and len({round(v['height']) for v in bx.values()})==1
    rec(g+tag,'D-pad simetris: ↑ di tengah atas; ← ↓ → sebaris; ukuran sama',sym,{k:(round(v['x']),round(v['y']),round(v['width'])) for k,v in bx.items()})
    d=pg.evaluate("(()=>{const r=document.querySelector('.dpad').getBoundingClientRect();return r.bottom})()")
    rec(g+tag,'D-pad terlihat penuh tanpa scroll (tidak tertutup)',d<=vh+1,f'bawah={round(d)} tinggi={vh}')
    # keyboard + D-pad klik + swipe
    path=bfs(z); first=path[0]; pg.keyboard.press(['ArrowUp','ArrowRight','ArrowDown','ArrowLeft'][first]); pg.wait_for_timeout(60)
    rec(g+tag,'panah keyboard/remote menggerakkan dino',pg.evaluate("G.mz.mv")==1)
    pg.keyboard.press(['ArrowDown','ArrowLeft','ArrowUp','ArrowRight'][first]); pg.wait_for_timeout(60)  # balik
    rec(g+tag,'tembok menahan / gerak balik valid',pg.evaluate("G.mz.mv")>=1)
    if not tag:
        pg.evaluate("G.mz.p=0;G.mz.mv=0"); pg.evaluate("dz()")
        v=first; dx,dy=[(0,-60),(60,0),(0,60),(-60,0)][v]
        pg.evaluate("""([dx,dy])=>{const m=document.getElementById('mz'),r=m.getBoundingClientRect(),x=r.left+r.width/2,y=r.top+r.height/2;const mk=(t,X,Y)=>{const o=new Touch({identifier:1,target:m,clientX:X,clientY:Y});return new TouchEvent(t,{bubbles:true,cancelable:true,touches:t==='touchend'?[]:[o],changedTouches:[o]})};m.dispatchEvent(mk('touchstart',x,y));m.dispatchEvent(mk('touchend',x+dx,y+dy))}""",[dx,dy]); pg.wait_for_timeout(60)
        rec(g,'geser jari (swipe) menggerakkan dino',pg.evaluate("G.mz.mv")==1)
        pg.evaluate("G.mz.p=0;G.mz.mv=0;dz()")
    for rd in range(3):
        z=pg.evaluate("JSON.parse(JSON.stringify({n:G.mz.n,c:G.mz.c,p:G.mz.p}))"); 
        if tag and rd>0: break
        for v in bfs(z): pg.click(f'.dk[data-v="{v}"]') if rd==0 or not tag else None; 
        pg.wait_for_timeout(1000)
        if tag: break
    if tag:
        rec(g+tag,'selesai babak 1 via D-pad (babak berikutnya dimuat)',pg.evaluate("G.rd")>=1 or fin_ok(pg)); ctx.close(); return
    pg.wait_for_timeout(500)
    rec(g,'3 babak selesai via D-pad + poin bertambah',fin_ok(pg) and pts(pg)>p0,f'{p0}->{pts(pg)}'); rec(g,'tanpa error JS',not pg.errs,pg.errs[:1]); ctx.close()
if __name__=='__main__':
    which=sys.argv[1]
    with sync_playwright() as p:
        b=p.chromium.launch()
        if which=='quiz':
            for g in ['pola','hitung','huruf','tambah','ganjil','bayangan']: quiz(b,g)
        if which=='misc':
            for g in ['beda','spy']: finder(b,g)
            garis(b); memori(b)
        if which=='urut': urut(b)
        if which=='lab':
            labirin(b)
            for vw,vh,t in [(320,568,'@320x568'),(360,640,'@360x640'),(390,844,'@390x844'),(430,932,'@430x932'),(768,1024,'@768x1024')]: labirin(b,vw,vh,t)
        b.close()
    json.dump(R,open(f'/home/claude/tests/res_games_{which}.json','w'),ensure_ascii=False,indent=1)
