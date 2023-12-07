with open('advent/3-input.txt') as f:
    data=f.readlines()
for line in range(len(data)):
    data[line] = data[line][:140]
safemap=[]
for line in data:
    safemap.append([0]*len(line))

for line in range(len(data)):
    for char in range(len(data[line])):
        if not data[line][char].isdigit() and data[line][char] != '.':
            safemap[line][char] = 1
            safemap[line-1][char-1] = 1
            safemap[line-1][char] = 1
            safemap[line-1][char+1] = 1
            safemap[line][char-1] = 1
            safemap[line][char+1] = 1
            safemap[line+1][char-1] = 1
            safemap[line+1][char] = 1
            safemap[line+1][char+1] = 1
partList = []
for line in range(len(data)):
    char = 0
    while char < len(data[line]):
        if data[line][char].isdigit():
            lenTest = data[line][char:]
            c=0
            while c < len(lenTest):
                test = data[line][char+c]
                if c == len(lenTest)-1 and data[line][char+c].isdigit():
                    if 1 in safemap[line][char:char+c]:
                        partList.append(int(data[line][char:char+c+1]))
                    char += 10
                    break
                if data[line][char+c].isdigit():
                    c+=1
                    continue
                else:
                    if 1 in safemap[line][char:char+c]:
                        partList.append(int(data[line][char:char+c]))
                    char += c
                    break
        else:
            char+=1
            continue

print(sum(partList))
                