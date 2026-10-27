/* Ikon permainan (SVG) + palet warna — Buku Belajar Anak v13 */
(function(){
'use strict';
function star(cx,cy,R,r,fill,stroke){
  var p=[];for(var i=0;i<10;i++){var a=-Math.PI/2+i*Math.PI/5,d=i%2?r:R;p.push((cx+d*Math.cos(a)).toFixed(1)+','+(cy+d*Math.sin(a)).toFixed(1))}
  return '<polygon points="'+p.join(' ')+'" fill="'+fill+'"'+(stroke?' stroke="'+stroke+'" stroke-width="3" stroke-linejoin="round"':'')+'/>';
}
function T(x,y,s,fill,t){return '<text x="'+x+'" y="'+y+'" font-size="'+s+'" font-weight="900" text-anchor="middle" fill="'+fill+'" font-family="ui-rounded,\'Baloo 2\',\'Trebuchet MS\',system-ui,sans-serif">'+t+'</text>'}
var I={
warna:'<path d="M32 7C17 7 5 17 5 31c0 13 10 22 22 22 5 0 6-3 6-6s2-5 5-5h9c8 0 13-5 13-12C60 17 47 7 32 7z" fill="#fcd9a0" stroke="#d98a1f" stroke-width="3.5" stroke-linejoin="round"/><circle cx="19" cy="27" r="5.5" fill="#ef4444"/><circle cx="31" cy="19" r="5.5" fill="#3b82f6"/><circle cx="45" cy="24" r="5.5" fill="#22c55e"/><circle cx="17" cy="41" r="5.5" fill="#eab308"/><circle cx="29" cy="40" r="3.4" fill="#fff" opacity=".7"/>',
garis:'<path d="M20 20C36 18 28 44 44 44" fill="none" stroke="#7c3aed" stroke-width="4.5" stroke-linecap="round"/><path d="M20 46C36 48 28 20 44 18" fill="none" stroke="#ec4899" stroke-width="4.5" stroke-linecap="round" stroke-dasharray="1 9"/><circle cx="13" cy="20" r="8" fill="#8b5cf6" stroke="#fff" stroke-width="2.5"/><circle cx="51" cy="44" r="8" fill="#f97316" stroke="#fff" stroke-width="2.5"/><circle cx="13" cy="46" r="8" fill="#ec4899" stroke="#fff" stroke-width="2.5"/><circle cx="51" cy="18" r="8" fill="#22c55e" stroke="#fff" stroke-width="2.5"/>',
pola:'<circle cx="17" cy="18" r="10" fill="#ef4444"/><rect x="38" y="8" width="20" height="20" rx="5" fill="#3b82f6"/><polygon points="7,56 27,56 17,38" fill="#eab308" stroke="#eab308" stroke-width="3" stroke-linejoin="round"/><rect x="38" y="38" width="20" height="20" rx="6" fill="#fff" stroke="#16a34a" stroke-width="3.5" stroke-dasharray="5 4"/>'+T(48,54,17,'#16a34a','?'),
beda:'<circle cx="26" cy="26" r="17" fill="#e0f2fe" stroke="#0284c7" stroke-width="5"/><line x1="39" y1="39" x2="56" y2="56" stroke="#92400e" stroke-width="8" stroke-linecap="round"/><circle cx="20" cy="27" r="5" fill="#ec4899"/><circle cx="32" cy="27" r="5" fill="#ec4899" opacity=".35"/><path d="M15 17a14 14 0 0 1 10-5" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>',
hitung:'<circle cx="16" cy="18" r="9" fill="#ef4444"/><circle cx="36" cy="18" r="9" fill="#ef4444"/><circle cx="26" cy="36" r="9" fill="#ef4444"/><path d="M16 9c0-4 3-5 5-5M36 9c0-4 3-5 5-5M26 27c0-4 3-5 5-5" fill="none" stroke="#16a34a" stroke-width="3" stroke-linecap="round"/><circle cx="46" cy="46" r="15" fill="#2563eb" stroke="#fff" stroke-width="3"/>'+T(46,53,20,'#fff','3'),
spy:'<path d="M3 32Q32 4 61 32Q32 60 3 32Z" fill="#fff" stroke="#1e3a8a" stroke-width="4" stroke-linejoin="round"/><circle cx="32" cy="32" r="14" fill="#3b82f6"/><circle cx="32" cy="32" r="7" fill="#0f172a"/><circle cx="37" cy="26" r="3.6" fill="#fff"/>',
huruf:'<g transform="rotate(-9 21 29)"><rect x="6" y="13" width="31" height="31" rx="7" fill="#f97316"/>'+T(21.5,38,24,'#fff','A')+'</g><g transform="rotate(8 44 40)"><rect x="29" y="26" width="29" height="29" rx="7" fill="#3b82f6"/>'+T(43.5,49,23,'#fff','B')+'</g>',
memori:'<g transform="rotate(-10 20 33)"><rect x="5" y="13" width="30" height="40" rx="6" fill="#fff" stroke="#0891b2" stroke-width="4"/>'+star(20,33,10,4.4,'#f59e0b')+'</g><g transform="rotate(10 44 31)"><rect x="29" y="11" width="30" height="40" rx="6" fill="#06b6d4" stroke="#0e7490" stroke-width="3"/>'+T(44,40,26,'#fff','?')+'</g>',
bayangan:star(40,42,19,8,'#94a3b8')+star(26,26,19,8,'#fbbf24','#d97706')+'<circle cx="21" cy="22" r="2.5" fill="#fff" opacity=".8"/>',
tambah:'<path d="M25 9h14v16h16v14H39v16H25V39H9V25h16z" fill="#22c55e" stroke="#15803d" stroke-width="3" stroke-linejoin="round"/><circle cx="55" cy="9" r="6" fill="#ef4444"/><circle cx="9" cy="55" r="6" fill="#f59e0b"/><circle cx="55" cy="55" r="6" fill="#ef4444"/><circle cx="9" cy="9" r="6" fill="#f59e0b"/>',
ganjil:'<circle cx="17" cy="20" r="11" fill="#3b82f6"/><circle cx="47" cy="20" r="11" fill="#3b82f6"/><circle cx="32" cy="46" r="15" fill="#fdf4ff" stroke="#c026d3" stroke-width="3" stroke-dasharray="5 4"/>'+star(32,46,10,4.5,'#f97316'),
labirin:'<rect x="5" y="5" width="54" height="54" rx="10" fill="#ccfbf1" stroke="#0d9488" stroke-width="5"/><path d="M5 22H38M26 38H59M5 50H36" stroke="#0d9488" stroke-width="5" stroke-linecap="round" fill="none"/><circle cx="14" cy="13" r="4.5" fill="#22c55e"/><ellipse cx="49" cy="49" rx="5.5" ry="7" fill="#fff" stroke="#f59e0b" stroke-width="3"/>',
urut:'<rect x="5" y="38" width="17" height="21" rx="5" fill="#22c55e"/><rect x="24" y="26" width="17" height="33" rx="5" fill="#f59e0b"/><rect x="43" y="11" width="17" height="48" rx="5" fill="#ef4444"/>'+T(13.5,54,15,'#fff','1')+T(32.5,54,15,'#fff','2')+T(51.5,54,15,'#fff','3'),
puzzle:'<path d="M8 16H24c-3-9 2-12 6-12s9 3 6 12H52v14c8-3 10 2 10 6s-2 9-10 6v14H36c3-8-2-12-6-12s-9 4-6 12H8V44c8 3 10-2 10-6s-2-9-10-6z" fill="#0ea5e9" stroke="#0369a1" stroke-width="3" stroke-linejoin="round"/>'+star(30,34,9,4,'#fde047')
};
/* palet warna: tiap permainan punya warna sendiri yang jelas berbeda */
var C={warna:'#f97316',garis:'#8b5cf6',pola:'#16a34a',beda:'#ec4899',hitung:'#2563eb',spy:'#ef4444',huruf:'#eab308',memori:'#06b6d4',bayangan:'#6366f1',tambah:'#65a30d',ganjil:'#c026d3',labirin:'#0d9488',urut:'#e11d48',puzzle:'#0284c7'};
window.GI=function(id){return I[id]?'<svg viewBox="0 0 64 64" aria-hidden="true" focusable="false">'+I[id]+'</svg>':''};
window.GCOL=C;
})();
