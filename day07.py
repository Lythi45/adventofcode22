root_dir={}
cur_dir=root_dir
dir_stack=[]
for line in open("day07.txt","r").readlines():
    parts=line.strip().split(" ")
    if parts[0]=="$":
        command=parts[1]
        if command=="cd":
            if parts[2]=="..":
                cur_dir=dir_stack.pop()
            elif parts[2]=="/":
                cur_dir=root_dir
                dir_stack=[]
            else:
                dir_stack.append(cur_dir)
                cur_dir=cur_dir[parts[2]]
    else:
        name=parts[1]
        if parts[0]=="dir":
            cur_dir[name]={}
        else:
            cur_dir[name]=int(parts[0])

summe=0
to_deleted=0
min_dir=0

def size(dir):
    global summe,to_deleted,min_dir
    s=sum([dir[x] if type(dir[x])==type(0) else size(dir[x]) for x in dir])
    if s<=100000:
        summe+=s
    if s>=to_deleted and s<min_dir:
        min_dir=s

    return s

total=size(root_dir)
print(summe)
to_deleted=total-40000000
min_dir=99999999
total=size(root_dir)
print(min_dir)

