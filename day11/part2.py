import sys
import copy

file = open(f'{sys.path[0]}/input.txt', 'r')
seats = [list(line[:-1] if line[-1] == '\n' else line) for line in file]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
rows = len(seats)
cols = len(seats[0])

def countOccupied(i, j, seats):
    occupied = 0
    for x, y in directions:
        tx, ty = i + x, j + y
        while (tx >= 0 and tx < rows and ty >= 0 and ty < cols):
            if (seats[tx][ty] != '.'):
                occupied += 1 if seats[tx][ty] == '#' else 0
                break
            tx += x
            ty += y
    return occupied

def step(seats):
    seatsCopy = copy.deepcopy(seats)
    for i in range(rows):
        for j in range(cols):
            if (seats[i][j] == 'L' and countOccupied(i, j, seats) == 0):
                seatsCopy[i][j] = '#'
            elif (seats[i][j] == '#' and countOccupied(i, j, seats) >= 5):
                seatsCopy[i][j] = 'L'
    return seatsCopy

stepped = None
while (stepped != seats):
    stepped = seats
    seats = step(seats)
print(sum(row.count('#') for row in seats))
