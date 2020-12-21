import re
import sys
import math

def getBorders(image):
    return [
        image[0],
        ''.join([row[-1] for row in image]),
        image[-1],
        ''.join([row[0] for row in image]),
    ]

def getFlips(image):
    return [
        image,
        image[::-1],
        [row[::-1] for row in image],
        [row[::-1] for row in image][::-1],
    ]

def getRotations(image):
    rotations = [image]
    for i in range(3):
        image = list(map(list, zip(*image)))
        rotations.append([''.join(row) for row in image])
    return rotations

def getTransformations(image):
    possible = []
    for flip in getFlips(image):
        possible.extend(getRotations(flip))
    transformations = []
    for pos in possible:
        if (pos not in transformations):
            transformations.append(pos)
    return transformations

class Tile:
    def __init__(self, id):
        self.id = int(id)
        self.image = []
        self.orientation = 0
        self.orientations = None

    def generateOrientations(self):
        self.orientations = getTransformations(self.image)

    def getOrientation(self):
        return self.orientations[self.orientation]

    def __repr__(self):
        return str(self.id)

tileRe = re.compile(r'Tile ([0-9]{4}):')
file = open(f'{sys.path[0]}/input.txt', 'r')
line = file.readline()
currentTile = None
tiles = []
tileMap = {}
while(line):
    isTileID = tileRe.match(line)
    if (isTileID):
        if (currentTile):
            currentTile.generateOrientations()
            tiles.append(currentTile)
            tileMap[currentTile.id] = currentTile
        id = isTileID.groups()[0]
        currentTile = Tile(id)
    elif (len(line) > 1):
        currentTile.image.append(line.strip('\n'))
    line = file.readline()
currentTile.generateOrientations()
tiles.append(currentTile)

borders = {}
for tile in tiles:
    for o in tile.orientations:
        for b in getBorders(o):
            if (b not in borders):
                borders[b] = set([tile.id])
            else:
                borders[b].add(tile.id)
mul = 1
corners = []
for tile in tiles:
    aloneCount = 0
    for o in tile.orientations:
        for b in getBorders(o):
            if (len(borders[b]) == 1):
                aloneCount += 1
    if (aloneCount == 16):
        corners.append(tile)

def countTraversed(corner, size):
    dp = [[None] * size for i in range(size)]
    dp[0][0] = corner
    used = {
        corner.id: True
    }
    count = 0
    for i in range(size):
        for j in range(size):
            if (i == 0 and j == 0):
                continue
            leftParent = None if j - 1 < 0 else dp[i][j - 1]
            topParent = None if i - 1 < 0 else dp[i - 1][j]
            for tile in tiles:
                if (tile.id in used):
                    continue
                valid = False
                for oI, o in enumerate(tile.orientations):
                    tTop, tRight, tBottom, tLeft = getBorders(o)
                    validX = True
                    validY = True
                    if (leftParent):
                        top, right, bottom, left = getBorders(leftParent.getOrientation())
                        if (tLeft != right):
                            validX = False
                    if (topParent):
                        top, right, bottom, left = getBorders(topParent.getOrientation())
                        if (tTop != bottom):
                            validY = False
                    if (validX and validY):
                        valid = True
                        tile.orientation = oI
                        break
                if (valid):
                    used[tile.id] = True
                    dp[i][j] = tile
                    count += 1
                    break
    return (count + 1), dp

size = math.isqrt(len(tiles))
validMapping = None
for corner in corners:
    valid = False
    for i, o in enumerate(corner.orientations):
        corner.orientation = i
        count, dp = countTraversed(corner, size)
        if (count == len(tiles)):
            validMapping = dp
            valid = True
            break
    if (valid):
        break

def removeBorders(image):
    newImage = [[0] * (len(image) - 2) for row in range(len(image) - 2)]
    for i in range(1, len(image) - 1):
        for j in range(1, len(image[0]) - 1):
            newImage[i - 1][j - 1] = image[i][j]
    return newImage

for tile in tiles:
    tile.orientations[tile.orientation] = removeBorders(tile.getOrientation())

grid = []
for row in validMapping:
    for i in range(8):
        rowBuffer = []
        for tile in row:
            rowBuffer.extend(tile.getOrientation()[i])
        grid.append(rowBuffer)

monster = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''
monster = [list(row) for row in monster.split('\n')]
monsterHashCount = sum(row.count('#') for row in monster)

def countMonsters(grid):
    count = 0
    for i in range(len(grid) - len(monster)):
        for j in range(len(grid[0]) - len(monster[0])):
            valid = True
            for mi in range(len(monster)):
                if (not valid):
                    break
                for mj in range(len(monster[0])):
                    if (monster[mi][mj] == '#'):
                        if (grid[i + mi][j + mj] != '#'):
                            valid = False
                            break
            if (valid):
                count += 1
    return monsterHashCount * count

total = sum(row.count('#') for row in grid)
for g in getTransformations(grid):
    if (type(g[0]) == str):
        g = [list(row) for row in g]
    numberSeaMonsters = countMonsters(g)
    if (numberSeaMonsters != 0):
        print(total - numberSeaMonsters)
        break
