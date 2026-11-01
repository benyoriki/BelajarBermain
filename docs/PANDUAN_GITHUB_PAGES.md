# Panduan unggah ke GitHub Pages
1. Ekstrak ZIP. Isi folder `Buku_anak/` adalah root situs.
2. Di repository: **Add file › Upload files**, unggah SELURUH isi folder (termasuk `audio/`, `mewarnai*.html`, `docs/` boleh dilewati) langsung di root. Commit.
3. **Settings › Pages**: branch `main`, folder `/ (root)`. Domain `belajarbermain.online` tetap lewat berkas CNAME yang sudah ada di repo (jangan dihapus).
4. Tunggu 1–2 menit, buka situs, muat ulang 2 kali. Service worker memasang versi baru otomatis (`update.js`).
5. Jika mengubah berkas lagi: `node tools/rilis.js` sebelum unggah (memperbarui hash cache + sitemap).
6. Rollback: unggah ulang `Buku_anak_v14_redesign.zip` (backup asli).
Cek manual di HP/TV: `docs/CHECKLIST_MANUAL.md`.
