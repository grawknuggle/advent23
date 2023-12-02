with open('advent/2-input.txt') as f:
    data=f.readlines()
total=[]
for x in range(len(data)): #games
    id = data[x][5:data[x].find(':')]
    games=data[x][data[x].find(':')+2:]
    gameslist=games.split('; ')
    red=0
    blue=0
    green=0
    for g in range(len(gameslist)): #draws
        gameslist[g] = gameslist[g].split(', ')
        for t in range(len(gameslist[g])): #colors
            color = gameslist[g][t]
            if color.find('red') != -1 and int(color[0:color.find(' ')])>red:
                red = int(color[0:color.find(' ')])
            if color.find('blue') != -1 and int(color[0:color.find(' ')])>blue:
                blue = int(color[0:color.find(' ')])
            if color.find('green') != -1 and int(color[0:color.find(' ')])>green:
                green = int(color[0:color.find(' ')])
                  
    
    total.append(red*green*blue)
    #print(total)
output = sum(total)
print(output)