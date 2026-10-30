/* games2.js — Tahap 2: Mewarnai, Menghubungkan Garis, Labirin. Dimuat SETELAH script.js dan bank.js. */
(function(){'use strict';
if(!window.BBA||typeof ACT==='undefined')return;
const B=BBA,I=B.img,AL=Object.values(B.ASSETS).filter(a=>!['bentuk','pendidikan'].includes(a.kategori));

/* ================= MEWARNAI: 35 gambar garis, area tertutup ================= */
const E=(x,y,a,b,r=0)=>`ellipse cx="${x}" cy="${y}" rx="${a}" ry="${b}"${r?` transform="rotate(${r} ${x} ${y})"`:''}`,
C=(x,y,r)=>`circle cx="${x}" cy="${y}" r="${r}"`,Q=(x,y,w,h,r=6)=>`rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${r}"`,
Pg=p=>`polygon points="${p}"`,Pa=d=>`path d="${d}"`,
ST=(x,y,R,r,n=5)=>Pg([...Array(n*2)].map((_,i)=>{const a=Math.PI*i/n-Math.PI/2,k=i%2?r:R;return(x+k*Math.cos(a)).toFixed(0)+','+(y+k*Math.sin(a)).toFixed(0)}).join(' ')),
EY=(x,y,r=4)=>`<circle cx="${x}" cy="${y}" r="${r}" class="ey"/>`,SM=(x,y)=>`<path class="o2" d="M${x} ${y} q8 7 16 0"/>`;
const DR=[];const add=(id,nama,kat,s,d='')=>DR.push({id,nama,kat,s,d});
const quad=(id,nama,o)=>{const s=[],hx=222,hy=o.neck?26:88,hr=o.neck?22:36;
 if(o.mane)s.push(C(hx-4,hy+4,o.mane));if(o.big)s.push(E(190,88,32,44));
 s.push(o.fox?E(62,108,34,16,-25):E(72,112,14,9,-30));
 [92,120,170,198].forEach(x=>s.push(Q(x,138,20,o.neck?50:42)));s.push(E(148,122,74,42));
 if(o.neck)s.push(Q(204,28,26,100));s.push(C(hx,hy,hr));
 const e=o.ear;if(e==='pt')s.push(Pg(`${hx-24},${hy-18} ${hx-16},${hy-52} ${hx-2},${hy-30}`),Pg(`${hx+4},${hy-30} ${hx+18},${hy-52} ${hx+24},${hy-18}`));
 if(e==='rd')s.push(C(hx-20,hy-28,12),C(hx+20,hy-28,12));if(e==='lg')s.push(E(hx-10,hy-48,9,30,-8),E(hx+12,hy-48,9,30,8));
 if(e==='fl')s.push(E(hx-24,hy+6,12,26,12));
 if(o.horn)s.push(Pg(`${hx-16},${hy-28} ${hx-26},${hy-70} ${hx-4},${hy-32}`),Pg(`${hx+4},${hy-32} ${hx+22},${hy-70} ${hx+16},${hy-28}`));
 if(o.trunk)s.push(Q(hx+20,hy+8,18,56,9));if(o.sn)s.push(C(hx+24,hy+10,13));
 add(id,nama,o.kat||'Hewan darat',s,EY(hx+6,hy-8)+SM(hx+12,hy+18));};
quad('kucing','Kucing',{ear:'pt'});quad('anjing','Anjing',{ear:'fl',sn:1});quad('singa','Singa',{mane:50,ear:'rd',sn:1});quad('gajah','Gajah',{big:1,trunk:1});
quad('kelinci','Kelinci',{ear:'lg'});quad('beruang','Beruang',{ear:'rd',sn:1});quad('monyet','Monyet',{ear:'rd',sn:1,fox:1});quad('rubah','Rubah',{ear:'pt',fox:1,sn:1});
quad('rusa','Rusa',{horn:1});quad('jerapah','Jerapah',{neck:1,ear:'pt'});
const L=(k)=>'Hewan laut';
add('ikan','Ikan',L(),[Pg('65,100 20,55 20,145'),Pg('120,58 150,22 185,60'),E(140,100,75,45),E(150,150,24,12,-20)],EY(190,90,5)+SM(200,112));
add('paus','Paus',L(),[Pg('50,105 10,58 30,118'),E(140,112,100,55),E(120,150,40,14,15),C(180,40,9),C(200,28,7)],EY(205,100,5)+SM(190,125));
add('penyu','Penyu',L(),[E(100,152,22,13,20),E(200,152,22,13,-20),E(95,72,22,13,-20),E(205,72,22,13,20),E(150,110,72,50),C(232,104,25),Pg('78,108 100,120 78,128')],EY(240,98,4)+SM(228,116));
add('bintang-laut','Bintang Laut',L(),[ST(150,105,95,42)],EY(135,95,5)+EY(165,95,5)+SM(142,115));
add('kepiting','Kepiting',L(),[Q(60,35,10,45,5),Q(230,35,10,45,5),C(65,38,28),C(235,38,28),E(60,140,26,10,-25),E(240,140,26,10,25),E(150,115,72,42),C(125,70,12),C(175,70,12)],EY(125,70,5)+EY(175,70,5)+SM(142,125));
add('burung-hantu','Burung Hantu','Burung',[Q(70,70,18,90,9),Q(212,70,18,90,9),Pg('100,50 108,12 132,46'),Pg('168,46 192,12 200,50'),E(150,110,62,78),C(125,85,23),C(175,85,23),Pg('142,102 158,102 150,122'),E(125,190,18,8),E(175,190,18,8)],EY(125,85,9)+EY(175,85,9));
add('bebek','Bebek','Burung',[Pg('62,115 20,90 70,140'),E(140,130,75,48),E(135,130,40,22),C(215,72,34),E(256,80,24,10),Q(120,175,10,18,4),Q(160,175,10,18,4)],EY(222,62,5));
add('burung','Burung Kecil','Burung',[Pg('75,100 20,70 25,130'),E(140,110,62,46),E(130,108,34,22,-15),C(205,78,30),Pg('232,72 262,82 232,92'),Q(125,150,8,34,3),Q(155,150,8,34,3)],EY(212,70,5));
const dn=(id,nama,s,d)=>add(id,nama,'Dinosaurus',s,d);
dn('dino','Dino Ramah',[Pg('85,105 15,150 95,135'),Pg('120,70 138,40 156,70'),Pg('155,66 172,36 190,68'),Q(100,138,24,46),Q(170,138,24,46),E(145,115,72,46),C(222,68,34),Q(196,86,36,40),Pg('210,48 224,22 236,48')],EY(230,60,5)+SM(222,80));
dn('brachiosaurus','Brakiosaurus',[Pg('70,120 15,165 80,150'),Q(75,140,24,46),Q(150,140,24,46),E(115,125,72,40),Q(170,18,26,115,12),E(188,18,30,17)],EY(198,14,4)+SM(184,22));
dn('triceratops','Triceratops',[Pg('62,125 12,160 70,150'),Q(85,148,26,40),Q(160,148,26,40),E(125,125,76,44),C(205,92,48),E(238,112,30,22),Pg('222,58 232,24 240,60'),Pg('196,52 190,20 214,50'),Pg('252,100 276,88 262,112')],EY(228,98,5));
dn('stegosaurus','Stegosaurus',[Pg('75,125 12,115 14,150'),Q(90,148,26,38),Q(185,148,26,38),Pg('100,95 120,52 140,92'),Pg('135,88 155,44 175,86'),Pg('170,92 190,52 208,100'),E(150,130,85,40),E(240,138,26,16)],EY(246,132,4)+SM(238,146));
add('apel','Apel','Buah',[Q(146,35,8,28,3),E(180,45,28,13,-25),C(150,115,68)],'<path class="o2" d="M150 62 q-6 -10 0 -20"/>');
add('pisang','Pisang','Buah',[Pa('M45 55 Q80 190 255 150 Q265 128 242 128 Q130 150 78 40Z'),Q(36,30,22,30,8)],'');
add('semangka','Semangka','Buah',[Pa('M35 80 A115 115 0 0 0 265 80Z'),Pa('M55 80 A95 95 0 0 0 245 80Z'),E(110,115,6,10),E(150,135,6,10),E(190,115,6,10)],'');
add('nanas','Nanas','Buah',[Pg('150,5 130,50 150,50'),Pg('150,5 170,50 150,50'),Pg('112,20 135,52 108,56'),Pg('188,20 165,52 192,56'),E(150,125,52,68)],'<path class="o2" d="M115 90 l70 70 M185 90 l-70 70"/>');
add('mobil','Mobil','Kendaraan',[Q(35,105,230,50,18),Pa('M78 105 L108 58 L200 58 L232 105Z'),Pg('92,100 114,66 148,66 148,100'),Pg('156,66 196,66 216,100 156,100'),C(85,158,26),C(215,158,26),C(85,158,10),C(215,158,10)]);
add('kapal','Kapal','Kendaraan',[Pg('25,118 275,118 238,172 62,172'),Q(105,72,92,46,6),Q(132,36,38,36,5),C(128,95,10),C(150,95,10),C(172,95,10),Pg('220,118 220,60 262,118')]);
add('pesawat','Pesawat','Kendaraan',[Pg('130,100 190,100 150,172 118,172'),Pg('130,100 190,100 150,28 118,28'),Pg('50,98 22,48 78,90'),E(150,100,112,26),C(205,98,8),C(175,98,8),C(145,98,8)]);
add('rumah','Rumah','Benda',[Q(70,95,160,92,4),Pg('48,100 150,28 252,100'),Q(130,130,40,57,4),Q(85,112,30,30,3),Q(185,112,30,30,3)]);
add('pohon','Pohon','Alam',[Q(130,105,40,88,6),C(150,62,56),C(100,100,38),C(200,100,38)]);
add('bunga','Bunga','Alam',[Q(145,100,10,92,4),E(115,150,28,11,-30),E(185,135,28,11,30),C(150,45,22),C(190,70,22),C(110,70,22),C(176,108,22),C(124,108,22),C(150,78,22)]);
add('matahari','Matahari','Alam',[...Array(8)].map((_,i)=>{const a=i*Math.PI/4,c=Math.cos(a),s=Math.sin(a);return Pg(`${150+60*c-12*s|0},${100+60*s+12*c|0} ${150+98*c|0},${100+98*s|0} ${150+60*c+12*s|0},${100+60*s-12*c|0}`)}).concat([C(150,100,52)]),EY(133,92,5)+EY(167,92,5)+SM(142,115));
const band=(r1,r2)=>Pa(`M${150-r2} 170 A${r2} ${r2} 0 0 1 ${150+r2} 170 L${150+r1} 170 A${r1} ${r1} 0 0 0 ${150-r1} 170Z`);
add('pelangi','Pelangi','Alam',[band(105,125),band(85,105),band(65,85),band(45,65),C(40,170,26),C(260,170,26)]);
add('awan-hujan','Awan Hujan','Alam',[C(110,70,40),C(160,55,48),C(205,78,34),Q(80,75,150,40,18),E(100,150,8,16),E(150,165,8,16),E(200,150,8,16)]);
add('robot','Robot Bentuk','Bentuk sederhana',[Q(145,6,10,24,4),C(150,12,10),Q(100,30,100,60,12),Q(85,95,130,70,10),Q(55,100,24,56,10),Q(221,100,24,56,10),Q(105,168,36,28,6),Q(159,168,36,28,6),C(128,58,13),C(172,58,13),Pg('135,125 165,125 150,148')],'');
B.DR=DR;const cp=Object.assign;
const PAL12=['#ff5252','#ff9800','#ffd600','#8bc34a','#2e9e4f','#26c6da','#2f9bff','#3f51b5','#9c27b0','#ff80ab','#8d6e63','#212121'];
const cnt=()=>Object.keys(P().art).filter(k=>k.startsWith(G.dr.id+'_')).length;
const upd=()=>{const f=$('#fb');if(f)f.textContent='Sudah '+cnt()+' dari '+G.dr.s.length+' bagian diwarnai 🎨'};
function pickDr(last){const so=[...DR].sort((a,b)=>a.s.length-b.s.length),D=dif(),st=Math.round(D/5*(so.length-12)),w=so.slice(st,st+12).filter(d=>d.id!==last);return pk(w.length?w:so)}
window.color=function(keep){const last=G.dr&&G.dr.id;G.dr=keep||pickDr(last);G.us=[];G.re=[];G.c=PAL12[0];const dr=G.dr,a=P().art;Object.keys(a).forEach(k=>k.startsWith(dr.id+'_')&&delete a[k]);save();
 M(`<section class="card">${gh(1)}<p class="tgt">${dr.nama} · ${dr.kat} · ${dr.s.length} bagian</p><div class="row pal">${PAL12.map((c,i)=>`<button class="sw ${i?'':'on'}" data-a="col" data-v="${c}" style="background:${c}" aria-label="Warna ${i+1}"></button>`).join('')}<button class="sw" data-a="col" data-v="#ffffff" style="background:#fff" aria-label="Hapus warna">🧽</button></div><svg class="cv" viewBox="0 0 300 200" role="img" aria-label="Gambar ${dr.nama} untuk diwarnai">${dr.s.map((s,i)=>`<${s} tabindex="0" data-a="fill" data-v="${i}" class="f" style="fill:${a[dr.id+'_'+i]||'#fff'}"/>`).join('')}${dr.d}</svg><p id="fb" class="tgt"></p><div class="row"><button class="ghost" data-a="undo">↩ Undo</button><button class="ghost" data-a="redo">↪ Redo</button><button class="ghost" data-a="rs">♻ Reset</button><button class="ghost" data-a="cnext">➡ Gambar lain</button><button class="cta" data-a="cdone">✅ Selesai</button></div></section>`);upd()};
const setF=(v,c)=>{const t=document.querySelector('.cv [data-v="'+v+'"]'),k=G.dr.id+'_'+v,a=P().art;if(t)t.style.fill=c;if(c==='#ffffff')delete a[k];else a[k]=c;save();upd()};
cp(ACT,{
fill(v){const k=G.dr.id+'_'+v,old=P().art[k]||'#ffffff';if(old===G.c)return;setF(v,G.c);G.us.push([v,old,G.c]);G.re=[]},
undo(){const u=G.us.pop();if(!u)return toast('Belum ada yang dibatalkan');setF(u[0],u[1]);G.re.push(u)},
redo(){const u=G.re.pop();if(!u)return toast('Tidak ada yang diulang');setF(u[0],u[2]);G.us.push(u)},
rs(){color(G.dr)},
cnext(){color()},
cdone(){const need=Math.ceil(G.dr.s.length*[.4,.5,.6,.7,.8,.9][dif()]);if(cnt()<need)return toast('Warnai minimal '+need+' bagian 🎨');fin()}});

/* ================= MENGHUBUNGKAN GARIS: 7 jenis, tak terbatas kombinasi, tap atau seret ================= */
const tx=t=>`<b class="tl">${t}</b>`,sm=shuf;
const LH=[['A','apel'],['B','bola'],['C','ceri'],['D','dino-biru'],['G','gajah'],['H','harimau'],['I','ikan-biru'],['J','jeruk'],['K','kepik'],['L','lebah'],['M','mangga'],['N','nanas'],['P','panda'],['R','rusa'],['S','semut'],['T','toga']];
const WN=[['apel','Merah','#e53935'],['pisang','Kuning','#fdd835'],['jeruk','Oranye','#fb8c00'],['anggur','Ungu','#8e24aa'],['kiwi','Hijau','#43a047'],['blueberry','Biru','#1e88e5']];
const TY={
 nama:()=>['Gambar dengan namanya',sm(AL).slice(0,9).map(a=>[I(a.id),tx(a.nama)])],
 bayangan:()=>['Gambar dengan bayangannya',sm(AL).slice(0,9).map(a=>[I(a.id),`<i class="sh">${I(a.id)}</i>`])],
 huruf:()=>['Huruf dengan gambar yang diawali huruf itu',sm(LH).slice(0,9).map(x=>[tx(x[0]),I(x[1])])],
 angka:()=>['Angka dengan jumlah gambarnya',sm([1,2,3,4,5,6,7,8,9]).slice(0,9).map(k=>[tx(k),`<span class="cnt mini">${B.imgs(pk(AL).id,k)}</span>`])],
 warna:()=>['Buah dengan warnanya',sm(WN).map(x=>[I(x[0]),`<i class="swb" style="background:${x[2]}"></i>${tx(x[1])}`])],
 bentuk:()=>['Bentuk dengan namanya',sm([['lingkaran','Lingkaran'],['segitiga','Segitiga'],['persegi','Persegi'],['bintang','Bintang'],['hati','Hati']]).map(x=>[I(x[0]),tx(x[1])])],
 makanan:()=>['Hewan dengan makanannya',sm([['monyet','pisang'],['penguin','ikan-biru'],['katak','belalang'],['kelinci','apel']]).map(x=>[I(x[0]),I(x[1])])]};
let lastT='';
window.lines=function(){const D=dif(),ks=Object.keys(TY).filter(k=>k!==lastT),k=lastT=pk(ks),[t,p]=TY[k](),n=Math.min([3,4,4,5,5,6][D],p.length),ex=D>=3?p.slice(n,n+2).map(x=>[x[1],'x']):[],
 R=sm(p.slice(0,n).map((x,i)=>[x[1],i]).concat(ex));G.pr=p.slice(0,n);G.m=0;G.s=null;G.cx=[];G.t=n;
 M(`<section class="card">${gh(1)}<p class="tgt">Hubungkan: ${t}${ex.length?' (ada gambar yang tidak punya pasangan!)':''}</p><div id="box" class="box"><svg id="sv"></svg><div class="col">${G.pr.map((x,i)=>`<button class="opt" data-a="L" data-v="${i}" id="l${i}">${x[0]}</button>`).join('')}</div><div class="col">${R.map(x=>`<button class="opt" data-a="R" data-v="${x[1]}">${x[0]}</button>`).join('')}</div></div><p class="sm">Ketuk satu gambar lalu pasangannya, atau seret garis dengan jari/mouse.</p><div class="row"><button class="ghost" data-a="go">🔁 Ulangi</button></div></section>`);drag()};
function drag(){const bx=$('#box'),sv=$('#sv');let d=null;
 const rel=e=>{const r=bx.getBoundingClientRect();return[e.clientX-r.left,e.clientY-r.top]};
 bx.addEventListener('pointerdown',e=>{const b=e.target.closest('[data-a=L]');if(!b||b.disabled)return;ACT.L(b.dataset.v,b);const r=b.getBoundingClientRect(),c=bx.getBoundingClientRect();d={b,x:e.clientX,y:e.clientY,ln:null,x1:r.left-c.left+r.width/2,y1:r.top-c.top+r.height/2}});
 bx.addEventListener('pointermove',e=>{if(!d)return;if(!d.ln){if(Math.hypot(e.clientX-d.x,e.clientY-d.y)<12)return;sv.insertAdjacentHTML('beforeend','<line id="tl" stroke="#ff9800" stroke-width="6" stroke-linecap="round" stroke-dasharray="2 10"/>');d.ln=$('#tl')}const[x,y]=rel(e);d.ln.setAttribute('x1',d.x1);d.ln.setAttribute('y1',d.y1);d.ln.setAttribute('x2',x);d.ln.setAttribute('y2',y)});
 const up=e=>{if(!d)return;const dd=d;d=null;if(dd.ln){dd.ln.remove();const t=document.elementFromPoint(e.clientX,e.clientY),r=t&&t.closest('[data-a=R]');if(r&&!r.disabled)ACT.R(r.dataset.v,r);else{ACT.L(dd.b.dataset.v,dd.b);}}};
 bx.addEventListener('pointerup',up);bx.addEventListener('pointercancel',()=>{if(d&&d.ln)d.ln.remove();d=null})}
const oR=ACT.R;ACT.R=function(v,t){if(G.s!==null&&String(v)!==String(G.s)&&!t.disabled){t.classList.add('wrong');setTimeout(()=>t.classList.remove('wrong'),500)}oR(v,t)};

/* ================= LABIRIN: 3 babak, makin besar, bintang, petunjuk, ada jalan bercabang & putaran ================= */
const HP=[['dino-biru','🥚'],['dino-merah','🥚'],['monyet','pisang'],['kelinci','apel'],['beruang','stroberi'],['penguin','ikan-biru'],['lebah','matahari'],['katak','kupu-kupu'],['singa','semangka'],['panda','melon'],['kepik','apel'],['rusa','pohon']];
const sp=x=>B.ASSETS[x]?I(x):x,DIR=[[0,-1,1,4],[1,0,2,8],[0,1,4,1],[-1,0,8,2]];
window.dz=function(){const z=G.mz;$('#mz').innerHTML=z.c.map((c,i)=>`<div style="background:${z.vis[i]?'#d8f3cf':z.hn.has(i)?'#fff3b0':'transparent'};border-width:${[1,2,4,8].map(b=>c.w&b?3:0).join('px ')}px">${i===z.p?z.h:i===z.n*z.n-1?z.g:z.st.has(i)?I('bintang'):''}</div>`).join('');const s=$('#ms');if(s)s.textContent=`Babak ${G.rd+1}/3 · ⭐ ${z.got}/${z.ns} · ${z.mv} langkah`};
window.maze=function(r){G.rd=r||0;const n=[6,7,8,9,10,11][dif()]+G.rd,c=[...Array(n*n)].map(()=>({w:15,v:0})),st=[0];c[0].v=1;
 while(st.length){const i=st[st.length-1],x=i%n,y=i/n|0,nb=shuf(DIR).filter(d=>{const a=x+d[0],b=y+d[1];return a>=0&&b>=0&&a<n&&b<n&&!c[b*n+a].v});if(!nb.length){st.pop();continue}const d=nb[0],j=(y+d[1])*n+x+d[0];c[i].w&=~d[2];c[j].w&=~d[3];c[j].v=1;st.push(j)}
 for(let k=0;k<n+G.rd*2;k++){const x=rnd(n-1),y=rnd(n-1),i=y*n+x,d=pk([DIR[1],DIR[2]]),j=(y+d[1])*n+x+d[0];c[i].w&=~d[2];c[j].w&=~d[3]}
 const hp=pk(HP),sts=new Set();while(sts.size<3)sts.add(1+rnd(n*n-2));
 G.mz={n,c,p:0,end:0,vis:{0:1},h:sp(hp[0]),g:sp(hp[1]),st:sts,ns:3,got:0,hn:new Set(),mv:0};
 M(`<section class="card">${gh(1)}<p class="tgt">Antar ${G.mz.h} ke ${G.mz.g}. Kumpulkan 3 ⭐ untuk bonus!</p><p id="ms" class="tgt" role="status"></p><div id="mz" class="mz" style="grid-template-columns:repeat(${n},1fr)"></div><div class="dp"><button class="opt" data-a="mv" data-v="0" aria-label="Atas">⬆️</button><br><button class="opt" data-a="mv" data-v="3" aria-label="Kiri">⬅️</button><button class="opt" data-a="mv" data-v="2" aria-label="Bawah">⬇️</button><button class="opt" data-a="mv" data-v="1" aria-label="Kanan">➡️</button></div><div class="row"><button class="ghost" data-a="hint">💡 Petunjuk</button><button class="ghost" data-a="mrs">🔁 Ulangi babak</button></div></section>`);dz();swipe()};
cp(ACT,{
mv(v){const z=G.mz;if(!z||z.end||G.id!=='labirin')return;const d=DIR[v];if(z.c[z.p].w&d[2])return beep(150);z.p+=d[1]*z.n+d[0];z.vis[z.p]=1;z.hn.delete(z.p);z.mv++;if(z.st.delete(z.p)){z.got++;beep(760)}beep(500);dz();
 if(z.p===z.n*z.n-1){z.end=1;ok();if(z.got===z.ns)add(5,'Semua bintang');later(()=>G.rd<2?maze(G.rd+1):fin(),700)}},
hint(){const z=G.mz;if(!z||z.end)return;const prev={[z.p]:-1},q=[z.p],T=z.n*z.n-1;while(q.length){const i=q.shift();if(i===T)break;DIR.forEach(d=>{if(z.c[i].w&d[2])return;const j=i+d[1]*z.n+d[0];if(!(j in prev)){prev[j]=i;q.push(j)}})}
 const path=[];for(let i=T;i!==-1&&i in prev;i=prev[i])path.unshift(i);z.hn=new Set(path.slice(1,5));dz()},
mrs(){maze(G.rd)}});
/* kontrol: go() memakai nama global color/lines/maze saat dipanggil, jadi override di atas langsung berlaku */
})();
