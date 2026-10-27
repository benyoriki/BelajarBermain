const V='bba-v16',F=['./','index.html','style.css','script.js','bank.js','games2.js','puzzle.js','suara.js','ikon.js','manifest.json','icon-192.png','icon-512.png','karakter.webp','aset.webp','icon-maskable-512.png','qris.png','audio/lagu_02.mp3','audio/lagu_03.mp3','audio/lagu_04.mp3'],BG='audio/lagu_01.mp3';
self.addEventListener('install',e=>e.waitUntil(caches.open(V).then(c=>c.addAll(F).then(()=>{c.add(BG).catch(()=>{})})).then(()=>self.skipWaiting())));
self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==V).map(x=>caches.delete(x)))).then(()=>self.clients.claim())));
/* Audio memakai permintaan Range: jawab dari cache dengan potongan 206 agar bisa loop/seek (Safari wajib) */
async function ranged(r){
  const c=await caches.open(V),h=await c.match(r.url);
  if(!h){c.add(r.url).catch(()=>{});return fetch(r)}
  const b=await h.arrayBuffer(),m=/bytes=(\d*)-(\d*)/.exec(r.headers.get('range')||''),n=b.byteLength;
  let s=m&&m[1]?+m[1]:0,t=m&&m[2]?Math.min(+m[2],n-1):n-1;
  if(s>=n)return new Response(null,{status:416,headers:{'Content-Range':'bytes */'+n}});
  return new Response(b.slice(s,t+1),{status:206,headers:{'Content-Type':h.headers.get('Content-Type')||'audio/mpeg','Content-Range':'bytes '+s+'-'+t+'/'+n,'Content-Length':t-s+1,'Accept-Ranges':'bytes'}});
}
self.addEventListener('fetch',e=>{const r=e.request;if(r.method!=='GET'||new URL(r.url).origin!==location.origin)return;
if(r.headers.has('range')){e.respondWith(ranged(r));return}
e.respondWith(caches.match(r).then(h=>h||fetch(r).then(n=>{if(n.ok&&n.status===200){const c=n.clone();caches.open(V).then(x=>x.put(r,c))}return n}).catch(()=>r.mode==='navigate'?caches.match('index.html'):Response.error())))});
