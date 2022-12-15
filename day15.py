import re
import time

occ=set()
yr=2000000
#yr=10
for line in open ("day15.txt"):
    elems=[ e for e in re.split(r'\W+',line.strip()) if e ]
    xp=int(elems[3])
    yp=int(elems[5])
    xs=int(elems[11])
    ys=int(elems[13])
    md=abs(xp-xs)+abs(yp-ys)
    yd=md-abs(yp-yr)
    if yd>=0:
        for x in range(xp-yd,xp+yd):
            occ.add(x)

xp=[]
yp=[]
xs=[]
ys=[]
md=[]
n=0
for line in open ("day15.txt"):
    elems=[ e.replace("x","-") for e in re.split(r'\W+',line.strip().replace("-","x")) if e ]
    xp.append(int(elems[3]))
    yp.append(int(elems[5]))
    xs=int(elems[11])
    ys=int(elems[13])
    md.append(abs(xp[n]-xs)+abs(yp[n]-ys))
    n+=1

le=len(xp)

def mdi(ax,ay,bx,by):
    return abs(ax-bx)+abs(ay-by)

def is_in(ax,ay,ex,ey):
    global le
    if ax==ex or ay==ey:
        return
    for i in range(le):
        xpo=xp[i]
        ypo=yp[i]
        m=md[i]
        if mdi(ax,ay,xpo,ypo)<=m and \
            mdi(ax,ey-1,xpo,ypo)<=m and \
            mdi(ex-1,ay,xpo,ypo)<=m and \
            mdi(ex-1,ey-1,xpo,ypo)<=m :
            return i
        
    if abs(ax-ex)==1 and abs(ay-ey)==1:
        raise Exception(str(ay+ax*4000000))
        return -1

    mx=(ax+ex)//2
    my=(ay+ey)//2

    is_in(ax,ay,mx,my)
    is_in(mx,ay,ex,my)
    is_in(ax,my,mx,ey)
    is_in(mx,my,ex,ey)
      
try:        
    is_in(0,0,4000000,4000000)
except Exception as error:
        print(str(error))

#visualisation for test
line="""
for y in range(20):
    line+="\n"
    for x in range(20):
        v=is_in(y,x,y+1,x+1)
        if v<0:
            line+="."
        else:
            line+=chr(ord("A")+v)
print(line)
"""
