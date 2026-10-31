/* service-worker.js — pembaruan otomatis.
   Kode (HTML/JS/CSS/JSON): JARINGAN DULU (batas 4 dtk), cadangan cache saat offline/lambat -> pengguna selalu dapat versi terbaru bila ada internet.
   Aset besar (gambar, font, audio): cache dulu agar cepat & hemat kuota.
   Jalankan `node tools/rilis.js` sebelum unggah: nomor versi (V) diperbarui otomatis dari isi berkas. */
const V='bba-0b47587b18',F=['./','index.html','style.css','script.js','bank.js','games2.js','gambar-baru.js','warna.css','puzzle.js','suara.js','update.js','ikon.js','pengunjung.js','modern.css','fonts/fredoka-latin-wght-normal.woff2','fonts/nunito-latin-wght-normal.woff2','manifest.json','icon-192.png','icon-512.png','karakter.webp','aset.webp','icon-maskable-512.png','mulai-cerita-500.webp','mulai-cerita-1000.webp','tombol-play.webp','audio/lagu_5.mp3','audio/lagu_6.mp3','audio/lagu_7.mp3','qris.png'];
self.addEventListener('install',e=>e.waitUntil(caches.open(V).then(c=>Promise.all(F.map(u=>fetch(new Request(u,{cache:'reload'})).then(r=>r.ok?c.put(u,r):0).catch(()=>0)))).then(()=>self.skipWaiting())));
self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==V).map(x=>caches.delete(x)))).then(()=>self.clients.claim())));
self.addEventListener('message',e=>{if(e.data==='SKIP_WAITING')self.skipWaiting()});
async function ranged(r){
  const c=await caches.open(V),h=await c.match(r.url);
  if(!h){c.add(r.url).catch(()=>{});return fetch(r)}
  const b=await h.arrayBuffer(),m=/bytes=(\d*)-(\d*)/.exec(r.headers.get('range')||''),n=b.byteLength;
  let s=m&&m[1]?+m[1]:0,t=m&&m[2]?Math.min(+m[2],n-1):n-1;
  if(s>=n)return new Response(null,{status:416,headers:{'Content-Range':'bytes */'+n}});
  return new Response(b.slice(s,t+1),{status:206,headers:{'Content-Type':h.headers.get('Content-Type')||'audio/mpeg','Content-Range':'bytes '+s+'-'+t+'/'+n,'Content-Length':t-s+1,'Accept-Ranges':'bytes'}});
}
const CODE=/\.(html|js|css|json|xml|webmanifest)$/i;
async function netFirst(r){const c=await caches.open(V);
  try{const n=await Promise.race([fetch(r,{cache:'no-cache'}),new Promise((_,j)=>setTimeout(()=>j(0),4000))]);if(n&&n.ok&&n.status===200)c.put(r,n.clone());return n}
  catch(x){const h=await c.match(r,{ignoreSearch:true});return h||(r.mode==='navigate'?c.match('index.html'):Response.error())}}
self.addEventListener('fetch',e=>{const r=e.request,u=new URL(r.url);if(r.method!=='GET'||u.origin!==location.origin)return;
if(r.headers.has('range')){e.respondWith(ranged(r));return}
if(u.pathname.endsWith('/version.json')){e.respondWith(fetch(r,{cache:'no-store'}).catch(()=>Response.error()));return}
if(r.mode==='navigate'||CODE.test(u.pathname)||u.pathname.endsWith('/')){e.respondWith(netFirst(r));return}
e.respondWith(caches.match(r).then(h=>h||fetch(r).then(n=>{if(n.ok&&n.status===200){const c=n.clone();caches.open(V).then(x=>x.put(r,c))}return n}).catch(()=>Response.error())))});
