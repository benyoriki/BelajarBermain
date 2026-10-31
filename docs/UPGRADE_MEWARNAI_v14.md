# Upgrade Mewarnai v14 — Buku Belajar Anak

## Ringkasan
84 gambar (36 lama dipertahankan + 48 baru), katalog bergambar, palet 24 warna, warna favorit, penghapus, simpan PNG, bagikan, favorit gambar, dan SEO (84 halaman statis + galeri + sitemap). Beranda, Belajar, Bermain, Peringkat, Profil, dan permainan lain tidak diubah.

## File
| File | Status | Keterangan |
|---|---|---|
| `gambar-baru.js` | BARU (21,9 KB) | 48 ilustrasi SVG inline, viewBox 300×200 |
| `warna.css` | BARU (5,5 KB) | Gaya katalog/kanvas, hanya kelas `.wk .w* .tf` dan `.cv` |
| `games2.js` | DIUBAH (16,6 → 28,2 KB) | Bagian Mewarnai ditulis ulang; Garis & Labirin tidak diubah |
| `index.html` | DIUBAH | +`warna.css`, +`gambar-baru.js`, meta/SEO, tautan noscript |
| `service-worker.js` | DIUBAH | cache `bba-v26` → `bba-v27`, +2 berkas |
| `manifest.json` | DIUBAH | deskripsi + shortcut "Gambar Mewarnai" |
| `update.js`, `version.json`, `tools/rilis.js` | BARU | Update otomatis (lihat `docs/UPDATE_OTOMATIS.md`); `service-worker.js` ditulis ulang (jaringan dulu untuk kode) |
| `sitemap.xml`, `mewarnai.html`, `mewarnai-*.html`, `mewarnai-seo.css` | BARU/DIBANGUN | 86 URL; dibangun ulang dengan `node tools/bangun-seo.js` |
| `tools/qa_gambar.py`, `tools/bangun-seo.js` | BARU | QA ilustrasi & generator SEO |

Tidak diubah: `script.js`, `style.css`, `modern.css`, `bank.js`, `puzzle.js`, `suara.js`.
Tanpa framework, CDN, atau library baru. Tambahan aset: ±27 KB (JS+CSS) dan halaman SEO ±1,2 MB yang TIDAK di-precache (hanya dimuat bila dikunjungi).

## Penyimpanan
- Format `bba1` tidak berubah. `p.art` tetap `idGambar_indeks` → warna (id baru tanpa garis bawah, sehingga tidak bisa berbenturan).
- Struktur baru terpisah per profil: `p.wn = {fav:[id], cf:[warna favorit ≤6], dn:{id: tanggal poin}}`, dibuat saat dibutuhkan; migrasi lama tidak menghapusnya.
- Perubahan perilaku: gambar yang dibuka kembali melanjutkan warna tersimpan (sebelumnya dihapus tiap sesi). Perlindungan poin diganti: wajib ≥2 ketukan warna di sesi itu, ≥ batas bagian sesuai `dif()`, hanya sekali per gambar per hari, plus `G.done` dan `DAYCAP` yang sudah ada.
- Reset menghapus hanya warna gambar yang sedang dibuka (perlu dua ketukan agar tidak terhapus tak sengaja).

## Pemilihan gambar
Tingkat: Mudah ≤5 area, Sedang 6–9, Sulit ≥10 (dihitung otomatis). `dif()` 0–1 → Mudah, 2–3 → Sedang, 4–5 → Sulit; pilihan acak tidak mengulang 10 gambar terakhir dan jatuh ke tingkat tetangga bila kolam kecil.

## Hasil pengujian (Chromium/Playwright, klik nyata)
- `test_mewarnai_v14.py`: seluruh 84 gambar (695 area) lolos — dapat diklik, warna masuk area benar, tanpa bocor, penghitung, Undo, Redo, Reset; plus 51 uji lain (filter, cari, favorit, penghapus, anti-eksploitasi Selesai, PNG 1200×920, Bagikan + fallback, katalog/Menu, data `bba1` lama, tanpa galat JS). Total uji sesi akhir 52/52 PASS (loop 84 gambar PASS pada putaran penuh sebelumnya; putaran akhir memakai 3 gambar agar cepat).
- `test_mewarnai_offline_layout.py`: 39/39 PASS — offline dengan service worker (katalog & kanvas), 5 ukuran layar (320, 360, tablet, PC, TV 1920) tanpa scroll horizontal, palet tidak menutupi gambar, swatch ≥44 px, 13 permainan lain tetap terbuka tanpa galat.
- QA ilustrasi: luas area terlihat minimum 380 satuan² (≈ 20×20 px di HP), tidak ada bentuk keluar kanvas.
- BELUM TERUJI: Safari/iOS, perangkat sentuh fisik, Smart TV fisik, Web Share di perangkat nyata (hanya dengan stub), suara. Lakukan uji manual di HP sebelum rilis. Skrip uji lama di `tests_otomatis` yang langsung mengharapkan kanvas setelah "Mulai Main" perlu menyesuaikan karena kini katalog tampil dulu.

## Bug/perbaikan
| ID | Temuan | Perbaikan |
|---|---|---|
| M01 | Reset sebelumnya langsung menghapus tanpa konfirmasi | Dua ketukan, timer aman (`later`) |
| M02 | Palet hanya 12 warna (+hapus) | 24 warna, favorit, penghapus |
| M03 | Warna lama dihapus tiap sesi (hilang progres) | Lanjut dari warna tersimpan; poin dijaga per gambar/hari |
| M04 | Pemilihan gambar bergantung urutan jumlah bentuk, bisa memberi gambar sama berulang | Kolam per tingkat + riwayat 10 gambar |
| M05 | Gambar lama tanpa pembulatan sambungan garis | `stroke-linejoin:round` |
| M06 | Tidak ada cara menyimpan/membagikan karya | PNG + Web Share + fallback unduh |
| T01 | Uji awal: titik klik dekat tepi bentuk menyebabkan galat uji (bukan bug aplikasi) | Uji memilih titik dalam area |

## Catatan jujur
- 36 gambar lama tetap bergaya geometris sederhana (sesuai instruksi mempertahankan). 48 gambar baru bergaya lebih kartun tetapi digambar manual dalam kode; mungkin perlu dipoles ilustrator.
- Gambar dengan 4 area (mangga, wortel) ada di bawah target 6 area karena tingkat Mudah.
- SEO: struktur data, sitemap, dan halaman statis meningkatkan kemudahan ditemukan, tetapi peringkat Google tidak dapat dijamin. Daftarkan sitemap di Google Search Console.
- Header masih menampilkan "Sistem Update v13" karena ada di luar lingkup (tidak diubah).

## Daftar 84 gambar
| No | ID | Nama | Kategori | Area | Tingkat | Asal |
|---|---|---|---|---|---|---|
| 1 | kucing | Kucing | Hewan darat | 9 | Sedang | lama |
| 2 | anjing | Anjing | Hewan darat | 9 | Sedang | lama |
| 3 | singa | Singa | Hewan darat | 11 | Sulit | lama |
| 4 | gajah | Gajah | Hewan darat | 9 | Sedang | lama |
| 5 | kelinci | Kelinci | Hewan darat | 9 | Sedang | lama |
| 6 | beruang | Beruang | Hewan darat | 10 | Sulit | lama |
| 7 | monyet | Monyet | Hewan darat | 10 | Sulit | lama |
| 8 | rubah | Rubah | Hewan darat | 10 | Sulit | lama |
| 9 | rusa | Rusa | Hewan darat | 9 | Sedang | lama |
| 10 | jerapah | Jerapah | Hewan darat | 10 | Sulit | lama |
| 11 | ikan | Ikan | Hewan laut | 4 | Mudah | lama |
| 12 | paus | Paus | Hewan laut | 5 | Mudah | lama |
| 13 | penyu | Penyu | Hewan laut | 7 | Sedang | lama |
| 14 | bintang-laut | Bintang Laut | Hewan laut | 1 | Mudah | lama |
| 15 | kepiting | Kepiting | Hewan laut | 9 | Sedang | lama |
| 16 | burung-hantu | Burung Hantu | Burung | 10 | Sulit | lama |
| 17 | bebek | Bebek | Burung | 7 | Sedang | lama |
| 18 | burung | Burung Kecil | Burung | 7 | Sedang | lama |
| 19 | dino | Dino Ramah | Dinosaurus | 9 | Sedang | lama |
| 20 | brachiosaurus | Brakiosaurus | Dinosaurus | 6 | Sedang | lama |
| 21 | triceratops | Triceratops | Dinosaurus | 9 | Sedang | lama |
| 22 | stegosaurus | Stegosaurus | Dinosaurus | 8 | Sedang | lama |
| 23 | apel | Apel | Buah dan sayuran | 3 | Mudah | lama |
| 24 | pisang | Pisang | Buah dan sayuran | 2 | Mudah | lama |
| 25 | semangka | Semangka | Buah dan sayuran | 5 | Mudah | lama |
| 26 | nanas | Nanas | Buah dan sayuran | 5 | Mudah | lama |
| 27 | mobil | Mobil | Kendaraan | 8 | Sedang | lama |
| 28 | kapal | Kapal | Kendaraan | 7 | Sedang | lama |
| 29 | pesawat | Pesawat | Kendaraan | 7 | Sedang | lama |
| 30 | rumah | Rumah | Benda | 5 | Mudah | lama |
| 31 | pohon | Pohon | Tumbuhan | 4 | Mudah | lama |
| 32 | bunga | Bunga | Tumbuhan | 9 | Sedang | lama |
| 33 | matahari | Matahari | Alam | 9 | Sedang | lama |
| 34 | pelangi | Pelangi | Alam | 6 | Sedang | lama |
| 35 | awan-hujan | Awan Hujan | Alam | 7 | Sedang | lama |
| 36 | robot | Robot Bentuk | Benda | 11 | Sulit | lama |
| 37 | panda | Panda | Hewan darat | 12 | Sulit | baru v14 |
| 38 | domba | Domba | Hewan darat | 11 | Sulit | baru v14 |
| 39 | koala | Koala | Hewan darat | 10 | Sulit | baru v14 |
| 40 | kupu-kupu | Kupu-kupu | Serangga | 10 | Sulit | baru v14 |
| 41 | kuda | Kuda | Hewan darat | 11 | Sulit | baru v14 |
| 42 | zebra | Zebra | Hewan darat | 14 | Sulit | baru v14 |
| 43 | harimau | Harimau | Hewan darat | 12 | Sulit | baru v14 |
| 44 | sapi | Sapi | Hewan darat | 10 | Sulit | baru v14 |
| 45 | kambing | Kambing | Hewan darat | 8 | Sedang | baru v14 |
| 46 | lumba-lumba | Lumba-lumba | Hewan laut | 7 | Sedang | baru v14 |
| 47 | gurita | Gurita | Hewan laut | 10 | Sulit | baru v14 |
| 48 | ubur-ubur | Ubur-ubur | Hewan laut | 8 | Sedang | baru v14 |
| 49 | hiu | Hiu | Hewan laut | 6 | Sedang | baru v14 |
| 50 | kuda-laut | Kuda Laut | Hewan laut | 6 | Sedang | baru v14 |
| 51 | ayam | Ayam | Burung | 12 | Sulit | baru v14 |
| 52 | bebek-kecil | Bebek Kecil | Burung | 9 | Sedang | baru v14 |
| 53 | merak | Merak | Burung | 12 | Sulit | baru v14 |
| 54 | burung-beo | Burung Beo | Burung | 8 | Sedang | baru v14 |
| 55 | lebah | Lebah | Serangga | 7 | Sedang | baru v14 |
| 56 | kepik | Kepik | Serangga | 12 | Sulit | baru v14 |
| 57 | capung | Capung | Serangga | 9 | Sedang | baru v14 |
| 58 | mawar | Mawar | Tumbuhan | 9 | Sedang | baru v14 |
| 59 | tulip | Tulip | Tumbuhan | 6 | Sedang | baru v14 |
| 60 | bunga-matahari | Bunga Matahari | Tumbuhan | 13 | Sulit | baru v14 |
| 61 | kaktus | Kaktus | Tumbuhan | 8 | Sedang | baru v14 |
| 62 | taman-bunga | Taman Bunga | Tumbuhan | 13 | Sulit | baru v14 |
| 63 | stroberi | Stroberi | Buah dan sayuran | 5 | Mudah | baru v14 |
| 64 | jeruk | Jeruk | Buah dan sayuran | 5 | Mudah | baru v14 |
| 65 | anggur | Anggur | Buah dan sayuran | 12 | Sulit | baru v14 |
| 66 | mangga | Mangga | Buah dan sayuran | 4 | Mudah | baru v14 |
| 67 | wortel | Wortel | Buah dan sayuran | 4 | Mudah | baru v14 |
| 68 | jagung | Jagung | Buah dan sayuran | 5 | Mudah | baru v14 |
| 69 | brokoli | Brokoli | Buah dan sayuran | 6 | Sedang | baru v14 |
| 70 | tomat | Tomat | Buah dan sayuran | 6 | Sedang | baru v14 |
| 71 | kereta-api | Kereta Api | Kendaraan | 14 | Sulit | baru v14 |
| 72 | bus-sekolah | Bus Sekolah | Kendaraan | 10 | Sulit | baru v14 |
| 73 | traktor | Traktor | Kendaraan | 9 | Sedang | baru v14 |
| 74 | ekskavator | Ekskavator | Kendaraan | 12 | Sulit | baru v14 |
| 75 | dokter | Dokter | Profesi | 8 | Sedang | baru v14 |
| 76 | polisi | Polisi | Profesi | 9 | Sedang | baru v14 |
| 77 | pemadam-kebakaran | Pemadam Kebakaran | Profesi | 8 | Sedang | baru v14 |
| 78 | koki | Koki | Profesi | 8 | Sedang | baru v14 |
| 79 | rumah-jamur | Rumah Jamur | Benda | 9 | Sedang | baru v14 |
| 80 | layang-layang | Layang-layang | Benda | 9 | Sedang | baru v14 |
| 81 | es-krim | Es Krim | Benda | 5 | Mudah | baru v14 |
| 82 | roket | Roket | Luar angkasa | 11 | Sulit | baru v14 |
| 83 | astronaut | Astronaut | Luar angkasa | 9 | Sedang | baru v14 |
| 84 | saturnus | Planet Saturnus | Luar angkasa | 8 | Sedang | baru v14 |

Ringkasan tingkat: Mudah 15, Sedang 43, Sulit 26
