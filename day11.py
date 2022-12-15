lines= [x.strip().split(" ") for x in open("day11.txt").readlines()]
monkeys=[]
for monkey in range(len(lines)//7+1):
    start=monkey*7
    items=[int(x.strip(",")) for x in lines[start+1][2:]]
    op = lines[start+2][4]
    arg= lines[start+2][5]
    if op == "+":
        f=lambda x:x+int(arg)
    else:
        if arg == "old":
            f=lambda x:x*x
        else:
            f=lambda x:x*int(arg)
    test = int(lines[start+3][3])
    tr = int(lines[start+4][5])
    fa = int(lines[start+5][5])
    monkeys.append({"items":items,"f":f,"test":test,"true":tr,"false":fa,"arg":arg,"n":0})

mu=1
for m in monkeys:
    mu*=m["test"]

for part in range(2):
    div=[3,1][part]
    for round in range([20,10000][part]):
        for m in monkeys:
            for i in m["items"]:
                arg=m["arg"]
                ni=((m["f"](i))//div)%mu
                if ni%m["test"]==0:
                    monkeys[m["true"]]["items"].append(ni)
                else:
                    monkeys[m["false"]]["items"].append(ni)
                m["n"]+=1
            m["items"]=[]
    so=sorted(monkeys,key=lambda x:x["n"])
    print(so[-1]["n"]*so[-2]["n"])
