sum=0
ops={"A":1,"B":2,"C":3}
mys={"X":1,"Y":2,"Z":3}
for line in open("day02.txt").readlines():
    op,my=map(lambda x:x.strip(),line.split(" "))
    sum+=mys[my]+(mys[my]-ops[op]+1)%3*3

print(sum)

sum=0
for line in open("day02.txt").readlines():
    op,my=map(lambda x:x.strip(),line.split(" "))
    n_my=(ops[op]+mys[my])%3+1
    #print(ops[op],mys[my],n_my)
    #print(n_my+(n_my-ops[op]+1)%3*3)
    sum+=n_my+(n_my-ops[op]+1)%3*3

print(sum)