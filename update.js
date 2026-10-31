/* update.js — pembaruan otomatis saat internet tersambung. Memeriksa versi baru saat: dibuka, kembali ke aplikasi, internet tersambung, dan tiap 15 menit.
   Versi baru terpasang diam-diam lalu halaman dimuat ulang otomatis (saat anak tidak sedang bermain; jika sedang bermain, menunggu selesai). Progres aman di LocalStorage. */
(function(){'use strict';if(!('serviceWorker'in navigator))return;
const KV='bba_ver',KR='bba_rl',had=!!navigator.serviceWorker.controller;let reg=null,pend=0,tm=0;
const busy=()=>{try{return V==='play'&&G&&G.id&&!G.done}catch(e){return false}};
function reload(){if(busy()){if(!pend){pend=1;note('✨ Versi baru siap! Dipasang otomatis setelah selesai bermain.');tm=setInterval(()=>{if(!busy()){clearInterval(tm);reload()}},3000)}return}
 try{const t=+sessionStorage.getItem(KR)||0;if(Date.now()-t<30000){setTimeout(reload,30500-(Date.now()-t));return}sessionStorage.setItem(KR,Date.now())}catch(e){}
 note('✨ Memperbarui ke versi terbaru…');setTimeout(()=>location.reload(),700)}
function note(t){try{toast(t)}catch(e){}}
function check(){if(!navigator.onLine)return;
 if(reg)reg.update().catch(()=>{});
 fetch('version.json?_='+Date.now(),{cache:'no-store'}).then(r=>r.ok?r.json():null).then(j=>{if(!j||!j.v)return;let o=null;try{o=localStorage.getItem(KV);localStorage.setItem(KV,j.v)}catch(e){}
  if(o&&o!==j.v){if(reg)reg.update().catch(()=>{});setTimeout(()=>{if(!reg||!reg.installing)reload()},4000)}}).catch(()=>{})}
navigator.serviceWorker.register('service-worker.js',{updateViaCache:'none'}).then(r=>{reg=r;
 r.addEventListener('updatefound',()=>{const w=r.installing;if(!w)return;w.addEventListener('statechange',()=>{if(w.state==='installed'&&navigator.serviceWorker.controller)w.postMessage('SKIP_WAITING')})});
 if(r.waiting&&navigator.serviceWorker.controller)r.waiting.postMessage('SKIP_WAITING');check()}).catch(()=>{});
navigator.serviceWorker.addEventListener('controllerchange',()=>{if(had)reload()});
addEventListener('online',check);document.addEventListener('visibilitychange',()=>{if(document.visibilityState==='visible')check()});setInterval(check,15*60*1000);
})();
