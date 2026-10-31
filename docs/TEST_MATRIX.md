# TEST MATRIX — Audit Permainan Buku Belajar Anak (v20.1)

Bukti: Chromium otomatis (Playwright) melawan server lokal. Input memakai ketukan/klik nyata (bukan memanggil fungsi), emulasi HP 360×800 dengan sentuhan dan desktop 1366×768 dengan mouse/keyboard; seret jari memakai sentuhan CDP. **Bukan** perangkat fisik atau hosting produksi. PASS hanya bila ada bukti terukur di kolom Aktual; yang tidak dapat diuji otomatis diberi BLOCKED dengan langkah manual.

## A. Ringkasan per permainan (HP sentuh / desktop)

| Permainan | Input | Jawaban benar/salah | Kondisi menang | Reset/Ulangi | Keluar/Menu | Pengulangan | Skor | Refresh | Responsif | Suara terdengar | Perangkat fisik |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Mewarnai | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | BLOCKED | BLOCKED |
| Pola & Logika | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | BLOCKED | BLOCKED |
| Hitung & Lingkarkan | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | BLOCKED | BLOCKED |
| Huruf & Kata | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | BLOCKED | BLOCKED |
| Tambah Bergambar | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | BLOCKED | BLOCKED |
| Mana yang Beda? | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | BLOCKED | BLOCKED |
| Menghubungkan Garis | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | BLOCKED | BLOCKED |
| Cari Perbedaan | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | BLOCKED | BLOCKED |
| I Spy Game | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | BLOCKED | BLOCKED |
| Puzzle & Memori | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | BLOCKED | BLOCKED |
| Cari Bayangan | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | BLOCKED | BLOCKED |
| Labirin | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | BLOCKED | BLOCKED |
| Ingat Urutan | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | BLOCKED | BLOCKED |
| Puzzle Petualangan | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | PASS/PASS | BLOCKED | BLOCKED |

Total baris uji per permainan: 286 (286 PASS, 0 FAIL). Selain itu: logika 106, poin/progres 16, fuzz 17, Smart TV+offline+update 15 baris (semua PASS pada putaran akhir). Tata letak: 184 pengukuran, 6 viewport + landscape.

Kolom dimensi: **Input** = buka lewat kartu & mulai dengan ketukan nyata; **Jawaban** = salah (poin tetap, bad+1, pesan ramah) dan benar; **Menang** = selesai hanya setelah langkah terakhir; **Reset** = tombol di dalam permainan, poin tidak berkurang; **Keluar** = tombol Menu dalam permainan dan navigasi global, lalu buka permainan lain tanpa kebocoran state; **Pengulangan** = Main Lagi → state bersih; **Skor** = rumus 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian); **Refresh** = di tengah permainan, poin tetap & tanpa error; **Responsif** = tanpa scroll horizontal/tombol tertutup pada potret dan landscape, state tetap.

## B. BLOCKED — tidak dapat dibuktikan otomatis, dengan langkah manual

| Permainan | Yang tidak teruji | Langkah manual |
|---|---|---|
| Mewarnai | Suara terdengar (lagu_5/6/7, tanpa bunyi "beb"); jari/perangkat fisik; Smart TV fisik; Safari/iOS | Di HP: ketuk 10 area berbeda dengan jari (bukan stylus); pastikan area kecil mudah dikenai; coba palet 12 warna dan 🧽 hapus; putar layar. Dengarkan: salah=lagu_5, benar=lagu_6, selesai=lagu_7. |
| Pola & Logika | Suara terdengar (lagu_5/6/7, tanpa bunyi "beb"); jari/perangkat fisik; Smart TV fisik; Safari/iOS | Di HP: jawab 5 soal; dengar suara benar/salah; pastikan gambar pola tidak terpotong pada layar 320px. Dengarkan: salah=lagu_5, benar=lagu_6, selesai=lagu_7. |
| Hitung & Lingkarkan | Suara terdengar (lagu_5/6/7, tanpa bunyi "beb"); jari/perangkat fisik; Smart TV fisik; Safari/iOS | Di HP: hitung objek 1–15 pada usia 3–4 dan 7–8; pastikan gambar jelas terhitung dan angka pilihan mudah diketuk. Dengarkan: salah=lagu_5, benar=lagu_6, selesai=lagu_7. |
| Huruf & Kata | Suara terdengar (lagu_5/6/7, tanpa bunyi "beb"); jari/perangkat fisik; Smart TV fisik; Safari/iOS | Di HP: pastikan huruf besar/kecil dan karakter tampil benar; ketuk tombol 🔊 (bila ada) tanpa internet. Dengarkan: salah=lagu_5, benar=lagu_6, selesai=lagu_7. |
| Tambah Bergambar | Suara terdengar (lagu_5/6/7, tanpa bunyi "beb"); jari/perangkat fisik; Smart TV fisik; Safari/iOS | Di HP usia 7–8: pastikan soal pengurangan (T − y) terbaca jelas oleh anak. Dengarkan: salah=lagu_5, benar=lagu_6, selesai=lagu_7. |
| Mana yang Beda? | Suara terdengar (lagu_5/6/7, tanpa bunyi "beb"); jari/perangkat fisik; Smart TV fisik; Safari/iOS | Di HP: pastikan jawaban "yang beda" masuk akal bagi anak (kelompok hewan/buah/bentuk jelas). Dengarkan: salah=lagu_5, benar=lagu_6, selesai=lagu_7. |
| Menghubungkan Garis | Suara terdengar (lagu_5/6/7, tanpa bunyi "beb"); jari/perangkat fisik; Smart TV fisik; Safari/iOS | Di HP: seret jari dari kiri ke kanan beberapa kali; pastikan halaman tidak bergulir; putar layar di tengah permainan. Dengarkan: salah=lagu_5, benar=lagu_6, selesai=lagu_7. |
| Cari Perbedaan | Suara terdengar (lagu_5/6/7, tanpa bunyi "beb"); jari/perangkat fisik; Smart TV fisik; Safari/iOS | Di HP: ketuk perbedaan pada layar kecil; pastikan kotak cukup besar untuk jari anak. Dengarkan: salah=lagu_5, benar=lagu_6, selesai=lagu_7. |
| I Spy Game | Suara terdengar (lagu_5/6/7, tanpa bunyi "beb"); jari/perangkat fisik; Smart TV fisik; Safari/iOS | Di HP: cari target dengan jari; ketuk area salah berkali-kali; pastikan tetap bisa selesai. Dengarkan: salah=lagu_5, benar=lagu_6, selesai=lagu_7. |
| Puzzle & Memori | Suara terdengar (lagu_5/6/7, tanpa bunyi "beb"); jari/perangkat fisik; Smart TV fisik; Safari/iOS | Di HP: buka 2 kartu salah lalu cepat ketuk kartu ke-3; pastikan diabaikan; selesaikan penuh. Dengarkan: salah=lagu_5, benar=lagu_6, selesai=lagu_7. |
| Cari Bayangan | Suara terdengar (lagu_5/6/7, tanpa bunyi "beb"); jari/perangkat fisik; Smart TV fisik; Safari/iOS | Di HP: pastikan siluet jelas dan pilihan tidak terlalu mirip untuk usia 3–4. Dengarkan: salah=lagu_5, benar=lagu_6, selesai=lagu_7. |
| Labirin | Suara terdengar (lagu_5/6/7, tanpa bunyi "beb"); jari/perangkat fisik; Smart TV fisik; Safari/iOS | Di HP: usap (swipe) di labirin dan gunakan tombol panah; Smart TV: gunakan tombol panah remote asli; pastikan kecepatan nyaman untuk anak. Dengarkan: salah=lagu_5, benar=lagu_6, selesai=lagu_7. |
| Ingat Urutan | Suara terdengar (lagu_5/6/7, tanpa bunyi "beb"); jari/perangkat fisik; Smart TV fisik; Safari/iOS | Di HP: perhatikan contoh, jawab; tekan 🔁 Ulangi contoh; pastikan jeda dan kecepatan sesuai anak 3–4 tahun. Dengarkan: salah=lagu_5, benar=lagu_6, selesai=lagu_7. |
| Puzzle Petualangan | Suara terdengar (lagu_5/6/7, tanpa bunyi "beb"); jari/perangkat fisik; Smart TV fisik; Safari/iOS | Di HP: seret keping dengan jari; ketuk keping lalu kotak; putar layar; Smart TV: Enter pada keping lalu kotak dengan remote asli. Dengarkan: salah=lagu_5, benar=lagu_6, selesai=lagu_7. |

Catatan: seret jari di Labirin (swipe), Garis, dan Puzzle sudah diuji dengan sentuhan CDP (PASS), tetapi tetap emulasi, bukan layar sentuh fisik.

## C. Bukti rinci per permainan

| VP | Permainan | Dimensi | Skenario | Diharapkan | Aktual | Status |
|---|---|---|---|---|---|---|
| desktop | Labirin | Input | Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai | layar permainan tampil, tanpa tombol tertutup | G.id=labirin | PASS |
| desktop | Labirin | Kondisi menang | Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1) | fin tepat di akhir | fin=True fin_terlalu_awal=False dok=3 done=1 | PASS |
| desktop | Labirin | Skor | Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN | sesuai rumus | delta=50 diharapkan=50 (dok=3) | PASS |
| desktop | Labirin | Pengulangan | Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda | state bersih | intro=True state=[0, 0] | PASS |
| desktop | Labirin | Jawaban benar/salah | Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid | sesuai | menabrak tembok tak bergerak; jalur benar bergerak | PASS |
| desktop | Labirin | Reset/Ulangi | Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin | state awal | [0, 0]; poin 50->50 (tidak berkurang) | PASS |
| desktop | Labirin | Responsif | Tanpa scroll horizontal/tombol tertutup di 1366×768 dan rotasi; state tidak hilang | bersih | potret hs=0 tertutup=[] <44px=[]; landscape hs=0 tertutup=[]; state tetap=True | PASS |
| desktop | Labirin | Keluar/Menu | Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor | beranda | beranda=True G.id=None errs=[] | PASS |
| desktop | Labirin | Keluar/Menu | Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor | bersih | dari tengah permainan lewat navigasi → buka hitung: G.id=hitung errs=[] | PASS |
| desktop | Labirin | Refresh | Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi | tetap | poin 50->50; kembali ke beranda; errs=[]; bba1 valid=True | PASS |
| desktop | Ingat Urutan | Input | Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai | layar permainan tampil, tanpa tombol tertutup | G.id=urut | PASS |
| desktop | Ingat Urutan | Kondisi menang | Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1) | fin tepat di akhir | fin=True fin_terlalu_awal=False dok=4 done=1 | PASS |
| desktop | Ingat Urutan | Skor | Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN | sesuai rumus | delta=60 diharapkan=60 (dok=4) | PASS |
| desktop | Ingat Urutan | Pengulangan | Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda | state bersih | intro=True state=[0, 0] | PASS |
| desktop | Ingat Urutan | Jawaban benar/salah | Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid | sesuai | salah → terkunci, bad+1, poin tetap, contoh diulang | PASS |
| desktop | Ingat Urutan | Reset/Ulangi | Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin | state awal | [1, 0]; poin 70->70 (tidak berkurang) | PASS |
| desktop | Ingat Urutan | Responsif | Tanpa scroll horizontal/tombol tertutup di 1366×768 dan rotasi; state tidak hilang | bersih | potret hs=0 tertutup=[] <44px=[]; landscape hs=0 tertutup=[]; state tetap=True | PASS |
| desktop | Ingat Urutan | Keluar/Menu | Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor | beranda | beranda=True G.id=None errs=[] | PASS |
| desktop | Ingat Urutan | Keluar/Menu | Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor | bersih | dari tengah permainan lewat navigasi → buka hitung: G.id=hitung errs=[] | PASS |
| desktop | Ingat Urutan | Refresh | Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi | tetap | poin 90->90; kembali ke beranda; errs=[]; bba1 valid=True | PASS |
| desktop | Puzzle Petualangan | Input | Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai | layar permainan tampil, tanpa tombol tertutup | G.id=puzzle | PASS |
| desktop | Puzzle Petualangan | Kondisi menang | Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1) | fin tepat di akhir | fin=True fin_terlalu_awal=False dok=1 done=1 | PASS |
| desktop | Puzzle Petualangan | Skor | Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN | sesuai rumus | delta=30 diharapkan=30 (dok=1) | PASS |
| desktop | Puzzle Petualangan | Pengulangan | Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda | state bersih | [0, 1] | PASS |
| desktop | Puzzle Petualangan | Jawaban benar/salah | Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid | sesuai | keping salah ditolak ramah; kotak benar terkunci | PASS |
| desktop | Puzzle Petualangan | Reset/Ulangi | Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin | state awal | [0, 4, 4]; poin 30->30 (tidak berkurang) | PASS |
| desktop | Puzzle Petualangan | Responsif | Tanpa scroll horizontal/tombol tertutup di 1366×768 dan rotasi; state tidak hilang | bersih | potret hs=0 tertutup=[] <44px=[]; landscape hs=0 tertutup=[]; state tetap=True | PASS |
| desktop | Puzzle Petualangan | Keluar/Menu | Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor | beranda | beranda=True G.id=None errs=[] | PASS |
| desktop | Puzzle Petualangan | Keluar/Menu | Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor | bersih | dari tengah permainan lewat navigasi → buka hitung: G.id=hitung errs=[] | PASS |
| desktop | Puzzle Petualangan | Refresh | Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi | tetap | poin 30->30; kembali ke beranda; errs=[]; bba1 valid=True | PASS |
| desktop | Pola & Logika | Input | Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai | layar permainan tampil, tanpa tombol tertutup | G.id=pola | PASS |
| desktop | Pola & Logika | Kondisi menang | Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1) | fin tepat di akhir | fin=True fin_terlalu_awal=False dok=5 done=1 | PASS |
| desktop | Pola & Logika | Skor | Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN | sesuai rumus | delta=80 diharapkan=80 (dok=5) | PASS |
| desktop | Pola & Logika | Pengulangan | Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda | state bersih | intro=True state=[0, 0] | PASS |
| desktop | Pola & Logika | Jawaban benar/salah | Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid | sesuai | salah: poin tetap, bad+1, pesan '❌ Hampir! Polanya A-B '; benar: poin naik | PASS |
| desktop | Pola & Logika | Reset/Ulangi | Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin | state awal | [0, 0]; poin 100->100 (tidak berkurang) | PASS |
| desktop | Pola & Logika | Responsif | Tanpa scroll horizontal/tombol tertutup di 1366×768 dan rotasi; state tidak hilang | bersih | potret hs=0 tertutup=[] <44px=[]; landscape hs=0 tertutup=[]; state tetap=True | PASS |
| desktop | Pola & Logika | Keluar/Menu | Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor | beranda | beranda=True G.id=None errs=[] | PASS |
| desktop | Pola & Logika | Keluar/Menu | Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor | bersih | dari tengah permainan lewat navigasi → buka hitung: G.id=hitung errs=[] | PASS |
| desktop | Pola & Logika | Refresh | Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi | tetap | poin 120->120; kembali ke beranda; errs=[]; bba1 valid=True | PASS |
| desktop | Hitung & Lingkarkan | Input | Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai | layar permainan tampil, tanpa tombol tertutup | G.id=hitung | PASS |
| desktop | Hitung & Lingkarkan | Kondisi menang | Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1) | fin tepat di akhir | fin=True fin_terlalu_awal=False dok=5 done=1 | PASS |
| desktop | Hitung & Lingkarkan | Skor | Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN | sesuai rumus | delta=80 diharapkan=80 (dok=5) | PASS |
| desktop | Hitung & Lingkarkan | Pengulangan | Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda | state bersih | intro=True state=[0, 0] | PASS |
| desktop | Hitung & Lingkarkan | Jawaban benar/salah | Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid | sesuai | salah: poin tetap, bad+1, pesan '❌ Hampir! Ada 1 Strobe'; benar: poin naik | PASS |
| desktop | Hitung & Lingkarkan | Reset/Ulangi | Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin | state awal | [0, 0]; poin 100->100 (tidak berkurang) | PASS |
| desktop | Hitung & Lingkarkan | Responsif | Tanpa scroll horizontal/tombol tertutup di 1366×768 dan rotasi; state tidak hilang | bersih | potret hs=0 tertutup=[] <44px=[]; landscape hs=0 tertutup=[]; state tetap=True | PASS |
| desktop | Hitung & Lingkarkan | Keluar/Menu | Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor | beranda | beranda=True G.id=None errs=[] | PASS |
| desktop | Hitung & Lingkarkan | Keluar/Menu | Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor | bersih | dari tengah permainan lewat navigasi → buka pola: G.id=pola errs=[] | PASS |
| desktop | Hitung & Lingkarkan | Refresh | Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi | tetap | poin 120->120; kembali ke beranda; errs=[]; bba1 valid=True | PASS |
| desktop | Cari Perbedaan | Input | Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai | layar permainan tampil, tanpa tombol tertutup | G.id=beda | PASS |
| desktop | Cari Perbedaan | Kondisi menang | Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1) | fin tepat di akhir | fin=True fin_terlalu_awal=False dok=3 done=1 | PASS |
| desktop | Cari Perbedaan | Skor | Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN | sesuai rumus | delta=50 diharapkan=50 (dok=3) | PASS |
| desktop | Cari Perbedaan | Pengulangan | Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda | state bersih | intro=True state=[0, 0] | PASS |
| desktop | Cari Perbedaan | Jawaban benar/salah | Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid | sesuai | salah: poin tetap bad+1; benar: +10 | PASS |
| desktop | Cari Perbedaan | Reset/Ulangi | Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin | state awal | [0, 0]; poin 70->70 (tidak berkurang) | PASS |
| desktop | Cari Perbedaan | Responsif | Tanpa scroll horizontal/tombol tertutup di 1366×768 dan rotasi; state tidak hilang | bersih | potret hs=0 tertutup=[] <44px=[]; landscape hs=0 tertutup=[]; state tetap=True | PASS |
| desktop | Cari Perbedaan | Keluar/Menu | Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor | beranda | beranda=True G.id=None errs=[] | PASS |
| desktop | Cari Perbedaan | Keluar/Menu | Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor | bersih | dari tengah permainan lewat navigasi → buka hitung: G.id=hitung errs=[] | PASS |
| desktop | Cari Perbedaan | Refresh | Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi | tetap | poin 90->90; kembali ke beranda; errs=[]; bba1 valid=True | PASS |
| desktop | I Spy Game | Input | Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai | layar permainan tampil, tanpa tombol tertutup | G.id=spy | PASS |
| desktop | I Spy Game | Kondisi menang | Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1) | fin tepat di akhir | fin=True fin_terlalu_awal=False dok=3 done=1 | PASS |
| desktop | I Spy Game | Skor | Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN | sesuai rumus | delta=50 diharapkan=50 (dok=3) | PASS |
| desktop | I Spy Game | Pengulangan | Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda | state bersih | intro=True state=[0, 0] | PASS |
| desktop | I Spy Game | Jawaban benar/salah | Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid | sesuai | salah: poin tetap bad+1; benar: +10 | PASS |
| desktop | I Spy Game | Reset/Ulangi | Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin | state awal | [0, 0]; poin 70->70 (tidak berkurang) | PASS |
| desktop | I Spy Game | Responsif | Tanpa scroll horizontal/tombol tertutup di 1366×768 dan rotasi; state tidak hilang | bersih | potret hs=0 tertutup=[] <44px=[]; landscape hs=0 tertutup=[]; state tetap=True | PASS |
| desktop | I Spy Game | Keluar/Menu | Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor | beranda | beranda=True G.id=None errs=[] | PASS |
| desktop | I Spy Game | Keluar/Menu | Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor | bersih | dari tengah permainan lewat navigasi → buka hitung: G.id=hitung errs=[] | PASS |
| desktop | I Spy Game | Refresh | Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi | tetap | poin 90->90; kembali ke beranda; errs=[]; bba1 valid=True | PASS |
| desktop | Huruf & Kata | Input | Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai | layar permainan tampil, tanpa tombol tertutup | G.id=huruf | PASS |
| desktop | Huruf & Kata | Kondisi menang | Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1) | fin tepat di akhir | fin=True fin_terlalu_awal=False dok=5 done=1 | PASS |
| desktop | Huruf & Kata | Skor | Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN | sesuai rumus | delta=80 diharapkan=80 (dok=5) | PASS |
| desktop | Huruf & Kata | Pengulangan | Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda | state bersih | intro=True state=[0, 0] | PASS |
| desktop | Huruf & Kata | Jawaban benar/salah | Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid | sesuai | salah: poin tetap, bad+1, pesan '❌ Hampir! Rusa diawali'; benar: poin naik | PASS |
| desktop | Huruf & Kata | Reset/Ulangi | Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin | state awal | [0, 0]; poin 100->100 (tidak berkurang) | PASS |
| desktop | Huruf & Kata | Responsif | Tanpa scroll horizontal/tombol tertutup di 1366×768 dan rotasi; state tidak hilang | bersih | potret hs=0 tertutup=[] <44px=[]; landscape hs=0 tertutup=[]; state tetap=True | PASS |
| desktop | Huruf & Kata | Keluar/Menu | Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor | beranda | beranda=True G.id=None errs=[] | PASS |
| desktop | Huruf & Kata | Keluar/Menu | Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor | bersih | dari tengah permainan lewat navigasi → buka hitung: G.id=hitung errs=[] | PASS |
| desktop | Huruf & Kata | Refresh | Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi | tetap | poin 120->120; kembali ke beranda; errs=[]; bba1 valid=True | PASS |
| desktop | Tambah Bergambar | Input | Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai | layar permainan tampil, tanpa tombol tertutup | G.id=tambah | PASS |
| desktop | Tambah Bergambar | Kondisi menang | Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1) | fin tepat di akhir | fin=True fin_terlalu_awal=False dok=5 done=1 | PASS |
| desktop | Tambah Bergambar | Skor | Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN | sesuai rumus | delta=80 diharapkan=80 (dok=5) | PASS |
| desktop | Tambah Bergambar | Pengulangan | Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda | state bersih | intro=True state=[0, 0] | PASS |
| desktop | Tambah Bergambar | Jawaban benar/salah | Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid | sesuai | salah: poin tetap, bad+1, pesan '❌ Hampir! 4 Stroberi +'; benar: poin naik | PASS |
| desktop | Tambah Bergambar | Reset/Ulangi | Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin | state awal | [0, 0]; poin 100->100 (tidak berkurang) | PASS |
| desktop | Tambah Bergambar | Responsif | Tanpa scroll horizontal/tombol tertutup di 1366×768 dan rotasi; state tidak hilang | bersih | potret hs=0 tertutup=[] <44px=[]; landscape hs=0 tertutup=[]; state tetap=True | PASS |
| desktop | Tambah Bergambar | Keluar/Menu | Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor | beranda | beranda=True G.id=None errs=[] | PASS |
| desktop | Tambah Bergambar | Keluar/Menu | Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor | bersih | dari tengah permainan lewat navigasi → buka hitung: G.id=hitung errs=[] | PASS |
| desktop | Tambah Bergambar | Refresh | Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi | tetap | poin 120->120; kembali ke beranda; errs=[]; bba1 valid=True | PASS |
| desktop | Mewarnai | Input | Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai | layar permainan tampil, tanpa tombol tertutup | G.id=warna | PASS |
| desktop | Mewarnai | Kondisi menang | Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1) | fin tepat di akhir | fin=True fin_terlalu_awal=False dok=0 done=1 | PASS |
| desktop | Mewarnai | Skor | Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN | sesuai rumus | delta=20 diharapkan=20 (dok=0) | PASS |
| desktop | Mewarnai | Pengulangan | Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda | state bersih | intro=True state=[0, 0] | PASS |
| desktop | Mewarnai | Jawaban benar/salah | Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid | sesuai | warna→hapus(🧽)→undo: 1,0,1 (tidak ada jawaban salah) | PASS |
| desktop | Mewarnai | Reset/Ulangi | Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin | state awal | bagian terwarnai=0; poin 20->20 (tidak berkurang) | PASS |
| desktop | Mewarnai | Responsif | Tanpa scroll horizontal/tombol tertutup di 1366×768 dan rotasi; state tidak hilang | bersih | potret hs=0 tertutup=[] <44px=[]; landscape hs=0 tertutup=[]; state tetap=True | PASS |
| desktop | Mewarnai | Keluar/Menu | Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor | beranda | beranda=True G.id=None errs=[] | PASS |
| desktop | Mewarnai | Keluar/Menu | Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor | bersih | dari tengah permainan lewat navigasi → buka hitung: G.id=hitung errs=[] | PASS |
| desktop | Mewarnai | Refresh | Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi | tetap | poin 20->20; kembali ke beranda; errs=[]; bba1 valid=True | PASS |
| desktop | Menghubungkan Garis | Input | Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai | layar permainan tampil, tanpa tombol tertutup | G.id=garis | PASS |
| desktop | Menghubungkan Garis | Kondisi menang | Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1) | fin tepat di akhir | fin=True fin_terlalu_awal=False dok=4 done=1 | PASS |
| desktop | Menghubungkan Garis | Skor | Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN | sesuai rumus | delta=60 diharapkan=60 (dok=4) | PASS |
| desktop | Menghubungkan Garis | Pengulangan | Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda | state bersih | intro=True state=[0, 0] | PASS |
| desktop | Menghubungkan Garis | Jawaban benar/salah | Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid | sesuai | pasangan salah: tanpa garis, bad+1; benar: 1 garis | PASS |
| desktop | Menghubungkan Garis | Reset/Ulangi | Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin | state awal | [0, 0, 0]; poin 80->80 (tidak berkurang) | PASS |
| desktop | Menghubungkan Garis | Responsif | Tanpa scroll horizontal/tombol tertutup di 1366×768 dan rotasi; state tidak hilang | bersih | potret hs=0 tertutup=[] <44px=[]; landscape hs=0 tertutup=[]; state tetap=True | PASS |
| desktop | Menghubungkan Garis | Keluar/Menu | Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor | beranda | beranda=True G.id=None errs=[] | PASS |
| desktop | Menghubungkan Garis | Keluar/Menu | Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor | bersih | dari tengah permainan lewat navigasi → buka hitung: G.id=hitung errs=[] | PASS |
| desktop | Menghubungkan Garis | Refresh | Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi | tetap | poin 100->100; kembali ke beranda; errs=[]; bba1 valid=True | PASS |
| desktop | Puzzle & Memori | Input | Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai | layar permainan tampil, tanpa tombol tertutup | G.id=memori | PASS |
| desktop | Puzzle & Memori | Kondisi menang | Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1) | fin tepat di akhir | fin=True fin_terlalu_awal=False dok=4 done=1 | PASS |
| desktop | Puzzle & Memori | Skor | Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN | sesuai rumus | delta=60 diharapkan=60 (dok=4) | PASS |
| desktop | Puzzle & Memori | Pengulangan | Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda | state bersih | intro=True state=[0, 0] | PASS |
| desktop | Puzzle & Memori | Jawaban benar/salah | Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid | sesuai | pasangan beda menutup kembali; poin tetap | PASS |
| desktop | Puzzle & Memori | Reset/Ulangi | Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin | state awal | [0, 0, 0]; poin 70->70 (tidak berkurang) | PASS |
| desktop | Puzzle & Memori | Responsif | Tanpa scroll horizontal/tombol tertutup di 1366×768 dan rotasi; state tidak hilang | bersih | potret hs=0 tertutup=[] <44px=[]; landscape hs=0 tertutup=[]; state tetap=True | PASS |
| desktop | Puzzle & Memori | Keluar/Menu | Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor | beranda | beranda=True G.id=None errs=[] | PASS |
| desktop | Puzzle & Memori | Keluar/Menu | Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor | bersih | dari tengah permainan lewat navigasi → buka hitung: G.id=hitung errs=[] | PASS |
| desktop | Puzzle & Memori | Refresh | Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi | tetap | poin 90->90; kembali ke beranda; errs=[]; bba1 valid=True | PASS |
| desktop | Mana yang Beda? | Input | Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai | layar permainan tampil, tanpa tombol tertutup | G.id=ganjil | PASS |
| desktop | Mana yang Beda? | Kondisi menang | Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1) | fin tepat di akhir | fin=True fin_terlalu_awal=False dok=5 done=1 | PASS |
| desktop | Mana yang Beda? | Skor | Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN | sesuai rumus | delta=80 diharapkan=80 (dok=5) | PASS |
| desktop | Mana yang Beda? | Pengulangan | Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda | state bersih | intro=True state=[0, 0] | PASS |
| desktop | Mana yang Beda? | Jawaban benar/salah | Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid | sesuai | salah: poin tetap, bad+1, pesan '❌ Hampir!  berbeda dar'; benar: poin naik | PASS |
| desktop | Mana yang Beda? | Reset/Ulangi | Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin | state awal | [0, 0]; poin 100->100 (tidak berkurang) | PASS |
| desktop | Mana yang Beda? | Responsif | Tanpa scroll horizontal/tombol tertutup di 1366×768 dan rotasi; state tidak hilang | bersih | potret hs=0 tertutup=[] <44px=[]; landscape hs=0 tertutup=[]; state tetap=True | PASS |
| desktop | Mana yang Beda? | Keluar/Menu | Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor | beranda | beranda=True G.id=None errs=[] | PASS |
| desktop | Mana yang Beda? | Keluar/Menu | Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor | bersih | dari tengah permainan lewat navigasi → buka hitung: G.id=hitung errs=[] | PASS |
| desktop | Mana yang Beda? | Refresh | Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi | tetap | poin 120->120; kembali ke beranda; errs=[]; bba1 valid=True | PASS |
| desktop | Cari Bayangan | Input | Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai | layar permainan tampil, tanpa tombol tertutup | G.id=bayangan | PASS |
| desktop | Cari Bayangan | Kondisi menang | Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1) | fin tepat di akhir | fin=True fin_terlalu_awal=False dok=5 done=1 | PASS |
| desktop | Cari Bayangan | Skor | Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN | sesuai rumus | delta=110 diharapkan=110 (dok=5, +30 harian) | PASS |
| desktop | Cari Bayangan | Pengulangan | Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda | state bersih | intro=True state=[0, 0] | PASS |
| desktop | Cari Bayangan | Jawaban benar/salah | Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid | sesuai | salah: poin tetap, bad+1, pesan '❌ Hampir! Bentuk bayan'; benar: poin naik | PASS |
| desktop | Cari Bayangan | Reset/Ulangi | Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin | state awal | [0, 0]; poin 130->130 (tidak berkurang) | PASS |
| desktop | Cari Bayangan | Responsif | Tanpa scroll horizontal/tombol tertutup di 1366×768 dan rotasi; state tidak hilang | bersih | potret hs=0 tertutup=[] <44px=[]; landscape hs=0 tertutup=[]; state tetap=True | PASS |
| desktop | Cari Bayangan | Keluar/Menu | Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor | beranda | beranda=True G.id=None errs=[] | PASS |
| desktop | Cari Bayangan | Keluar/Menu | Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor | bersih | dari tengah permainan lewat navigasi → buka hitung: G.id=hitung errs=[] | PASS |
| desktop | Cari Bayangan | Refresh | Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi | tetap | poin 150->150; kembali ke beranda; errs=[]; bba1 valid=True | PASS |
| hp | Labirin | Input | Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai | layar permainan tampil, tanpa tombol tertutup | G.id=labirin | PASS |
| hp | Labirin | Kondisi menang | Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1) | fin tepat di akhir | fin=True fin_terlalu_awal=False dok=3 done=1 | PASS |
| hp | Labirin | Skor | Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN | sesuai rumus | delta=50 diharapkan=50 (dok=3) | PASS |
| hp | Labirin | Pengulangan | Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda | state bersih | intro=True state=[0, 0] | PASS |
| hp | Labirin | Jawaban benar/salah | Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid | sesuai | menabrak tembok tak bergerak; jalur benar bergerak | PASS |
| hp | Labirin | Reset/Ulangi | Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin | state awal | [0, 0]; poin 50->50 (tidak berkurang) | PASS |
| hp | Labirin | Responsif | Tanpa scroll horizontal/tombol tertutup di 360×800 dan rotasi; state tidak hilang | bersih | potret hs=0 tertutup=[] <44px=[]; landscape hs=0 tertutup=[]; state tetap=True | PASS |
| hp | Labirin | Keluar/Menu | Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor | beranda | beranda=True G.id=None errs=[] | PASS |
| hp | Labirin | Keluar/Menu | Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor | bersih | dari tengah permainan lewat navigasi → buka hitung: G.id=hitung errs=[] | PASS |
| hp | Labirin | Refresh | Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi | tetap | poin 50->50; kembali ke beranda; errs=[]; bba1 valid=True | PASS |
| hp | Ingat Urutan | Input | Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai | layar permainan tampil, tanpa tombol tertutup | G.id=urut | PASS |
| hp | Ingat Urutan | Kondisi menang | Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1) | fin tepat di akhir | fin=True fin_terlalu_awal=False dok=4 done=1 | PASS |
| hp | Ingat Urutan | Skor | Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN | sesuai rumus | delta=60 diharapkan=60 (dok=4) | PASS |
| hp | Ingat Urutan | Pengulangan | Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda | state bersih | intro=True state=[0, 0] | PASS |
| hp | Ingat Urutan | Jawaban benar/salah | Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid | sesuai | salah → terkunci, bad+1, poin tetap, contoh diulang | PASS |
| hp | Ingat Urutan | Reset/Ulangi | Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin | state awal | [1, 0]; poin 70->70 (tidak berkurang) | PASS |
| hp | Ingat Urutan | Responsif | Tanpa scroll horizontal/tombol tertutup di 360×800 dan rotasi; state tidak hilang | bersih | potret hs=0 tertutup=[] <44px=[]; landscape hs=0 tertutup=[]; state tetap=True | PASS |
| hp | Ingat Urutan | Keluar/Menu | Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor | beranda | beranda=True G.id=None errs=[] | PASS |
| hp | Ingat Urutan | Keluar/Menu | Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor | bersih | dari tengah permainan lewat navigasi → buka hitung: G.id=hitung errs=[] | PASS |
| hp | Ingat Urutan | Refresh | Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi | tetap | poin 90->90; kembali ke beranda; errs=[]; bba1 valid=True | PASS |
| hp | Puzzle Petualangan | Input | Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai | layar permainan tampil, tanpa tombol tertutup | G.id=puzzle | PASS |
| hp | Puzzle Petualangan | Kondisi menang | Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1) | fin tepat di akhir | fin=True fin_terlalu_awal=False dok=1 done=1 | PASS |
| hp | Puzzle Petualangan | Skor | Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN | sesuai rumus | delta=30 diharapkan=30 (dok=1) | PASS |
| hp | Puzzle Petualangan | Pengulangan | Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda | state bersih | [0, 1] | PASS |
| hp | Puzzle Petualangan | Jawaban benar/salah | Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid | sesuai | keping salah ditolak ramah; kotak benar terkunci | PASS |
| hp | Puzzle Petualangan | Reset/Ulangi | Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin | state awal | [0, 4, 4]; poin 30->30 (tidak berkurang) | PASS |
| hp | Puzzle Petualangan | Responsif | Tanpa scroll horizontal/tombol tertutup di 360×800 dan rotasi; state tidak hilang | bersih | potret hs=0 tertutup=[] <44px=[]; landscape hs=0 tertutup=[]; state tetap=True | PASS |
| hp | Puzzle Petualangan | Keluar/Menu | Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor | beranda | beranda=True G.id=None errs=[] | PASS |
| hp | Puzzle Petualangan | Keluar/Menu | Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor | bersih | dari tengah permainan lewat navigasi → buka hitung: G.id=hitung errs=[] | PASS |
| hp | Puzzle Petualangan | Refresh | Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi | tetap | poin 30->30; kembali ke beranda; errs=[]; bba1 valid=True | PASS |
| hp | Pola & Logika | Input | Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai | layar permainan tampil, tanpa tombol tertutup | G.id=pola | PASS |
| hp | Pola & Logika | Kondisi menang | Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1) | fin tepat di akhir | fin=True fin_terlalu_awal=False dok=5 done=1 | PASS |
| hp | Pola & Logika | Skor | Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN | sesuai rumus | delta=80 diharapkan=80 (dok=5) | PASS |
| hp | Pola & Logika | Pengulangan | Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda | state bersih | intro=True state=[0, 0] | PASS |
| hp | Pola & Logika | Jawaban benar/salah | Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid | sesuai | salah: poin tetap, bad+1, pesan '❌ Hampir! Polanya A-B '; benar: poin naik | PASS |
| hp | Pola & Logika | Reset/Ulangi | Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin | state awal | [0, 0]; poin 100->100 (tidak berkurang) | PASS |
| hp | Pola & Logika | Responsif | Tanpa scroll horizontal/tombol tertutup di 360×800 dan rotasi; state tidak hilang | bersih | potret hs=0 tertutup=[] <44px=[]; landscape hs=0 tertutup=[]; state tetap=True | PASS |
| hp | Pola & Logika | Keluar/Menu | Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor | beranda | beranda=True G.id=None errs=[] | PASS |
| hp | Pola & Logika | Keluar/Menu | Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor | bersih | dari tengah permainan lewat navigasi → buka hitung: G.id=hitung errs=[] | PASS |
| hp | Pola & Logika | Refresh | Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi | tetap | poin 120->120; kembali ke beranda; errs=[]; bba1 valid=True | PASS |
| hp | Hitung & Lingkarkan | Input | Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai | layar permainan tampil, tanpa tombol tertutup | G.id=hitung | PASS |
| hp | Hitung & Lingkarkan | Kondisi menang | Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1) | fin tepat di akhir | fin=True fin_terlalu_awal=False dok=5 done=1 | PASS |
| hp | Hitung & Lingkarkan | Skor | Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN | sesuai rumus | delta=80 diharapkan=80 (dok=5) | PASS |
| hp | Hitung & Lingkarkan | Pengulangan | Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda | state bersih | intro=True state=[0, 0] | PASS |
| hp | Hitung & Lingkarkan | Jawaban benar/salah | Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid | sesuai | salah: poin tetap, bad+1, pesan '❌ Hampir! Ada 3 Lebah.'; benar: poin naik | PASS |
| hp | Hitung & Lingkarkan | Reset/Ulangi | Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin | state awal | [0, 0]; poin 100->100 (tidak berkurang) | PASS |
| hp | Hitung & Lingkarkan | Responsif | Tanpa scroll horizontal/tombol tertutup di 360×800 dan rotasi; state tidak hilang | bersih | potret hs=0 tertutup=[] <44px=[]; landscape hs=0 tertutup=[]; state tetap=True | PASS |
| hp | Hitung & Lingkarkan | Keluar/Menu | Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor | beranda | beranda=True G.id=None errs=[] | PASS |
| hp | Hitung & Lingkarkan | Keluar/Menu | Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor | bersih | dari tengah permainan lewat navigasi → buka pola: G.id=pola errs=[] | PASS |
| hp | Hitung & Lingkarkan | Refresh | Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi | tetap | poin 120->120; kembali ke beranda; errs=[]; bba1 valid=True | PASS |
| hp | Cari Perbedaan | Input | Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai | layar permainan tampil, tanpa tombol tertutup | G.id=beda | PASS |
| hp | Cari Perbedaan | Kondisi menang | Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1) | fin tepat di akhir | fin=True fin_terlalu_awal=False dok=3 done=1 | PASS |
| hp | Cari Perbedaan | Skor | Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN | sesuai rumus | delta=50 diharapkan=50 (dok=3) | PASS |
| hp | Cari Perbedaan | Pengulangan | Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda | state bersih | intro=True state=[0, 0] | PASS |
| hp | Cari Perbedaan | Jawaban benar/salah | Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid | sesuai | salah: poin tetap bad+1; benar: +10 | PASS |
| hp | Cari Perbedaan | Reset/Ulangi | Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin | state awal | [0, 0]; poin 70->70 (tidak berkurang) | PASS |
| hp | Cari Perbedaan | Responsif | Tanpa scroll horizontal/tombol tertutup di 360×800 dan rotasi; state tidak hilang | bersih | potret hs=0 tertutup=[] <44px=[]; landscape hs=0 tertutup=[]; state tetap=True | PASS |
| hp | Cari Perbedaan | Keluar/Menu | Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor | beranda | beranda=True G.id=None errs=[] | PASS |
| hp | Cari Perbedaan | Keluar/Menu | Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor | bersih | dari tengah permainan lewat navigasi → buka hitung: G.id=hitung errs=[] | PASS |
| hp | Cari Perbedaan | Refresh | Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi | tetap | poin 90->90; kembali ke beranda; errs=[]; bba1 valid=True | PASS |
| hp | I Spy Game | Input | Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai | layar permainan tampil, tanpa tombol tertutup | G.id=spy | PASS |
| hp | I Spy Game | Kondisi menang | Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1) | fin tepat di akhir | fin=True fin_terlalu_awal=False dok=3 done=1 | PASS |
| hp | I Spy Game | Skor | Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN | sesuai rumus | delta=50 diharapkan=50 (dok=3) | PASS |
| hp | I Spy Game | Pengulangan | Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda | state bersih | intro=True state=[0, 0] | PASS |
| hp | I Spy Game | Jawaban benar/salah | Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid | sesuai | salah: poin tetap bad+1; benar: +10 | PASS |
| hp | I Spy Game | Reset/Ulangi | Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin | state awal | [0, 0]; poin 70->70 (tidak berkurang) | PASS |
| hp | I Spy Game | Responsif | Tanpa scroll horizontal/tombol tertutup di 360×800 dan rotasi; state tidak hilang | bersih | potret hs=0 tertutup=[] <44px=[]; landscape hs=0 tertutup=[]; state tetap=True | PASS |
| hp | I Spy Game | Keluar/Menu | Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor | beranda | beranda=True G.id=None errs=[] | PASS |
| hp | I Spy Game | Keluar/Menu | Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor | bersih | dari tengah permainan lewat navigasi → buka hitung: G.id=hitung errs=[] | PASS |
| hp | I Spy Game | Refresh | Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi | tetap | poin 90->90; kembali ke beranda; errs=[]; bba1 valid=True | PASS |
| hp | Huruf & Kata | Input | Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai | layar permainan tampil, tanpa tombol tertutup | G.id=huruf | PASS |
| hp | Huruf & Kata | Kondisi menang | Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1) | fin tepat di akhir | fin=True fin_terlalu_awal=False dok=5 done=1 | PASS |
| hp | Huruf & Kata | Skor | Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN | sesuai rumus | delta=80 diharapkan=80 (dok=5) | PASS |
| hp | Huruf & Kata | Pengulangan | Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda | state bersih | intro=True state=[0, 0] | PASS |
| hp | Huruf & Kata | Jawaban benar/salah | Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid | sesuai | salah: poin tetap, bad+1, pesan '❌ Hampir! Bola diawali'; benar: poin naik | PASS |
| hp | Huruf & Kata | Reset/Ulangi | Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin | state awal | [0, 0]; poin 100->100 (tidak berkurang) | PASS |
| hp | Huruf & Kata | Responsif | Tanpa scroll horizontal/tombol tertutup di 360×800 dan rotasi; state tidak hilang | bersih | potret hs=0 tertutup=[] <44px=[]; landscape hs=0 tertutup=[]; state tetap=True | PASS |
| hp | Huruf & Kata | Keluar/Menu | Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor | beranda | beranda=True G.id=None errs=[] | PASS |
| hp | Huruf & Kata | Keluar/Menu | Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor | bersih | dari tengah permainan lewat navigasi → buka hitung: G.id=hitung errs=[] | PASS |
| hp | Huruf & Kata | Refresh | Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi | tetap | poin 120->120; kembali ke beranda; errs=[]; bba1 valid=True | PASS |
| hp | Tambah Bergambar | Input | Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai | layar permainan tampil, tanpa tombol tertutup | G.id=tambah | PASS |
| hp | Tambah Bergambar | Kondisi menang | Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1) | fin tepat di akhir | fin=True fin_terlalu_awal=False dok=5 done=1 | PASS |
| hp | Tambah Bergambar | Skor | Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN | sesuai rumus | delta=80 diharapkan=80 (dok=5) | PASS |
| hp | Tambah Bergambar | Pengulangan | Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda | state bersih | intro=True state=[0, 0] | PASS |
| hp | Tambah Bergambar | Jawaban benar/salah | Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid | sesuai | salah: poin tetap, bad+1, pesan '❌ Hampir! 3 Pisang + 2'; benar: poin naik | PASS |
| hp | Tambah Bergambar | Reset/Ulangi | Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin | state awal | [0, 0]; poin 100->100 (tidak berkurang) | PASS |
| hp | Tambah Bergambar | Responsif | Tanpa scroll horizontal/tombol tertutup di 360×800 dan rotasi; state tidak hilang | bersih | potret hs=0 tertutup=[] <44px=[]; landscape hs=0 tertutup=[]; state tetap=True | PASS |
| hp | Tambah Bergambar | Keluar/Menu | Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor | beranda | beranda=True G.id=None errs=[] | PASS |
| hp | Tambah Bergambar | Keluar/Menu | Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor | bersih | dari tengah permainan lewat navigasi → buka hitung: G.id=hitung errs=[] | PASS |
| hp | Tambah Bergambar | Refresh | Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi | tetap | poin 120->120; kembali ke beranda; errs=[]; bba1 valid=True | PASS |
| hp | Mewarnai | Input | Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai | layar permainan tampil, tanpa tombol tertutup | G.id=warna | PASS |
| hp | Mewarnai | Kondisi menang | Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1) | fin tepat di akhir | fin=True fin_terlalu_awal=False dok=0 done=1 | PASS |
| hp | Mewarnai | Skor | Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN | sesuai rumus | delta=20 diharapkan=20 (dok=0) | PASS |
| hp | Mewarnai | Pengulangan | Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda | state bersih | intro=True state=[0, 0] | PASS |
| hp | Mewarnai | Jawaban benar/salah | Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid | sesuai | warna→hapus(🧽)→undo: 1,0,1 (tidak ada jawaban salah) | PASS |
| hp | Mewarnai | Reset/Ulangi | Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin | state awal | bagian terwarnai=0; poin 20->20 (tidak berkurang) | PASS |
| hp | Mewarnai | Responsif | Tanpa scroll horizontal/tombol tertutup di 360×800 dan rotasi; state tidak hilang | bersih | potret hs=0 tertutup=[] <44px=[]; landscape hs=0 tertutup=[]; state tetap=True | PASS |
| hp | Mewarnai | Keluar/Menu | Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor | beranda | beranda=True G.id=None errs=[] | PASS |
| hp | Mewarnai | Keluar/Menu | Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor | bersih | dari tengah permainan lewat navigasi → buka hitung: G.id=hitung errs=[] | PASS |
| hp | Mewarnai | Refresh | Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi | tetap | poin 20->20; kembali ke beranda; errs=[]; bba1 valid=True | PASS |
| hp | Menghubungkan Garis | Input | Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai | layar permainan tampil, tanpa tombol tertutup | G.id=garis | PASS |
| hp | Menghubungkan Garis | Kondisi menang | Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1) | fin tepat di akhir | fin=True fin_terlalu_awal=False dok=4 done=1 | PASS |
| hp | Menghubungkan Garis | Skor | Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN | sesuai rumus | delta=60 diharapkan=60 (dok=4) | PASS |
| hp | Menghubungkan Garis | Pengulangan | Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda | state bersih | intro=True state=[0, 0] | PASS |
| hp | Menghubungkan Garis | Jawaban benar/salah | Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid | sesuai | pasangan salah: tanpa garis, bad+1; benar: 1 garis | PASS |
| hp | Menghubungkan Garis | Reset/Ulangi | Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin | state awal | [0, 0, 0]; poin 80->80 (tidak berkurang) | PASS |
| hp | Menghubungkan Garis | Responsif | Tanpa scroll horizontal/tombol tertutup di 360×800 dan rotasi; state tidak hilang | bersih | potret hs=0 tertutup=[] <44px=[]; landscape hs=0 tertutup=[]; state tetap=True | PASS |
| hp | Menghubungkan Garis | Keluar/Menu | Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor | beranda | beranda=True G.id=None errs=[] | PASS |
| hp | Menghubungkan Garis | Keluar/Menu | Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor | bersih | dari tengah permainan lewat navigasi → buka hitung: G.id=hitung errs=[] | PASS |
| hp | Menghubungkan Garis | Refresh | Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi | tetap | poin 100->100; kembali ke beranda; errs=[]; bba1 valid=True | PASS |
| hp | Puzzle & Memori | Input | Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai | layar permainan tampil, tanpa tombol tertutup | G.id=memori | PASS |
| hp | Puzzle & Memori | Kondisi menang | Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1) | fin tepat di akhir | fin=True fin_terlalu_awal=False dok=4 done=1 | PASS |
| hp | Puzzle & Memori | Skor | Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN | sesuai rumus | delta=60 diharapkan=60 (dok=4) | PASS |
| hp | Puzzle & Memori | Pengulangan | Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda | state bersih | intro=True state=[0, 0] | PASS |
| hp | Puzzle & Memori | Jawaban benar/salah | Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid | sesuai | pasangan beda menutup kembali; poin tetap | PASS |
| hp | Puzzle & Memori | Reset/Ulangi | Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin | state awal | [0, 0, 0]; poin 70->70 (tidak berkurang) | PASS |
| hp | Puzzle & Memori | Responsif | Tanpa scroll horizontal/tombol tertutup di 360×800 dan rotasi; state tidak hilang | bersih | potret hs=0 tertutup=[] <44px=[]; landscape hs=0 tertutup=[]; state tetap=True | PASS |
| hp | Puzzle & Memori | Keluar/Menu | Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor | beranda | beranda=True G.id=None errs=[] | PASS |
| hp | Puzzle & Memori | Keluar/Menu | Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor | bersih | dari tengah permainan lewat navigasi → buka hitung: G.id=hitung errs=[] | PASS |
| hp | Puzzle & Memori | Refresh | Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi | tetap | poin 90->90; kembali ke beranda; errs=[]; bba1 valid=True | PASS |
| hp | Mana yang Beda? | Input | Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai | layar permainan tampil, tanpa tombol tertutup | G.id=ganjil | PASS |
| hp | Mana yang Beda? | Kondisi menang | Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1) | fin tepat di akhir | fin=True fin_terlalu_awal=False dok=5 done=1 | PASS |
| hp | Mana yang Beda? | Skor | Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN | sesuai rumus | delta=80 diharapkan=80 (dok=5) | PASS |
| hp | Mana yang Beda? | Pengulangan | Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda | state bersih | intro=True state=[0, 0] | PASS |
| hp | Mana yang Beda? | Jawaban benar/salah | Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid | sesuai | salah: poin tetap, bad+1, pesan '❌ Hampir!  berbeda dar'; benar: poin naik | PASS |
| hp | Mana yang Beda? | Reset/Ulangi | Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin | state awal | [0, 0]; poin 100->100 (tidak berkurang) | PASS |
| hp | Mana yang Beda? | Responsif | Tanpa scroll horizontal/tombol tertutup di 360×800 dan rotasi; state tidak hilang | bersih | potret hs=0 tertutup=[] <44px=[]; landscape hs=0 tertutup=[]; state tetap=True | PASS |
| hp | Mana yang Beda? | Keluar/Menu | Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor | beranda | beranda=True G.id=None errs=[] | PASS |
| hp | Mana yang Beda? | Keluar/Menu | Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor | bersih | dari tengah permainan lewat navigasi → buka hitung: G.id=hitung errs=[] | PASS |
| hp | Mana yang Beda? | Refresh | Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi | tetap | poin 120->120; kembali ke beranda; errs=[]; bba1 valid=True | PASS |
| hp | Cari Bayangan | Input | Buka permainan lewat ketukan/klik pada kartu (bukan fungsi), lalu Mulai | layar permainan tampil, tanpa tombol tertutup | G.id=bayangan | PASS |
| hp | Cari Bayangan | Kondisi menang | Selesai muncul hanya setelah langkah terakhir; selesai sekali (done=1) | fin tepat di akhir | fin=True fin_terlalu_awal=False dok=5 done=1 | PASS |
| hp | Cari Bayangan | Skor | Poin = 10×benar + 10 per 5 beruntun + 20 selesai (+30 harian bila tantangan hari ini); tanpa NaN | sesuai rumus | delta=110 diharapkan=110 (dok=5, +30 harian) | PASS |
| hp | Cari Bayangan | Pengulangan | Tombol Main Lagi → intro → state bersih (done=0, mulai dari awal), tanpa hadiah ganda | state bersih | intro=True state=[0, 0] | PASS |
| hp | Cari Bayangan | Jawaban benar/salah | Salah: poin tetap + pesan ramah; benar: poin naik / aksi valid | sesuai | salah: poin tetap, bad+1, pesan '❌ Hampir! Bentuk bayan'; benar: poin naik | PASS |
| hp | Cari Bayangan | Reset/Ulangi | Tombol di dalam permainan mengembalikan ke awal tanpa mengurangi poin | state awal | [0, 0]; poin 130->130 (tidak berkurang) | PASS |
| hp | Cari Bayangan | Responsif | Tanpa scroll horizontal/tombol tertutup di 360×800 dan rotasi; state tidak hilang | bersih | potret hs=0 tertutup=[] <44px=[]; landscape hs=0 tertutup=[]; state tetap=True | PASS |
| hp | Cari Bayangan | Keluar/Menu | Tombol Menu di dalam permainan → Beranda; tanpa error/timer bocor | beranda | beranda=True G.id=None errs=[] | PASS |
| hp | Cari Bayangan | Keluar/Menu | Keluar dari tengah permainan via navigasi global lalu buka permainan lain: state tidak bocor | bersih | dari tengah permainan lewat navigasi → buka hitung: G.id=hitung errs=[] | PASS |
| hp | Cari Bayangan | Refresh | Refresh di tengah permainan: progres (poin) tetap, tidak error, bisa mulai lagi | tetap | poin 150->150; kembali ke beranda; errs=[]; bba1 valid=True | PASS |
| hp-sentuh | Labirin | Input sentuh | Usap (swipe) jari menggerakkan karakter satu langkah dan halaman tidak ikut bergulir | langkah=1, scrollY tetap | arah 1: langkah=1, scrollY 0->0, halaman_bisa_scroll=True | PASS |
| hp-sentuh | Menghubungkan Garis | Input sentuh | Seret jari dari gambar kiri ke pasangannya membentuk 1 garis; halaman tidak bergulir | 1 garis, scrollY tetap | garis=1 cocok=1 scrollY 142->142 | PASS |
| hp-sentuh | Puzzle Petualangan | Input sentuh | Seret keping dengan jari ke kotak benar → terkunci; halaman tidak bergulir | ok=1, scrollY tetap | terkunci=1 scrollY 166->166 halaman_bisa_scroll=True titik_sentuh_mengenai=pzp2/BUTTON | PASS |
| hp-sentuh | umum | Penyimpanan gagal (kuota penuh) | Tidak crash, permainan tetap bisa dilanjutkan, pesan ramah tampil sekali | tanpa error + pesan | error=[] lanjut=True poin_memori 0->10 toast="+10 ⭐" | PASS |
| hp-sentuh | umum | Migrasi data lama | Reload berulang tidak mengubah data lagi | idempoten | JSON tersimpan identik setelah reload ke-2 dan ke-3 (migrasi idempoten) | PASS |
| hp-sentuh | umum | Data lama × 14 permainan | Memainkan/membuka semua 14 permainan dengan profil lama: tak ada kolom hilang, tak ada error | semua utuh | Budi utuh=True (poin 720), Sari utuh=True, pengaturan suara utuh=True, errs=[] | PASS |

## D. Sebelum/sesudah (skenario bug yang sama pada v19.5 dan v20.1)

| Skenario | v19.5 | v20.1 |
|---|---|---|
| tanggal_lokal | SALAH (today=2026-10-30 lokal=2026-10-31 utc=2026-10-30) | OK |
| reset_warna_gambar_sama | SALAH (bebek->burung) | OK |
| warna_tambang_poin | SALAH (selesai tanpa mewarnai) | OK (ditolak) |
| labirin_timer_bocor | SALAH (home=False, errs=[]) | OK |
| simon_kunci_setelah_salah | SALAH (input masih diterima) | OK |
| puzzle_tambang_poin | SALAH (+20 poin untuk puzzle yang sudah pernah selesai) | OK |
| puzzle_timpa_beranda | OK | OK |
| garis_resize | OK | OK |
| data_rusak_dicadangkan | SALAH (data rusak ditimpa tanpa cadangan) | OK |
| profil_lama_tanpa_kolom | SALAH [260, 4] errs=["Cannot read properties of undefined (reading '2026-10-30')"] | OK pts=260 |

`puzzle_timpa_beranda` dan `garis_resize` tidak dapat direproduksi pada v19.5 di lingkungan uji; perbaikannya pencegahan.

## E. Uji pendukung

| Sumber | Baris | PASS |
|---|---|---|
| Logika 14 permainan (klik nyata, 1 viewport) | 106 | 106 |
| Poin/level/lencana/harian/migrasi | 16 | 16 |
| Fuzz soal/aset/papan/labirin | 17 | 17 |
| Smart TV keyboard, offline, update cache | 15 | 15 |

Catatan jujur tentang pengujian: beberapa FAIL awal pada skrip uji ternyata kesalahan skrip (mis. mengetuk tombol yang sudah nonaktif, mendeteksi teks "Hebat" pada umpan balik, titik sentuh tertutup navigasi bawah di viewport 520px). Itu diperbaiki di skrip, bukan dengan melonggarkan kriteria aplikasi. Satu bug aplikasi nyata ditemukan oleh uji per permainan: 9 permainan tidak punya tombol Ulangi/Menu di dalam layar (B19).