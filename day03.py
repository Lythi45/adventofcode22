def num(char):
    return ord(char)-ord('a')+1 if char >='a' and char <='z' else ord(char)-ord('A')+27
su=0
rlist=[]

for line in open("day03.txt").readlines():
    ls=line.strip()
    r1=set(list(ls[:len(ls)//2]))
    r2=set(list(ls[len(ls)//2:]))
    rlist.append(set(list(ls)))
    common=(r1&r2).pop()
    print(common,num(common))
    su+=num(common)

print(su)

print(sum([num((rlist[i]&rlist[i+1]&rlist[i+2]).pop()) for i in range(0,len(rlist),3)]))