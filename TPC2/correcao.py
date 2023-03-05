from sys import stdin
from itertools import takewhile

ligado=False
total = 0

for line in stdin:

    line = line.lower()
    while len(line)>0:
        if line[:3] == "off":
            ligado = False
            line = line[3:]
        elif line[:2] == "on":
            ligado = True
            line = line[2:]
        elif line[0].isDigit():
            digits = ''.join(takewhile(lambda x: x.isDigit(), line))
            line = line[len(digits):]
            if ligado:
                total += int(digits)
        elif line[0] == '=':
            print(total)
            line = line[1:]
        else:
            line = line[1:]


print(total)