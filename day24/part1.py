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
print(sum(1 if isBlack else 0 for isBlack in tiles.values()))
