/* Suara (musik & efek) + Pengaturan Suara + Donasi QRIS — Buku Belajar Anak */
(function(){
'use strict';
var BASE='audio/',MODES=['all','sfx','off'];
/* efek suara: ok = jawaban benar (lagu_6), bad = jawaban salah (lagu_5), fin = level selesai (lagu_7) */
var SFXF={ok:'lagu_6.mp3',bad:'lagu_5.mp3',fin:'lagu_7.mp3'},SFXK=['ok','bad','fin'];
var ICON={all:'🔊',sfx:'🔔',off:'🔇'};
var bgm=null,sfx={},started=false,duckT=null,lastOpener=null;

/* ---------- state ---------- */
if(MODES.indexOf(S.sm)<0)S.sm=(S.snd===0||S.snd===false)?'off':'all';
if(typeof S.mv!=='number')S.mv=.5;
function sync(){S.snd=S.sm==='off'?0:1;save()}
sync();

/* ---------- audio ---------- */
function mkAudio(f,loop){var a=new Audio(BASE+f);a.preload=loop?'none':'auto';a.loop=!!loop;return a}
function getBgm(){if(!bgm){bgm=mkAudio('lagu_01.mp3',true);bgm.volume=S.mv}return bgm}
function getSfx(n){if(!sfx[n]){sfx[n]=mkAudio(SFXF[n]);sfx[n].volume=.6}return sfx[n]}

function musicOn(){return S.sm==='all'}
function playBgm(){if(!musicOn()||document.hidden)return;var a=getBgm();a.volume=S.mv;var p=a.play();if(p&&p.catch)p.catch(function(){started=false})}
function stopBgm(){if(bgm)bgm.pause()}

function duck(ms){
  if(!bgm||bgm.paused)return;
  bgm.volume=Math.max(0,S.mv*.25);
  clearTimeout(duckT);
  duckT=setTimeout(function(){if(bgm)bgm.volume=S.mv},ms+150);
}
function play(n){
  if(S.sm==='off')return;
  /* hentikan efek lain agar tidak bertumpuk */
  SFXK.forEach(function(i){if(i!==n&&sfx[i]){sfx[i].pause();try{sfx[i].currentTime=0}catch(e){}}});
  var a=getSfx(n);
  try{a.currentTime=0}catch(e){}
  var p=a.play();if(p&&p.catch)p.catch(function(){});
  duck((a.duration&&isFinite(a.duration)?a.duration:1.6)*1000);
}

/* buka kunci audio pada gestur pertama pengguna (kebijakan autoplay browser & iOS) */
function unlock(){
  if(started)return;started=true;
  SFXK.forEach(function(i){
    var a=getSfx(i);a.muted=true;
    var p=a.play();
    var done=function(){a.pause();try{a.currentTime=0}catch(e){}a.muted=false};
    if(p&&p.then)p.then(done).catch(function(){a.muted=false});else done();
  });
  playBgm();
}
['pointerdown','touchend','keydown','click'].forEach(function(ev){
  document.addEventListener(ev,function h(){unlock();if(started)document.removeEventListener(ev,h,true)},true);
});
document.addEventListener('visibilitychange',function(){
  if(document.hidden)stopBgm();else if(started)playBgm();
});

/* ---------- pemicu suara pada permainan ---------- */
var _ok=window.ok,_bad=window.bad,_fin=window.fin;
window.ok=function(){_ok.apply(this,arguments);play('ok')};   /* lagu_6: jawaban benar */
window.bad=function(){_bad.apply(this,arguments);play('bad')};  /* lagu_5: jawaban salah */
window.fin=function(){var first=!G.done;var r=_fin.apply(this,arguments);if(first)play('fin');return r}; /* lagu_7: level selesai */

window.sfxPlay=play;   /* dipakai game yang tidak lewat ok()/bad(), mis. Puzzle Petualangan */

/* ---------- modal ---------- */
function modal(html,cls){
  closeModal(true);
  var d=document.createElement('div');d.id='md';d.className='md';
  d.innerHTML='<div class="mb '+(cls||'')+'" role="dialog" aria-modal="true" aria-labelledby="mt"><button class="mx" data-a="mclose" aria-label="Tutup">✕</button>'+html+'</div>';
  d.addEventListener('click',function(e){if(e.target===d)closeModal()});
  document.body.appendChild(d);document.documentElement.classList.add('mo');
  var c=d.querySelector('.mx');if(c)c.focus();
  return d;
}
function closeModal(silent){
  var d=document.getElementById('md');if(!d)return;
  d.remove();document.documentElement.classList.remove('mo');
  if(!silent&&lastOpener&&document.contains(lastOpener)){try{lastOpener.focus()}catch(e){}}
}
document.addEventListener('keydown',function(e){if(e.key==='Escape')closeModal()});

/* ---------- Pengaturan suara ---------- */
var OPT=[
  ['all','🎵','Semua suara hidup','Musik utama + efek suara'],
  ['sfx','🔔','Hanya efek suara','Musik utama mati, efek tetap bunyi'],
  ['off','🔇','Semua suara mati','Tanpa musik dan tanpa efek suara']
];
function settingsHtml(){
  return '<h2 id="mt">⚙️ Pengaturan Suara</h2><div class="so" role="radiogroup" aria-label="Mode suara">'+
  OPT.map(function(o){var on=S.sm===o[0];
    return '<button class="sopt'+(on?' on':'')+'" role="radio" aria-checked="'+on+'" data-a="smode" data-v="'+o[0]+'"><span class="si">'+o[1]+'</span><span class="st"><b>'+o[2]+'</b><small>'+o[3]+'</small></span><span class="sc" aria-hidden="true">'+(on?'✔':'')+'</span></button>'}).join('')+
  '</div><label class="sv'+(S.sm==='all'?'':' dis')+'">🎼 Volume musik<input id="mvol" type="range" min="0" max="100" step="5" value="'+Math.round(S.mv*100)+'"'+(S.sm==='all'?'':' disabled')+'></label>'+
  '<button class="cta mok" data-a="mclose">Selesai</button>';
}
function openSettings(t){lastOpener=t||null;modal(settingsHtml());bindVol()}
function bindVol(){
  var r=document.getElementById('mvol');if(!r)return;
  r.addEventListener('input',function(){S.mv=r.value/100;if(bgm)bgm.volume=S.mv;save()});
}
function setMode(m){
  if(MODES.indexOf(m)<0)return;
  S.sm=m;sync();
  if(m==='all'){started=false;unlock()}else stopBgm();
  if(m!=='off')play('ok'); /* contoh bunyi */
  var d=document.getElementById('md');
  if(d){var b=d.querySelector('.mb'),x=b.querySelector('.mx');var tmp=document.createElement('div');tmp.innerHTML=settingsHtml();
    while(b.lastChild&&b.lastChild!==x)b.removeChild(b.lastChild);
    while(tmp.firstChild)b.appendChild(tmp.firstChild);bindVol();
    var cur=b.querySelector('.sopt.on');if(cur)cur.focus();}
  hdr();
}

/* ---------- Donasi ---------- */
var QRIS_NAME='RIKI HERMAWAN, DIGITAL & KREATIF',NMID='ID1026615097429';
function donHtml(){
  return '<div class="dm-h"><span class="dm-ic" aria-hidden="true">💛</span><div><h2 id="mt">Donasi melalui QRIS</h2><p class="dm-sub">Dukungan kecil, semangat besar untuk anak-anak Indonesia.</p></div></div>'+
  '<p class="dm-p"><b>Satu kebaikan kecil dapat membuka lebih banyak kesempatan untuk belajar.</b> Buku Belajar Anak hadir untuk menemani anak-anak Indonesia mengenal huruf, berhitung, melatih logika, dan menjelajahi dunia melalui permainan yang menyenangkan.</p>'+
  '<p class="dm-p">Kami ingin ruang belajar ini tetap mudah diakses, ramah anak, dan terus berkembang. Di balik setiap permainan, ada waktu untuk merancang soal, membuat ilustrasi, mengembangkan fitur, serta merawat website agar tetap nyaman digunakan.</p>'+
  '<section class="dm-b" aria-label="Manfaat dukungan Anda"><h3>Dukungan Anda membantu kami untuk</h3><ul>'+
  '<li><span aria-hidden="true">🎮</span><div><b>Menghadirkan permainan baru</b><br>Lebih banyak aktivitas yang mengajak anak belajar sambil bermain.</div></li>'+
  '<li><span aria-hidden="true">🎨</span><div><b>Mengembangkan ilustrasi dan cerita</b><br>Karakter, gambar, dan petualangan yang membuat anak semakin antusias.</div></li>'+
  '<li><span aria-hidden="true">🎵</span><div><b>Menyempurnakan pengalaman belajar</b><br>Musik, suara, dan interaksi yang membantu anak menikmati proses belajar.</div></li>'+
  '<li><span aria-hidden="true">🛠️</span><div><b>Merawat dan meningkatkan website</b><br>Perbaikan, pembaruan, serta pengembangan agar Buku Belajar Anak terus bertumbuh.</div></li></ul></section>'+
  '<section class="dm-q" aria-label="Donasi lewat QRIS"><h3>Donasi sukarela melalui QRIS</h3><p class="dm-p">Jika Anda berkenan mendukung perjalanan ini, silakan berdonasi sesuai kemampuan dan keikhlasan. Tidak ada nominal minimum.</p><div class="qw"><img src="qris.png" alt="Kode QRIS donasi atas nama '+QRIS_NAME+'" width="800" height="924" decoding="async" loading="lazy"></div>'+
  '<p class="dm-n"><b>'+QRIS_NAME+'</b><span>NMID: '+NMID+'</span></p>'+
  '<a class="cta dm-dl" href="qris.png" download="QRIS-Donasi-Buku-Belajar-Anak.png">⬇ Unduh Kode QRIS</a></section>'+
  '<ol class="dm-s"><li>Pindai QRIS di atas atau unduh gambar QRIS.</li><li>Buka aplikasi e-wallet atau mobile banking (GoPay, OVO, DANA, ShopeePay, LinkAja, dll).</li><li>Pilih <b>Scan</b> (atau <b>Upload dari galeri</b>), isi nominal sesuai keikhlasan, lalu konfirmasi.</li></ol>'+
  '<blockquote class="dm-k"><b>Tidak bisa berdonasi saat ini?</b> Tidak apa-apa. Menemani anak belajar, membagikan website kepada keluarga, atau memberikan saran juga merupakan dukungan yang sangat berarti. Terima kasih! 🦕💛</blockquote>'+
  '<p class="dm-f">Terima kasih telah menjadi bagian dari perjalanan kecil ini. Semoga semakin banyak anak dapat belajar, bermain, dan tumbuh dengan gembira. 🦖💛</p>'+
  '<button class="ghost dm-x" data-a="mclose">Tutup</button>';
}
function openDon(t){lastOpener=t||null;modal(donHtml(),'dmod')}
function donCard(){
  return '<section class="card dcard" aria-labelledby="dt"><span class="dheart" aria-hidden="true">💛</span><h2 id="dt">Bantu Buku Belajar Anak<br>Terus Bertumbuh</h2>'+
  '<p class="lead"><b>Satu kebaikan kecil dapat membuka lebih banyak kesempatan untuk belajar.</b></p>'+
  '<p class="lead">Dukungan Anda membantu kami menghadirkan permainan baru, ilustrasi yang lebih menarik, dan pengalaman belajar yang lebih baik untuk anak-anak Indonesia.</p>'+
  '<ul class="pl dpl" aria-label="Manfaat dukungan"><li>🎮 Permainan baru yang lebih seru</li><li>🎨 Ilustrasi, karakter, dan cerita</li><li>🎵 Musik dan suara yang lebih menyenangkan</li><li>🛠️ Perawatan dan pembaruan website</li></ul>'+
  '<button class="don dcta" data-a="don">💛 Dukung Sekarang</button><p class="dsub">Sesuai keikhlasan Anda. Berapa pun sangat berarti. Terima kasih telah mendukung anak-anak Indonesia belajar dengan gembira. 🦕💛</p></section>';
}
var _home=window.home,_prof=window.prof;
window.home=function(){return _home.apply(this,arguments).replace('<!--DON-->',donCard())};
window.prof=function(){return _prof.apply(this,arguments)+donCard()};

/* ---------- aksi ---------- */
ACT.snd=function(v,t){openSettings(t)};
ACT.smode=function(v){setMode(v)};
ACT.don=function(v,t){openDon(t)};
ACT.mclose=function(){closeModal()};

window.Suara={icon:function(){return ICON[S.sm]||'🔊'},open:openSettings};
var _render=window.render;window.render=function(){var r=_render.apply(this,arguments);if(window.VC)VC.paint();return r};
hdr();render();
})();
