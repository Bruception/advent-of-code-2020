import sys

class HashedCircularList:
    class Node:
        def __init__(self, value):
            self.next = None
            self.prev = None
            self.value = value

        def setNextPrev(self, next, prev):
            self.next = next
            self.prev = prev

    def __init__(self, nums):
        self.nodeMap = {}
        self.head = self.Node(None)
        self.head.setNextPrev(self.head, self.head)
        self.minValue, self.maxValue = 1, 9
        for num in nums:
            self.addLast(num)
        last = self.head.prev
        self.head = self.head.next
        self.head.prev = last
        last.next = self.head

    def addLast(self, num):
        newNode = self.Node(num)
        self.nodeMap[num] = newNode
        prevTail = self.head.prev
        prevTail.next = newNode
        newNode.setNextPrev(self.head, prevTail)
        self.head.prev = newNode

    def getNextThree(self, value):
        currentNode = self.nodeMap[value]
        nextNode = currentNode.next.next.next.next
        threeCups = currentNode.next
        currentNode.next = nextNode
        nextNode.prev = currentNode
        return threeCups

    def addThreeAt(self, value, threeCups):
        destNode = self.nodeMap[value]
        prevNext = destNode.next
        destNode.next = threeCups
        threeCups.prev = destNode
        threeCups.next.next.next = prevNext
        prevNext = threeCups.next.next

nums = [int(num) for num in list(open(f'{sys.path[0]}/input.txt', 'r').readline())]

def playRound(hcl, current):
    nextThree = hcl.getNextThree(current.value)
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
