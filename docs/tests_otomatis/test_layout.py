import sys,collections; sys.path.insert(0,'/home/claude/work/audit/tests')
from common import *
VP=[('HP kecil',320,568),('HP umum',360,800),('HP besar',430,932),('Tablet',768,1024),('Laptop',1366,768),('Desktop',1920,1080)]
GAMES=['warna','garis','pola','beda','hitung','spy','huruf','memori','bayangan','tambah','ganjil','labirin','urut','puzzle']
JS="""(()=>{const de=document.documentElement,vis=e=>{const r=e.getBoundingClientRect(),c=getComputedStyle(e);return r.width>0&&r.height>0&&c.visibility!=='hidden'&&c.display!=='none'};
const els=[...document.querySelectorAll('#main button,#main a[href],#main input:not([type=hidden]),#main [role=button]')].filter(vis);
const small=[...new Set(els.filter(e=>{const r=e.getBoundingClientRect();return Math.min(r.width,r.height)<44}).map(e=>(e.dataset.a||e.tagName)+' '+Math.round(e.getBoundingClientRect().width)+'x'+Math.round(e.getBoundingClientRect().height)))];
const off=els.filter(e=>{const r=e.getBoundingClientRect();return r.right>innerWidth+1||r.left<-1}).map(e=>e.dataset.a||e.tagName);
const hs=de.scrollWidth-de.clientWidth;
const clipped=[...document.querySelectorAll('#main *')].filter(e=>{const c=getComputedStyle(e);return (c.overflow==='hidden'||c.textOverflow==='ellipsis')&&e.clientWidth>0&&e.scrollWidth>e.clientWidth+2&&!e.matches('svg,svg *,.ai,.pzb,.pzw,.mz,.pzp,.pzs2,.pzp2')}).map(e=>e.className||e.tagName).slice(0,3);
const cov=[];els.slice(0,70).forEach(e=>{e.scrollIntoView({block:'center'});const r=e.getBoundingClientRect(),x=r.left+r.width/2,y=r.top+r.height/2;if(x<0||y<0||x>innerWidth||y>innerHeight)return;const t=document.elementFromPoint(x,y);if(t&&!(e.contains(t)||t.contains(e)))cov.push((e.dataset.a||e.tagName)+' ditutup '+(t.id||t.className||t.tagName))});
window.scrollTo(0,document.documentElement.scrollHeight);const last=els[els.length-1];let lastcov='';if(last){const r=last.getBoundingClientRect(),x=r.left+r.width/2,y=Math.min(r.top+r.height/2,innerHeight-1),t=document.elementFromPoint(x,y);if(r.top<innerHeight&&t&&!(last.contains(t)||t.contains(last)))lastcov='tombol terakhir ditutup '+(t.id||t.className||t.tagName)}
window.scrollTo(0,0);
return {hs,small,off,clipped,cov:[...new Set(cov)].slice(0,4),lastcov,n:els.length,imgbad:[...document.images].filter(i=>i.complete&&i.naturalWidth===0).length}})()"""
RES=[]
def metr(pg,vp,scr,gid):
    m=pg.evaluate(JS); m.update(vp=vp,scr=scr,game=gid); RES.append(m)
with sync_playwright() as p:
    b=p.chromium.launch()
    for name,w,h in VP:
        ctx,pg=mkpage(b,w,h,touch=(w<800)); mkprofile(pg)
        pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()")
        metr(pg,name,'beranda','-')
        for gid in GAMES:
            open_game(pg,gid); metr(pg,name,'intro',gid)
            go(pg)
            if gid=='puzzle':
                metr(pg,name,'menu',gid); pg.click('[data-a=pzgo]'); pg.wait_for_selector('#pzb',timeout=6000); pg.wait_for_timeout(200)
            if gid=='urut': pg.wait_for_timeout(200)
            metr(pg,name,'main',gid)
            if w in (320,) and gid in('garis','memori','labirin','puzzle','warna','hitung','beda'): pg.screenshot(path=f'/home/claude/work/audit/tests/shot_{w}_{gid}.png')
            if w==1920 and gid in('garis','memori','labirin','puzzle','hitung'): pg.screenshot(path=f'/home/claude/work/audit/tests/shot_{w}_{gid}.png')
            pg.evaluate("ACT.nav('home')")
        # rotasi: landscape HP
        if w==360:
            pg.set_viewport_size({'width':800,'height':360}); pg.wait_for_timeout(200)
            for gid in ['garis','labirin','puzzle','memori']:
                open_game(pg,gid); go(pg)
                if gid=='puzzle': pg.click('[data-a=pzgo]'); pg.wait_for_selector('#pzb',timeout=6000)
                metr(pg,'HP landscape 800x360','main',gid); pg.evaluate("ACT.nav('home')")
        ctx.close()
    b.close()
json.dump(RES,open('/home/claude/work/audit/tests/hasil_layout.json','w'),ensure_ascii=False)
agg=collections.defaultdict(lambda:collections.defaultdict(set))
for m in RES:
    k=(m['vp'])
    if m['hs']>0: agg['SCROLL HORIZONTAL'][k].add(f"{m['game']}/{m['scr']}(+{m['hs']}px)")
    if m['off']: agg['ELEMEN KELUAR LAYAR'][k].add(f"{m['game']}/{m['scr']}:{','.join(set(m['off']))}")
    if m['clipped']: agg['TEKS TERPOTONG'][k].add(f"{m['game']}/{m['scr']}:{m['clipped'][0]}")
    if m['cov'] or m['lastcov']: agg['TOMBOL TERTUTUP'][k].add(f"{m['game']}/{m['scr']}:{(m['cov'] or [m['lastcov']])[0]}")
    if m['imgbad']: agg['GAMBAR GAGAL'][k].add(f"{m['game']}/{m['scr']}")
for t,d in agg.items():
    print('##',t)
    for k,v in d.items(): print('  ',k,':',sorted(v)[:8])
sm=collections.Counter()
for m in RES:
    if m['vp'] in('HP kecil','HP umum') and m['scr']=='main':
        for s in m['small']: sm[(m['game'],s)]+=1
print('## TARGET SENTUH <44px (HP, layar permainan):',sorted(sm)[:25])
print('total evaluasi',len(RES))
