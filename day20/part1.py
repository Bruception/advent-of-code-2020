import re
import sys

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

    def __repr__(self):
        return str(self.id)

tileRe = re.compile(r'Tile ([0-9]{4}):')
file = open(f'{sys.path[0]}/input.txt', 'r')
line = file.readline()
currentTile = None
tiles = []
while(line):
    isTileID = tileRe.match(line)
    if (isTileID):
        if (currentTile):
            currentTile.generateOrientations()
            tiles.append(currentTile)
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
for tile in tiles:
    aloneCount = 0
    for o in tile.orientations:
        for b in getBorders(o):
            if (len(borders[b]) == 1):
                aloneCount += 1
    if (aloneCount == 16):
        mul *= tile.id
print(mul)
