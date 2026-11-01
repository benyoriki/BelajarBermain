from h import *
import os
O='/home/claude/work/Buku_anak/docs/screenshots_v15/'; os.makedirs(O,exist_ok=True)
def S(pg,n): pg.screenshot(path=O+n+'.png')
with sync_playwright() as p:
    b=p.chromium.launch()
    for vw,vh,t,touch in [(360,740,'hp360',1),(320,568,'hp320',1),(1366,768,'pc1366',0),(1920,1080,'tv1080',0)]:
        ctx,pg=page(b,vw,vh,touch=bool(touch))
        if t=='tv1080': pg.evaluate("ACT.tv()")
        S(pg,t+'_01_beranda')
        play(pg,'warna');go(pg);S(pg,t+'_02_mewarnai_katalog')
        pg.click('[data-a=wcatp]');pg.wait_for_timeout(150);S(pg,t+'_03_mewarnai_kategori')
        pg.click('.wcb');pg.wait_for_timeout(350);S(pg,t+'_04_mewarnai_kanvas')
        play(pg,'urut');go(pg);pg.wait_for_timeout(2500);S(pg,t+'_05_urut_giliran')
        play(pg,'puzzle');go(pg);S(pg,t+'_06_puzzle_langkah1')
        pg.click('[data-a=pzcat][data-v=dinosaurus]');pg.wait_for_timeout(450);S(pg,t+'_07_puzzle_langkah2')
        pg.click('[data-a=pzimg]');pg.wait_for_timeout(450);S(pg,t+'_08_puzzle_langkah3')
        pg.click('[data-a=pzlv][data-v="2"]');pg.wait_for_timeout(450);S(pg,t+'_09_puzzle_siap')
        pg.click('[data-a=pzgo]');pg.wait_for_timeout(1500);S(pg,t+'_10_puzzle_papan')
        play(pg,'labirin');go(pg);S(pg,t+'_11_labirin')
        play(pg,'hitung');go(pg);S(pg,t+'_12_hitung')
        ctx.close()
    ctx,pg=page(b,740,360,touch=True);play(pg,'labirin');go(pg);S(pg,'land740_labirin');ctx.close()
    b.close()
