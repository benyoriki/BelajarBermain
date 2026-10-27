/* Penghitung pengunjung otomatis — Buku Belajar Anak
   Memakai layanan counter gratis Abacus (abacus.jasoncameron.dev). Hanya angka yang dihitung:
   tidak ada nama, foto, atau data profil yang dikirim.
   - "Pengunjung"  = browser/perangkat unik (dihitung sekali per browser)
   - "Kunjungan"   = jumlah sesi membuka website (sekali per sesi tab)
   Penghitungan hanya aktif di domain resmi, jadi uji coba lokal tidak menambah angka. */
(function(){
'use strict';
var C={api:'https://abacus.jasoncameron.dev',ns:'belajarbermain.online',hosts:['belajarbermain.online','www.belajarbermain.online'],U:'pengunjung',V:'kunjungan'};
var KEY='bba_vc',val={u:null,v:null},shown={u:0,v:0};
try{var c=JSON.parse(localStorage.getItem(KEY));if(c&&c.u>=0&&c.v>=0){val.u=+c.u;val.v=+c.v}}catch(e){}
var live=C.hosts.indexOf(location.hostname)>-1&&!navigator.webdriver;
function fmt(n){return Number(n).toLocaleString('id-ID')}
function writable(s){try{var k='bba_t';s.setItem(k,'1');s.removeItem(k);return true}catch(e){return false}}
function call(kind,key){
  return fetch(C.api+'/'+kind+'/'+C.ns+'/'+key,{cache:'no-store'}).then(function(r){
    if(r.ok)return r.json();if(r.status===404)return{value:0};throw new Error(r.status)
  }).then(function(j){var n=Number(j.value);if(!isFinite(n))throw new Error('nan');return n});
}
var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion:reduce)').matches;
function paint(){
  var ready=val.u!==null&&val.v!==null;
  [].forEach.call(document.querySelectorAll('[data-vcw]'),function(e){var m=+e.getAttribute('data-vcmin')||0;e.hidden=!ready||val.u<m});
  if(!ready)return;
  [].forEach.call(document.querySelectorAll('[data-vc]'),function(e){
    var k=e.getAttribute('data-vc'),to=val[k],from=shown[k];
    if(reduce||from===to||e.dataset.done){e.textContent=fmt(to);return}
    var t0=performance.now();e.dataset.done='1';
    (function step(t){var p=Math.min(1,(t-t0)/700),n=Math.round(from+(to-from)*(1-Math.pow(1-p,3)));e.textContent=fmt(n);if(p<1)requestAnimationFrame(step);else shown[k]=to})(t0);
  });
}
function set(k,n){val[k]=n;shown[k]=shown[k]||0;try{localStorage.setItem(KEY,JSON.stringify(val))}catch(e){}paint()}
function run(){
  var newUser=live&&writable(localStorage)&&!localStorage.getItem('bba_v');
  var newSess=live&&writable(sessionStorage)&&!sessionStorage.getItem('bba_s');
  var pu=call(newUser?'hit':'get',C.U).then(function(n){if(newUser)try{localStorage.setItem('bba_v','1')}catch(e){}return n});
  var pv=call(newSess?'hit':'get',C.V).then(function(n){if(newSess)try{sessionStorage.setItem('bba_s','1')}catch(e){}return n});
  pu.then(function(n){set('u',n)}).catch(function(){});
  pv.then(function(n){set('v',n)}).catch(function(){});
}
window.VC={paint:paint,fmt:fmt,get:function(k){return val[k]}};
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',function(){paint();run()});else{paint();run()}
})();
