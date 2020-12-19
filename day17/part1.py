import sys

def enumerateDirections(buffer, dirs, allZeroes = True):
    if (len(buffer) == 3):
        if (not allZeroes):
            dirs.append(tuple(buffer))
        return
    for i in range(-1, 2):
        buffer.append(i)
        enumerateDirections(buffer, dirs, allZeroes and i == 0)
        buffer.pop()
    return dirs

dirs = tuple(enumerateDirections([], []))

def countActive(space, coord):
    active = 0
    x, y, z = coord
    for (x1, y1, z1) in dirs:
        dx, dy, dz = x + x1, y + y1, z + z1
        coord = (dx, dy, dz)
        if (coord in space):
            active += 1
    return active
    
def step(space, curr, dim, spaceCopy, coord):
    minD = min(c[curr] for c in space)
    maxD = max(c[curr] for c in space)
    for d in range(minD - 1, maxD + 2):
        coord.append(d)
        if (dim != 1):
            step(space, curr + 1, dim - 1, spaceCopy, coord)
        else:
            c = tuple(coord)
            active = countActive(space, c)
            if (c in space and (active == 2 or active == 3)):
                spaceCopy.add(c)
            elif (c not in space and active == 3):
                spaceCopy.add(c)
        coord.pop()
    return spaceCopy

def simulate():
    steps = 0
    space = set()
    file = open(f'{sys.path[0]}/input.txt', 'r')
    firstSlice = [list(line[:-1] if line[-1] == '\n' else line) for line in file]
    for x in range(len(firstSlice)):
        for y in range(len(firstSlice[0])):
            if (firstSlice[x][y] == '#'):
                space.add((x, y, 0))
    while (steps < 6):
        spaceCopy = step(space, 0, 3, set(), [])
        space = spaceCopy
        steps += 1
    print(len(space))
simulate()
