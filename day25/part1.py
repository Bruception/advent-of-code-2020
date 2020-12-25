import sys

def transformSubjectNumber(subjectNumber, loopSize):
    return pow(subjectNumber, loopSize, 20201227)

file = open(f'{sys.path[0]}/input.txt', 'r')
cardKey = int(file.readline())
doorKey = int(file.readline())
loopSizeDoor = 1
subjectNumber = 7
while (transformSubjectNumber(subjectNumber, loopSizeDoor) != doorKey):
    loopSizeDoor += 1
print(transformSubjectNumber(cardKey, loopSizeDoor))
