import re
import sys

def createTuple(bag):
    bag = bag.lstrip()
    amount = int(re.match('([0-9]+)', bag).group(1))
    cleaned = re.sub(r'[0-9]+ ', '', bag).replace(' bag', '')
    cleaned = cleaned[:-1] if cleaned[-1] == 's' else cleaned
    return (amount, cleaned)

file = open(f'{sys.path[0]}/input.txt', 'r')
fullBag = re.compile(r'^([a-z\s]+) bags contain ((\s?[0-9]+ [a-z\s]+ bags?,?)+)\.$')
bags = {}
for line in file:
    matchesFullBag = fullBag.match(line)
    if (matchesFullBag):
        matchedGroups = matchesFullBag.groups()
        containedBags = [createTuple(bag) for bag in matchedGroups[1].split(',')]
        containingBag = matchedGroups[0]
        bags[containingBag] = containedBags

def explore(bag):
    if (bag not in bags):
        return 0
    subtotal = 0
    for child in bags[bag]:
        amount, color = child
        subtotal += (amount * explore(color)) + amount
    return subtotal

print(explore('shiny gold'))
