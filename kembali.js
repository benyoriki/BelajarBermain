/* kembali.js — tombol Kembali HP (Android/iOS/PWA) bekerja DI DALAM aplikasi.
   Sebelumnya: Kembali di HP keluar dari halaman / memuat ulang website dari awal.
   Sekarang: Kembali = mundur satu langkah (tutup jendela → keluar permainan → kembali ke menu → Beranda).
   Di Beranda: tekan Kembali dua kali dalam 2 detik untuk keluar (agar anak tidak tak sengaja keluar).
   Cara kerja: satu "entri jaga" di riwayat browser; setiap Kembali ditangkap lalu dipasang lagi.
   Tidak mengubah skor, profil, atau localStorage. Dimuat setelah script.js, suara.js, dan update.js. */
(function () {
  'use strict';
  if (!window.history || !history.pushState) return;

  var ROOT = 'bba-root', APP = 'bba-app', armed = false, armT = 0, leaving = false;

  function st(o) { try { return history.state && history.state.k === o; } catch (e) { return false; } }
  function arm() { try { history.pushState({ k: APP }, ''); } catch (e) {} }

  /* pasang entri jaga sekali saja (aman saat halaman dimuat ulang) */
  try {
    if (!st(APP) && !st(ROOT)) { history.replaceState({ k: ROOT }, ''); arm(); }
    else if (st(ROOT)) arm();
  } catch (e) { return; }

  function say(t) { try { toast(t); } catch (e) {} }

  function mundur() {
    /* 1) jendela terbuka (suara / donasi) → tutup */
    if (document.documentElement.classList.contains('mo') && ACT.mclose) { ACT.mclose(); return true; }
    /* 2) formulir profil → batal (hanya bila sudah ada profil) */
    if (ED !== null && P()) { ACT.cancel(); return true; }
    /* 3) di dalam permainan */
    if (V === 'play' && G && G.id) {
      if (G.id === 'warna' && G.dr && ACT.wback) { ACT.wback(); return true; }
      ACT.nav(BELAJAR.includes(G.id) ? 'belajar' : 'main');
      return true;
    }
    /* 4) halaman lain → Beranda */
    if (V !== 'home' && P()) { ACT.nav('home'); return true; }
    return false;
  }

  addEventListener('popstate', function (e) {
    if (leaving) return;
    if (e.state && e.state.k === APP) return;      /* maju: abaikan */
    if (mundur()) { arm(); return; }
    /* sudah di Beranda */
    if (armed) { leaving = true; clearTimeout(armT); history.back(); return; }
    armed = true;
    say('Tekan Kembali sekali lagi untuk keluar 👋');
    clearTimeout(armT);
    armT = setTimeout(function () { armed = false; }, 2000);
    arm();
  });
})();
