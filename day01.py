elv_calories=[0]
for line in open("day01.txt").readlines():
    if line.strip()=="":
        elv_calories.append(0)
    else:
        elv_calories[-1]+=int(line)
print(max(elv_calories))
print(sum(sorted(elv_calories)[-3:]))