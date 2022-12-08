search_4=True
input=open("day06.txt","r").read()
for i in range(len(input)-3):
    if search_4 and len(set(list(input[i:i+4])))==4:
        print(i+4)
        search_4=False
    if len(set(list(input[i:i+14])))==14:
        print(i+14)
        break
        
