import sys; sys.path.insert(0,'/home/claude/work/audit/tests')
from common import *
import datetime
Rp=[]
def r(s,h,a,ok): Rp.append(dict(skenario=s,harapan=h,aktual=str(a),status='PASS' if ok else 'FAIL'))
def session(pg,gid,correct=True):
    pg.evaluate("ACT.nav('home')"); open_game(pg,gid); go(pg)
    for i in range(5):
        q=pg.evaluate("G.q"); idx=q['a'] if correct else [k for k in range(len(q['o'])) if k!=q['a']][0]
        pg.click(f'#main [data-a=ans][data-v="{idx}"]'); pg.click('#main [data-a=nq]'); pg.wait_for_timeout(40)
with sync_playwright() as p:
    b=p.chromium.launch()
    ctx,pg=mkpage(b); mkprofile(pg)
    daily=pg.evaluate("DAILY()"); other=[g for g in ['hitung','pola','huruf'] if g!=daily][0]
    # sesi 1 semua benar
    session(pg,other); P1=P(pg)
    r('Sesi sempurna (5 benar)','+50 +10 (5 beruntun) +20 = 80',P1['pts'],P1['pts']==80)
    r('Lencana awal','Langkah Pertama + 5 Beruntun (5 benar beruntun), belum 100 Poin',P1['bd'],sorted(P1['bd'])==['5 Beruntun','Langkah Pertama'])
    r('Dimainkan vs diselesaikan','played=1, done=1',(P1['played'],P1['done']),(P1['played'],P1['done'])==(1,1))
    # jawaban salah semua tidak mengurangi
    before=pts(pg); session(pg,other,correct=False); a=P(pg)
    r('Sesi semua salah','Poin tidak berkurang; hanya +20 selesai',(before,a['pts']),a['pts']==before+20)
    r('Level & lencana 100 Poin','Level naik ke 2 saat >=100; lencana 100 Poin',(a['pts'],a['bd']),a['pts']>=100 and '100 Poin' in a['bd'])
    # tantangan harian: sekali per hari
    session(pg,daily); d1=P(pg); session(pg,daily); d2=P(pg)
    r('Tantangan harian','bonus +30 hanya sekali per hari (dc=1)',(d1['dc'],d2['dc']),d1['dc']==1 and d2['dc']==1)
    # monoton + batas harian
    seq=[]; 
    for i in range(14): session(pg,other); seq.append(pts(pg))
    day=P(pg)['days'][pg.evaluate("today()")]
    r('Poin tidak pernah berkurang','urutan poin naik/tetap',seq[:6],all(x<=y for x,y in zip(seq,seq[1:])))
    r('Batas poin harian (anti tambang)','total hari ini <= 600 + 30 (bonus harian)',day,day<=630)
    last=pts(pg); session(pg,other); r('Setelah batas tercapai','tidak ada poin tambahan, permainan tetap bisa dilanjutkan, pesan ramah',(last,pts(pg),pg.inner_text('#main')[:60].replace('\n',' ')),pts(pg)==last and on_fin(pg))
    r('Level tidak melompat','level = hasil perhitungan dari poin',pg.evaluate("[P().pts,lvl(P())]"),pg.evaluate("lvl(P())")==max(i for i,v in enumerate([0,100,300,600,1000]) if pg.evaluate("P().pts")>=v))
    # refresh
    sv=P(pg); pg.reload(); pg.wait_for_timeout(300); pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()")
    r('Refresh','poin, done, lencana, hari sama',(sv['pts'],pg.evaluate("P().pts")),pg.evaluate("P().pts")==sv['pts'] and pg.evaluate("P().done")==sv['done'])
    # profil kedua terpisah
    pg.evaluate("ACT.who()"); pg.click('[data-a=new]'); pg.fill('#nm','Ani'); pg.click('[data-a=saveP]'); pg.wait_for_timeout(200)
    r('Ganti profil','profil baru mulai 0 poin; profil lama utuh',(pts(pg),[x['pts'] for x in pg.evaluate("S.p")]),pts(pg)==0 and pg.evaluate("S.p")[0]['pts']==sv['pts'])
    # sesi dimainkan lalu keluar: played naik, done tidak
    pg.evaluate("ACT.nav('home')"); open_game(pg,'hitung'); go(pg); pg.click('#main [data-a=ans]'); pg.evaluate("ACT.nav('home')")
    pp=P(pg); r('Keluar sebelum selesai','played+1, done tetap 0',(pp['played'],pp['done']),pp['played']==1 and pp['done']==0)
    ctx.close()
    # hari lokal: 23:50 WIB tgl 30 (=16:50 UTC) lalu 00:10 tgl 31
    ctx=b.new_context(viewport={'width':412,'height':900},service_workers='block',timezone_id='Asia/Jakarta'); pg=ctx.new_page(); pg.errs=[]; pg.route('https://*/**',lambda r:r.abort())
    ctx.clock.install(time=datetime.datetime(2026,10,30,16,50,0,tzinfo=datetime.timezone.utc)); pg.goto(URL); pg.wait_for_timeout(300); mkprofile(pg)
    d_a=pg.evaluate("[today(),DAILY()]"); session(pg,'hitung'); k1=list(P(pg)['days'].keys())
    ctx.clock.set_fixed_time(datetime.datetime(2026,10,30,17,10,0,tzinfo=datetime.timezone.utc)); d_b=pg.evaluate("[today(),DAILY()]")
    r('Pergantian hari lokal (WIB 23:50 -> 00:10)','tanggal & tantangan harian berganti pada 00:00 lokal',(d_a,d_b),d_a[0]=='2026-10-30' and d_b[0]=='2026-10-31' and d_a[1]!=d_b[1])
    r('Kunci hari poin','memakai tanggal lokal',k1,k1==['2026-10-30'])
    ctx.close()
    # migrasi data lama dengan banyak profil + foto
    old={'p':[{'id':'k1','name':'Budi','av':'🦖','age':0,'pts':640,'done':12,'ok':50,'bad':9,'best':7,'dc':2,'dcDay':'2026-10-01','bd':['Langkah Pertama','100 Poin'],'hist':['x'],'days':{'2026-10-29':80},'art':{'a_0':'#fff'},'photo':'data:image/jpeg;base64,AAA'},{'id':'k2','name':'Sari','av':'🐱','age':2,'pts':20,'done':1,'ok':2,'bad':0,'best':2,'dc':0,'dcDay':'','bd':[],'hist':[],'days':{},'art':{}}],'cur':'k1','snd':1,'sm':'sfx','mv':.3}
    ctx,pg=mkpage(b,seed=old); pg.evaluate("document.getElementById('ld')&&document.getElementById('ld').remove()")
    S2=pg.evaluate("JSON.parse(localStorage.getItem('bba1'))"); mem=pg.evaluate("S.p.map(x=>[x.name,x.pts,x.done,!!x.photo])")
    r('Migrasi data lama (format v13+) 2 profil','poin, foto, lencana, pengaturan suara tetap sama',mem,mem==[['Budi',640,12,True],['Sari',20,1,False]] and pg.evaluate("S.sm")=='sfx')
    ctx.close(); b.close()
import json; json.dump(Rp,open('hasil_poin.json','w'),ensure_ascii=False,indent=1)
for x in Rp: print(x['status'],'|',x['skenario'],'|',x['aktual'][:90])
