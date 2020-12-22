import sys
from collections import deque

file = open(f'{sys.path[0]}/input.txt', 'r')
file.readline()

crabDeck = deque()
playerDeck = deque()
currentDeck = playerDeck
for line in file:
    if (line == '\n'):
        continue
    if ('Player' in line):
        currentDeck = crabDeck
        continue
    else:
        currentDeck.append(int(line))

def getScore(deck):
    amountOfCards = len(deck)
    score = 0
    for card in deck:
        score += amountOfCards * card
        amountOfCards -= 1
    return score

def playGame():
    while (len(playerDeck) != 0 and len(crabDeck) != 0):
        playerCard = playerDeck.popleft()
        crabCard = crabDeck.popleft()
        if (playerCard > crabCard):
            playerDeck.append(playerCard)
            playerDeck.append(crabCard)
        else:  
            crabDeck.append(crabCard)
            crabDeck.append(playerCard)
    return getScore(playerDeck) if len(playerDeck) > len(crabDeck) else getScore(crabDeck)

print(playGame())
