# Sistem Update Otomatis

## Penyebab HP ke-2, ke-3, dst tidak ikut update
1. `service-worker.js` lama memakai **cache dulu untuk semuanya**, termasuk `index.html`, JS, dan CSS. Selama cache `bba-v26/27` ada, HP selalu menyajikan berkas lama, walau server sudah baru.
2. HP baru tahu ada versi baru hanya jika **isi `service-worker.js` berubah** (harus ingat menaikkan nomor `V`). Lupa menaikkan = tidak ada HP yang update. Browser juga memeriksa file itu paling sering sekali per ~24 jam, dan GitHub Pages men-cache berkas ±10 menit.
3. Saat pemasangan, `cache.addAll` bisa mengambil berkas dari cache HTTP browser yang masih lama, sehingga cache baru berisi isi lama.
4. Setelah worker baru aktif, halaman yang sedang terbuka tetap versi lama sampai dimuat ulang manual (hanya muncul toast).

## Solusi
| Komponen | Fungsi |
|---|---|
| `service-worker.js` | Kode (HTML/JS/CSS/JSON/halaman) **jaringan dulu** (batas 4 dtk), cadangan cache saat offline/lambat. Aset berat (gambar, font, audio) tetap cache dulu. Pemasangan memakai `cache:'reload'`. `version.json` tidak pernah di-cache. |
| `update.js` | Memeriksa versi baru saat dibuka, saat kembali ke aplikasi, saat internet tersambung, dan tiap 15 menit. Memasang worker baru dan **memuat ulang otomatis**. Jika anak sedang bermain, menunggu sampai selesai/keluar. Pelindung agar tidak reload berulang (maks. 1× / 30 dtk). Progres aman karena tersimpan di LocalStorage. |
| `tools/rilis.js` | Satu perintah sebelum unggah: `node tools/rilis.js` → menghitung hash semua berkas, mengisi nomor versi cache `V` otomatis, menulis `version.json`, dan membangun ulang halaman SEO. Tidak perlu lagi menaikkan `V` manual. |

## Cara rilis
1. Ubah file yang perlu. 2. `node tools/rilis.js`. 3. Unggah semua ke GitHub Pages. HP yang online akan update dalam hitungan detik saat aplikasi dibuka/dikembalikan ke depan (maks. 15 menit jika dibiarkan terbuka). HP yang offline akan update begitu online.

## Pengujian (`test_update_otomatis.py`, 10/10 PASS di Chromium)
Versi baru (HTML+JS) terdeteksi dan halaman dimuat ulang otomatis; HTML dan JS baru berjalan; cache lama dihapus; tanpa galat; offline tetap terbuka dari cache; tidak reload paksa saat sedang bermain, lalu reload otomatis setelah keluar.

## Batasan
- HP yang SUDAH memasang versi lama (service worker lama, cache dulu) perlu **dibuka sekali sambil online dan dimuat ulang manual sekali** agar menerima service worker baru. Setelah itu seterusnya otomatis. iOS Safari bisa lebih lambat memeriksa pembaruan di latar belakang; pembaruan terjadi saat aplikasi dibuka.
- Berkas besar (gambar/audio) hanya diperbarui saat nomor versi berubah (otomatis lewat `rilis.js` bila isinya berubah).
- Tidak diuji di perangkat fisik/Safari.
