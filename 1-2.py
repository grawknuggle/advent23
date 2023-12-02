with open('advent/1-input.txt') as f:
    data=f.readlines()
words = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
ttn = []
for line in data:
    ttnline=[]
    for c in range(len(line)):
        for pair in words.keys():
            if line[c:].find(pair) == 0:
                ttnline.append(str(words.get(pair)))
        if line[c].isdigit():
            ttnline.append(str(line[c]))
    ttn.append(ttnline)
numbers = []
for line in ttn:
    linenum = []
    for c in line:
        if c.isdigit():
            linenum.append(c)
    numbers.append(linenum)
digits = []
for line in numbers:
    td=str(line[0])+str(line[len(line)-1])
    td=int(td)
    digits.append(td)
output = sum(digits)
