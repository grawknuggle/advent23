with open('advent/4-input.txt') as f:
    data=f.readlines()
results = []
for x in range(len(data)):
    data[x]=data[x].split(':')
    data[x][1]=data[x][1].split('|')
    data[x][1][0]=data[x][1][0].split(None)
    data[x][1][1]=data[x][1][1].split(None)
    total = 0
    for i in data[x][1][0]:
        total += data[x][1][1].count(i)
    if total > 0:
        score = 2**(total-1)
    else:
        score = 0
    results.append(score)
print(sum(results))


