import re
import sys

dirMap = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0),
}

angleMap = {
    90: 'N',
    270: 'S',
    0: 'E',
    180: 'W',
}

x, y, angle = 0, 0, 0
pattern = re.compile(r'^([A-Z]{1})([0-9]+)$')
file = open(f'{sys.path[0]}/input.txt', 'r')
moves = [pattern.match(line).groups() for line in file]
for move in moves:
    dir, amount = move
    amount = int(amount)
    isLeft = dir == 'L'
    if (isLeft or dir == 'R'):
        way = 1 if isLeft else -1
        angle += amount * way
        if (angle < 0):
            angle += 360
        angle %= 360
    else:
        key = angleMap[angle] if dir == 'F' else dir
        dx, dy = dirMap[key]
        x += dx * amount
        y += dy * amount
print(abs(x) + abs(y))
