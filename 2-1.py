with open('advent/2-input.txt') as f:
    data=f.readlines()

#12 red, 13 green, 14 blue
badgame = []
total = 0
for x in range(len(data)):
    id = data[x][5:data[x].find(':')]
    games=data[x][data[x].find(':')+2:]
    gameslist=games.split('; ')
    for g in range(len(gameslist)):
        gameslist[g] = gameslist[g].split(', ')
        for t in range(len(gameslist[g])):
            if gameslist[g][t].find('red') != -1:
                if int(gameslist[g][t][0:gameslist[g][t].find(' ')])>12:
                    badgame.append(int(data[x][5:data[x].find(':')]))
                    break
            if gameslist[g][t].find('blue') != -1:
                if int(gameslist[g][t][0:gameslist[g][t].find(' ')])>14:
                    badgame.append(int(data[x][5:data[x].find(':')]))
                    break
            if gameslist[g][t].find('green') != -1:
                if int(gameslist[g][t][0:gameslist[g][t].find(' ')])>13:
                    badgame.append(int(data[x][5:data[x].find(':')]))
                    break     
    total += int(data[x][5:data[x].find(':')])

print(total)
print(badgame)
print(total-sum(list(set(badgame))))