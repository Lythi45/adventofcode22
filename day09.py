hpos=(0,0)
tpos=hpos
tpset=set()
tpset.add(tpos)
rich={"D":(0,1),"U":(0,-1),"L":(-1,0),"R":(1,0)}
for line in open("day09.txt").readlines():
    ri,steps = (lambda x: (rich[x[0]],int(x[1]))) (line.strip().split(" "))
    print(ri,steps)
    for i in range(steps):
        hpos=(hpos[0]+ri[0],hpos[1]+ri[1])
        xd = tpos[0]-hpos[0]
        yd = tpos[1]-hpos[1]
        xs = xd//abs(xd) if abs(xd)>1 or abs(xd)>0 and abs(yd)>1 else 0
        ys = yd//abs(yd) if abs(yd)>1 or abs(yd)>0 and abs(xd)>1 else 0
        tpos=(tpos[0]-xs,tpos[1]-ys)
        tpset.add(tpos)
        vis="""
        for y in range(-4,1):
            l=""
            for x in range(6):
                if (x,y)==hpos:
                    l+="H"
                elif (x,y)==tpos:
                    l+="T"
                else:
                    l+="."
            print(l)
        print(tpos,hpos)
        """
print(len(tpset))

posl=[(0,0) for _ in range(10)]
tpset=set()
tpset.add(posl[0])

rich={"D":(0,1),"U":(0,-1),"L":(-1,0),"R":(1,0)}
for line in open("day09.txt").readlines():
    ri,steps = (lambda x: (rich[x[0]],int(x[1]))) (line.strip().split(" "))
    print(ri,steps)
    for i in range(steps):
        posl[0]=(posl[0][0]+ri[0],posl[0][1]+ri[1])
        for i in range(9):
            hpos=posl[i]
            tpos=posl[i+1]
            
            xd = tpos[0]-hpos[0]
            yd = tpos[1]-hpos[1]
            xs = xd//abs(xd) if abs(xd)>1 or abs(xd)>0 and abs(yd)>1 else 0
            ys = yd//abs(yd) if abs(yd)>1 or abs(yd)>0 and abs(xd)>1 else 0
            posl[i+1]=(tpos[0]-xs,tpos[1]-ys)

        tpset.add(posl[9])
            
    print(posl)
print(len(tpset))