import re
import sys

dirs = {
    'e': (1, -1, 0),
    'w': (-1, 1, 0),
    'se': (0, -1, 1),
    'sw': (-1, 0, 1),
    'nw': (0, 1, -1),
    'ne': (1, 0, -1),
}

tiles = {}
file = open(f'{sys.path[0]}/input.txt', 'r')
pattern = re.compile(r'(e|s[ew]|w|n[ew])')
for line in file:
    tileMovements = pattern.findall(line)
    x, y, z = 0, 0, 0
    for tile in tileMovements:
        dx, dy, dz = dirs[tile]
        x += dx
        y += dy
        z += dz
    coord = (x, y, z)
    tiles[coord] = not tiles[coord] if coord in tiles else True

def countBlackTiles(coord, tiles, new = {}):
    count = 0
    x, y, z = coord
    for (dx, dy, dz) in dirs.values():
        dCoord = (x + dx, y + dy, z + dz)
        if (dCoord in tiles and tiles[dCoord]):
            count += 1
        elif (dCoord not in tiles):
            new[dCoord] = False
    return count

def step(tiles):
    newTiles = {}
    new = {}
    for coord in tiles:
        isBlack = tiles[coord]
        count = countBlackTiles(coord, tiles, new)
        if (isBlack and (count == 0 or count > 2)):
            newTiles[coord] = False
        elif (not isBlack and count == 2):
            newTiles[coord] = True
        else:
            newTiles[coord] = isBlack
    for coord in new:
        count = countBlackTiles(coord, tiles)
        newTiles[coord] = count == 2
    return newTiles

for i in range(100):
    tiles = step(tiles)
print(sum(1 if isBlack else 0 for isBlack in tiles.values()))
