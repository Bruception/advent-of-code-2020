import sys
import copy

file = open(f'{sys.path[0]}/input.txt', 'r')
seats = [list(line[:-1] if line[-1] == '\n' else line) for line in file]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
rows = len(seats)
cols = len(seats[0])

def countOccupied(i, j, seats):
    global rows, cols
    occupied = 0
    for x, y in directions:
        tx, ty = i, j
        while (True):
            tx += x
            ty += y
            if (tx < 0 or tx >= rows or ty < 0 or ty >= cols):
                break
            if (seats[tx][ty] != '.'):
                occupied = occupied + 1 if seats[tx][ty] == '#' else occupied
                break
    return occupied

def step(seats):
    seatsCopy = copy.deepcopy(seats)
    for i in range(rows):
        for j in range(cols):
            if (seats[i][j] == 'L'):
                if (countOccupied(i, j, seats) == 0):
                    seatsCopy[i][j] = '#'
            elif (seats[i][j] == '#'):
                if (countOccupied(i, j, seats) >= 5):
                    seatsCopy[i][j] = 'L'
    return seatsCopy

stepped = None
while (stepped != seats):
    stepped = seats
    seats = step(seats)

print(sum(row.count('#') for row in seats))
