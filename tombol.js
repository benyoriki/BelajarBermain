/* tombol.js — ikon tombol yang seragam (SVG ringan), menggantikan emoji/simbol yang tampil berbeda di tiap HP.
   Hanya mengubah tampilan teks tombol; tidak menyentuh data-a, skor, atau localStorage. Dimuat setelah script.js. */
(function () {
  'use strict';
  var A = 'fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"';
  function s(d, f) { return '<svg class="ik" viewBox="0 0 24 24" aria-hidden="true" focusable="false" ' + (f || A) + '>' + d + '</svg>'; }
  var I = {
    kiri: s('<path d="m14.5 5.5-6.5 6.5 6.5 6.5"/>'),
    kanan: s('<path d="m9.5 5.5 6.5 6.5-6.5 6.5"/>'),
    main: s('<path d="M8 5.5v13a.8.8 0 0 0 1.2.7l10-6.5a.8.8 0 0 0 0-1.4l-10-6.5A.8.8 0 0 0 8 5.5z" fill="currentColor" stroke="none"/>', 'fill="currentColor"'),
    cek: s('<path d="m4.5 12.5 5 5 10-11"/>'),
    x: s('<path d="M6 6l12 12M18 6 6 18"/>'),
    ulang: s('<path d="M3.5 12a8.5 8.5 0 1 0 2.6-6.1"/><path d="M3.5 4v4.5H8"/>'),
    hapus: s('<path d="M4 7h16M10 11v6M14 11v6M6 7l1 12a1.5 1.5 0 0 0 1.5 1.4h7A1.5 1.5 0 0 0 17 19l1-12M9 7V4.5h6V7"/>'),
    ubah: s('<path d="M4 20h4L19 9a2.8 2.8 0 0 0-4-4L4 16z"/><path d="m13.5 6.5 4 4"/>'),
    layar: s('<path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/>'),
    tv: s('<rect x="3" y="5" width="18" height="12" rx="2.5"/><path d="M8 21h8M12 17v4"/>'),
    anak: s('<circle cx="9" cy="8" r="3.2"/><path d="M3 20a6 6 0 0 1 12 0"/><path d="M16 5.2a3.2 3.2 0 0 1 0 5.6M18 14.5a6 6 0 0 1 3 5.5"/>'),
    unduh: s('<path d="M12 4v11m0 0 4.5-4.5M12 15l-4.5-4.5M5 20h14"/>'),
    roket: s('<path d="M12 3c3.5 1.5 5.5 5 5 9l-2.5 2.5h-5L7 12c-.5-4 1.5-7.500 5-9z"/><circle cx="12" cy="9.500" r="1.600"/><path d="M9.500 14.500 7 17l-.5 3.500L10 20l1.500-2M14.500 14.500 17 17l.5 3.500L14 20l-1.500-2"/>'),
    hati: s('<path d="M12 20s-7.500-4.600-7.500-10A4.300 4.300 0 0 1 12 7.300 4.300 4.300 0 0 1 19.500 10c0 5.400-7.500 10-7.500 10z"/>'),
    mata: s('<path d="M2.500 12S6 5.500 12 5.500 21.500 12 21.500 12 18 18.500 12 18.500 2.500 12 2.500 12z"/><circle cx="12" cy="12" r="2.800"/>'),
    lampu: s('<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.500 10.900c.6.500 1 1.200 1 2V16h5v-.100c0-.800.400-1.500 1-2A6 6 0 0 0 12 3z"/>'),
    grid: s('<rect x="4" y="4" width="6.500" height="6.500" rx="1.600"/><rect x="13.500" y="4" width="6.500" height="6.500" rx="1.600"/><rect x="4" y="13.500" width="6.500" height="6.500" rx="1.600"/><rect x="13.500" y="13.500" width="6.500" height="6.500" rx="1.600"/>'),
    jeda: s('<path d="M8.500 5v14M15.500 5v14" stroke-width="3.400"/>'),
    cari: s('<circle cx="11" cy="11" r="6.500"/><path d="m16 16 4.500 4.500"/>'),
    dadu: s('<rect x="4" y="4" width="16" height="16" rx="3.500"/><circle cx="9" cy="9" r="1.100" fill="currentColor"/><circle cx="15" cy="15" r="1.100" fill="currentColor"/><circle cx="15" cy="9" r="1.100" fill="currentColor"/><circle cx="9" cy="15" r="1.100" fill="currentColor"/>')
  };
  window.IK = I;

  /* data-a → [ikon, posisi(0=depan,1=belakang), syarat teks (opsional)] */
  var MAP = {
    go: ['main', 0], pzgo: ['main', 0], nq: ['kanan', 1], nr: ['kanan', 1], pznext: ['kanan', 1],
    cdone: ['cek', 0], saveP: ['cek', 0], pset: ['cek', 0], cancel: ['x', 0],
    del: ['hapus', 0], pdel: ['hapus', 0], edit: ['ubah', 0], reset: ['ulang', 0], rs: ['ulang', 0], pzre: ['ulang', 0],
    fs: ['layar', 0], tv: ['tv', 0], who: ['anak', 0], inst: ['unduh', 0], don: ['hati', 0], srep: ['mata', 0], pzref: ['mata', 0],
    pzhint: ['lampu', 0], hint: ['lampu', 0], pzmenu: ['grid', 0], pzpause: ['jeda', 0], pzzoom: ['cari', 0],
    wback: ['grid', 0], wrand: ['dadu', 0], new: ['roket', 0]
  };
  var LEAD = /^[\s\u2190-\u21ff\u2300-\u23ff\u25a0-\u27bf\u2b00-\u2bff\ufe0f\u200d\uff0b\u{1F000}-\u{1FFFF}]+/u;
  var TRAIL = /[\s\u25b6\u25b8\u2192]+$/u;

  function pick(b) {
    var a = b.dataset.a, t = (b.textContent || '').trim();
    if (a === 'nav') {
      if (b.closest('.hero')) return /Belajar/.test(t) ? ['main', 0] : ['grid', 0];
      if (/Kembali|^[\W]*Pilih Permainan/.test(t) && b.classList.contains('ghost')) return ['kiri', 0];
      if (/Mulai Belajar/.test(t)) return ['main', 0];
      if (/Pilih Permainan/.test(t)) return ['grid', 0];
      if (/Batal/.test(t)) return ['x', 0];
      return null;
    }
    if (a === 'play') return /Lagi|Mulai/.test(t) ? ['ulang', 0] : null;
    return MAP[a] || null;
  }

  function enhance() {
    var bs = document.querySelectorAll('#main button.cta,#main button.ghost,.mo button.cta,.mo button.ghost,#hd button.cta');
    for (var i = 0; i < bs.length; i++) {
      var b = bs[i];
      if (b.dataset.ik || b.children.length) continue;      /* sudah diproses atau bukan tombol teks polos */
      var m = pick(b); if (!m) continue;
      var t = (b.textContent || '').replace(LEAD, '').replace(TRAIL, '');
      b.dataset.ik = '1';
      b.innerHTML = '';
      var sp = document.createElement('span'); sp.textContent = t; sp.className = 'tt';
      var ic = document.createElement('span'); ic.className = 'ic'; ic.setAttribute('aria-hidden', 'true'); ic.innerHTML = I[m[0]];
      if (m[1]) { b.appendChild(sp); b.appendChild(ic); } else { b.appendChild(ic); b.appendChild(sp); }
    }
    /* tombol bulat: Kembali & Ulangi di kepala permainan */
    document.querySelectorAll('.gback span:not([data-ik])').forEach(function (e) { e.dataset.ik = '1'; e.innerHTML = I.kiri; });
    document.querySelectorAll('.gre span:not([data-ik])').forEach(function (e) { e.dataset.ik = '1'; e.innerHTML = I.ulang; });
  }

  var raf = 0, mo;
  function sched() { if (raf) return; raf = requestAnimationFrame(function () { raf = 0; mo.disconnect(); try { enhance(); } catch (e) {} arm(); }); }
  function arm() { mo.observe(document.body, { childList: true, subtree: true }); }
  mo = new MutationObserver(sched);
  enhance(); arm();
})();
