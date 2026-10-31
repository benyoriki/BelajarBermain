from PIL import Image, ImageDraw, ImageFont, ImageFilter
art=Image.open('preview.jpg').convert('RGB').resize((1200,630),Image.LANCZOS)
W,H=1200,630; im=art.copy().convert('RGBA')
F=lambda n,s:ImageFont.truetype('/usr/share/fonts/truetype/google-fonts/Poppins-%s.ttf'%n,s)
BH=96; band=Image.new('RGBA',(W,BH)); px=band.load()
for x in range(W):
    t=x/(W-1); c=(int(255*(1-t)+236*t),int(145*(1-t)+64*t),int(30*(1-t)+140*t),255)
    for y in range(BH): px[x,y]=c
mask=Image.new('L',(W,BH),0); ImageDraw.Draw(mask).rounded_rectangle((0,0,W,BH+40),radius=36,fill=255); band.putalpha(mask)
sh=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(sh).rectangle((0,H-BH-6,W,H-BH+2),fill=(0,0,0,70)); im=Image.alpha_composite(im,sh.filter(ImageFilter.GaussianBlur(8)))
im.alpha_composite(band,(0,H-BH)); d=ImageDraw.Draw(im); y0=H-BH
def ts(xy,t,f,fill=(255,255,255),off=2): d.text((xy[0]+off,xy[1]+off),t,font=f,fill=(120,30,0,140)); d.text(xy,t,font=f,fill=fill)
ts((34,y0+10),'14 GAME EDUKASI GRATIS',F('Bold',38))
d.text((36,y0+58),'Untuk anak usia 3–8 tahun  •  Tanpa iklan  •  Langsung main',font=F('Medium',22),fill=(255,244,226))
bx0,by0,bx1,by1=W-372,y0+16,W-28,y0+80
d.rounded_rectangle((bx0,by0+4,bx1,by1+4),radius=32,fill=(24,110,52)); d.rounded_rectangle((bx0,by0,bx1,by1),radius=32,fill=(46,196,92),outline=(255,255,255),width=3)
d.polygon([(bx0+36,by0+18),(bx0+36,by0+46),(bx0+60,by0+32)],fill=(255,255,255)); d.text((bx0+76,by0+10),'MAIN SEKARANG',font=F('Bold',26),fill=(255,255,255))
cx,cy,r=104,112,84
d.ellipse((cx-r+3,cy-r+5,cx+r+3,cy+r+5),fill=(0,0,0,70)); d.ellipse((cx-r,cy-r,cx+r,cy+r),fill=(255,196,0),outline=(255,255,255),width=6); d.ellipse((cx-r+12,cy-r+12,cx+r-12,cy+r-12),outline=(255,140,0),width=3)
def ctr(t,f,y,col): w=d.textlength(t,font=f); d.text((cx-w/2,y),t,font=f,fill=col)
ctr('100%',F('Bold',26),cy-52,(200,70,0)); ctr('GRATIS',F('Bold',38),cy-26,(214,40,40)); ctr('usia 3–8 th',F('Bold',19),cy+24,(110,50,0))
im.convert('RGB').save('preview-wa.jpg',quality=84,optimize=True,progressive=True)
