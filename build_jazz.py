from PIL import Image,ImageDraw,ImageFont
import random,math,os
root=os.path.dirname(os.path.abspath(__file__))
W,H=480,200
random.seed(77)
stars=[(random.randint(5,475),random.randint(5,95),random.randint(0,23)) for _ in range(65)]
buildings=[]
x=0
while x<480:
 w=random.randint(13,33);ht=random.randint(25,90)
 buildings.append((x,w,ht,random.randint(0,10)));x+=w+2
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',19)
small=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf',8)
frames=[]
for t in range(32):
 im=Image.new('RGB',(W,H));p=im.load()
 for y in range(H):
  for x in range(W):
   k=y/H;p[x,y]=(int(9+11*k),int(11+8*k),int(30+11*k))
 d=ImageDraw.Draw(im)
 # moon glow & moon
 for r in range(40,13,-3):d.ellipse((380-r,38-r,380+r,38+r),outline=(19+int((40-r)*.55),22+int((40-r)*.4),46+int((40-r)*.9)))
 d.ellipse((364,22,396,54),fill='#eedca9');d.ellipse((372,17,401,50),fill='#14172b')
 for x,y,phase in stars:
  c=110+int(85*(.5+.5*math.sin((t+phase)/4)))
  d.point((x,y),fill=(c,c-15, min(255,c+15)))
 # skyline
 for bx,bw,bh,seed in buildings:
  y0=132-bh
  d.rectangle((bx,y0,bx+bw,139),fill='#13192e')
  d.rectangle((bx,y0,bx+bw,y0+2),fill='#242942')
  for yy in range(y0+7,132,8):
   for xx in range(bx+4,bx+bw-3,7):
    if (xx*7+yy*3+seed)%5<2:
     c='#ebaa62' if (t//8+xx+yy)%4 else '#6d4266'
     d.rectangle((xx,yy,xx+2,yy+3),fill=c)
 # street, club facade
 d.rectangle((0,139,479,199),fill='#181426')
 for y in range(146,200,12):d.line((0,y,480,y),fill='#2b2035')
 for x in range(0,480,18):d.line((x,139,x-10,200),fill='#1c192b')
 # warm jazz club backdrop
 d.rectangle((118,63,335,167),fill='#29203b',outline='#8f5065',width=2)
 d.rectangle((128,78,325,157),fill='#493044',outline='#c4785b',width=2)
 for n in range(5):
  xx=131+n*38
  d.line((xx,80,xx,153),fill='#63354d',width=2)
 d.rectangle((153,68,290,80),fill='#1a172a',outline='#f3b66d',width=2)
 d.text((165,69),'MIDNIGHT JAZZ',font=small,fill='#edc88c')
 # floor warm spotlight pixel concentric
 for r in range(72,10,-6):
  col=(min(82,33+int((75-r)*.7)),min(55,28+int((75-r)*.25)),38)
  d.ellipse((240-r*1.4,158-r*.32,240+r*1.4,158+r*.32),outline=col,width=3)
 # upright bass at right
 d.line((307,99,317,159),fill='#d6a26b',width=3)
 d.ellipse((300,125,326,163),fill='#b76b4d',outline='#e6a071',width=2)
 d.ellipse((304,132,322,150),fill='#ce8050')
 d.line((313,110,313,168),fill='#382032',width=2)
 d.arc((302,136,312,144),45,280,fill='#3c2537',width=2)
 d.arc((315,143,324,151),185,410,fill='#3c2537',width=2)
 # upright bass neck + tuning
 d.rectangle((311,94,315,129),fill='#a36c53');d.rectangle((310,91,319,95),fill='#e1ae79')
 # drums on right
 d.ellipse((258,148,294,170),fill='#713453',outline='#f0ac78',width=2)
 d.ellipse((270,154,285,162),outline='#d59b89',width=2)
 d.line((263,145,263,133),fill='#b7adb0',width=2)
 d.ellipse((249,130,277,135),fill='#e0a36c')
 d.line((295,142,295,128),fill='#b7adb0',width=2)
 d.ellipse((284,127,306,130),fill='#e0a36c')
 # piano left - angled grand silhouette
 d.polygon([(127,137),(190,123),(210,132),(182,147)],fill='#120f21')
 d.line((127,137,190,123),fill='#936075',width=2)
 d.polygon([(143,142),(190,135),(191,141),(150,151)],fill='#e6c9a8')
 for i in range(10):
  xx=150+i*4
  d.line((xx,142-i//6,xx+1,147-i//6),fill='#302337')
 d.line((153,149,149,174),fill='#9e7d89',width=3)
 d.line((188,146,193,176),fill='#9e7d89',width=3)
 # sax player pixel silhouette center
 bob=round(math.sin(t*math.pi/8))
 d.ellipse((210,93+bob,230,113+bob),fill='#b88a8f')
 d.polygon([(207,110+bob),(231,108+bob),(240,147+bob),(206,146+bob)],fill='#202335')
 d.polygon([(206,116+bob),(197,135+bob),(218,140+bob),(223,127+bob)],fill='#242943')
 d.line((214,140+bob,212,167),fill='#192031',width=7)
 d.line((230,140+bob,238,167),fill='#192031',width=7)
 # hands + gold sax; bell
 d.line((211,121+bob,232,131+bob),fill='#dcb5a0',width=4)
 d.line((223,115+bob,238,134+bob),fill='#c89180',width=4)
 d.line((219,116+bob,231,139+bob),fill='#e8b562',width=4)
 d.line((231,139+bob,246,147+bob),fill='#ecc271',width=4)
 d.ellipse((243,140+bob,252,151+bob),fill='#f0ca70')
 for xx,yy in [(225,122),(227,128),(229,133)]:d.rectangle((xx,yy+bob,xx+2,yy+2+bob),fill='#6a423b')
 # music note particles on right moving upward
 for j in range(5):
  x=245+j*14+round(2*math.sin(t/4+j))
  y=112-((t*2+j*16)%56)
  d.ellipse((x,y,x+3,y+3),fill='#f3d28c');d.line((x+3,y,x+3,y-7),fill='#f3d28c')
  if j%2==0:d.line((x+3,y-7,x+7,y-5),fill='#f3d28c')
 # overlay left / title
 d.rectangle((9,12,192,60),fill='#101429',outline='#58425b')
 d.text((17,18),'aliiimc',font=font,fill='#f6d9a2',stroke_width=0)
 d.text((17,43),'CODE  /  JAZZ  /  IDEAS',font=small,fill='#aa8fba')
 # light flicker corner lamp
 for x in [135,313]:
  lit=180+int(45*math.sin(t/3+x))
  d.rectangle((x-3,86,x+3,94),fill=(lit,105,52))
 # bottom info
 d.rectangle((0,183,479,199),fill='#111526')
 d.text((13,187),'CREATIVE CODING  |  AI  |  NIGHT SESSIONS',font=small,fill='#dfac86')
 d.text((405,187),'VOL. 01',font=small,fill='#9d91b5')
 frames.append(im.resize((960,400),Image.Resampling.NEAREST))
frames[0].save(root+'/assets/midnight-jazz.gif',save_all=True,append_images=frames[1:],duration=110,loop=0,optimize=True)
frames[0].save(root+'/assets/midnight-jazz-preview.png')
print('gif MB',os.path.getsize(root+'/assets/midnight-jazz.gif')/1e6)
