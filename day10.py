x=1
cycle=0
sum_x=0
disp=""

def test_cyc(x):
    global sum_x,cycle,disp
    disp+="#" if abs(x-cycle%40)<2 else "."
    cycle+=1
    if cycle in range(20,221,40):
        sum_x+=cycle*x

for line in open("day10.txt").readlines():
    parts=line.strip().split(" ")
    if parts[0]=="addx":
        test_cyc(x)
        test_cyc(x)
        x+=int(parts[1])
    else:
        test_cyc(x)
print(sum_x)
for r in range(0,240,40):
    print(disp[r:r+40])