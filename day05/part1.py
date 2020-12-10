import sys
import math

def getRow(sequence):
    low = 0
    high = 127
    seqID = 0
    while (low < high):
        middle = ((high - low) / 2) + low
        if (sequence[seqID] == 'F'):
            high = math.floor(middle)
        else:
            low = math.ceil(middle)
        seqID += 1
    return low

def getColumn(sequence):
    low = 0
    high = 7
    seqID = 0
    while (low < high):
        middle = ((high - low) / 2) + low
        if (sequence[seqID] == 'L'):
            high = math.floor(middle)
        else:
            low = math.ceil(middle)
        seqID += 1
    return low

def getSeatID(r, c):
    return r * 8 + c

file = open(f'{sys.path[0]}/input.txt', 'r')
maxID = 0
for line in file:
    rowPart = line[0:7]
    columnPart = line[7:]
    row = getRow(rowPart)
    column = getColumn(columnPart)
    seatID = getSeatID(row, column)
    maxID = max(maxID, seatID)
print(maxID)
