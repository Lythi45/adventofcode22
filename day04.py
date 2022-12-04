contains=0
overlap=0
for line in open("day04.txt").readlines():
    elf_range1,elf_range2=[set(range(x[0],x[1]+1)) for x in [list(map(int,r.split("-"))) for r in line.strip().split(",")]]
    #elf_range1,elf_range2=[map(int,r.split("-")) for r in line.strip().split(",")]
    
    print(elf_range1,elf_range2)
    if elf_range1-elf_range2==set() or elf_range2-elf_range1==set():
        contains+=1
    if elf_range1&elf_range2!=set():
        overlap+=1

print(contains)
print(overlap)