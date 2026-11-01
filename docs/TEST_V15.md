# Hasil Pengujian v15

**Jenis bukti:** otomatis — Chromium 141 (Playwright) melawan server lokal, ketukan/klik/keyboard nyata. **Bukan** perangkat fisik (HP Android, Smart TV, remote asli) dan bukan hosting produksi.

## Fungsional: 166/166 PASS
| Area | PASS | FAIL |
|---|---|---|
| pola | 6 | 0 |
| hitung | 6 | 0 |
| huruf | 6 | 0 |
| tambah | 6 | 0 |
| ganjil | 6 | 0 |
| bayangan | 6 | 0 |
| beda | 4 | 0 |
| spy | 4 | 0 |
| garis | 6 | 0 |
| memori | 4 | 0 |
| urut | 8 | 0 |
| labirin | 8 | 0 |
| labirin@320x568 | 5 | 0 |
| labirin@360x640 | 5 | 0 |
| labirin@390x844 | 5 | 0 |
| labirin@430x932 | 5 | 0 |
| labirin@768x1024 | 5 | 0 |
| warna | 25 | 0 |
| puzzle | 22 | 0 |
| navigasi | 9 | 0 |
| header | 1 | 0 |
| permainan | 1 | 0 |
| data | 3 | 0 |
| keyboard | 1 | 0 |
| TV | 4 | 0 |
| offline | 5 | 0 |

Rincian: `hasil_v15_fungsional.json`. Skrip: `docs/tests_v15/`. Catatan: pada putaran pertama 2 uji gagal karena kesalahan skrip uji (bukan aplikasi) dan diperbaiki lalu diulang; semua lulus pada putaran akhir.

## Tata letak: 10 ukuran × 39 layar
320×568, 360×740, 390×844, 430×932, 768×1024, 1366×768, 1280×720 (TV), 1920×1080 (TV), landscape 740×360 dan 844×390. Diukur: scroll horizontal, elemen keluar layar, tombol tertutup navigasi, target sentuh <40px, D-pad Labirin, error JS.
Hasil: 0 scroll horizontal, 0 terpotong, 0 error JS. Catatan jujur:
- 320px, puzzle 35 keping: kotak papan 37px (7 kolom); ada tombol Zoom. Ukuran papan tidak diubah.
- Landscape 740: satu peringatan `navoverlap` ternyata positif palsu (render lambat `content-visibility`), terverifikasi tidak tertutup.
- 320×568: dasar D-pad 4px dari tepi layar; terlihat tanpa scroll tapi sangat pas.

## Belum teruji (butuh perangkat fisik)
Suara terdengar, gesekan di HP asli/gestur Android, instal PWA, remote Smart TV, berbagi ke WhatsApp, performa HP lama. Pakai `CHECKLIST_MANUAL.md`.

## Verifikasi dokumentasi lama
Dokumen lama di `docs/` memakai penomoran v19–v26 dan merujuk `tools/` serta halaman SEO di root, tidak cocok dengan ZIP v14. Klaim 84 gambar, 24 warna, 14 permainan, kunci `bba1` terbukti sesuai kode; letak `tools/` dan halaman SEO tidak sesuai (diperbaiki di v15). Laporan lama hanya arsip.
