import sys
file = open(f'{sys.path[0]}/input.txt', 'r')
map = [list(line)[0:-1] for line in file]
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
numRows = len(map)
numCols = len(map[0])
def getNumTrees(slope):
    slopeX, slopeY = slope
    x, y = 0, 0
    trueY = 0
    numTrees = 0
    while (trueY < numRows):
        if (map[y][x] == '#'):
            numTrees += 1
        x = (x + slopeX) % numCols
        y = (y + slopeY) % numRows
        trueY += slopeY
    return numTrees
multiple = 1
for slope in slopes:
    multiple *= getNumTrees(slope)
print(multiple)
