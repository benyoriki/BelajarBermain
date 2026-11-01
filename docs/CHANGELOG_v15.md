# Perubahan v15 (dari v14 redesign)

## Temuan audit v14 (terbukti di screenshot `docs/screenshots_v14_sebelum/`)
1. Puzzle: tombol Main Puzzle + Beranda melayang menutupi langkah karakter; semua langkah tampil sekaligus dengan pilihan bawaan.
2. Labirin: D-pad tertutup navigasi bawah di HP 360×740.
3. Ingat Urutan: dua tombol Ulangi bersamaan ("Ulangi contoh" dan "Ulangi").
4. Mewarnai: chip kategori terpotong dan harus digeser; tombol hati besar; label tingkat dominan.
5. 85 halaman SEO berada di `mewarnai/` padahal sitemap/tautan menunjuk root (404 bila diunggah apa adanya).
6. Header lebar/TV: logo menabrak menu.

## Perubahan
- **Navigasi:** bar bawah lebih pendek (52px); di dalam permainan (HP) navigasi global disembunyikan, diganti ← dan 🔁 di header permainan. PC/TV tetap menampilkan menu di header.
- **Header permainan seragam (14 permainan):** [←] Judul [tingkat] [🔁]. Ulangi tidak lagi disisipkan di bawah.
- **Umpan balik:** salah = "💛 Hampir!", warna oranye lembut (bukan ❌ merah).
- **Layar selesai:** Main Lagi + Pilih Permainan.
- **Ingat Urutan:** indikator giliran besar berwarna (Perhatikan / Giliranmu / Hebat / Tidak apa-apa), titik progres, animasi contoh jelas (lainnya meredup), tombol "Lihat Contoh Lagi" nonaktif saat contoh jalan, satu tombol Ulangi (header). Algoritma dan skor tidak diubah.
- **Puzzle:** pilihan bertahap 1/3 → 2/3 → 3/3 → Main Puzzle; kategori 2 kolom, karakter 3 kolom (2 di <360px), tingkat 2 kolom; otomatis lanjut; pilihan tidak hilang saat kembali (karakter hanya direset jika kategori diganti); tanpa tombol Beranda; timer opsional di langkah akhir; di papan hanya kontrol yang perlu (Zoom hanya >12 keping, Jeda hanya bila timer, tombol Suara ganda dihapus).
- **Labirin:** instruksi satu baris, status ringkas, tinggi labirin responsif (`dvh`), D-pad simetris dan selalu terlihat.
- **Mewarnai:** Gambar Acak lebar penuh; pencarian; tampilan Semua/Favorit/Karyaku; tombol kategori + panel 12 kategori (tanpa geser, kategori aktif berwarna); favorit = hati kecil; kartu = nama + titik tingkat; kanvas: ← kembali ke katalog, toolbar 4+3 rapi, Selesai hijau, petunjuk geser palet.
- **TV/remote:** cincin fokus 5px kuning+ungu pada Mode TV; header lebar di TV.
- **Rilis:** halaman SEO dipindah ke root; `rilis.js`, `bangun-seo.js`, `qa_gambar.py` ke `tools/` (sesuai dokumentasi); versi cache baru; lencana v15.

## Tidak diubah
Algoritma soal/labirin/urutan, skor, `DAYCAP`, kunci `bba1`, profil, level, peringkat, suara, manifest, aset, 84 gambar, 24 warna, 7 tingkat puzzle. Tidak ada library/CDN baru, tidak ada migrasi data. Tambahan CSS ±9 KB.

## File diubah
`script.js`, `games2.js`, `puzzle.js`, `kids.css`, `index.html` (teks versi), `service-worker.js` + `version.json` (hash rilis), `sitemap.xml` (dibangun ulang), 85 halaman `mewarnai*.html` (pindah ke root), `docs/*` (baru). File baru: `tools/` , `docs/tests_v15`, `docs/screenshots_*`.
