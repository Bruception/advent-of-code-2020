import re
import sys

def clean(bag):
    bag = re.sub(r'[0-9]+ ', '', bag.lstrip())
    cleaned = bag.replace(' bag', '')
    return cleaned[:-1] if cleaned[-1] == 's' else cleaned

file = open(f'{sys.path[0]}/input.txt', 'r')
fullBag = re.compile(r'^([a-z\s]+) bags contain ((\s?[0-9]+ [a-z\s]+ bags?,?)+)\.$')
bags = {}
for line in file:
    matchesFullBag = fullBag.match(line)
    if (matchesFullBag):
        matchedGroups = matchesFullBag.groups()
        containedBags = [clean(bag) for bag in matchedGroups[1].split(',')]
        containingBag = matchedGroups[0]
        bags[containingBag] = containedBags

def explore(bag):
    if (bag not in bags):
        return False
    if ('shiny gold' in bags[bag]):
        return True
    for bag in bags[bag]:
        contained = explore(bag)
        if (contained):
            return True

numBagsHoldGold = 0

for bag in bags:
    contained = explore(bag)
    if (contained):
        numBagsHoldGold += 1

print(numBagsHoldGold)


