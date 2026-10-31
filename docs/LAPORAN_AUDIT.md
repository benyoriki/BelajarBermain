# LAPORAN AUDIT — Buku Belajar Anak v20.1 (audit permainan)

Sumber kebenaran: kode proyek terbaru di sesi ini (v19.5). Tidak ada ZIP baru yang dilampirkan bersama permintaan audit, sehingga audit dilakukan pada hasil putaran sebelumnya. Backup: `Buku_Belajar_Anak_v19.5_BACKUP_sebelum_audit.zip`.

## 1. Inventaris arsitektur
| File | Fungsi |
|---|---|
| `index.html` | Cangkang, layar loading (3 dtk), urutan `<script defer>`: ikon → pengunjung → bank → script → games2 → puzzle → suara |
| `script.js` | Inti: penyimpanan `bba1`, profil, poin/level/lencana (`add/ok/bad/fin`), navigasi (`ACT.nav`), render, kuis (`GEN`, `next`, `ans`), Cari Perbedaan/I Spy (`findR`,`bd`), Memori (`mem`,`flip`), Ingat Urutan (`simon`,`sPlay`,`sp`), keyboard/TV |
| `bank.js` | Katalog 87 aset sprite + bank 950 soal (hitung 180, tambah 680, pola 42, huruf 48) dengan validasi otomatis |
| `games2.js` | Mewarnai (36 gambar SVG), Menghubungkan Garis (7 jenis), Labirin (3 babak) |
| `puzzle.js` | Puzzle Petualangan (menu, 7 tingkat, drag + ketuk, timer, jeda) |
| `suara.js` | Musik/efek, modal pengaturan suara, modal donasi, kartu donasi |
| `service-worker.js` / `manifest.json` | PWA: cache-first, precache 26 berkas, audio via Range |

Pemicu permainan: `ACT.play(id)` → `start(id)` → `intro(id)` → `ACT.go()` → generator permainan. Selesai: `fin()` (sekali per sesi lewat `G.done`). Keluar: `ACT.nav()` yang kini mengosongkan `G`.

## 2. Bug yang ditemukan dan diperbaiki
| ID | Tingkat | Bug | Bukti | Perbaikan (file) |
|---|---|---|---|---|
| B01 | Tinggi | Tantangan harian & kunci poin harian memakai tanggal UTC (berganti 07.00 WIB, bukan tengah malam) | Uji jam palsu 03.00 WIB tgl 31: `today()` = tgl 30 | `script.js` (`ymd`, `today`, `DAILY` lokal) |
| B02 | Tinggi | Mewarnai: lembar tersimpan membuat "Selesai" langsung memberi +20 tanpa mewarnai (tambang poin) | Terbukti pada v19.5 | `games2.js` (lembar baru tiap sesi) |
| B03 | Sedang | Mewarnai: Reset mengganti ke gambar lain; "Gambar lain" bisa memilih gambar yang sama | Terbukti (pelangi→rumah) | `games2.js` (`color(keep)`, `pickDr(last)`) |
| B04 | Tinggi | Puzzle: tiap sesi baru memberi +20 walau puzzle sudah pernah diselesaikan | Terbukti (+20) | `puzzle.js` (hadiah hanya untuk penyelesaian pertama) |
| B05 | Tinggi | Timer tidak dibersihkan: keluar tepat setelah babak Labirin selesai → labirin baru menimpa Beranda; hal serupa pada selesai/Memori/Ingat Urutan/Puzzle | Terbukti pada Labirin | `script.js` (`later()`, `nav` mengosongkan `G`, guard `fin`), `games2.js`, `puzzle.js` |
| B06 | Sedang | Ingat Urutan: setelah salah, ketukan selama jeda 900 ms masih diterima dan replay bisa bertumpuk; urutan input tidak direset; tidak ada tombol Ulangi contoh | Terbukti | `script.js` (kunci langsung, `G.pv`, `srep`) |
| B07 | Tinggi | Poin tanpa batas lewat Main Lagi berulang | Analisis + uji batas | `script.js` (`DAYCAP=600`/hari/profil; lihat §4) |
| B08 | Tinggi | Data `bba1` rusak ditimpa diam-diam; profil lama tanpa kolom `days/art` membuat error saat poin ditambah | Terbukti (`Cannot read properties of undefined`) | `script.js` (salinan `bba1_rusak`, migrasi tipe data tanpa menghapus apa pun) |
| B09 | Sedang | Penyimpanan penuh/dimatikan gagal tanpa pesan | Analisis kode | `script.js` (toast ramah sekali) |
| B10 | Sedang | Soal bisa berulang dalam satu sesi (generator Mana yang Beda?/Bayangan) | Analisis kode | `script.js` (`G.seen` di `next`) |
| B11 | Rendah | Cari Perbedaan/I Spy: ketukan setelah semua target ditemukan masih dihitung salah dan memutus beruntun | Uji | `script.js` (guard `bd`) |
| B12 | Rendah | Garis: koordinat garis tidak mengikuti resize/rotasi | Tidak terbukti pada uji 340 px; perbaikan pencegahan | `script.js` (`redrawL`) |
| B13 | Sedang | Tambah Bergambar mode bank hanya penjumlahan; usia 7–8 tidak ada pengurangan | Analisis kode | `script.js` (pengurangan, diverifikasi 900 soal) |
| B14 | Sedang | Anak tidak bisa memilih tingkat lebih mudah/lebih sulit | Analisis kode | `script.js` (tombol 🌱 Lebih mudah / ⭐ Pas / 🚀 Lebih seru, tersimpan per profil) |
| B15 | Rendah | "Dimainkan" tidak dibedakan dari "selesai" | Analisis kode | `script.js` (`p.played`) |
| B16 | Rendah | Palet warna 42 px; kartu Memori terlalu tinggi di HP landscape; ikon hati donasi terpotong | Ukur layout | `modern.css` |
| B17 | Rendah | Efek `lagu_7` berbunyi walau `fin()` ditolak | Analisis kode | `suara.js` |
| B18 | Rendah | Tidak ada pemberitahuan versi baru; `qris.png` tidak di-precache | Analisis kode | `script.js`, `service-worker.js` (`bba-v26`) |
| B19 | Sedang | 9 permainan (Pola, Hitung, Huruf, Tambah, Mana yang Beda, Bayangan, Cari Perbedaan, I Spy, Memori) tidak punya tombol Ulangi maupun Kembali ke Menu di dalam layar; Ingat Urutan tidak punya mulai-ulang | Dipetakan dari DOM tiap layar permainan | `script.js` (kontrol seragam `.gctl`, `ACT.rst`), `modern.css` |

## 2b. Verifikasi per permainan
Setiap dari 14 permainan diuji individual pada 9 dimensi (input, jawaban, menang, reset, keluar, pengulangan, skor, refresh, responsif) di emulasi HP dan desktop — lihat `TEST_MATRIX.md` bagian A–C. Lolos pemeriksaan sintaks tidak dipakai sebagai bukti. Kompatibilitas `bba1`: tidak ada perubahan format; uji data lama 2 profil (foto, kolom tak dikenal, lencana, pengaturan suara) × 14 permainan, migrasi idempoten, data rusak disalin ke `bba1_rusak`, dan kuota penuh tidak membuat crash.

## 3. Fitur yang diperiksa dan sudah berfungsi (tidak diubah)
Pembuatan profil, avatar, simpan/muat profil, bank soal (0 galat validasi; 900 soal acak tanpa NaN/duplikat/negatif), pilihan jawaban ditentukan dari data (bukan posisi), jawaban salah tidak mengurangi poin, Labirin (135 labirin acak semuanya dapat diselesaikan), Memori (pasangan lengkap), Garis (108 papan acak tanpa pasangan ambigu), navigasi keyboard/TV, modal tertutup dengan Escape, offline (8 permainan + sprite), pembaruan cache menghapus versi lama dan progres tetap.

## 4. Aturan poin (satu sumber: `script.js`)
| Kejadian | Poin |
|---|---|
| Jawaban benar | +10 |
| Setiap kelipatan 5 jawaban benar beruntun | +10 bonus |
| Aktivitas selesai (`fin`, sekali per sesi) | +20 |
| Tantangan harian (sekali per hari lokal, di luar batas harian) | +30 |
| Labirin: semua bintang di satu babak | +5 |
| Puzzle: penyelesaian pertama per gambar per tingkat | +10 + 5 × tingkat |
| Jawaban salah | 0 (tidak pernah mengurangi) |
| **Batas harian per profil (BARU)** | **600 poin** (selebihnya tetap bisa bermain, tanpa poin) |

Level: 0 / 100 / 300 / 600 / 1000 poin (tidak turun). **PERUBAHAN ATURAN YANG PERLU PERSETUJUAN ANDA:** batas 600/hari adalah satu-satunya pengubah saldo masa depan; saldo lama tidak berkurang. Ubah nilai `DAYCAP` di `script.js` jika kurang cocok. Transisi UTC→lokal: pada hari pergantian, bonus tantangan harian bisa terhitung dua kali sekali saja.

## 5. Yang BELUM diuji / belum selesai
- Perangkat fisik: HP Android, Smart TV sungguhan, tablet; yang diuji hanya emulasi viewport Chromium dan keyboard. Sentuhan nyata (swipe Labirin, seret keping/garis dengan jari), stylus, multitouch belum diuji.
- Browser lain (Safari/iOS, Firefox) belum diuji.
- Audio tidak didengar langsung (hanya dicatat file apa yang diputar); musik latar `lagu_01.mp3` (1,5 MB) tidak di-precache sehingga offline hanya jika sudah pernah diputar saat online.
- Instal PWA (A2HS) belum diuji; performa di HP menengah belum diukur.
- Hosting produksi belum diuji (semua uji lokal).
- Fallback generator lama `huruf` (aktif hanya bila `bank.js` gagal dimuat) dapat menghasilkan huruf ganda; tidak diperbaiki karena tidak terjangkau selama bank termuat.
- Mewarnai: Bintang Laut (1 area) dan Pisang (2 area) sangat sederhana; masih dapat diselesaikan.
- Puzzle tidak masuk rotasi tantangan harian (13 permainan), sama seperti sebelumnya.
- Cerita Tiga Dino proyek terpisah; tidak terhubung ke poin.
- Nada sintetis Ingat Urutan/Labirin dipertahankan (bagian permainan).

## 6. File yang diubah (v19.5 → v20.0)
`script.js`, `games2.js`, `puzzle.js`, `suara.js`, `modern.css`, `service-worker.js`, `README.md`. Berkas baru: `docs/`. Tidak ada aset gambar/audio diubah.

## 7. Deploy
1. Ekstrak ZIP; unggah **isi** folder `Buku_anak/` (termasuk `docs/` boleh diabaikan) ke repositori situs utama, commit.
2. Tunggu 1–2 menit, buka situs, muat ulang dua kali; muncul toast "Versi baru sudah siap" lalu cache `bba-v26` aktif.
3. Pemulihan: ganti dengan isi `Buku_Belajar_Anak_v19.5_BACKUP_sebelum_audit.zip`. Data anak di `localStorage` kunci `bba1` tidak berubah oleh pemulihan.
4. Situs cerita tidak perlu diunggah ulang.
