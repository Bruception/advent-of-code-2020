import sys

line = open(f'{sys.path[0]}/input.txt', 'r').readline().split(',')
turnMap = {}
turnCount = {}
lastNum = 0
for i, num in enumerate(line):
    n = int(num)
    turnMap[n] = (i, i)
    turnCount[n] = 1
    lastNum = n
turn = len(turnMap)
while (turn < 30000000):
    timesSeen = turnCount[lastNum]
    if (timesSeen <= 1):
        lastNum = 0
        turnCount[0] += 1
        t1, t2 = turnMap[0]
        turnMap[0] = (t2, turn)
    else:
        t1, t2 = turnMap[lastNum]
        lastNum = t2 - t1
        turnCount[lastNum] = 1 if lastNum not in turnCount else turnCount[lastNum] + 1
        t3, t4 = (turn, turn) if lastNum not in turnMap else turnMap[lastNum]
        turnMap[lastNum] = (t4, turn)
    turn += 1
print(lastNum)
