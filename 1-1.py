
with open('advent/1-input.txt') as f:
    data=f.readlines()
numbers = []
for line in data:
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
print(output)