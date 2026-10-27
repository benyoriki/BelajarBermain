/* Suara (musik & efek) + Pengaturan Suara + Donasi QRIS — Buku Belajar Anak */
(function(){
'use strict';
var BASE='audio/',MODES=['all','sfx','off'];
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
function getSfx(n){if(!sfx[n]){sfx[n]=mkAudio('lagu_0'+n+'.mp3');sfx[n].volume=1}return sfx[n]}

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
  [2,3,4].forEach(function(i){if(i!==n&&sfx[i]){sfx[i].pause();try{sfx[i].currentTime=0}catch(e){}}});
  var a=getSfx(n);
  try{a.currentTime=0}catch(e){}
  var p=a.play();if(p&&p.catch)p.catch(function(){});
  duck((a.duration&&isFinite(a.duration)?a.duration:1.6)*1000);
}

/* buka kunci audio pada gestur pertama pengguna (kebijakan autoplay browser & iOS) */
function unlock(){
  if(started)return;started=true;
  [2,3,4].forEach(function(i){
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
window.ok=function(){_ok.apply(this,arguments);play(2)};   /* lagu_02: jawaban benar */
window.bad=function(){_bad.apply(this,arguments);play(4)};  /* lagu_04: jawaban salah */
window.fin=function(){var first=!G.done;var r=_fin.apply(this,arguments);if(first)play(3);return r}; /* lagu_03: level selesai */

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
  if(m!=='off')play(2); /* contoh bunyi */
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
  return '<h2 id="mt">💝 Terima Kasih Telah Peduli</h2>'+
  '<p class="dl">Setiap senyum anak yang berhasil menyelesaikan satu level adalah alasan kami terus berkarya. Buku Belajar Anak dirancang agar <b>gratis, bebas iklan, dan aman</b> untuk si kecil — dan itu hanya bisa bertahan dengan dukungan orang-orang baik seperti Anda.</p>'+
  '<ul class="dk"><li>🎮 Permainan dan soal baru yang lebih seru</li><li>🎨 Ilustrasi, karakter, dan musik yang lebih menarik</li><li>🚫 Tetap bebas iklan &amp; aman untuk anak</li><li>🛠️ Perawatan dan pembaruan berkelanjutan</li></ul>'+
  '<p class="dl dq">“Kebaikan sekecil apa pun, jika dilakukan bersama, tumbuh menjadi masa depan yang besar bagi anak-anak kita.”</p>'+
  '<div class="qw"><img src="qris.png" alt="Kode QRIS donasi atas nama '+QRIS_NAME+'" width="800" height="924" decoding="async"></div>'+
  '<p class="dn"><b>'+QRIS_NAME+'</b><br>NMID: '+NMID+'</p>'+
  '<a class="cta dbtn" href="qris.png" download="QRIS-Donasi-Buku-Belajar-Anak.png">⬇ Unduh QRIS</a>'+
  '<ol class="dh"><li>Unduh QRIS, atau scan langsung dari layar ini.</li><li>Buka e-wallet atau mobile banking Anda (GoPay, OVO, DANA, ShopeePay, LinkAja, dll.).</li><li>Pilih <b>Scan</b> (atau <b>Upload dari galeri</b>), isi nominal sesuai keikhlasan, lalu konfirmasi.</li></ol>'+
  '<p class="dl sm">Donasi bersifat sukarela. Doa dan dukungan Anda sangat berarti — terima kasih telah menjadi bagian dari tumbuh kembang anak-anak kita 🦕💛</p>';
}
function openDon(t){lastOpener=t||null;modal(donHtml(),'don')}
function donCard(){
  return '<section class="card dcard" aria-labelledby="dt"><span class="dheart" aria-hidden="true">💝</span><small class="ey">Ajakan dari hati</small><h2 id="dt">Satu Kebaikan Kecil,<br>Dampak yang Besar</h2>'+
  '<p class="lead">Buku Belajar Anak dibuat dengan cinta agar setiap anak bisa belajar dengan gembira — <b>gratis dan bebas iklan</b>. Di balik tiap permainan ada waktu, tenaga, dan biaya yang tidak sedikit.</p>'+
  '<p class="lead">Dukungan Anda memastikan karya ini tetap gratis, terus bertambah seru, dan menjangkau lebih banyak anak Indonesia.</p>'+
  '<ul class="pl dpl" aria-label="Manfaat donasi"><li>🎮 Permainan baru</li><li>🎨 Ilustrasi &amp; musik</li><li>🛠️ Perawatan rutin</li></ul>'+
  '<button class="don dcta" data-a="don">💝 Dukung via QRIS</button><p class="dsub">Nominal bebas — berapa pun sangat berarti. Terima kasih 🦕💛</p></section>';
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
hdr();render();
})();
