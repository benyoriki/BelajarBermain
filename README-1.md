# Buku Belajar Anak
Belajar, Bermain, Tumbuh dengan Ceria! — Developed by @benyoriki

## Cara memasang di GitHub Pages
1. Buat repository baru di github.com (mis. `BukuBelajarAnak`, Public).
2. Klik **Add file › Upload files**, unggah SEMUA file (index.html, style.css, script.js, manifest.json, service-worker.js, icon-192.png, icon-512.png, README.md) langsung di root, tanpa folder. Klik **Commit changes**.
3. Buka **Settings › Pages**, pilih Source **Deploy from a branch**, branch `main`, folder `/ (root)`, Save.
4. Tunggu 1–2 menit; akses di `https://USERNAME.github.io/BukuBelajarAnak/` (HTTPS, wajib untuk PWA).

## Instal PWA
- Android/Chrome/Edge/Windows: tombol **Pasang Aplikasi** di halaman Profil, atau menu ⋮ › Instal aplikasi.
- iPhone/iPad: Safari › Bagikan › **Tambah ke Layar Utama**.
- Smart TV: buka lewat browser TV. Dukungan instal berbeda tiap merek/sistem/browser dan tidak dijamin.

## Mode offline
Setelah dibuka sekali secara online, file dan semua soal (lokal) tersimpan oleh Service Worker sehingga bisa dimainkan tanpa internet. Indikator Online/Mode Offline tampil di header.

## LocalStorage dan keterbatasan
Profil, poin, dan progres disimpan di browser perangkat ini. Itu bukan akun/login online: tidak ada sinkronisasi cloud, tidak terenkripsi, hilang jika data browser dihapus, dan terbaca pengguna lain di perangkat yang sama. Peringkat hanya antarprofil di perangkat ini. "Skor Belajar" bukan tes IQ atau diagnosis. Tidak ada data dikirim ke server mana pun.

## Memperbarui versi / menghapus cache
Setelah mengubah file, ganti `V='bba-v1'` di service-worker.js menjadi `bba-v3` (dst.), commit, lalu muat ulang 2 kali. Manual: DevTools › Application › Clear storage, atau pengaturan situs di browser.

## Catatan versi 2
Foto profil disimpan lokal (JPEG kecil) di LocalStorage. Tombol ⬇ Pasang Aplikasi ada di header; jika browser tidak mendukung tombol otomatis, halaman panduan instal (HP, iPhone, PC, Smart TV Android) akan tampil.

Versi 3: tampilan premium (glass header, kartu 3D, cincin level, konfeti), navigasi remote TV dengan panah + OK.

## Versi 4
Unggah juga `karakter.webp` (sprite 30 karakter) ke root. Cache sekarang `bba-v4`. Mode TV dan Layar Penuh ada di halaman Profil; dukungan tiap Smart TV berbeda-beda.

## Versi 5
Kesulitan permainan mengikuti usia + level anak (6 tingkat). Cache `bba-v5`.

## Versi 6
Kartu permainan baru dengan deskripsi, latar pemandangan SVG ringan, header solid, perbaikan input foto. Cache `bba-v6`.
