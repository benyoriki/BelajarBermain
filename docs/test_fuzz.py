import sys; sys.path.insert(0,'/home/claude/work/audit/tests')
from common import *
RF=[]
def r(g,s,h,a,ok): RF.append(dict(game=g,skenario=s,harapan=h,aktual=str(a),status='PASS' if ok else 'FAIL'))
Q="""(()=>{const bad=[],B=BBA;const T=(x)=>/undefined|NaN|Infinity|miss|null/.test(x);
const cntI=h=>(h.match(/<i class="ai"/g)||[]).length;
const out={};
['pola','hitung','huruf','tambah','ganjil','bayangan'].forEach(g=>{let n=0,e=[];for(let a=0;a<=5;a++)for(let k=0;k<150;k++){const q=GEN[g](a);n++;
 const ids=new Set(q.o);if(q.o.length<2)e.push('opsi<2');if(ids.size!==q.o.length)e.push('opsi ganda');if(!(q.a>=0&&q.a<q.o.length))e.push('indeks jawaban');
 if(T(q.q)||q.o.some(o=>T(String(o)))||T(q.w||''))e.push('teks cacat:'+(q.q+q.o.join('')).slice(0,60));
 if(g==='hitung'){const c=cntI(q.q);if(c!==+q.o[q.a])e.push('jumlah gambar '+c+' != jawaban '+q.o[q.a])}
 if(g==='tambah'){const m=q.q.match(/diambil (\\d+) → (\\d+) − (\\d+)/);if(m){const T0=cntI(q.q);if(T0!==+m[2]||+m[2]-+m[3]!==+q.o[q.a])e.push('pengurangan salah '+q.w)}else{const parts=q.q.split('➕');const a1=cntI(parts[0]),b1=cntI(parts[1]||'');if(a1+b1!==+q.o[q.a])e.push('penjumlahan salah '+a1+'+'+b1+'!='+q.o[q.a])}}
 if(g==='tambah'&&(+q.o[q.a]<0||q.o.some(x=>+x<0)))e.push('negatif');
 if(g==='ganjil'&&q.o.length<3)e.push('ganjil <3');
}out[g]={n,err:[...new Set(e)].slice(0,3)}});return out})()"""
with sync_playwright() as p:
    b=p.chromium.launch(); ctx,pg=mkpage(b); mkprofile(pg); pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()")
    warn=[]; pg.on('console',lambda m: warn.append(m.text) if 'Aset hilang' in m.text or 'Bank soal' in m.text else None)
    res=pg.evaluate(Q)
    for g,v in res.items(): r(g,'Fuzz 900 soal (semua tingkat)','tanpa duplikat opsi, indeks valid, jumlah gambar = jawaban, tanpa NaN/undefined/negatif',f"n={v['n']} err={v['err']}",not v['err'])
    # Bank validasi
    v=pg.evaluate("BBA.validate()"); r('bank','Validasi bank soal','0 galat',f"ok={v['ok']} err={len(v['errors'])} counts={v['counts']}",v['ok'])
    # aset: semua id yang dirujuk games2/script ada
    src=open('/home/claude/work/audit/proj/games2.js').read()
    import re
    ids=set(re.findall(r"\['([a-z-]+)'\s*,\s*'([a-z-]*)'\]",src))
    flat=set(x for t in ids for x in t if x and '-' in x or x in ('apel','bola','ceri','gajah','harimau','ikan','jeruk','kepik','lebah','mangga','nanas','panda','rusa','semut','toga','monyet','pisang','penguin','katak','belalang','kelinci','pohon','matahari','melon','stroberi','ikan-biru','kupu-kupu','semangka','lingkaran','segitiga','persegi','bintang','hati','anggur','kiwi','blueberry','dino-biru','dino-merah','singa','beruang'))
    miss=pg.evaluate("ids=>ids.filter(i=>!BBA.ASSETS[i])",sorted(flat))
    r('aset','Rujukan id aset di games2.js','semua ada di katalog',f'{len(flat)} id diperiksa, hilang={miss}',not miss)
    # semua sel sprite yang dipakai tidak kosong
    from PIL import Image
    im=Image.open('/home/claude/work/audit/proj/aset.webp').convert('RGBA'); W,H=im.size
    emp=[]
    for a in pg.evaluate("Object.values(BBA.ASSETS)"):
        c=im.crop((a['c']*80,a['r']*80,a['c']*80+80,a['r']*80+80)); ext=c.getchannel('A').getextrema()
        if a['c']*80+80>W or a['r']*80+80>H or ext[1]==0: emp.append(a['id'])
    r('aset','Sel sprite aset.webp tiap id katalog','ukuran %dx%d, tidak ada sel kosong/di luar'%(W,H),f'{len(pg.evaluate("Object.keys(BBA.ASSETS)"))} aset, kosong={emp}',not emp)
    # Garis: 80 papan di semua tingkat
    pg.evaluate("ACT.play('garis')"); pg.evaluate("document.querySelector('#main [data-a=go]').click()")
    res=pg.evaluate("""(()=>{const err=[];const types={};for(let adj of [-1,0,1])for(let age of [0,1,2]){P().age=age;P().adj=adj;for(let k=0;k<12;k++){lines();const L=[...document.querySelectorAll('[data-a=L]')],Rr=[...document.querySelectorAll('[data-a=R]')];
 const t=document.querySelector('.tgt').textContent;types[t.split(':')[1].trim().slice(0,22)]=1;
 const vs=Rr.map(e=>e.dataset.v);if(L.some(l=>vs.filter(v=>v===l.dataset.v).length!==1))err.push('kiri tanpa pasangan unik');
 if(new Set(L.map(e=>e.innerHTML)).size!==L.length)err.push('kiri ganda: '+t.slice(0,25));
 const real=Rr.filter(e=>e.dataset.v!=='x');if(new Set(real.map(e=>e.innerHTML)).size!==real.length)err.push('kanan ganda: '+t.slice(0,25));
 if(/miss|undefined|NaN/.test(document.querySelector('#box').innerHTML))err.push('aset hilang: '+t.slice(0,25));
 if(L.length<3)err.push('terlalu sedikit pasangan')}}return {err:[...new Set(err)].slice(0,4),types:Object.keys(types)}})()""")
    r('garis','Fuzz 108 papan (3 usia × 3 tingkat × 12)','tiap kiri tepat 1 pasangan, tanpa duplikat ambigu, tanpa aset hilang',f"jenis={len(res['types'])} err={res['err']}",not res['err'])
    # beda & spy
    for gid in ['beda','spy']:
        pg.evaluate(f"ACT.nav('home');ACT.play('{gid}')"); pg.evaluate("document.querySelector('#main [data-a=go]').click()")
        res=pg.evaluate("""(()=>{const err=[];for(let age of [0,1,2])for(let adj of [-1,0,1]){P().age=age;P().adj=adj;for(let k=0;k<8;k++){findR();const cells=[...document.querySelectorAll('[data-a=bd]')],d=G.d;
 if(new Set(d).size!==G.k||d.length!==G.k)err.push('target ganda');if(d.some(i=>i<0||i>=cells.length))err.push('indeks luar');
 if(G.id==='spy'){const tgt=document.querySelector('.tgt .big').innerHTML;const m=cells.filter(c=>c.innerHTML===tgt).length;if(m!==G.k)err.push('jumlah target '+m+' != '+G.k)}
 else{const A=[...document.querySelectorAll('.cell')];const diff=cells.map((c,i)=>c.innerHTML!==A[i].innerHTML?i:-1).filter(i=>i>=0);if(diff.sort().join()!==[...d].sort().join())err.push('perbedaan tidak sesuai data')}
 if(cells.length<4)err.push('sel terlalu sedikit')}}return [...new Set(err)]})()""")
        r(gid,'Fuzz 72 papan','jumlah/posisi target sesuai data, gambar A≠B tepat di target',res,not res)
    # memori
    pg.evaluate("ACT.nav('home');ACT.play('memori')"); pg.evaluate("document.querySelector('#main [data-a=go]').click()")
    res=pg.evaluate("""(()=>{const err=[];for(let age of [0,1,2])for(let adj of [-1,0,1]){P().age=age;P().adj=adj;for(let k=0;k<6;k++){mem();const c={};document.querySelectorAll('[data-a=flip]').forEach(e=>c[e.dataset.k]=(c[e.dataset.k]||0)+1);if(Object.values(c).some(v=>v!==2)||Object.keys(c).length!==G.t)err.push('pasangan tidak lengkap');if(new Set(G.e.map(x=>x)).size!==G.e.length)err.push('gambar ganda')}}return [...new Set(err)]})()""")
    r('memori','Fuzz 54 papan','tiap kartu tepat 2, gambar unik',res,not res)
    # labirin
    pg.evaluate("ACT.nav('home');ACT.play('labirin')"); pg.evaluate("document.querySelector('#main [data-a=go]').click()")
    res=pg.evaluate("""(()=>{const err=[];let n0=0;for(let age of [0,1,2])for(let adj of [-1,0,1]){P().age=age;P().adj=adj;for(let rd=0;rd<3;rd++)for(let k=0;k<5;k++){maze(rd);const z=G.mz,n=z.n,T=n*n-1,seen=new Set([0]),q=[0];while(q.length){const i=q.shift();[[0,-1,1],[1,0,2],[0,1,4],[-1,0,8]].forEach(d=>{if(z.c[i].w&d[2])return;const x=i%n+d[0],y=(i/n|0)+d[1];if(x<0||y<0||x>=n||y>=n)return;const j=y*n+x;/* simetri dinding */if(z.c[j].w&({1:4,2:8,4:1,8:2}[d[2]]))err.push('dinding tidak simetris');if(!seen.has(j)){seen.add(j);q.push(j)}})}
 if(!seen.has(T))err.push('tujuan tak terjangkau');[...z.st].forEach(s=>{if(!seen.has(s)||s===0||s===T)err.push('bintang tak valid')});n0++}}return {n0,err:[...new Set(err)]}})()""")
    r('labirin','Fuzz 135 labirin (3 babak × 9 tingkat × 5)','jalur awal→tujuan ada, dinding simetris, bintang terjangkau',res,not res['err'])
    # mewarnai: tiap gambar punya area; sample tiap 35
    res=pg.evaluate("""(()=>{const err=[];BBA.DR.forEach(d=>{if(!d.s.length)err.push(d.id+' kosong');if(d.s.length<1)err.push(d.id+' tanpa area')});return {n:BBA.DR.length,err}})()""")
    r('warna','Katalog gambar mewarnai','semua gambar punya >=1 area (bintang-laut=1, pisang=2: tipis tapi dapat diselesaikan)',res,not res['err'])
    r('umum','Peringatan konsol "Aset hilang"/"Bank soal" selama fuzz','tidak ada',warn[:3],not warn)
    r('umum','Error JS selama fuzz','tidak ada',pg.errs[:3],not pg.errs)
    ctx.close(); b.close()
json.dump(RF,open('hasil_fuzz.json','w'),ensure_ascii=False,indent=1)
for x in RF: print(x['status'],'|',x['game'],'|',x['skenario'][:42],'|',x['aktual'][:150])
