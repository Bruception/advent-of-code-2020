import sys

class HashedCircularList:

    class Node:
        def __init__(self, value):
            self.next = None
            self.value = value

    def __init__(self, nums):
        self.nodeMap = {}
        self.head = self.Node(None)
        self.minValue, self.maxValue = 1, 9
        self.addNums(nums)

    def addNums(self, nums):
        current = self.head
        for num in nums:
            current.next = self.Node(num)
            current = current.next
            self.nodeMap[num] = current
        current.next = self.head.next
        self.head = self.head.next

    def getNextThree(self, node):
        nextNode = node.next.next.next.next
        threeCups = node.next
        node.next = nextNode
        return threeCups

    def addThreeAt(self, value, threeCups):
        destNode = self.nodeMap[value]
        prevNext = destNode.next
        destNode.next = threeCups
        threeCups.next.next.next = prevNext

nums = [int(num) for num in list(open(f'{sys.path[0]}/input.txt', 'r').readline())]

def playRound(hcl, current):
    nextThree = hcl.getNextThree(current)
    first, second, third = nextThree.value, nextThree.next.value, nextThree.next.next.value
    destValue = current.value - 1
    while (destValue == first or destValue == second or destValue == third or destValue == 0):
        destValue -= 1
        if (destValue < hcl.minValue):
            destValue = hcl.maxValue
    hcl.addThreeAt(destValue, nextThree)

def cupsAfter1(hcl):
    buffer = []
    current = hcl.nodeMap[1].next
    while (current.value != 1):
        buffer.append(str(current.value))
        current = current.next
    return ''.join(buffer)

currentRound = 0
hcl = HashedCircularList(nums)
currentCup = hcl.head
while (currentRound < 100):
    playRound(hcl, currentCup)
    currentCup = currentCup.next
    currentRound += 1
print(cupsAfter1(hcl))
