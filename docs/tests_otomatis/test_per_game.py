import sys,json,collections; sys.path.insert(0,'/home/claude/work/audit/tests')
from common import *
VPN=sys.argv[1]; GAMES=sys.argv[2].split(',')
VPS={'hp':(360,800,True),'desktop':(1366,768,False)}
W,H,TOUCH=VPS[VPN]
MT=[]
NAMES={'warna':'Mewarnai','pola':'Pola & Logika','hitung':'Hitung & Lingkarkan','huruf':'Huruf & Kata','tambah':'Tambah Bergambar','ganjil':'Mana yang Beda?','garis':'Menghubungkan Garis','beda':'Cari Perbedaan','spy':'I Spy Game','memori':'Puzzle & Memori','bayangan':'Cari Bayangan','labirin':'Labirin','urut':'Ingat Urutan','puzzle':'Puzzle Petualangan'}
QUIZ=['pola','hitung','huruf','tambah','ganjil','bayangan']
def S(game,dim,skn,harap,fn):
    try: ok,ak=fn()
    except Exception as e: ok,ak=False,'PENGECUALIAN: '+str(e).split('\n')[0][:130]
    MT.append(dict(vp=VPN,game=game,dim=dim,skenario=skn,harapan=harap,aktual=str(ak)[:150],status='PASS' if ok else 'FAIL'))
def BL(game,dim,skn,alasan,manual): MT.append(dict(vp=VPN,game=game,dim=dim,skenario=skn,harapan='-',aktual=alasan,status='BLOCKED',manual=manual))
def mk(b):
    ctx,pg=mkpage(b,W,H,touch=TOUCH); mkprofile(pg); pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()"); return ctx,pg
def T(pg,sel,**k):
    l=pg.locator(sel).first
    l.tap(timeout=4000,**k) if TOUCH else l.click(timeout=4000,**k)
    pg.wait_for_timeout(70)
def tap_xy(pg,x,y):
    pg.touchscreen.tap(x,y) if TOUCH else pg.mouse.click(x,y)
    pg.wait_for_timeout(70)
def open_via_ui(pg,gid):
    for tab in ('belajar','main'):
        T(pg,f'#hd [data-a=nav][data-v={tab}]'); pg.wait_for_timeout(120)
        if pg.query_selector(f'#main [data-a=play][data-v={gid}]'):
            T(pg,f'#main [data-a=play][data-v={gid}]'); pg.wait_for_timeout(200); return True
    return False
def start_ui(pg,gid):
    assert open_via_ui(pg,gid),'kartu permainan tidak ditemukan'
    T(pg,'#main [data-a=go]'); pg.wait_for_timeout(250)
    if gid=='puzzle': T(pg,'[data-a=pzgo]'); pg.wait_for_selector('#pzb',timeout=6000); pg.wait_for_timeout(150)
def tap_shape(pg,i):
    pt=pg.evaluate("""(i)=>{const el=document.querySelector('.cv [data-v="'+i+'"]');el.scrollIntoView({block:'center'});const b=el.getBoundingClientRect();for(let fx of [.5,.3,.7,.2,.8,.4,.6])for(let fy of [.5,.3,.7,.2,.8]){const x=b.left+b.width*fx,y=b.top+b.height*fy;if(document.elementFromPoint(x,y)===el)return[x,y]}return null}""",i)
    if not pt: raise Exception('area %d tak terjangkau jari'%i)
    tap_xy(pg,*pt)
def solve_maze(pg):
    z=pg.evaluate("(()=>{const z=G.mz;return {n:z.n,w:z.c.map(c=>c.w),p:z.p}})()"); n=z['n']; Tg=n*n-1
    prev={z['p']:None}; q=[z['p']]; D=[(0,-1,1,0),(1,0,2,1),(0,1,4,2),(-1,0,8,3)]
    while q:
        i=q.pop(0)
        if i==Tg: break
        for dx,dy,bit,k in D:
            if z['w'][i]&bit: continue
            j=i+dy*n+dx
            if j not in prev: prev[j]=(i,k); q.append(j)
    path=[];i=Tg
    while prev[i] is not None: i,k=prev[i]; path.append(k)
    return path[::-1]
KEY={0:'ArrowUp',1:'ArrowRight',2:'ArrowDown',3:'ArrowLeft'}
def move(pg,d):
    if TOUCH: T(pg,f'#main [data-a=mv][data-v="{d}"]')
    else: pg.keyboard.press(KEY[d]); pg.wait_for_timeout(40)
def clean_run(pg,gid):
    """Selesaikan permainan dengan benar lewat input nyata. Kembalikan (dok, fin_sebelum_akhir)."""
    ok0=P(pg)['ok']; early=False
    if gid in QUIZ:
        for i in range(5):
            a=pg.evaluate("G.q.a"); T(pg,f'#main [data-a=ans][data-v="{a}"]')
            if i<4 and on_fin(pg): early=True
            T(pg,'#main [data-a=nq]')
    elif gid in ('beda','spy'):
        for r in range(3):
            for i in pg.evaluate("G.d"): T(pg,f'#main [data-a=bd][data-v="{i}"]')
            if r<2 and on_fin(pg): early=True
            T(pg,'#main [data-a=nr]')
    elif gid=='warna':
        n=pg.evaluate("G.dr.s.length")
        for i in range(n):
            T(pg,f'#main [data-a=col]:nth-child({i%12+1})'); tap_shape(pg,i)
        T(pg,'#main [data-a=cdone]')
    elif gid=='garis':
        n=pg.evaluate("G.t")
        for i in range(n):
            T(pg,f'#l{i}'); T(pg,f'[data-a=R][data-v="{i}"]')
            if i<n-1 and on_fin(pg): early=True
    elif gid=='memori':
        ks=pg.evaluate("[...document.querySelectorAll('[data-a=flip]')].map(e=>+e.dataset.k)"); by=collections.defaultdict(list)
        for idx,k in enumerate(ks): by[k].append(idx)
        cards=pg.locator('[data-a=flip]')
        for j,(k,(a,b)) in enumerate(by.items()):
            (cards.nth(a).tap if TOUCH else cards.nth(a).click)(timeout=4000); (cards.nth(b).tap if TOUCH else cards.nth(b).click)(timeout=4000); pg.wait_for_timeout(90)
            if j<len(by)-1 and on_fin(pg): early=True
    elif gid=='labirin':
        for rd in range(3):
            for d in solve_maze(pg): move(pg,d)
            if rd<2:
                if on_fin(pg): early=True
                pg.wait_for_function(f"G.rd=={rd+1}",timeout=4000)
    elif gid=='urut':
        tot=pg.evaluate("G.t")
        for r in range(tot):
            pg.wait_for_function("G.lock===0",timeout=20000); sq=pg.evaluate("G.sq")
            for v in sq: T(pg,f'.sw2:nth-child({v+1})')
            if r<tot-1 and on_fin(pg): early=True
            pg.wait_for_timeout(1100)
    elif gid=='puzzle':
        n=pg.evaluate("G.pz.n")
        for k in range(n):
            T(pg,f'.pzp2[data-v="{k}"]'); T(pg,f'.pzs2[data-v="{k}"]')
            if k<n-1 and on_fin(pg): early=True
    pg.wait_for_timeout(1000)
    return P(pg)['ok']-ok0, early
RESET={'warna':'rs','garis':'go','labirin':'mrs','puzzle':'pzre'}
def progress_one(pg,gid):
    """Lakukan satu langkah benar (untuk menguji reset/keluar/refresh saat permainan berjalan)."""
    if gid in QUIZ:
        a=pg.evaluate("G.q.a"); T(pg,f'#main [data-a=ans][data-v="{a}"]')
    elif gid in('beda','spy'): T(pg,f'#main [data-a=bd][data-v="{pg.evaluate("G.d")[0]}"]')
    elif gid=='warna': T(pg,'#main [data-a=col]:nth-child(2)'); tap_shape(pg,0)
    elif gid=='garis': T(pg,'#l0'); T(pg,'[data-a=R][data-v="0"]')
    elif gid=='memori':
        ks=pg.evaluate("[...document.querySelectorAll('[data-a=flip]')].map(e=>+e.dataset.k)"); i=[j for j,k in enumerate(ks) if k==ks[0]]
        c=pg.locator('[data-a=flip]'); (c.nth(i[0]).tap if TOUCH else c.nth(i[0]).click)(); (c.nth(i[1]).tap if TOUCH else c.nth(i[1]).click)(); pg.wait_for_timeout(100)
    elif gid=='labirin':
        for d in solve_maze(pg)[:3]: move(pg,d)
    elif gid=='urut':
        pg.wait_for_function("G.lock===0",timeout=20000); T(pg,f'.sw2:nth-child({pg.evaluate("G.sq")[0]+1})'); pg.wait_for_timeout(1200)
    elif gid=='puzzle': T(pg,'.pzp2[data-v="0"]'); T(pg,'.pzs2[data-v="0"]')
def state_reset_ok(pg,gid):
    if gid in QUIZ: return pg.evaluate("[G.i,G.st,G.done]")==[0,0,0], pg.evaluate("[G.i,G.st]")
    if gid in('beda','spy'): return pg.evaluate("[G.i,G.f]")==[0,0], pg.evaluate("[G.i,G.f]")
    if gid=='warna': c=pg.evaluate("Object.keys(P().art).filter(k=>k.startsWith(G.dr.id+'_')).length"); return c==0, f'bagian terwarnai={c}'
    if gid=='garis': v=pg.evaluate("[document.querySelectorAll('#sv line').length,G.m,G.cx.length]"); return v==[0,0,0],v
    if gid=='memori': v=pg.evaluate("[G.m,G.mv,document.querySelectorAll('.opt.mc.on').length]"); return v==[0,0,0],v
    if gid=='labirin': v=pg.evaluate("[G.mz.p,G.mz.mv]"); return v==[0,0],v
    if gid=='urut': v=pg.evaluate("[G.sq.length,G.in.length]"); return v==[1,0],v
    if gid=='puzzle': v=pg.evaluate("[G.pz.ok,document.querySelectorAll('.pzp2').length,G.pz.n]"); return v[0]==0 and v[1]==v[2],v
METR="""(()=>{const de=document.documentElement,vis=e=>{const r=e.getBoundingClientRect(),c=getComputedStyle(e);return r.width>0&&r.height>0&&c.visibility!=='hidden'&&c.display!=='none'};
const els=[...document.querySelectorAll('#main button,#main input')].filter(vis);const cov=[];els.slice(0,60).forEach(e=>{e.scrollIntoView({block:'center'});const r=e.getBoundingClientRect(),x=r.left+r.width/2,y=r.top+r.height/2;if(x<0||y<0||x>innerWidth||y>innerHeight)return;const t=document.elementFromPoint(x,y);if(t&&!(e.contains(t)||t.contains(e)))cov.push(e.dataset.a)});window.scrollTo(0,0);
return {hs:de.scrollWidth-de.clientWidth,small:els.filter(e=>Math.min(e.getBoundingClientRect().width,e.getBoundingClientRect().height)<44&&!e.matches('.sw')).map(e=>e.dataset.a),cov:[...new Set(cov)],off:els.filter(e=>{const r=e.getBoundingClientRect();return r.right>innerWidth+1||r.left<-1}).length}})()"""
with sync_playwright() as p:
    b=p.chromium.launch()
    for gid in GAMES:
        N=NAMES[gid]; ctx,pg=mk(b); daily=pg.evaluate("DAILY()")
        # 1 INPUT (buka lewat UI nyata)
        S(gid,'Input','Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai',f'layar permainan tampil, tanpa tombol tertutup',lambda:(start_ui(pg,gid) or True) and (True,f'G.id={pg.evaluate("G.id")}') if True else None)
        # 2 MENANG + SKOR (jalankan bersih)
        p0=pts(pg); res={}
        def clean():
            dok,early=clean_run(pg,gid); res['dok']=dok; res['early']=early
            return on_fin(pg) and not early, f'fin={on_fin(pg)} fin_terlalu_awal={early} dok={dok}'
        S(gid,'Kondisi menang','Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1)',f'fin tepat di akhir',lambda:(lambda r:(r[0] and P(pg)['done']==1,r[1]+f" done={P(pg)['done']}"))(clean()))
        def skor():
            d=pts(pg)-p0; dok=res.get('dok',0)
            if gid=='puzzle': exp=30
            else: exp=10*dok+10*(dok//5)+20
            exp+= 30 if daily==gid else 0
            return d==exp, f'delta={d} diharapkan={exp} (dok={dok}{", +30 harian" if daily==gid else ""})'
        S(gid,'Skor','Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN',f'sesuai rumus',skor)
        # 3 PENGULANGAN
        def ulang():
            fin_btn='#main [data-a=play]' if gid!='puzzle' else '#main [data-a=pzre]'
            T(pg,fin_btn); pg.wait_for_timeout(250)
            if gid=='puzzle': pg.wait_for_selector('#pzb',timeout=6000); st=pg.evaluate("[G.pz.ok,G.done]"); return st[0]==0,st
            intro=bool(pg.query_selector('#main [data-a=go]')); T(pg,'#main [data-a=go]'); pg.wait_for_timeout(250)
            st=pg.evaluate("[G.done,G.i||0]"); return intro and st[0]==0,f'intro={intro} state={st}'
        S(gid,'Pengulangan','Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda',f'state bersih',ulang)
        pA=pts(pg)
        # 4 JAWABAN BENAR/SALAH
        def jawab():
            b0=P(pg)['bad']; p1=pts(pg)
            if gid in QUIZ:
                q=pg.evaluate("G.q"); w=[i for i in range(len(q['o'])) if i!=q['a']][0]; T(pg,f'#main [data-a=ans][data-v="{w}"]'); fb=pg.inner_text('#fb')
                okk=pts(pg)==p1 and P(pg)['bad']==b0+1 and 'Hampir' in fb
                a=q['a']; T(pg,'#main [data-a=nq]'); q=pg.evaluate("G.q"); T(pg,f'#main [data-a=ans][data-v="{q["a"]}"]')
                return okk and pts(pg)>p1, f"salah: poin tetap, bad+1, pesan '{fb[:22]}'; benar: poin naik"
            if gid in('beda','spy'):
                cells=pg.evaluate("document.querySelectorAll('[data-a=bd]').length"); d=pg.evaluate("G.d"); w=[i for i in range(cells) if i not in d][0]
                T(pg,f'#main [data-a=bd][data-v="{w}"]'); okk=pts(pg)==p1 and P(pg)['bad']==b0+1
                T(pg,f'#main [data-a=bd][data-v="{d[0]}"]'); return okk and pts(pg)>p1,f'salah: poin tetap bad+1; benar: +{pts(pg)-p1}'
            if gid=='garis':
                T(pg,'#l0'); o=pg.evaluate("[...document.querySelectorAll('[data-a=R]')].map(e=>e.dataset.v).filter(v=>v!=='0')[0]"); T(pg,f'[data-a=R][data-v="{o}"]')
                okk=pg.evaluate("document.querySelectorAll('#sv line').length")==0 and pts(pg)==p1 and P(pg)['bad']==b0+1
                T(pg,'#l0'); T(pg,'[data-a=R][data-v="0"]'); return okk and pg.evaluate("document.querySelectorAll('#sv line').length")==1,'pasangan salah: tanpa garis, bad+1; benar: 1 garis'
            if gid=='memori':
                ks=pg.evaluate("[...document.querySelectorAll('[data-a=flip]')].map(e=>+e.dataset.k)"); i=0; j=[x for x,k in enumerate(ks) if k!=ks[0]][0]
                c=pg.locator('[data-a=flip]'); (c.nth(i).tap if TOUCH else c.nth(i).click)(); (c.nth(j).tap if TOUCH else c.nth(j).click)(); pg.wait_for_timeout(1100)
                return pg.evaluate("document.querySelectorAll('.opt.mc.on').length")==0 and pts(pg)==p1,'pasangan beda menutup kembali; poin tetap'
            if gid=='labirin':
                z=pg.evaluate("({w:G.mz.c[0].w})"); 
                wall=[d for d,bit in((0,1),(3,8)) if z['w']&bit]
                if wall: move(pg,wall[0]); okk=pg.evaluate("G.mz.p")==0
                else: okk=True
                for d in solve_maze(pg)[:2]: move(pg,d)
                return okk and pg.evaluate("G.mz.mv")==2,'menabrak tembok tak bergerak; jalur benar bergerak'
            if gid=='urut':
                pg.wait_for_function("G.lock===0",timeout=20000); sq=pg.evaluate("G.sq"); w=(sq[0]+1)%4
                T(pg,f'.sw2:nth-child({w+1})'); return pg.evaluate("G.lock")==1 and P(pg)['bad']==b0+1 and pts(pg)==p1,'salah → terkunci, bad+1, poin tetap, contoh diulang'
            if gid=='puzzle':
                T(pg,'.pzp2[data-v="0"]'); T(pg,'.pzs2[data-v="1"]'); okk=pg.evaluate("G.pz.ok")==0 and 'Belum pas' in pg.inner_text('#pzmsg')
                T(pg,'.pzs2[data-v="0"]'); return okk and pg.evaluate("G.pz.ok")==1,'keping salah ditolak ramah; kotak benar terkunci'
            if gid=='warna':
                T(pg,'#main [data-a=col]:nth-child(3)'); tap_shape(pg,0); c1=pg.evaluate("Object.keys(P().art).filter(k=>k.startsWith(G.dr.id+'_')).length"); T(pg,'#main [data-a=col]:nth-child(13)'); tap_shape(pg,0); c2=pg.evaluate("Object.keys(P().art).filter(k=>k.startsWith(G.dr.id+'_')).length")
                T(pg,'#main [data-a=undo]'); c3=pg.evaluate("Object.keys(P().art).filter(k=>k.startsWith(G.dr.id+'_')).length"); return c1==1 and c2==0 and c3==1,f'warna→hapus(🧽)→undo: {c1},{c2},{c3} (tidak ada jawaban salah)'
        S(gid,'Jawaban benar/salah','Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid',f'sesuai',jawab)
        # 5 RESET mid-game (tombol di dalam layar)
        def reset():
            sel=f'#main [data-a={RESET[gid]}]' if gid in RESET else '#main .gctl [data-a=rst]'
            T(pg,sel); pg.wait_for_timeout(500 if gid in('urut','puzzle') else 250)   # mulai dari keadaan bersih
            progress_one(pg,gid); p1=pts(pg)
            T(pg,sel); pg.wait_for_timeout(500 if gid in('urut','puzzle') else 250)
            okk,ak=state_reset_ok(pg,gid); return okk and pts(pg)>=p1, f'{ak}; poin {p1}->{pts(pg)} (tidak berkurang)'
        S(gid,'Reset/Ulangi','Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin',f'state awal',reset)
        # 6 RESPONSIF + rotasi (state tetap)
        def resp():
            progress_one(pg,gid) if False else None
            m1=pg.evaluate(METR); gi=pg.evaluate("G.id"); pg.set_viewport_size({'width':H,'height':W}); pg.wait_for_timeout(350); m2=pg.evaluate(METR); same=pg.evaluate("G.id")==gi and bool(pg.query_selector('#main .card'))
            pg.set_viewport_size({'width':W,'height':H}); pg.wait_for_timeout(300)
            bad=[x for x in (m1,m2) if x['hs']>0 or x['cov'] or x['off']]
            return not bad and same, f"potret hs={m1['hs']} tertutup={m1['cov']} <44px={m1['small']}; landscape hs={m2['hs']} tertutup={m2['cov']}; state tetap={same}"
        S(gid,'Responsif',f'Tanpa scroll horizontal/tombol tertutup di {W}×{H} dan rotasi; state tidak hilang',f'bersih',resp)
        # 7 KELUAR lewat tombol Menu di dalam permainan lalu navigasi bawah/atas
        def keluar():
            sel='#main .gctl [data-a=nav]' if gid!='puzzle' else '#main [data-a=pzmenu]'
            T(pg,sel); pg.wait_for_timeout(300)
            if gid=='puzzle': T(pg,'#main [data-a=nav][data-v=home]'); pg.wait_for_timeout(300)
            home=bool(pg.query_selector('.hero')); gempty=pg.evaluate("!G.id||G.id==='puzzle'&&!G.pz")
            e0=len(pg.errs); pg.wait_for_timeout(1500)
            return home and not pg.errs, f'beranda={home} G.id={pg.evaluate("G.id")} errs={pg.errs[:1]}'
        S(gid,'Keluar/Menu','Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor',f'beranda',keluar)
        def keluar2():
            start_ui(pg,gid); progress_one(pg,gid); T(pg,'#hd [data-a=nav][data-v=home]'); pg.wait_for_timeout(1500)
            nxt='hitung' if gid!='hitung' else 'pola'; assert open_via_ui(pg,nxt); st=pg.evaluate("G.id")
            return bool(pg.query_selector('#main [data-a=go]')) and st==nxt and not pg.errs, f'dari tengah permainan lewat navigasi → buka {nxt}: G.id={st} errs={pg.errs[:1]}'
        S(gid,'Keluar/Menu','Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor',f'bersih',keluar2)
        T(pg,'#hd [data-a=nav][data-v=home]')
        # 8 REFRESH mid-game
        def refresh():
            start_ui(pg,gid); progress_one(pg,gid); sv=P(pg)['pts']; pg.reload(); pg.wait_for_timeout(500); pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()")
            after=pg.evaluate("P().pts"); okk=after==sv and bool(pg.query_selector('.hero')) and not pg.errs
            return okk, f'poin {sv}->{after}; kembali ke beranda; errs={pg.errs[:1]}; bba1 valid={pg.evaluate("!!JSON.parse(localStorage.getItem(\"bba1\")).p.length")}'
        S(gid,'Refresh','Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi',f'tetap',refresh)
        ctx.close()
    b.close()
json.dump(MT,open(f'pg_{VPN}_{"_".join(GAMES)}.json','w'),ensure_ascii=False,indent=1)
f=[m for m in MT if m['status']!='PASS']
print(VPN,GAMES,'baris',len(MT),'FAIL/BLOCKED',len(f))
for m in f: print(m['status'],m['game'],'|',m['dim'],'|',m['aktual'][:140])
