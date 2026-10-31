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
Profil, poin, dan progres disimpan di browser perangkat ini. Itu bukan akun/login online: tidak ada sinkronisasi cloud, tidak terenkripsi, hilang jika data browser dihapus, dan terbaca pengguna lain di perangkat yang sama. Peringkat hanya antarprofil di perangkat ini. "Skor Belajar" bukan tes IQ atau diagnosis. Profil, foto, dan progres tidak dikirim ke server mana pun; satu-satunya yang dikirim adalah hitungan pengunjung anonim (lihat Versi 17).

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
- Musik & efek suara (folder `audio/`): `lagu_01.mp3` musik utama (loop), `lagu_5.mp3` jawaban benar, `lagu_6.mp3` jawaban salah, `lagu_7.mp3` level selesai (v19). Tombol 🔊 di header membuka **Pengaturan Suara**: Semua suara hidup / Hanya efek suara / Semua suara mati, plus volume musik. Musik baru mulai setelah anak menyentuh layar (aturan autoplay browser).
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

## Versi 17 — Penghitung pengunjung
- `pengunjung.js` menghitung **pengunjung unik** (sekali per browser) dan **kunjungan** (sekali per sesi) lewat layanan gratis Abacus, namespace `belajarbermain.online`, key `pengunjung` dan `kunjungan`. Angka tampil di footer (semua halaman) dan di layar sambutan.
- Hanya aktif di domain `belajarbermain.online`; di localhost/GitHub Pages hanya membaca angka. Ubah di objek `C` pada `pengunjung.js`.
- Keterbatasan: hitungan per browser (bukan per orang; hapus data browser = terhitung lagi), angka tidak kebal manipulasi, dan layanan gratis pihak ketiga bisa berubah. Counter kedaluwarsa jika 6 bulan tanpa akses.
- Cache `bba-v17`.

## Versi 18 — Tampilan modern 2026 (tetap ringan)
- `modern.css` (lapisan tampilan): latar aurora pastel, header & dock navigasi kaca, kartu dan tombol lebih halus, hero beranda bergradasi, layar sambutan 2 kolom di PC, animasi muncul saat scroll (CSS murni, otomatis mati bila "kurangi gerakan").
- Font lokal `fonts/` (Fredoka untuk judul, Nunito untuk teks; total ±69 KB, lisensi OFL) agar tampil seragam di semua perangkat. Tanpa library tambahan.
- Perbaikan: header tidak lagi tinggi/kosong di layar sambutan (bentrok nama class), header tidak sesak di lebar 800–1100 px (mode desktop di HP), kartu permainan tidak lagi menyisakan baris yatim (Belajar 6 kartu, Bermain 8 kartu), layar loading 1,8 dtk pada kunjungan pertama dan 0,25 dtk berikutnya (sebelumnya selalu 3 dtk).
- Pill "N pengunjung" di layar sambutan baru muncul jika pengunjung ≥ 50 (bukti sosial yang kuat); angka di footer selalu tampil.
- Cache `bba-v18`.

## Versi 19
- **Lebih ringan**: loader pendek (0,5 dtk, bukan 1,8 dtk), skrip `defer`, tanpa blur/backdrop-filter, tanpa animasi denyut box-shadow & animasi scroll-driven, animasi loncat berhenti sendiri, `lagu_01.mp3` 2,9 MB → 1,4 MB (64 kbps mono) dan tidak lagi diunduh paksa saat instal (disimpan otomatis setelah pertama diputar).
- **Suara baru**: `lagu_5.mp3` (benar), `lagu_6.mp3` (salah), `lagu_7.mp3` (level selesai). Untuk menukar peran, ubah `SFXF` di `suara.js`. `lagu_02/03/04` dihapus. Cache `bba-v20`.
- **Tombol Pasang** kini hanya ikon unduh.
- **Tombol gambar "Mulai Cerita"** (`mulai-cerita-500.webp`, `mulai-cerita-1000.webp`) di layar awal dan dasbor; membuka https://benyoriki.github.io/Kisah3Dino/ di tab yang sama (`location.replace`).

## Versi 19.1
- Jendela "Terima Kasih Telah Peduli" didesain ulang (header lembut, manfaat, kartu QRIS, langkah, penutup) dengan teks baru.
- Tombol "Donasi untuk Pengembangan" dan penghitung pengunjung di footer hanya tampil di Beranda; di Belajar, Bermain, Peringkat, dan Profil footer hanya berisi teks. Cache `bba-v20`.

## Versi 19.2
- Ikon play (`tombol-play.webp`, 30 KB) ditumpuk di tombol "Mulai Cerita" dengan animasi memantul + cincin berdenyut (hanya transform/opacity, ringan; mati otomatis jika perangkat meminta gerakan dikurangi).
- Tombol "Dukung via QRIS" dihapus; kartu donasi di Beranda dan Profil kini memakai tombol "Donasi untuk Pengembangan". Tombol donasi di footer dihapus. Cache `bba-v21`.

## Versi 19.3 — Integrasi Mulai Cerita (proyek cerita terpisah)
- Cerita Tiga Dino adalah **proyek terpisah** (`Kisah3Dino`, https://benyoriki.github.io/Kisah3Dino/). Tidak ada gambar, musik, atau teks cerita di repositori ini.
- Tombol/banner **Mulai Cerita** sekarang tautan `<a href>` biasa ke situs cerita di tab yang sama. Sebelumnya memakai `location.replace` lewat event handler (`data-a="dino"`), yang menghapus halaman ini dari riwayat sehingga tombol Back browser tidak kembali ke sini. Tombol 🏠 di situs cerita membuka kembali https://belajarbermain.online/.
- Jika perangkat sedang offline, tombol menampilkan pesan "Cerita butuh internet" alih-alih membuka halaman galat browser. Mode offline situs ini **tidak** membuat situs cerita tersedia offline.
- Service worker situs ini hanya menangani permintaan satu-origin; navigasi ke situs cerita tidak dicegat. Cache `bba-v22`.
- Data `localStorage` kunci `bba1` tidak diubah.

## Versi 19.4 — Perbaikan efek suara
- Bunyi "beb" (nada sintetis dari `beep()`) saat poin bertambah dan saat keping Puzzle Petualangan ditempatkan sudah dihapus.
- Pemetaan efek suara kini: **jawaban salah = `audio/lagu_5.mp3`**, **jawaban benar = `audio/lagu_6.mp3`**, **aktivitas/level selesai = `audio/lagu_7.mp3`** (diatur di `SFXF` pada `suara.js`). Puzzle Petualangan ikut memakai suara benar/salah yang sama lewat `sfxPlay()`.
- Nada sintetis yang tersisa sengaja dipertahankan karena bagian dari permainan, bukan umpan jawaban: nada tombol warna di Ingat Urutan, langkah/dinding di Labirin, dan ketukan karakter di galeri. Beri tahu jika ingin dihapus juga.
- Cache `bba-v23`.

## Versi 19.5
- **Layar loading selalu 3 detik** (kunjungan pertama maupun berikutnya): `min=3000` di skrip loader `index.html`, bilah progres 3 dtk (`modern.css`), loncat dino 4 kali (`style.css`). Pengaman jika halaman macet: tertutup otomatis di 5 detik.
- **Teks donasi baru** (kartu donasi di Beranda/Profil dan jendela QRIS) di `suara.js`, mengikuti naskah "Bantu Buku Belajar Anak Terus Bertumbuh". Tombol kini "Dukung Sekarang". QRIS, nama, dan NMID tidak berubah. Cache `bba-v24`.

## Versi 20.1 — Audit permainan
Laporan lengkap: `docs/LAPORAN_AUDIT.md`; matriks uji: `docs/TEST_MATRIX.md`; uji manual: `docs/CHECKLIST_MANUAL.md`; skrip uji otomatis (Playwright): `docs/tests_otomatis/`.
Ringkas: tanggal harian lokal; batas poin 600/hari (konstanta `DAYCAP`, perlu persetujuan); lembar Mewarnai baru tiap sesi; hadiah Puzzle hanya penyelesaian pertama; timer permainan batal saat keluar; Ingat Urutan terkunci saat jeda + tombol Ulangi contoh; migrasi aman `bba1` (data rusak disalin ke `bba1_rusak`); pilihan tingkat Lebih mudah/Pas/Lebih seru; pengurangan untuk 7–8 tahun; dedupe soal; notifikasi versi baru; cache `bba-v26`; kontrol Ulangi + Menu seragam di dalam semua permainan.

## Versi 20.2 — Pratinjau tautan WhatsApp
Gambar baru `preview-wa.jpg` (1200×630) dan judul/deskripsi OG & Twitter yang lebih menjual (tanpa klaim "aman"/"offline"). Panduan kata-kata Status dan cara menyegarkan cache pratinjau: `docs/KATA_PROMOSI_WHATSAPP.md`.
