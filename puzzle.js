/* puzzle.js — Puzzle Petualangan. Dimuat SETELAH script.js, bank.js, games2.js. Memakai sistem poin/profil yang sudah ada. */
(function(){'use strict';
if(!window.BBA||typeof ACT==='undefined')return;
const B=BBA,LV=[['Pemula',4,2,2],['Mudah',6,3,2],['Mudah Plus',9,3,3],['Sedang',12,4,3],['Menantang',16,4,4],['Sulit',24,6,4],['Master',35,7,5]],
GUIDE=[.35,.3,.25,.12,0,0,0],
CATS=[['dinosaurus','Dinosaurus','🦕'],['hewan-darat','Hewan Darat','🦁'],['hewan-air','Hewan Air','🐳'],['burung-serangga','Burung & Serangga','🦋'],['buah','Buah-buahan','🍎'],['benda','Benda Sekitar','🏠'],['kendaraan','Kendaraan','🚗'],['alam','Alam & Cuaca','🌈'],['pendidikan','Huruf & Angka','🔤']],
TH={dinosaurus:['#8fd3ff','#d4f5b0','#5fbf4a','#3f9e3a'],'hewan-darat':['#7cc7ff','#cdeeff','#7ed957','#4fb648'],'hewan-air':['#2f9bff','#8fe3ff','#1976d2','#0d5ca8'],'burung-serangga':['#8fd3ff','#fff2b8','#8bdc5a','#5cc24a'],buah:['#ffe29a','#ffc6d9','#ffb74d','#ff8a65'],benda:['#c7e8ff','#fff3c4','#ffd180','#ffab91'],kendaraan:['#8fd3ff','#e3f6ff','#9e9e9e','#757575'],alam:['#5cb8ff','#c4ecff','#7ed957','#43a047'],pendidikan:['#d1c4ff','#ffe0f0','#ffcc80','#f48fb1']};
GM.puzzle=['🧩','Puzzle Petualangan'];GD.puzzle=['#00a8e8','Susun potongan, temukan keajaiban!'];
INS.puzzle='Pilih gambar dan jumlah keping, lalu seret atau ketuk keping ke posisi yang benar.';
HOW.puzzle=['Pilih gambar dan tingkat','Seret keping (atau ketuk keping, lalu ketuk kotak)','Susun sampai gambar utuh'];
const sel={cat:'dinosaurus',img:'dino-biru',lv:0,timer:0},SH=new Image();SH.src='aset.webp';
const ready=()=>Promise.race([new Promise(r=>{if(SH.complete&&SH.naturalWidth)return r();SH.onload=SH.onerror=r}),new Promise(r=>setTimeout(r,1200))]);
const tg=t=>{[...t.parentNode.children].forEach(b=>b.classList.remove('on'));t.classList.add('on')},msg=t=>{const m=$('#pzmsg');if(m)m.textContent=t},
list=c=>Object.values(B.ASSETS).filter(a=>a.kategori===c);
/* ---- gambar sumber: latar tema + dekor + sprite aset, digambar ke canvas lalu dipotong lewat CSS (posisi tepat per keping) ---- */
function draw(a,W,H){const c=document.createElement('canvas');c.width=W;c.height=H;let x=null;try{x=c.getContext('2d')}catch(e){}if(!x)return'';
 x.imageSmoothingQuality='high';const th=TH[a.kategori]||TH.benda;let s=[...a.id].reduce((q,ch)=>(q*31+ch.charCodeAt(0))>>>0,7);const r=()=>(s=(s*1664525+1013904223)>>>0)/4294967296;
 const g=x.createLinearGradient(0,0,0,H);g.addColorStop(0,th[0]);g.addColorStop(.7,th[1]);g.addColorStop(1,th[1]);x.fillStyle=g;x.fillRect(0,0,W,H);
 for(let i=0;i<16;i++){x.fillStyle='rgba(255,255,255,.35)';x.beginPath();x.arc(r()*W,r()*H*.8,4+r()*12,0,7);x.fill()}
 x.fillStyle=th[2];x.beginPath();x.ellipse(W*.3,H*1.02,W*.6,H*.28,0,0,7);x.fill();x.fillStyle=th[3];x.beginPath();x.ellipse(W*.85,H*1.05,W*.6,H*.25,0,0,7);x.fill();
 const ok=SH.naturalWidth>0,sp=(rr,cc,cx,cy,z)=>{if(ok)x.drawImage(SH,cc*80,rr*80,80,80,cx-z/2,cy-z/2,z,z)},m=Math.min(W,H);
 if(a.kategori!=='hewan-air'){sp(7,9,W*.86,H*.16,m*.26);sp(7,10,W*.16,H*.15,m*.28);sp(7,12,W*.1,H*.82,m*.3)}
 x.fillStyle='rgba(0,0,0,.18)';x.beginPath();x.ellipse(W/2,H*.9,m*.28,m*.05,0,0,7);x.fill();sp(a.r,a.c,W/2,H*.53,m*.78);
 try{return c.toDataURL('image/jpeg',.88)}catch(e){return''}}
B.pzDraw=draw;
/* ---- menu: kategori -> gambar -> tingkat ---- */
const grid=()=>{const pz=P().pz||{};return list(sel.cat).map(a=>`<button class="pzt ${a.id===sel.img?'on':''}" data-a="pzimg" data-v="${a.id}">${B.img(a.id)}<small>${a.nama}${pz[a.id]?' ✔'+pz[a.id].length:''}</small></button>`).join('')};
function pzMenu(){clr();const pz=P().pz||{};G.pz=null;
 M(`<section class="card pzm"><div class="cnt">${['dino-biru','dino-merah','dino-kuning','pterodaktil'].map(B.img).join('')}</div><h1>🧩 Puzzle Petualangan</h1><p class="tgt">Susun Potongan, Temukan Keajaiban!</p><p class="sm">Gambar yang pernah selesai: ${Object.keys(pz).length}</p>
 <div class="row">${CATS.map(c=>`<button class="opt ${c[0]===sel.cat?'on':''}" data-a="pzcat" data-v="${c[0]}">${c[2]} ${c[1]}</button>`).join('')}</div><div class="pzg">${grid()}</div>
 <p><b>Tingkat</b> <span class="sm">(makin banyak keping, makin sedikit bantuan)</span></p><div class="row">${LV.map((l,i)=>`<button class="opt ${i===sel.lv?'on':''}" data-a="pzlv" data-v="${i}"><b>${l[1]}</b> keping<small>${l[0]}</small></button>`).join('')}</div>
 <label class="pzo"><input type="checkbox" id="pzt" ${sel.timer?'checked':''}> ⏱ Pakai timer (boleh dimatikan)</label><p><button class="cta" data-a="pzgo">▶ Main Puzzle</button> <button class="ghost" data-a="nav" data-v="home">🏠 Beranda</button></p></section>`)}
function clr(){if(G.pz&&G.pz.iv){clearInterval(G.pz.iv);G.pz.iv=0}}
/* ---- bermain ---- */
async function pzStart(){clr();const a=B.ASSETS[sel.img],[nm,n,cols,rows]=LV[sel.lv];M('<section class="card"><p class="tgt">Menyiapkan puzzle…</p></section>');const g0=G;await ready();if(G!==g0)return;
 const src=draw(a,cols*100,rows*100),z=G.pz={a,nm,n,cols,rows,src,ok:0,steps:0,hints:0,sec:0,sel:null,paused:0,done:0,nc:0,iv:0};
 const bs=`${cols*100}% ${rows*100}%`,bp=k=>`${k%cols/(cols-1)*100}% ${(k/cols|0)/(rows-1)*100}%`;
 M(`<section class="card pzp" style="${src?`--bi:url('${src}');`:''}--bs:${bs}"><div class="pzh"><button class="ghost" data-a="pzmenu">⬅ Menu</button><b>${a.nama}</b><span class="lv">${nm} · ${n} keping</span></div>
 <div class="pzs"><span>👣 <b id="pzst">0</b></span><span id="pztm" ${sel.timer?'':'hidden'}>⏱ 0:00</span><span>🧩 <b id="pzpg">0</b>/${n}</span></div><div class="bar"><i id="pzbar" style="width:0"></i></div>
 <div class="pzw" id="pzw"><div id="pzb" class="pzb" style="--c:${cols}">${[...Array(n).keys()].map(i=>`<button class="pzs2" data-a="pzslot" data-v="${i}" aria-label="Kotak baris ${(i/cols|0)+1} kolom ${i%cols+1}" style="--bp:${bp(i)};--go:${GUIDE[sel.lv]}"></button>`).join('')}</div></div>
 <div class="pzy" id="pzy">${shuf([...Array(n).keys()]).map(k=>`<button class="pzp2" data-a="pzpick" data-v="${k}" aria-label="Keping ${k+1}" style="--bp:${bp(k)}"></button>`).join('')}</div>
 <p id="pzmsg" class="tgt" role="status">Seret keping ke kotak, atau ketuk keping lalu ketuk kotak.</p>
 <div class="row"><button class="ghost" data-a="pzhint">💡 Petunjuk</button><button class="ghost" data-a="pzref">👁 Gambar</button><button class="ghost" data-a="pzzoom">🔍 Zoom</button><button class="ghost" data-a="pzpause" id="pzpa">⏸ Jeda</button><button class="ghost" data-a="pzre">🔁 Acak Ulang</button><button class="ghost" data-a="snd">${S.snd?'🔊':'🔇'} Suara</button></div>
 <div id="pzr" class="pzr" hidden data-a="pzref"><img alt="Gambar utuh ${a.nama}"><p class="sm">Ketuk untuk menutup</p></div></section>`);
 const im=$('#pzr img');if(src)im.src=src;else im.hidden=true;bind($('.pzp'));fit();
 if(sel.timer)z.iv=setInterval(()=>{const e=$('#pztm');if(!e||G.pz!==z)return clearInterval(z.iv);if(!z.paused&&!z.done){z.sec++;e.textContent='⏱ '+(z.sec/60|0)+':'+String(z.sec%60).padStart(2,'0')}},1000)}
function fit(){const z=G.pz,b=$('#pzb'),p=$('.pzp');if(!z||!b)return;p.style.setProperty('--ps',Math.max(40,Math.min(96,b.clientWidth/z.cols*.92))+'px')}
addEventListener('resize',fit);
function stat(){const z=G.pz;$('#pzst').textContent=z.steps;$('#pzpg').textContent=z.ok;$('#pzbar').style.width=z.ok/z.n*100+'%'}
function place(k,i){const z=G.pz,sl=document.querySelector('.pzs2[data-v="'+i+'"]');if(!z||z.done||z.paused||!sl||sl.classList.contains('lk'))return;z.steps++;
 if(k===i){sl.classList.add('lk');sl.classList.remove('hint');sl.disabled=true;const pc=document.querySelector('.pzp2[data-v="'+k+'"]');if(pc)pc.remove();z.ok++;z.sel=null;window.sfxPlay&&sfxPlay('ok');msg('✅ Pas! Keping terkunci.')}
 else{sl.classList.add('no');setTimeout(()=>sl.classList.remove('no'),350);window.sfxPlay&&sfxPlay('bad');msg('Belum pas, coba kotak lain ya 🙂')}
 stat();if(z.ok===z.n)win()}
function pick(k){const z=G.pz;if(!z||z.paused||z.done)return;z.sel=k;document.querySelectorAll('.pzp2').forEach(b=>b.classList.toggle('sel',+b.dataset.v===k))}
function bind(el){let d=null;
 el.addEventListener('pointerdown',e=>{const b=e.target.closest('.pzp2');if(!b||(e.button>0))return;try{b.setPointerCapture(e.pointerId)}catch(x){}d={b,x:e.clientX,y:e.clientY,cl:null,s:0}});
 el.addEventListener('pointermove',e=>{if(!d)return;if(!d.cl){if(Math.hypot(e.clientX-d.x,e.clientY-d.y)<8)return;d.s=d.b.getBoundingClientRect().width;const c=d.b.cloneNode();c.className='pzp2 pzf';c.style.width=c.style.height=d.s+'px';document.body.appendChild(c);d.cl=c;pick(+d.b.dataset.v)}d.cl.style.left=e.clientX-d.s/2+'px';d.cl.style.top=e.clientY-d.s/2+'px'});
 const end=e=>{if(!d)return;const q=d;d=null;if(!q.cl)return;q.cl.remove();G.pz.nc=1;setTimeout(()=>{if(G.pz)G.pz.nc=0},60);if(e.type==='pointerup'){const t=document.elementFromPoint(e.clientX,e.clientY),s=t&&t.closest('.pzs2');if(s)place(+q.b.dataset.v,+s.dataset.v)}};
 el.addEventListener('pointerup',end);el.addEventListener('pointercancel',end)}
function win(){const z=G.pz,p=P(),id=z.a.id;z.done=1;clr();p.pz=p.pz||{};const arr=p.pz[id]=p.pz[id]||[],first=!arr.includes(sel.lv);let b='';
 if(first){arr.push(sel.lv);const pt=10+sel.lv*5;p.ok++;add(pt,'Puzzle '+z.a.nama+' ('+z.n+')');b=' Bonus puzzle baru +'+pt+'.'}else save();
 const info=`<p class="sm">👣 ${z.steps} langkah · 💡 ${z.hints} petunjuk${sel.timer?' · ⏱ '+(z.sec/60|0)+':'+String(z.sec%60).padStart(2,'0'):''}${b?'':' · Puzzle ini sudah pernah selesai di tingkat ini, jadi tanpa bonus baru.'}</p><p><button class="cta" data-a="pznext">▶ Puzzle Berikutnya</button> <button class="ghost" data-a="pzre">🔁 Main Lagi</button> <button class="ghost" data-a="pzmenu">🧩 Menu Puzzle</button></p>`;
 later(()=>{if(first&&!G.done){fin();const c=$('#main .card');if(c)c.insertAdjacentHTML('beforeend',info)}else{boom();M(`<section class="card"><h1>🎉 Puzzle Selesai!</h1><div class="cnt">${B.img(z.a.id)}</div><p class="big pop">⭐⭐⭐</p>${info}</section>`)}},500)}
Object.assign(ACT,{
pzcat(v,t){sel.cat=v;sel.img=list(v)[0].id;tg(t);$('.pzg').innerHTML=grid()},pzimg(v,t){sel.img=v;tg(t)},pzlv(v,t){sel.lv=+v;tg(t)},
pzgo(){sel.timer=$('#pzt').checked?1:0;pzStart()},pzmenu:pzMenu,pzre:pzStart,
pznext(){const l=list(B.ASSETS[sel.img].kategori),i=l.findIndex(a=>a.id===sel.img);sel.img=l[(i+1)%l.length].id;pzStart()},
pzpick(v){if(G.pz&&G.pz.nc)return;pick(+v);msg('Sekarang ketuk kotak tujuan.')},
pzslot(v){const z=G.pz;if(!z||z.paused)return;if(z.sel===null)return msg('Pilih keping dulu ya 🙂');place(z.sel,+v)},
pzhint(){const z=G.pz;if(!z||z.done||z.paused)return;const k=z.sel!==null?z.sel:+(document.querySelector('.pzp2')||{dataset:{v:-1}}).dataset.v;if(k<0)return;pick(k);z.hints++;const s=document.querySelector('.pzs2[data-v="'+k+'"]');if(s){s.classList.add('hint');s.scrollIntoView({block:'nearest',inline:'nearest'});setTimeout(()=>s.classList.remove('hint'),3000)}msg('💡 Kotak yang berkedip adalah tempat keping ini.')},
pzref(){const r=$('#pzr');if(r)r.hidden=!r.hidden},
pzzoom(){const w=$('#pzw');w.classList.toggle('zoom');fit()},
pzpause(){const z=G.pz;if(!z||z.done)return;z.paused=!z.paused;$('.pzp').classList.toggle('pause',!!z.paused);$('#pzpa').textContent=z.paused?'▶ Lanjutkan':'⏸ Jeda';msg(z.paused?'Jeda. Ketuk Lanjutkan kalau sudah siap.':'')}});
const og=ACT.go;ACT.go=function(){G.id==='puzzle'?pzMenu():og.apply(this,arguments)};
try{render()}catch(e){}
})();
