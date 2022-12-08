field=[[(int(e),0) for e in line.strip()] for line in open("day08.txt")]

for dir in range(4):
    nfield=[[] for _ in range(len(field[0]))]
    for line in field:
        max_h=-1
        for x,tree in enumerate(line):
            h=tree[0]
            if h>max_h:
                max_h=h
                nfield[-1-x].append((h,1))
            else:
                nfield[-1-x].append((h,tree[1]))
    field=nfield  
   
print(sum([sum([t[1] for t in line ]) for line in field]))

field=[[(int(e),1) for e in line.strip()] for line in open("day08.txt")]

for dir in range(4):
    nfield=[[] for _ in range(len(field[0]))]
    for line in field:
        max_h=-1
        for x,tree in enumerate(line):
            h=tree[0]
            xx=x-1
            while xx>=0 and line[xx][0]<h:
                xx-=1
            nfield[-1-x].append((h,tree[1]*(x-(xx if xx>=0 else 0))))
    field=nfield  

print(max([max([t[1] for t in line ]) for line in field]))

