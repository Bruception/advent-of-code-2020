import sys
from collections import deque
from itertools import islice

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

def playGame(p1Deck, p2Deck):
    deckSet = set()
    while (len(p1Deck) != 0 and len(p2Deck) != 0):
        key = (str(p1Deck), str(p2Deck))
        if (key in deckSet):
            return 1
        deckSet.add(key)
        p1Card = p1Deck.popleft()
        p2Card = p2Deck.popleft()
        roundWinner = 1
        if (p1Card <= len(p1Deck) and p2Card <= len(p2Deck)):
            p1DeckCopy = deque(islice(p1Deck, p1Card))
            p2DeckCopy = deque(islice(p2Deck, p2Card))
            roundWinner = playGame(p1DeckCopy, p2DeckCopy)
        else:
            roundWinner = 1 if p1Card > p2Card else 2
        if (roundWinner == 1):
            p1Deck.append(p1Card)
            p1Deck.append(p2Card)
        else:
            p2Deck.append(p2Card)
            p2Deck.append(p1Card)
    return 1 if len(p1Deck) > len(p2Deck) else 2

winner = playGame(playerDeck, crabDeck)
print(getScore(playerDeck) if winner == 1 else getScore(crabDeck))
