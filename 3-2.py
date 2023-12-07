with open('advent/3-input.txt') as f:
    data=f.readlines()
for line in range(len(data)):
    data[line] = data[line][:140]
safemap=[]
gearMap=[]
for line in data:
    safemap.append([0]*len(line))
    gearMap.append([0]*len(line))

for line in range(len(data)):
    for char in range(len(data[line])):
        if data[line][char] == '*':
            safemap[line][char] = '*'
            safemap[line-1][char-1] = 1
            safemap[line-1][char] = 1
            safemap[line-1][char+1] = 1
            safemap[line][char-1] = 1
            safemap[line][char+1] = 1
            safemap[line+1][char-1] = 1
            safemap[line+1][char] = 1
            safemap[line+1][char+1] = 1

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
                        for i in range(char,char+c):
                            safemap[line][i] += 1
                    char += 10
                    break
                if data[line][char+c].isdigit():
                    c+=1
                    continue
                else:
                    if 1 in safemap[line][char:char+c]:
                        for i in range(char,char+c):
                            safemap[line][i] += 1
                    char += c
                    break
        else:
            char+=1
            continue
ind = 1
for line in range(len(safemap)):
    for char in range(len(safemap[line])):
        if safemap[line][char] == '*':
            safemap[line][char] = 1
            maxrows = []
            maxrows.append([safemap[line-1][char-1],safemap[line-1][char],safemap[line-1][char+1]])
            maxrows.append([safemap[line][char-1],safemap[line][char],safemap[line][char+1]])
            maxrows.append([safemap[line+1][char-1],safemap[line+1][char],safemap[line+1][char+1]])
            gears1 = maxrows.count([2,1,1])
            gears2 = maxrows.count([2,2,1])
            gears3 = maxrows.count([2,1,2])*2
            gears4 = maxrows.count([2,2,2])
            gears5 = maxrows.count([1,2,2])
            gears6 = maxrows.count([1,2,1])
            gears7 = maxrows.count([1,1,2])
            gears = gears1+gears2+gears3+gears4+gears5+gears6+gears7
            if gears == 2:
                gearMap[line][char] = '*'
                gearMap[line-1][char-1] = ind
                gearMap[line-1][char] = ind
                gearMap[line-1][char+1] = ind
                gearMap[line][char-1] = ind
                gearMap[line][char+1] = ind
                gearMap[line+1][char-1] = ind
                gearMap[line+1][char] = ind
                gearMap[line+1][char+1] = ind
                ind+=1
partList = [1]*330
for line in range(len(data)):
    char = 0
    while char < len(data[line]):
        print(data[line][char])
        if data[line][char].isdigit() and gearMap[line][char]>0: 
            if data[line][char-1].isdigit():
                if data[line][char-2].isdigit():
                    start=char-2
                else:
                    start=char-1
            else:
                start=char
            if data[line][char+1].isdigit():
                if data[line][char+2].isdigit():
                    end=char+2
                else:
                    end=char+1
            else:
                end=char
            value = int(data[line][start:end+1])
            print(value)
            partList[gearMap[line][char]]*=value
            diff = end - char
            char += diff+1
        else:
            char+=1
print(sum(partList)-1)

    