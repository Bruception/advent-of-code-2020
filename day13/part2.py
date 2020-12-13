import sys

def egcd(a, b):
    x, y = 0, 1
    lastx, lasty = 1, 0
    while (b):
        a, (q, b) = b, divmod(a, b)
        x, lastx = lastx - (q * x), x
        y, lasty = lasty - (q * y), y
    return (lastx, lasty, a)

def crt(congruences):
    N = 1
    for a, n in congruences:
        N *= n
    result = 0
    for a, n in congruences:
        m = N // n
        r, s, d = egcd(n, m)
        result += a * s * m
    return result % N

file = open(f'{sys.path[0]}/input.txt', 'r')
file.readline()
buses = file.readline().split(',')
busOffsets = [(int(buses[i]), i) for i in range(len(buses)) if buses[i] != 'x']
congruences = [((busID - offset) % busID, busID) for busID, offset in busOffsets]
print(crt(congruences))
