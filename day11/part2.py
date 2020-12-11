import sys

file = open(f'{sys.path[0]}/input.txt', 'r')
seats = [list(line[:-1] if line[-1] == '\n' else line) for line in file]
directions = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))
rows = len(seats)
cols = len(seats[0])

def countOccupied(i, j):
    occupied = 0
    for x, y in directions:
        tx, ty = i + x, j + y
        while (tx >= 0 and tx < rows and ty >= 0 and ty < cols):
            seat = seats[tx][ty]
            if (seat != '.'):
                occupied += 1 if seat == '#' else 0
                break
            tx += x
            ty += y
    return occupied

def step(seats):
    seatsCopy = list(map(list, seats))
    for i in range(rows):
        for j in range(cols):
            seat = seats[i][j]
            if (seat == '.'): continue
            occupied = countOccupied(i, j)
            if (seat == 'L' and occupied == 0):
                seatsCopy[i][j] = '#'
            elif (seat == '#' and occupied >= 5):
                seatsCopy[i][j] = 'L'
    return seatsCopy

stepped = None
while (stepped != seats):
    stepped = seats
    seats = step(seats)
print(sum(row.count('#') for row in seats))
