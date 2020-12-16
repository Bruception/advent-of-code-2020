import sys

line = [int(n) for n in open(f'{sys.path[0]}/input.txt', 'r').readline().split(',')]
turnMap = {}
for i, num in enumerate(line):
    turnMap[num] = i
turn = len(turnMap)
lastNum, nextNum = line[-1], 0
while (turn < 30000000):
    prev = turn - 1
    nextNum = prev - turnMap[lastNum] if lastNum in turnMap else 0
    turnMap[lastNum] = prev
    lastNum = nextNum
    turn += 1
print(lastNum)
