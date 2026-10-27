/* bank.js — Katalog aset + Bank Soal (Buku Belajar Anak, tahap 1)
   Sumber gambar: aset.webp (sprite 13 kolom x 8 baris). Setiap aset punya ID unik, nama, kategori, alt.
   Dimuat SEBELUM script.js. Jika file ini gagal dimuat, script.js memakai generator lama (tidak rusak). */
(function (g) {
'use strict';
// [id, nama, kategori]; null = sel sprite duplikat / belum terverifikasi, sengaja tidak dipakai.
const R = [
 [['dino-biru','Dino Biru'],['dino-merah','Dino Merah'],['dino-kuning','Dino Kuning'],['dino-hijau','Dino Hijau'],['pterodaktil','Pterodaktil'],['buaya','Buaya','hewan-darat'],['naga-ungu','Naga Ungu']],
 [['singa','Singa'],['harimau','Harimau'],['gajah','Gajah'],['panda','Panda'],['beruang','Beruang'],['monyet','Monyet'],['rubah','Rubah'],['kelinci','Kelinci'],['jerapah','Jerapah'],['rusa','Rusa'],['koala','Koala']],
 [['paus','Paus'],['lumba-lumba','Lumba-lumba'],['gurita','Gurita'],['kepiting','Kepiting'],['penyu','Penyu'],['ikan-biru','Ikan Biru'],['ikan-badut','Ikan Badut'],['kuda-laut','Kuda Laut'],['ubur-ubur','Ubur-ubur'],['bintang-laut','Bintang Laut']],
 [['beo','Burung Beo'],['penguin','Penguin'],['burung-hantu','Burung Hantu'],['burung-biru','Burung Biru'],['anak-ayam','Anak Ayam'],['katak','Katak','hewan-darat'],['kepik','Kepik'],['lebah','Lebah'],['kupu-kupu','Kupu-kupu'],['belalang','Belalang'],['siput','Siput','hewan-darat'],['semut','Semut']],
 [['apel','Apel'],['pisang','Pisang'],['jeruk','Jeruk'],['stroberi','Stroberi'],['anggur','Anggur'],['semangka','Semangka'],['nanas','Nanas'],['melon','Melon'],['mangga','Mangga'],['ceri','Ceri'],['lemon','Lemon'],['pir','Pir'],['kelapa','Kelapa']],
 [['kiwi','Kiwi'],['buah-naga','Buah Naga'],['pepaya','Pepaya'],['alpukat','Alpukat'],['blueberry','Blueberry'],['frambos','Frambos'],['manggis','Manggis'],null,['delima','Delima'],['persik','Persik'],null,null,null],
 [['mobil','Mobil','kendaraan'],['bola','Bola','benda'],['mainan-susun','Mainan Susun','benda'],['bebek-karet','Bebek Karet','benda'],['balok-abc','Balok ABC','pendidikan'],['palet','Palet Warna','benda'],['kaca-pembesar','Kaca Pembesar','benda'],['puzzle','Puzzle','benda'],['buku','Buku','benda'],['toga','Toga','pendidikan'],['lampu','Lampu','benda'],['globe','Globe','pendidikan']],
 [['pensil','Pensil','benda'],['buku-terbuka','Buku Terbuka','benda'],['papan-tulis','Papan Tulis','pendidikan'],['angka-123','Angka 123','pendidikan'],['lingkaran','Lingkaran Merah','bentuk'],['segitiga','Segitiga Kuning','bentuk'],['persegi','Persegi Biru','bentuk'],['bintang','Bintang Hijau','bentuk'],['hati','Hati Pink','bentuk'],['matahari','Matahari','alam'],['awan','Awan','alam'],['pelangi','Pelangi','alam'],['pohon','Pohon','alam']]
];
const CAT0 = ['dinosaurus','hewan-darat','hewan-air','burung-serangga','buah','buah','benda','benda'];
const ASSETS = {};
R.forEach((row, r) => row.forEach((e, c) => { if (e) ASSETS[e[0]] = { id: e[0], nama: e[1], kategori: e[2] || CAT0[r], alt: 'Gambar ' + e[1], r, c, sheet: 'aset.webp' }; }));

const nm = id => ASSETS[id] ? ASSETS[id].nama : id;
const img = id => {
  const a = ASSETS[id];
  if (!a) { try { console.warn('Aset hilang:', id); } catch (e) {} return '<span class="miss">' + String(id).replace(/[<>&"]/g, '') + '</span>'; }
  return '<i class="ai" role="img" aria-label="' + a.alt + '" style="--x:' + (a.c / 12 * 100).toFixed(1) + '%;--y:' + (a.r / 7 * 100).toFixed(1) + '%"></i>';
};
const imgs = (id, n) => Array(n).fill(id).map(img).join('');

const BANK = [];
// ---- Hitung & Lingkarkan: 12 objek x 15 jumlah. Usia 0: 1-5, usia 1: 6-10, usia 2: 11-15
const HO = ['apel','pisang','stroberi','ikan-biru','kupu-kupu','mobil','bintang','bola','dino-biru','burung-biru','lebah','kepik'];
HO.forEach(o => { for (let n = 1; n <= 15; n++) {
  const age = n <= 5 ? 0 : n <= 10 ? 1 : 2;
  BANK.push({ id: 'hitung-' + o + '-' + n, game: 'hitung', age, diff: age + 1, assets: [o], n, answer: n,
    options: [n + 1, n - 1, n + 2, n - 2].filter(x => x > 0).slice(0, 2).concat(n),
    hint: 'Ketuk satu per satu sambil menghitung.', explain: 'Ada ' + n + ' ' + nm(o) + '.', points: 10 });
} });
// ---- Tambah Bergambar: 8 objek; usia 0 jumlah<=5, usia 1 jumlah 6-10, usia 2 jumlah 11-15 (a,b>=1)
['apel','pisang','stroberi','ikan-biru','mobil','dino-biru','bola','lebah'].forEach(o => {
  for (let a = 1; a <= 12; a++) for (let b = 1; b <= 12; b++) {
    const c = a + b; if (c > 15 || (c > 10 && (a < 3 || b < 3))) continue;
    const age = c <= 5 ? 0 : c <= 10 ? 1 : 2;
    BANK.push({ id: 'tambah-' + o + '-' + a + '-' + b, game: 'tambah', age, diff: age + 1, assets: [o], a, b, answer: c,
      options: [c + 1, c - 1, c + 2, c - 2].filter(x => x > 0).slice(0, 2).concat(c),
      hint: 'Hitung kelompok pertama, lalu lanjutkan menghitung kelompok kedua.',
      explain: a + ' ' + nm(o) + ' + ' + b + ' ' + nm(o) + ' = ' + c + ' ' + nm(o) + '.', points: 10 });
  }
});
// ---- Pola & Logika: 7 tema x 6 pola = 42 soal
const TH = {
  bentuk: ['lingkaran','segitiga','persegi','bintang','hati'],
  buah: ['apel','pisang','jeruk','stroberi','anggur','semangka'],
  hewan: ['singa','gajah','panda','kelinci','monyet','rubah'],
  dino: ['dino-biru','dino-merah','dino-kuning','dino-hijau','pterodaktil'],
  laut: ['paus','penyu','kepiting','gurita','ikan-badut'],
  serangga: ['lebah','kepik','kupu-kupu','semut','belalang'],
  alam: ['matahari','awan','pelangi','pohon','bola']
};
const PT = [['ab',0],['aab',0],['abc',1],['abb',1],['aabb',2],['abcb',2]];
Object.keys(TH).forEach((t, ti) => PT.forEach(([p, age], pi) => {
  const L = TH[t], k = (ti + pi) % L.length, rot = L.slice(k).concat(L.slice(0, k)), map = { a: rot[0], b: rot[1], c: rot[2] };
  const len = Math.max(5, 2 * p.length - 1), seq = [...Array(len)].map((_, i) => map[p[i % p.length]]), ans = map[p[len % p.length]];
  const ds = rot.filter(x => x !== ans).slice(0, age === 2 ? 3 : 2);
  BANK.push({ id: 'pola-' + t + '-' + p, game: 'pola', age, diff: age + 1, assets: seq.concat(ds), seq, answer: ans, options: [ans].concat(ds),
    hint: 'Cari bagian yang berulang.', explain: 'Polanya ' + p.toUpperCase().split('').join('-') + ' berulang, jadi berikutnya ' + nm(ans) + '.', points: 10 });
}));
// ---- Huruf & Kata: 16 kata; awal huruf (usia 0), huruf hilang (usia 1: huruf ke-2, usia 2: huruf terakhir)
const HW = [['apel','Apel'],['bola','Bola'],['ceri','Ceri'],['dino-biru','Dino'],['gajah','Gajah'],['harimau','Harimau'],['ikan-biru','Ikan'],['jeruk','Jeruk'],['kepik','Kepik'],['lebah','Lebah'],['mangga','Mangga'],['nanas','Nanas'],['panda','Panda'],['rusa','Rusa'],['semut','Semut'],['toga','Toga']];
const LET = 'AIUEOKLMNRST';
const dl = (ans, k) => { const r = []; for (let i = 0; r.length < 3; i++) { const x = LET[(k + i * 3) % LET.length]; if (x !== ans && !r.includes(x)) r.push(x); } return r; };
HW.forEach(([id, w], k) => {
  const W = w.toUpperCase(), F = W[0];
  BANK.push({ id: 'huruf-awal-' + id, game: 'huruf', kind: 'awal', age: 0, diff: 1, assets: [id], word: w, answer: F, options: [F].concat(dl(F, k)), hint: 'Ucapkan nama gambar, dengarkan bunyi pertamanya.', explain: w + ' diawali huruf ' + F + '.', points: 10 });
  [[1, 1], [2, W.length - 1]].forEach(([age, i]) => {
    const a = W[i];
    BANK.push({ id: 'huruf-hilang-' + id + '-' + i, game: 'huruf', kind: 'hilang', age, diff: age + 1, assets: [id], word: w, hide: i, answer: a, options: [a].concat(dl(a, k + i)), hint: 'Eja kata itu pelan-pelan.', explain: 'Katanya ' + W + ': huruf yang hilang adalah ' + a + '.', points: 10 });
  });
});

// ---- Validasi seluruh data
function validate(bank) {
  const e = [], seen = {}, cnt = {};
  (bank || BANK).forEach(q => {
    if (seen[q.id]) e.push('ID ganda ' + q.id); seen[q.id] = 1; cnt[q.game] = (cnt[q.game] || 0) + 1;
    q.assets.forEach(a => { if (!ASSETS[a]) e.push(q.id + ': aset hilang ' + a); });
    if (!q.options.includes(q.answer)) e.push(q.id + ': jawaban tidak ada di pilihan');
    if (new Set(q.options).size !== q.options.length) e.push(q.id + ': pilihan ganda');
    if (q.game === 'hitung' && imgs(q.assets[0], q.n).split('<i ').length - 1 !== q.answer) e.push(q.id + ': jumlah gambar != jawaban');
    if (q.game === 'tambah' && q.a + q.b !== q.answer) e.push(q.id + ': a+b != jawaban');
    if (q.game === 'huruf' && q.kind === 'awal' && q.word[0].toUpperCase() !== q.answer) e.push(q.id + ': huruf awal salah');
    if (q.game === 'huruf' && q.kind === 'hilang' && q.word.toUpperCase()[q.hide] !== q.answer) e.push(q.id + ': huruf hilang salah');
  });
  return { ok: !e.length, errors: e, counts: cnt };
}
const V = validate(), GOOD = BANK.filter(q => !V.errors.some(m => m.startsWith(q.id + ':') || m === 'ID ganda ' + q.id));
if (!V.ok) try { console.warn('Bank soal: ' + V.errors.length + ' masalah, soal bermasalah dilewati', V.errors.slice(0, 5)); } catch (e) {}

// ---- Pemilihan acak, hindari pengulangan cepat
const recent = {};
function pick(game, band, upTo) {
  let pool = GOOD.filter(q => q.game === game && (upTo ? q.age <= band : q.age === band));
  if (!pool.length) pool = GOOD.filter(q => q.game === game);
  const r = recent[game] = recent[game] || [];
  let f = pool.filter(q => !r.includes(q.id));
  if (!f.length) { recent[game] = []; f = pool; }
  const q = f[Math.floor(Math.random() * f.length)];
  recent[game].push(q.id); if (recent[game].length > Math.min(20, pool.length - 1)) recent[game].shift();
  return q;
}
g.BBA = { ASSETS, BANK: GOOD, nm, img, imgs, pick, validate };
if (typeof module !== 'undefined') module.exports = g.BBA;
})(typeof window !== 'undefined' ? window : globalThis);
