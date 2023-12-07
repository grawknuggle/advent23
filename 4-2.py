with open('advent/4-input.txt') as f:
    data=f.readlines()
base = []
for x in range(len(data)):
    data[x]=data[x].split(':')
    data[x][1]=data[x][1].split('|')
    data[x][1][0]=data[x][1][0].split(None)
    data[x][1][1]=data[x][1][1].split(None)
    total = 0
    for i in data[x][1][0]:
        total += data[x][1][1].count(i)
    if total > 0:
        score = total
    else:
        score = 0
    base.append(score)
hits = [1]*len(base)
for x in range(len(base)):
    val = base[x]
    z=0
    while z < hits[x]:
        for y in range(x+1,x+val+1):
            hits[y] += 1
        z+=1
print(sum(hits))
