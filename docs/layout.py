from h import *
import json,sys
VPS={'hp320':(320,568),'hp360':(360,740),'hp390':(390,844),'hp430':(430,932),'tab768':(768,1024),'pc1366':(1366,768),'tv720':(1280,720),'tv1080':(1920,1080),'land740':(740,360),'land844':(844,390)}
GAMES=['warna','garis','pola','beda','hitung','spy','huruf','memori','bayangan','tambah','ganjil','labirin','urut','puzzle']
M="""(()=>{const W=innerWidth,H=innerHeight,out=[];
const sc=el=>{for(let e=el.parentElement;e&&e!==document.body;e=e.parentElement){const o=getComputedStyle(e).overflowX;if((o==='auto'||o==='scroll')&&e.scrollWidth>e.clientWidth+1)return true}return false};
if(document.documentElement.scrollWidth>W+1)out.push('hscroll '+document.documentElement.scrollWidth+'>'+W);
const els=[...document.querySelectorAll('#main button,#main a,#main input[type=search],header button,nav button')];
els.forEach(b=>{const r=b.getBoundingClientRect();if(r.width<2||r.height<2)return;const n=(b.dataset.a||b.className||b.tagName)+'';
 if((r.left<-1||r.right>W+1)&&!sc(b))out.push('clip '+n+' L'+Math.round(r.left)+' R'+Math.round(r.right));
 if((r.width<40||r.height<40)&&!/mc|sw$|sw |wfv/.test(b.className+' ')&&!b.closest('.pzy,.wpal'))out.push('small '+n+' '+Math.round(r.width)+'x'+Math.round(r.height));});
scrollTo(0,document.body.scrollHeight);const nav=document.querySelector('nav'),nr=nav&&getComputedStyle(nav).display!=='none'&&getComputedStyle(nav).position==='fixed'?nav.getBoundingClientRect():null;
if(nr)document.querySelectorAll('#main button,#main a,#main [data-a]').forEach(b=>{const r=b.getBoundingClientRect();if(r.width>1&&r.bottom>nr.top+1&&r.top<nr.bottom&&r.right>nr.left&&r.left<nr.right)out.push('navoverlap '+(b.dataset.a||b.className))});
scrollTo(0,0);return out})()"""
def chk(pg,tag,res,extra=None):
    o=pg.evaluate(M)
    if extra: o+=extra(pg)
    res.append((tag,o))
def run(vpname):
    vw,vh=VPS[vpname];res=[]
    with sync_playwright() as p:
        b=p.chromium.launch(); touch=vw<900 or vpname.startswith('land')
        ctx,pg=page(b,vw,vh,touch=touch)
        for v in ['home','belajar','main','rank','prof']:
            pg.evaluate(f"ACT.nav('{v}')");pg.wait_for_timeout(120);chk(pg,v,res)
        for g in GAMES:
            play(pg,g);chk(pg,g+'/intro',res)
            if g=='puzzle':
                pg.evaluate("ACT.go()");pg.wait_for_timeout(150);chk(pg,'puzzle/1',res)
                pg.click('[data-a=pzcat][data-v=dinosaurus]');pg.wait_for_timeout(450);chk(pg,'puzzle/2',res)
                pg.click('[data-a=pzimg]');pg.wait_for_timeout(450);chk(pg,'puzzle/3',res)
                pg.click('[data-a=pzlv][data-v="6"]');pg.wait_for_timeout(450);chk(pg,'puzzle/4',res)
                pg.click('[data-a=pzgo]');pg.wait_for_timeout(1500);chk(pg,'puzzle/papan35',res)
            else:
                pg.evaluate("ACT.go()");pg.wait_for_timeout(250)
                if g=='warna':
                    chk(pg,'warna/katalog',res)
                    pg.click('[data-a=wcatp]');pg.wait_for_timeout(100);chk(pg,'warna/katalog+kat',res)
                    pg.click('.wcb');pg.wait_for_timeout(350);chk(pg,'warna/kanvas',res)
                elif g=='labirin':
                    def lab(pg):
                        r=pg.evaluate("(()=>{const d=document.querySelector('.dpad').getBoundingClientRect(),m=document.querySelector('#mz').getBoundingClientRect();return[Math.round(d.bottom),innerHeight,Math.round(m.width),Math.round(d.top-m.bottom)]})()")
                        return ([f'dpad_tertutup bottom{r[0]}>{r[1]}'] if r[0]>r[1]+1 and 'land' not in vpname else [])+([f'maze_kecil {r[2]}px'] if r[2]<150 else [])
                    chk(pg,'labirin/main',res,lab)
                else: chk(pg,g+'/main',res)
        errs=pg.errs; b.close()
    bad=[(t,o) for t,o in res if o]
    print(f'== {vpname} {vw}x{vh}: {len(res)} layar, {len(bad)} bermasalah, jsErr={len(errs)}')
    for t,o in bad: print('  ',t,'|',' ; '.join(sorted(set(o))[:6]))
    for e in errs[:3]: print('  ERR',e[:150])
    return res
if __name__=='__main__':
    for n in sys.argv[1:]: run(n)
