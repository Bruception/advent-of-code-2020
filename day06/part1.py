import sys

def getUnique(string):
    letterMap = {}
    unique = 0
    for ch in string:
        if (ch not in letterMap):
            unique += 1
            letterMap[ch] = True
    return unique

group = []
total = 0
file = open(f'{sys.path[0]}/input.txt', 'r')
for line in file:
    if (line != '\n'):
        group.append(line[:-1])
    else:
        total += getUnique(''.join(group))
        group.clear()
total += getUnique(''.join(group))
print(total)
