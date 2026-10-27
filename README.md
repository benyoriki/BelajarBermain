# Buku Belajar Anak
Belajar, Bermain, Tumbuh dengan Ceria! — Developed by @benyoriki

## Cara memasang di GitHub Pages
1. Buat repository baru di github.com (mis. `BukuBelajarAnak`, Public).
2. Klik **Add file › Upload files**, unggah SEMUA file (index.html, style.css, script.js, manifest.json, service-worker.js, icon-192.png, icon-512.png, README.md) langsung di root, tanpa folder. Klik **Commit changes**.
3. Buka **Settings › Pages**, pilih Source **Deploy from a branch**, branch `main`, folder `/ (root)`, Save.
4. Tunggu 1–2 menit; akses di `https://belajarbermain.online/` (HTTPS, wajib untuk PWA).

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

## Versi 7
File baru: `aset.webp` (91 gambar hewan, buah, benda), `preview.jpg` (pratinjau WhatsApp 1200x628), `icon-maskable-512.png`, `apple-touch-icon.png`. Setelah mengubah gambar pratinjau, WhatsApp menyimpan cache lama; kirim tautan dengan `?v=2` di belakangnya, atau gunakan https://developers.facebook.com/tools/debug/ untuk menyegarkan.

## Versi 8 (tahap 1 upgrade)
File baru `bank.js` (katalog aset ber-ID + bank soal tervalidasi untuk Hitung, Tambah, Pola, Huruf). Unggah ke root bersama script.js, index.html, style.css, service-worker.js. Cache `bba-v8`. Hapus `README-1.md` (salinan lama).

## Versi 9
File baru `games2.js` (Mewarnai 35 gambar, Menghubungkan Garis 7 jenis + seret, Labirin 3 babak). Loading screen 3 detik di index.html + style.css. Cache `bba-v9`.

## Versi 10
File baru `puzzle.js` (Puzzle Petualangan, 7 tingkat). Unggah juga `puzzle.js`; cache `bba-v10`.

## Versi 11
- Musik & efek suara (folder `audio/`): `lagu_01.mp3` musik utama (loop), `lagu_02.mp3` jawaban benar, `lagu_03.mp3` level selesai, `lagu_04.mp3` jawaban salah. Tombol 🔊 di header membuka **Pengaturan Suara**: Semua suara hidup / Hanya efek suara / Semua suara mati, plus volume musik. Musik baru mulai setelah anak menyentuh layar (aturan autoplay browser).
- `lagu_01.mp3` dikompres ke 128 kbps (±2,9 MB) agar ringan untuk data seluler.
- `benyoriki.com` di layar loading dan footer kini tautan yang membuka tab baru.
- Tombol & halaman **Donasi QRIS** (`qris.png`, dengan tombol Unduh). Untuk mengganti QRIS, timpa `qris.png` dan ubah nama/NMID di `suara.js` (`QRIS_NAME`, `NMID`).
- File baru: `suara.js`, `qris.png`, `audio/*`. Cache `bba-v13` (v11.1: kartu Orang Tua & Dukungan didesain ulang).

## Versi 13
- Ikon menu permainan diganti SVG buatan sendiri (`ikon.js`) dengan palet warna baru; tampil jelas di HP dan PC. Warna kartu diatur di `GCOL` pada `ikon.js`.
- Lencana "Sistem Update v13" di bawah judul (header & layar loading). File baru: `ikon.js`. Cache `bba-v13`.

## Domain baru
Domain website: **https://belajarbermain.online/** (canonical, Open Graph, dan Twitter image di `index.html`). Link `benyoriki.com` tetap mengarah ke website pengembang. Pratinjau WhatsApp bisa tersimpan cache; kirim tautan dengan `?v=2` atau segarkan lewat https://developers.facebook.com/tools/debug/.

## SEO / Google (v15)
- Judul, deskripsi, Open Graph, Twitter Card, JSON-LD (WebSite + SoftwareApplication), `robots.txt`, `sitemap.xml`, hreflang, dan teks cadangan untuk crawler sudah dipasang untuk **https://belajarbermain.online/**.
- Langkah wajib di sisi Anda: daftarkan domain di **Google Search Console** (jenis "Domain" atau "URL prefix"), verifikasi (DNS TXT atau tag meta), kirim `https://belajarbermain.online/sitemap.xml`, lalu klik **Inspeksi URL › Minta pengindeksan**. Tampilan di hasil pencarian baru berubah setelah Google meng-crawl ulang (hari hingga minggu); Google tidak menjamin tampilan snippet.

## Versi 16
Layar sambutan baru (hero, statistik, keunggulan, 3 langkah) untuk pengunjung baru & profil belum dipilih; tombol donasi di footer disembunyikan pada layar ini. Cache `bba-v16`.
