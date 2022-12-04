contains=0
overlap=0
for line in open("day04.txt").readlines():
    elf_range1,elf_range2=[set(range(x[0],x[1]+1)) for x in [list(map(int,r.split("-"))) for r in line.strip().split(",")]]
    
    if elf_range1-elf_range2==set() or elf_range2-elf_range1==set():
        contains+=1
    if elf_range1&elf_range2!=set():
        overlap+=1

print(contains)
print(overlap)

#One-liner
print(sum([(lambda x:x[0]<=x[2] and x[1]>=x[3] or x[2]<=x[0] and x[3]>=x[1])(list(map(int,line.strip().replace("-",",").split(",")))) for line in open("day04.txt").readlines()]))
print(sum([(lambda x:x[2]<=x[1] and x[0]<=x[3])(list(map(int,line.strip().replace("-",",").split(",")))) for line in open("day04.txt").readlines()]))

