import sys
file = open(f'{sys.path[0]}/input.txt', 'r')
map = [list(line)[0:-1] for line in file]
numRows = len(map)
numCols = len(map[0])
x, y = 0, 0
trueY = 0
numTrees = 0
while (trueY < numRows):
    if (map[y][x] == '#'):
        numTrees += 1
    x = (x + 3) % numCols
    y = (y + 1) % numRows
    trueY += 1
print(numTrees)
