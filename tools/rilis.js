/* Jalankan SEBELUM mengunggah ke GitHub Pages:  node tools/rilis.js
   - menghitung sidik jari (hash) semua berkas aplikasi -> memperbarui nomor versi cache di service-worker.js
   - menulis version.json (dibaca update.js di semua HP untuk tahu ada versi baru)
   - membangun ulang halaman SEO (tools/bangun-seo.js) */
const fs=require('fs'),cr=require('crypto'),path=require('path'),R=path.join(__dirname,'..');
require('child_process').execSync('node '+path.join(__dirname,'bangun-seo.js'),{stdio:'inherit'});
const sw=fs.readFileSync(path.join(R,'service-worker.js'),'utf8');
const list=eval(sw.match(/F=(\[.*?\]);/s)[1]).filter(f=>f!=='./').concat(['update.js','version.json'].filter(f=>f==='update.js'));
const h=cr.createHash('sha1');[...new Set(list)].sort().forEach(f=>{try{h.update(f);h.update(fs.readFileSync(path.join(R,f)))}catch(e){console.warn('lewati',f)}});
const v=h.digest('hex').slice(0,10);
fs.writeFileSync(path.join(R,'service-worker.js'),sw.replace(/const V='[^']*'/,"const V='bba-"+v+"'"));
fs.writeFileSync(path.join(R,'version.json'),JSON.stringify({v,t:new Date().toISOString()})+'\n');
console.log('Versi rilis:',v);
