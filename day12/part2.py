import re
import sys
import math

dirMap = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0),
}

def rotateAround(ox, oy, x, y, angle):
    rads = math.radians(angle)
    cx, cy = round(math.cos(rads)), round(math.sin(rads))
    dx, dy = x - ox, y - oy
    rx = (dx * cx) - (dy * cy)
    ry = (dy * cx) + (dx * cy)
    return (ox + rx, oy + ry)

x, y = 0, 0
wx, wy = 10, 1
pattern = re.compile(r'^([A-Z]{1})([0-9]+)$')
file = open(f'{sys.path[0]}/input.txt', 'r')
moves = [pattern.match(line).groups() for line in file]
for move in moves:
    dir, amount = move
    amount = int(amount)
    isLeft = dir == 'L'
    if (isLeft or dir == 'R'):
        way = 1 if isLeft else -1
        wx, wy = rotateAround(x, y, wx, wy, amount * way)
    elif (dir == 'F'):
        dx, dy = wx - x, wy - y
        x += amount * dx
        y += amount * dy
        wx += amount * dx
        wy += amount * dy
    else:
        dx, dy = dirMap[dir]
        wx += dx * amount
        wy += dy * amount
print(abs(x) + abs(y))
