import sys
import math

file = open(f'{sys.path[0]}/input.txt', 'r')
time = int(file.readline())
buses = [int(element) for element in file.readline().split(',') if element != 'x']
minTime = math.inf
targetID = -1
for busID in buses:
    amount = math.floor(time / busID) + 1
    nextTime = busID * amount
    if (nextTime < minTime):
        targetID = busID
        minTime = nextTime
    minTime = min(minTime, nextTime)
print((minTime - time) * targetID)
