def rd(f): return open(f,encoding='utf-8').read()
def wr(f,s): open(f,'w',encoding='utf-8').write(s)
def sub(s,a,b,cnt=1):
    assert s.count(a)==cnt,(s.count(a),a[:100]); return s.replace(a,b)
s=rd('script.js')
s=sub(s,"today=()=>new Date().toISOString().slice(0,10)","ymd=d=>d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0'),today=()=>ymd(new Date())")
s=sub(s,"const DAILY=()=>IDS[Math.floor(Date.now()/864e5)%IDS.length]","const DAILY=()=>{const d=new Date();return IDS[Math.floor(Date.UTC(d.getFullYear(),d.getMonth(),d.getDate())/864e5)%IDS.length]}")
s=sub(s,"p.days[new Date(Date.now()-(6-i)*864e5).toISOString().slice(0,10)]||0","p.days[ymd(new Date(Date.now()-(6-i)*864e5))]||0")
s=sub(s,"try{S=Object.assign(S,JSON.parse(localStorage.getItem(K)))}catch(e){}",
"try{const raw=localStorage.getItem(K);if(raw){try{const o=JSON.parse(raw);if(o&&typeof o==='object'&&!Array.isArray(o))S=Object.assign(S,o)}catch(e){try{localStorage.setItem(K+'_rusak',raw)}catch(x){}}}}catch(e){}")
s=sub(s,"const save=()=>{try{localStorage.setItem(K,JSON.stringify(S))}catch(e){}};",
"let SE=0;const save=()=>{try{localStorage.setItem(K,JSON.stringify(S))}catch(e){if(!SE){SE=1;setTimeout(()=>toast('Penyimpanan penuh atau dimatikan. Progres mungkin tidak tersimpan 🙏'),0)}}};")
mig="""const fx=v=>Number.isFinite(+v)?Math.max(0,Math.floor(+v)):0,isO=o=>o&&typeof o==='object'&&!Array.isArray(o);
/* Migrasi ringan: hanya memperbaiki tipe data yang rusak/kurang. Poin, profil, foto, dan kolom tak dikenal TIDAK dihapus. */
(function(){if(!Array.isArray(S.p))S.p=[];S.p=S.p.filter(x=>isO(x)&&x.id);S.p.forEach(p=>{['pts','done','ok','bad','best','dc','played'].forEach(k=>p[k]=fx(p[k]));if(typeof p.dcDay!=='string')p.dcDay='';if(!Array.isArray(p.bd))p.bd=[];if(!Array.isArray(p.hist))p.hist=[];p.hist=p.hist.filter(h=>typeof h==='string');if(!isO(p.days))p.days={};if(!isO(p.art))p.art={};if('pz' in p&&!isO(p.pz))p.pz={};p.name=String(p.name||'Anak').slice(0,12);p.age=[0,1,2].includes(+p.age)?+p.age:1;if(!AV.includes(p.av))p.av=AV[0];p.adj=[-1,0,1].includes(+p.adj)?+p.adj:0});if(S.cur&&!S.p.some(x=>x.id===S.cur))S.cur=null})();
"""
s=sub(s,"const M=h=>{const m=$('#main')",mig+"const M=h=>{const m=$('#main')")
s=sub(s,"NEW=()=>({pts:0,done:0,ok:0,bad:0,best:0,dc:0,dcDay:'',bd:[],hist:[],days:{},art:{}})","NEW=()=>({pts:0,done:0,ok:0,bad:0,best:0,dc:0,dcDay:'',bd:[],hist:[],days:{},art:{},played:0,adj:0})")
i=s.index("function add(n,m){"); j=s.index("function hdr(){")
core='''const DAYCAP=600;   /* batas poin per hari per profil (bonus tantangan harian tidak dihitung). Mencegah tambang poin lewat Main Lagi; tidak pernah mengurangi saldo. */
const later=(f,ms)=>{const g=G;return setTimeout(()=>{if(G===g)f()},ms)};   /* timer batal otomatis jika permainan sudah ditutup/diganti */
function add(n,m,free){const p=P(),l0=lvl(p),got=free?n:Math.min(n,Math.max(0,DAYCAP-(p.days[today()]||0)));if(got<n&&!G.capT){G.capT=1;setTimeout(()=>toast('Poin hari ini sudah penuh 🌟 Tetap boleh bermain dan belajar!'),900)}if(!got){save();hdr();return 0}p.pts+=got;if(lvl(p)>l0){boom();setTimeout(()=>toast('🎉 Naik level! '+LV[lvl(p)][1]),1400)}p.days[today()]=(p.days[today()]||0)+got;if(m)p.hist=[today()+' · '+m+' +'+got,...p.hist].slice(0,15);BD.forEach(b=>{if(!p.bd.includes(b[1])&&b[2](p)){p.bd.push(b[1]);toast('🎖️ Lencana: '+b[1])}});save();toast('+'+got+' ⭐');hdr();return got}
function ok(){const p=P();p.ok++;G.st=(G.st||0)+1;p.best=Math.max(p.best,G.st);add(10);if(G.st%5===0)add(10,'5 jawaban beruntun')}
function bad(){P().bad++;G.st=0;save()}
function fin(){if(!G.id||V!=='play'||G.done)return;const p=P();G.done=1;p.done++;let g=add(20,GM[G.id][1]+' selesai'),b='';if(G.id===DAILY()&&p.dcDay!==today()){p.dcDay=today();p.dc++;g+=add(30,'Tantangan harian',1);b=' (termasuk bonus tantangan harian)'}save();boom();M(`<section class="card"><h1>🎉 Hebat!</h1><p class="big pop">⭐⭐⭐</p><p>${g?'Aktivitas selesai! +'+g+' poin'+b+'.':'Aktivitas selesai! Poin hari ini sudah penuh, tapi kamu hebat sekali 🌟'}</p><button class="cta" data-a="play" data-v="${G.id}">🔁 Main Lagi</button> <button class="ghost" data-a="nav" data-v="home">🏠 Beranda</button></section>`)}
'''
s=s[:i]+core+s[j:]
s=sub(s,"nav(v){V=v;ED=null;render()}","nav(v){G={};V=v;ED=null;render()}")
s=sub(s,"const dif=()=>Math.min(5,P().age+lvl(P())),stars","const dif=()=>Math.max(0,Math.min(5,P().age+lvl(P())+(P().adj||0))),stars")
i=s.index("function start(id){"); j=s.index("function next(){")
st='''function intro(id){const a=P().adj||0;M(`<section class="card intro"><div class="ib2">${window.GI&&GI(id)||GM[id][0]}</div><h1>${GM[id][1]}</h1><p class="lv">Tingkat ${stars()} · makin tinggi level, makin seru!</p><ol class="how">${HOW[id].map((t,i)=>`<li><b>${i+1}</b>${t}</li>`).join('')}</ol><div class="row" role="group" aria-label="Pilih tingkat kesulitan">${[[-1,'🌱 Lebih mudah'],[0,'⭐ Pas'],[1,'🚀 Lebih seru']].map(x=>`<button class="opt ${a===x[0]?'on':''}" data-a="adj" data-v="${x[0]}" aria-pressed="${a===x[0]}">${x[1]}</button>`).join('')}</div><button class="cta" data-a="go">▶ Mulai Main</button> <button class="ghost" data-a="nav" data-v="home">⬅ Kembali</button></section>`)}
function start(id){if(!P()||!GM[id])return render();G={id,i:0,n:({beda:3,spy:3}[id]||5),st:0,done:0};P().played=(P().played||0)+1;save();V='play';hdr();intro(id)}
'''
s=s[:i]+st+s[j:]
s=sub(s,"nq(){G.i++;next()},","nq(){G.i++;next()},adj(v){const id=G.id;if(!id||!P())return;P().adj=+v;save();intro(id)},srep(){if(G.id==='urut'&&!G.lock)sPlay()},")
s=sub(s,"function next(){if(G.i>=G.n)return fin();const q=G.q=GEN[G.id](dif());G.L=0;",
"function next(){if(G.i>=G.n)return fin();let q,k=0,key;G.seen=G.seen||new Set();do{q=GEN[G.id](dif());key=q.q+'|'+q.o[q.a]}while(G.seen.has(key)&&++k<15);G.seen.add(key);G.q=q;G.L=0;")
s=s.replace("setTimeout(fin,","later(fin,")
s=s.replace("setTimeout(sPlay,900)","later(sPlay,900)").replace("setTimeout(sNext,900)","later(sNext,900)")
n=s.count("bad();G.in=[];")
s=s.replace("bad();G.in=[];","bad();G.lock=1;G.in=[];"); print('wrong-lock patches',n)
i=s.index("function sPlay(){"); j=s.index("function fl(v){")
s=s[:i]+"function sPlay(){if(!$('#sm'))return;const v=G.pv=(G.pv||0)+1,g=G;G.lock=1;G.in=[];$('#sm').textContent='👀 Perhatikan...';sd();const T=(f,ms)=>setTimeout(()=>{if(G===g&&G.pv===v)f()},ms);G.sq.forEach((x,i)=>T(()=>fl(x),G.sp*(i+1)));T(()=>{const m=$('#sm');if(m){G.lock=0;m.textContent='👆 Giliranmu!'}},G.sp*G.sq.length+G.sp)}\n"+s[j:]
s=sub(s,'''aria-label="Hewan ${i+1}">${AN[i]}</button>`).join('')}</div></section>`);sNext()}''','''aria-label="Hewan ${i+1}">${AN[i]}</button>`).join('')}</div><div class="row"><button class="ghost" data-a="srep">🔁 Ulangi contoh</button></div></section>`);sNext()}''')
old='''$('#sv').insertAdjacentHTML('beforeend',`<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="#1e88ff" stroke-width="6" stroke-linecap="round"/>`);'''
s=sub(s,old,"(G.cx=G.cx||[]).push(v);redrawL();")
s=sub(s,"G.m=0;G.s=null;G.t=n;M(","G.m=0;G.s=null;G.cx=[];G.t=n;M(",1)
s=sub(s,"function dz(){",'''function redrawL(){const sv=$('#sv'),bx=$('#box');if(!sv||!bx||!G.cx)return;sv.innerHTML='';const c=bx.getBoundingClientRect();G.cx.forEach(v=>{const l=$('#l'+v),r=document.querySelector('[data-a=R][data-v="'+v+'"]');if(!l||!r)return;const a=l.getBoundingClientRect(),b=r.getBoundingClientRect();sv.insertAdjacentHTML('beforeend','<line x1="'+(a.left-c.left+a.width/2)+'" y1="'+(a.top-c.top+a.height/2)+'" x2="'+(b.left-c.left+b.width/2)+'" y2="'+(b.top-c.top+b.height/2)+'" stroke="#1e88ff" stroke-width="6" stroke-linecap="round"/>')})}
addEventListener('resize',()=>requestAnimationFrame(redrawL));addEventListener('orientationchange',()=>setTimeout(redrawL,300));
function dz(){''')
s=sub(s,"bd(v,t){if(t.disabled)return;","bd(v,t){if(t.disabled||G.f>=G.k)return;")
s=sub(s,"tambah(a){const q=pq('tambah',a),i=q.assets[0];return mk(",'''tambah(a){const q=pq('tambah',a),i=q.assets[0];if(a>=4&&q.answer>=4&&rnd(2)){const T=q.answer,y=q.b,r=q.a;return mk(`<div class="cnt">${B.imgs(i,T)}</div>diambil ${y} → ${T} − ${y} = ?`,r,[r+1,r+2,r-1,r-2].filter(v=>v>=0&&v!==r).slice(0,2),T+' − '+y+' = '+r)}return mk(''')
s=sub(s,"if('serviceWorker'in navigator)addEventListener('load',()=>navigator.serviceWorker.register('service-worker.js').catch(()=>{}));",
"if('serviceWorker'in navigator){const had=!!navigator.serviceWorker.controller;addEventListener('load',()=>navigator.serviceWorker.register('service-worker.js').catch(()=>{}));navigator.serviceWorker.addEventListener('controllerchange',()=>{if(had)toast('Versi baru sudah siap ✨ Muat ulang halaman ya!')})}")
wr('script.js',s)
g=rd('games2.js')
g=sub(g,"function pickDr(){","function pickDr(last){")
g=sub(g,"w=so.slice(st,st+12).filter(d=>!G.dr||d.id!==G.dr.id);return pk(w)}","w=so.slice(st,st+12).filter(d=>d.id!==last);return pk(w.length?w:so)}")
g=sub(g,"window.color=function(){G.dr=null;G.dr=pickDr();G.us=[];G.re=[];G.c=PAL12[0];const dr=G.dr,a=P().art;",
"window.color=function(keep){const last=G.dr&&G.dr.id;G.dr=keep||pickDr(last);G.us=[];G.re=[];G.c=PAL12[0];const dr=G.dr,a=P().art;Object.keys(a).forEach(k=>k.startsWith(dr.id+'_')&&delete a[k]);save();")
g=sub(g,"rs(){const a=P().art;Object.keys(a).forEach(k=>k.startsWith(G.dr.id+'_')&&delete a[k]);save();color()},","rs(){color(G.dr)},")
g=sub(g,"G.pr=p.slice(0,n);G.m=0;G.s=null;G.t=n;","G.pr=p.slice(0,n);G.m=0;G.s=null;G.cx=[];G.t=n;")
g=sub(g,"setTimeout(()=>G.rd<2?maze(G.rd+1):fin(),700)","later(()=>G.rd<2?maze(G.rd+1):fin(),700)")
wr('games2.js',g)
z=rd('puzzle.js')
z=sub(z,'''M('<section class="card"><p class="tgt">Menyiapkan puzzle…</p></section>');await ready();''','''M('<section class="card"><p class="tgt">Menyiapkan puzzle…</p></section>');const g0=G;await ready();if(G!==g0)return;''')
z=sub(z,"setTimeout(()=>{if(!G.done){fin();","later(()=>{if(first&&!G.done){fin();")
wr('puzzle.js',z)
print('patched OK')
