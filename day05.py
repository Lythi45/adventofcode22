for modus in range(2):
    stacks=[[] for i in range(9)]
    crane=False

    for line in open("day05.txt").readlines():
        if not crane:
            if line.strip()=="":
                crane=True
            elif line[1]!="1":
                [stacks[n].insert(0,line[n*4+1]) for n in range(9) if n*4+1<len(line) and line[n*4+1]!=" "]
        else:
            command=line.strip().split(" ")
            n=int(command[1])
            fro=int(command[3])-1
            to=int(command[5])-1
            stacks[to]+=stacks[fro][-n:] if modus==1 else stacks[fro][:-n-1:-1]
            stacks[fro]=stacks[fro][:-n]

    print("".join([stack.pop() for stack in stacks]))

           


