import sys; sys.path.insert(0,'/home/claude/work/audit/tests')
from common import *
import heapq,collections
QUIZ=['pola','hitung','huruf','tambah','ganjil','bayangan']
def finpts(g): return g
with sync_playwright() as p:
    b=p.chromium.launch()
    # ---------- QUIZ ----------
    for gid in QUIZ:
        ctx,pg=mkpage(b); mkprofile(pg)
        open_game(pg,gid); intro=pg.inner_text('#main')
        rec(gid,'Buka permainan','Layar intro + tombol Mulai & Kembali','go' if pg.query_selector('#main [data-a=go]') and pg.query_selector('#main [data-a=nav]') else 'tidak ada',bool(pg.query_selector('#main [data-a=go]') and pg.query_selector('#main [data-a=nav]')))
        go(pg); has=len(pg.query_selector_all('#main [data-a=ans]'))
        rec(gid,'Mulai','>=3 pilihan jawaban',has,has>=3)
        p0=pts(pg); sig=set(); dup=False; empty=False
        # salah dulu
        q=pg.evaluate("G.q"); wrong=[i for i in range(len(q['o'])) if i!=q['a']][0]
        b0=P(pg)['bad']
        pg.click(f'#main [data-a=ans][data-v="{wrong}"]'); fb=pg.inner_text('#fb')
        rec(gid,'Jawab salah','Poin tetap, bad+1, pesan ramah',f"pts {p0}->{pts(pg)}, bad {b0}->{P(pg)['bad']}, '{fb[:30]}'",pts(pg)==p0 and P(pg)['bad']==b0+1 and 'Hampir' in fb)
        pg.click('#main [data-a=nq]'); pg.wait_for_timeout(100)
        for i in range(1,5):
            q=pg.evaluate("G.q"); key=q['q']+str(q['o'][q['a']])
            if key in sig: dup=True
            sig.add(key)
            if len(q['o'])<2 or any(o in ('',None) for o in q['o']) or len(set(q['o']))!=len(q['o']): empty=True
            pg.click(f'#main [data-a=ans][data-v="{q["a"]}"]'); pg.wait_for_timeout(60)
            pg.click('#main [data-a=nq]'); pg.wait_for_timeout(120)
        d=pts(pg)-p0
        rec(gid,'Soal unik & pilihan valid (5 soal)','tanpa duplikat, tanpa pilihan kosong/ganda',f'dup={dup} invalid={empty}',not dup and not empty)
        rec(gid,'Selesaikan','Layar selesai muncul, poin 4x10 + 20 (+30 bila tantangan harian), tanpa NaN',f'delta={d}',on_fin(pg) and d in (60,90) and pg.evaluate("Number.isFinite(P().pts)"))
        done=P(pg)['done']
        rec(gid,'Aktivitas selesai bertambah 1','done=1',done,done==1)
        pg.evaluate("fin()"); pg.evaluate("fin()")
        rec(gid,'fin() dipanggil ganda','tidak ada hadiah ganda',f"done={P(pg)['done']} pts={pts(pg)-p0}",P(pg)['done']==1 and pts(pg)-p0==d)
        pg.click('#main [data-a=play]'); pg.wait_for_timeout(200)
        st=pg.evaluate("[G.i,G.done,G.st]")
        rec(gid,'Main Lagi','State direset (i=0,done=0,st=0)',st,st==[0,0,0] and bool(pg.query_selector('#main [data-a=go]')))
        go(pg); pg.click('#main [data-a=ans]'); pg.evaluate("document.querySelector('[data-a=nav][data-v=home]').click()"); pg.wait_for_timeout(1500)
        rec(gid,'Keluar sebelum selesai','Kembali ke beranda, tanpa error, tanpa hadiah',f"errs={pg.errs[:2]}",not pg.errs and bool(pg.query_selector('.hero')))
        pg.reload(); pg.wait_for_timeout(300); pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()")
        pp=pg.evaluate("(()=>{const x=JSON.parse(localStorage.getItem('bba1'));return [x.p[0].pts,x.p[0].done]})()")
        rec(gid,'Refresh setelah progres tersimpan','pts & done sama setelah reload',pp,pp[0]>=d and pp[1]==1)
        ctx.close()
    # ---------- CARI PERBEDAAN & I SPY ----------
    for gid in ['beda','spy']:
        ctx,pg=mkpage(b); mkprofile(pg); open_game(pg,gid); go(pg)
        p0=pts(pg); bad0=P(pg)['bad']
        d=pg.evaluate("G.d"); cells=pg.evaluate("document.querySelectorAll('[data-a=bd]').length")
        wrong=[i for i in range(cells) if i not in d][0]
        pg.click(f'[data-a=bd][data-v="{wrong}"]'); 
        rec(gid,'Ketuk area salah','poin tetap, bad+1, bisa lanjut',f"pts {p0}->{pts(pg)} bad+{P(pg)['bad']-bad0}",pts(pg)==p0 and P(pg)['bad']==bad0+1)
        ok=True; fb=''
        for r in range(3):
            d=pg.evaluate("G.d")
            for k,i in enumerate(d):
                pg.click(f'[data-a=bd][data-v="{i}"]',force=True)
                if k==0: pg.click(f'[data-a=bd][data-v="{i}"]',force=True,timeout=800) if False else None
            fb=pg.inner_text('#fb')
            if 'Hebat' not in fb: ok=False
            # ketuk salah setelah semua ketemu tidak boleh menambah bad
            bb=P(pg)['bad']
            w=[i for i in range(cells) if i not in d][0]
            pg.evaluate(f"document.querySelector('[data-a=bd][data-v=\"{w}\"]').click()")
            if P(pg)['bad']!=bb: ok=False
            pg.click('#main [data-a=nr]'); pg.wait_for_timeout(150)
        rec(gid,'Temukan semua target tiap babak (3 babak)','selesai hanya saat semua target ditemukan; ketukan setelah selesai diabaikan',f'ok={ok}',ok and on_fin(pg))
        d2=pts(pg)-p0
        rec(gid,'Poin','sesuai ok() per target + 20',d2,d2>0 and pg.evaluate("Number.isFinite(P().pts)"))
        # keluar saat berjalan
        pg.click('#main [data-a=play]'); go(pg); pg.evaluate("document.querySelector('[data-a=nav][data-v=home]').click()"); pg.wait_for_timeout(800)
        rec(gid,'Keluar sebelum selesai','tanpa error',pg.errs[:2],not pg.errs)
        ctx.close()
    # ---------- MEWARNAI ----------
    ctx,pg=mkpage(b); mkprofile(pg); open_game(pg,'warna'); go(pg)
    n=pg.evaluate("G.dr.s.length"); did=pg.evaluate("G.dr.id"); p0=pts(pg)
    pg.click('#main [data-a=cdone]'); rec('warna','Selesai tanpa mewarnai','ditolak, tidak ada poin',f'pts {p0}->{pts(pg)}',pts(pg)==p0 and not on_fin(pg))
    def paint(i,ci):
        pg.click(f'#main [data-a=col]:nth-child({ci+1})')
        pg.evaluate(f"document.querySelector('.cv [data-v=\"{i}\"]').dispatchEvent(new MouseEvent('click',{{bubbles:true}}))")
    paint(0,1); paint(1,2)
    cnt=pg.evaluate("Object.keys(P().art).length")
    rec('warna','Pilih warna & ketuk area','area terwarnai sesuai warna terpilih',f"art={pg.evaluate('JSON.stringify(P().art)')[:60]}",cnt==2 and pg.evaluate("document.querySelector('.cv [data-v=\"0\"]').style.fill!==''"))
    pg.click('#main [data-a=undo]'); c1=pg.evaluate("Object.keys(P().art).length")
    pg.click('#main [data-a=redo]'); c2=pg.evaluate("Object.keys(P().art).length")
    rec('warna','Undo / Redo','undo 2->1, redo 1->2',f'{c1},{c2}',c1==1 and c2==2)
    pg.click('#main [data-a=rs]'); did2=pg.evaluate("G.dr.id"); c3=pg.evaluate("Object.keys(P().art).length")
    rec('warna','Reset','gambar SAMA, semua warna dihapus',f'{did}->{did2}, art={c3}',did==did2 and c3==0)
    need=-(-n*5//10)  # dif=1 -> .5
    for i in range(n): paint(i,i%12)
    pg.click('#main [data-a=cdone]'); pg.wait_for_timeout(300)
    rec('warna','Selesai setelah cukup bagian','fin muncul, +20 saja (tidak ada poin tambahan dari mewarnai)',f'delta={pts(pg)-p0}',on_fin(pg) and pts(pg)-p0 in (20,50))
    pg.click('#main [data-a=play]'); go(pg); pg.click('#main [data-a=cdone]')
    rec('warna','Main Lagi lalu langsung Selesai (anti tambang poin)','ditolak karena lembar baru kosong',f'fin={on_fin(pg)}',not on_fin(pg))
    pg.click('#main [data-a=cnext]'); did3=pg.evaluate("G.dr.id"); pg.click('#main [data-a=cnext]'); did4=pg.evaluate("G.dr.id")
    rec('warna','Gambar lain','tidak mengulang gambar yang sama berturut-turut',f'{did3},{did4}',did3!=did4)
    sc=pg.evaluate("[document.documentElement.scrollWidth,document.documentElement.clientWidth]")
    rec('warna','Tanpa scroll horizontal (412px)','scrollWidth<=clientWidth',sc,sc[0]<=sc[1])
    ctx.close()
    # ---------- GARIS ----------
    ctx,pg=mkpage(b); mkprofile(pg); open_game(pg,'garis'); go(pg)
    n=pg.evaluate("G.t"); p0=pts(pg); b0=P(pg)['bad']
    if n>1:
        pg.click('#l0'); other=pg.evaluate("[...document.querySelectorAll('[data-a=R]')].map(e=>e.dataset.v).filter(v=>v!=='0')[0]")
        pg.click(f'[data-a=R][data-v="{other}"]')
        rec('garis','Pasangan salah','tidak ada garis, poin tetap, bad+1',f"lines={pg.evaluate('document.querySelectorAll(\"#sv line\").length')} bad+{P(pg)['bad']-b0}",pg.evaluate('document.querySelectorAll("#sv line").length')==0 and pts(pg)==p0 and P(pg)['bad']==b0+1)
    # pasangan benar: pertama via tap, kedua via drag mouse
    pg.click('#l0'); pg.click('[data-a=R][data-v="0"]')
    rec('garis','Pasangan benar via ketuk','1 garis, kedua tombol terkunci',f"lines={pg.evaluate('document.querySelectorAll(\"#sv line\").length')}",pg.evaluate('document.querySelectorAll("#sv line").length')==1 and pg.evaluate("document.getElementById('l0').disabled"))
    pg.click('#l0',force=True); pg.wait_for_timeout(50)
    bx=pg.query_selector('#l1').bounding_box(); rx=pg.query_selector('[data-a=R][data-v="1"]').bounding_box()
    pg.mouse.move(bx['x']+bx['width']/2,bx['y']+bx['height']/2); pg.mouse.down(); pg.mouse.move(bx['x']+60,bx['y']+30,steps=4); pg.mouse.move(rx['x']+rx['width']/2,rx['y']+rx['height']/2,steps=6); pg.mouse.up(); pg.wait_for_timeout(100)
    rec('garis','Pasangan benar via seret mouse','garis ke-2 terbentuk, tidak dihitung dua kali',f"lines={pg.evaluate('document.querySelectorAll(\"#sv line\").length')} m={pg.evaluate('G.m')}",pg.evaluate('document.querySelectorAll("#sv line").length')==2 and pg.evaluate('G.m')==2)
    # resize -> garis mengikuti
    pg.set_viewport_size({'width':340,'height':700}); pg.wait_for_timeout(400)
    err=pg.evaluate("""(()=>{const c=document.getElementById('box').getBoundingClientRect();let m=0;[...document.querySelectorAll('#sv line')].forEach((ln,i)=>{const v=G.cx[i],a=document.getElementById('l'+v).getBoundingClientRect();const x1=a.left-c.left+a.width/2,y1=a.top-c.top+a.height/2;m=Math.max(m,Math.abs(+ln.getAttribute('x1')-x1),Math.abs(+ln.getAttribute('y1')-y1))});return m})()""")
    rec('garis','Resize/rotasi layar','titik ujung garis tetap pada tombol (selisih <2px)',f'maks selisih {err:.1f}px',err<2)
    pg.set_viewport_size({'width':412,'height':900}); pg.wait_for_timeout(300)
    for i in range(2,n): pg.click(f'#l{i}',force=True); pg.click(f'[data-a=R][data-v="{i}"]',force=True)
    pg.wait_for_timeout(1000)
    rec('garis','Selesaikan semua pasangan','fin muncul sekali',f"fin={on_fin(pg)} done={P(pg)['done']}",on_fin(pg) and P(pg)['done']==1)
    pg.click('#main [data-a=play]'); go(pg); pg.click('#main [data-a=go]') if pg.query_selector('#main [data-a=go]') else None
    rec('garis','Ulangi','garis kosong lagi & G.cx kosong',f"lines={pg.evaluate('document.querySelectorAll(\"#sv line\").length')} cx={pg.evaluate('G.cx.length')}",pg.evaluate('document.querySelectorAll("#sv line").length')==0 and pg.evaluate('G.cx.length')==0)
    ctx.close()
    # ---------- MEMORI ----------
    ctx,pg=mkpage(b); mkprofile(pg); open_game(pg,'memori'); go(pg)
    ks=pg.evaluate("[...document.querySelectorAll('[data-a=flip]')].map(e=>+e.dataset.k)"); p0=pts(pg)
    by=collections.defaultdict(list)
    for idx,k in enumerate(ks): by[k].append(idx)
    cards=pg.query_selector_all('[data-a=flip]')
    ka=list(by); a,bb=by[ka[0]][0],by[ka[1]][0]
    cards[a].click(); cards[bb].click(); cards[by[ka[2]][0]].click()   # kartu ke-3 saat terkunci
    third=pg.evaluate("document.querySelectorAll('.opt.mc.on').length")
    rec('memori','Dua kartu beda + ketuk kartu ke-3 saat terkunci','kartu ke-3 diabaikan (2 terbuka), poin tetap',f'terbuka={third} pts {p0}->{pts(pg)}',third==2 and pts(pg)==p0)
    pg.wait_for_timeout(1000)
    closed=pg.evaluate("document.querySelectorAll('.opt.mc.on').length")
    rec('memori','Pasangan salah menutup kembali','0 kartu terbuka setelah jeda 0.8 dtk',closed,closed==0)
    for k in ka:
        i,j=by[k]; cards[i].click(); cards[j].click(); pg.wait_for_timeout(100)
    pg.wait_for_timeout(1000)
    rec('memori','Temukan semua pasangan','fin muncul sekali, hanya setelah semua pasangan',f"fin={on_fin(pg)} done={P(pg)['done']}",on_fin(pg) and P(pg)['done']==1)
    pg.click('#main [data-a=play]'); go(pg); st=pg.evaluate("[G.m,G.mv,document.querySelectorAll('.opt.mc.on').length]")
    rec('memori','Ulangi','kartu & langkah direset',st,st==[0,0,0])
    pg.evaluate("document.querySelector('[data-a=nav][data-v=home]').click()"); pg.wait_for_timeout(900)
    rec('memori','Keluar saat berjalan','tanpa error',pg.errs[:2],not pg.errs)
    ctx.close()
    # ---------- LABIRIN ----------
    ctx,pg=mkpage(b); mkprofile(pg); open_game(pg,'labirin'); go(pg); p0=pts(pg)
    def solve(pg):
        z=pg.evaluate("(()=>{const z=G.mz;return {n:z.n,w:z.c.map(c=>c.w),p:z.p}})()"); n=z['n']; T=n*n-1
        prev={z['p']:None}; q=[z['p']]; D=[(0,-1,1,'ArrowUp'),(1,0,2,'ArrowRight'),(0,1,4,'ArrowDown'),(-1,0,8,'ArrowLeft')]
        while q:
            i=q.pop(0)
            if i==T: break
            for dx,dy,bit,key in D:
                if z['w'][i]&bit: continue
                j=i+dy*n+dx
                if j not in prev: prev[j]=(i,key); q.append(j)
        path=[];i=T
        while prev[i] is not None: i,k=prev[i][0],prev[i][1]; path.append(k)
        return path[::-1]
    # tembok
    z=pg.evaluate("(()=>{const z=G.mz;return {w:z.c[0].w,p:z.p}})()")
    wallkey=None
    for bit,key in [(1,'ArrowUp'),(8,'ArrowLeft'),(2,'ArrowRight'),(4,'ArrowDown')]:
        if z['w']&bit: wallkey=key;break
    if wallkey:
        pg.keyboard.press(wallkey); rec('labirin','Menabrak tembok','posisi tidak berubah',pg.evaluate('G.mz.p'),pg.evaluate('G.mz.p')==0 and pg.evaluate('G.mz.mv')==0)
    pg.click('#main [data-a=hint]'); hn=pg.evaluate('G.mz.hn.size')
    rec('labirin','Petunjuk','menandai jalur (>0 sel)',hn,hn>0)
    for rd in range(3):
        for key in solve(pg): pg.keyboard.press(key)
        pg.wait_for_timeout(1000)
    rec('labirin','Selesaikan 3 babak (keyboard)','fin muncul setelah babak 3',f"fin={on_fin(pg)} done={P(pg)['done']}",on_fin(pg) and P(pg)['done']==1)
    pg.click('#main [data-a=play]'); go(pg)
    # tombol D-pad
    path=solve(pg); mp={'ArrowUp':0,'ArrowRight':1,'ArrowDown':2,'ArrowLeft':3}
    for key in path[:3]: pg.click(f'#main [data-a=mv][data-v="{mp[key]}"]')
    rec('labirin','Kontrol tombol sentuh (D-pad)','karakter bergerak sesuai tombol',pg.evaluate('G.mz.mv'),pg.evaluate('G.mz.mv')==min(3,len(path)))
    pg.click('#main [data-a=mrs]'); rec('labirin','Ulangi babak','posisi awal',pg.evaluate('[G.mz.p,G.mz.mv]'),pg.evaluate('G.mz.p')==0 and pg.evaluate('G.mz.mv')==0)
    # selesaikan babak lalu keluar < 700ms
    for key in solve(pg): pg.keyboard.press(key)
    pg.evaluate("document.querySelector('[data-a=nav][data-v=home]').click()"); pg.wait_for_timeout(1500)
    rec('labirin','Keluar tepat setelah babak selesai (timer 700ms)','tetap di beranda, tanpa error',f"home={bool(pg.query_selector('.hero'))} errs={pg.errs[:2]}",bool(pg.query_selector('.hero')) and not pg.errs)
    ctx.close()
    # ---------- URUT ----------
    ctx,pg=mkpage(b); mkprofile(pg); open_game(pg,'urut'); go(pg); p0=pts(pg)
    def wait_unlock(pg): pg.wait_for_function("G.lock===0",timeout=15000)
    pg.click('#main [data-a=srep]'); lk=pg.evaluate("G.lock")
    rec('urut','Tombol Ulangi contoh saat demo berjalan','diabaikan (tetap terkunci)',lk,lk==1)
    wait_unlock(pg)
    rec('urut','Input hanya setelah contoh selesai','G.lock=0 setelah demo','ok',True)
    pg.click('#main [data-a=srep]'); rec('urut','Ulangi contoh','terkunci lagi saat demo',pg.evaluate('G.lock'),pg.evaluate('G.lock')==1); wait_unlock(pg)
    sq=pg.evaluate("G.sq"); wrong=(sq[0]+1)%4; b0=P(pg)['bad']
    pg.click(f'.sw2:nth-child({wrong+1})'); lk=pg.evaluate("G.lock"); pg.click(f'.sw2:nth-child(1)',force=True); pg.click(f'.sw2:nth-child(2)',force=True)
    rec('urut','Jawab salah','terkunci segera, input saat replay diabaikan, bad+1',f"lock={lk} in={pg.evaluate('G.in.length')} bad+{P(pg)['bad']-b0}",lk==1 and pg.evaluate('G.in.length')==0 and P(pg)['bad']==b0+1)
    wait_unlock(pg)
    tot=pg.evaluate("G.t")
    for r in range(tot):
        wait_unlock(pg); sq=pg.evaluate("G.sq")
        for v in sq: pg.click(f'.sw2:nth-child({v+1})',force=True)
        pg.wait_for_timeout(1200 if r<tot-1 else 900)
    rec('urut','Selesaikan semua ronde (urutan benar)','fin muncul, urutan bertambah tiap ronde',f"fin={on_fin(pg)} done={P(pg)['done']}",on_fin(pg) and P(pg)['done']==1)
    pg.click('#main [data-a=play]'); go(pg); pg.evaluate("document.querySelector('[data-a=nav][data-v=home]').click()"); pg.wait_for_timeout(5000)
    rec('urut','Keluar saat demo berjalan','timer demo tidak bocor; tanpa error',pg.errs[:2],not pg.errs and bool(pg.query_selector('.hero')))
    ctx.close()
    # ---------- PUZZLE ----------
    ctx,pg=mkpage(b); mkprofile(pg); open_game(pg,'puzzle'); go(pg)
    menu=bool(pg.query_selector('[data-a=pzgo]')); rec('puzzle','Buka menu puzzle','menu kategori/gambar/tingkat',menu,menu)
    pg.click('[data-a=pzgo]'); pg.wait_for_selector('#pzb',timeout=6000)
    n=pg.evaluate("G.pz.n"); p0=pts(pg)
    pg.click('.pzp2[data-v="0"]'); wrong=1
    pg.click(f'.pzs2[data-v="{wrong}"]'); rec('puzzle','Keping di kotak salah','tidak terkunci, tetap bisa dicoba lagi',f"ok={pg.evaluate('G.pz.ok')} msg='{pg.inner_text('#pzmsg')[:25]}'",pg.evaluate('G.pz.ok')==0 and 'Belum pas' in pg.inner_text('#pzmsg'))
    # drag keping 0 ke kotak 0
    a=pg.query_selector('.pzp2[data-v="0"]').bounding_box(); s=pg.query_selector('.pzs2[data-v="0"]').bounding_box()
    pg.mouse.move(a['x']+a['width']/2,a['y']+a['height']/2); pg.mouse.down(); pg.mouse.move(a['x']+30,a['y']+30,steps=4); pg.mouse.move(s['x']+s['width']/2,s['y']+s['height']/2,steps=6); pg.mouse.up(); pg.wait_for_timeout(150)
    rec('puzzle','Seret keping ke kotak benar','keping terkunci',pg.evaluate('G.pz.ok'),pg.evaluate('G.pz.ok')==1)
    pg.click('[data-a=pzhint]'); pg.click('[data-a=pzpause]'); pg.click('.pzp2',force=True) if False else None
    okp=pg.evaluate('G.pz.paused'); pg.click('[data-a=pzpause]')
    rec('puzzle','Petunjuk & Jeda','petunjuk menyorot kotak; jeda dapat dilanjutkan',f'paused={okp}',okp==1 and pg.evaluate('G.pz.paused')==0)
    for k in range(1,n):
        pg.click(f'.pzp2[data-v="{k}"]',force=True); pg.click(f'.pzs2[data-v="{k}"]',force=True)
    pg.wait_for_timeout(900)
    d=pts(pg)-p0
    rec('puzzle','Selesaikan puzzle (ketuk)','layar selesai, hadiah +20 +bonus tingkat (10) sekali',f'delta={d} fin={on_fin(pg)}',on_fin(pg) and d in (30,60) and P(pg)['done']==1)
    pg.click('[data-a=pzre]'); pg.wait_for_selector('#pzb',timeout=6000)
    for k in range(n):
        pg.click(f'.pzp2[data-v="{k}"]',force=True); pg.click(f'.pzs2[data-v="{k}"]',force=True)
    pg.wait_for_timeout(900); d2=pts(pg)-p0
    rec('puzzle','Main lagi puzzle yang sama (anti tambang)','tanpa poin baru',f'delta {d}->{d2}',d2==d)
    # keluar saat memuat
    pg.click('[data-a=pzmenu]'); pg.click('[data-a=pzgo]'); pg.evaluate("document.querySelector('[data-a=nav][data-v=home]').click()"); pg.wait_for_timeout(2500)
    rec('puzzle','Keluar saat puzzle sedang disiapkan','tidak menimpa beranda, tanpa error',f"home={bool(pg.query_selector('.hero'))} errs={pg.errs[:2]}",bool(pg.query_selector('.hero')) and not pg.errs)
    ctx.close()
    b.close()
json.dump(R,open('/home/claude/work/audit/tests/hasil_logika.json','w'),ensure_ascii=False,indent=1)
f=[r for r in R if r['status']!='PASS']
print('total',len(R),'FAIL',len(f))
for r in f: print('FAIL',r['game'],'|',r['skenario'],'|',r['harapan'],'|',r['aktual'])
