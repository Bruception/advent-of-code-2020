import sys

def getConsensus(group):
    letterMap = {}
    for ch in ''.join(group):
        letterMap[ch] = 1 if ch not in letterMap else letterMap[ch] + 1
    total = 0
    for key in letterMap:
        if (letterMap[key] == len(group)):
            total += 1
    return total

group = []
total = 0
file = open(f'{sys.path[0]}/input.txt', 'r')
for line in file:
    if (line != '\n'):
        group.append(line[:-1])
    else:
        total += getConsensus(group)
        group.clear()
total += getConsensus(group)
print(total)
