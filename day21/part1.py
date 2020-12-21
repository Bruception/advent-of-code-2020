import re
import sys
from collections import defaultdict

pattern = re.compile(r'(([a-z]+ )+)\(contains(( [a-z]+,?)+)+\)')
file = open(f'{sys.path[0]}/input.txt', 'r')
lines = [line.strip('\n') for line in file]

foods = []
allAllergens = set()
allIngredients = set()
ingredientCount = defaultdict(int)
for line in lines:
    match = pattern.match(line).groups()
    ingredients = set(match[0][:-1].split(' '))
    allergens = set([allergen.lstrip() for allergen in match[2].split(',')])
    for ingredient in ingredients:
        ingredientCount[ingredient] += 1
    allIngredients |= ingredients
    allAllergens |= allergens
    foods.append((ingredients, allergens))

ingredientMapping = {i: set(allAllergens) for i in allIngredients}    
for ingredients, allergens in foods:
    for allergen in allergens:
        for ingredient in allIngredients:
            if (ingredient not in ingredients):
                ingredientMapping[ingredient].discard(allergen)

total = 0
for ingredient in ingredientMapping:
    if (len(ingredientMapping[ingredient]) == 0):
        total += ingredientCount[ingredient]
print(total)
