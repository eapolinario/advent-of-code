#!/usr/bin/env python3

import re
from collections import Counter, defaultdict

def parse_food(line):
    r = re.compile(r"^(?P<ingredients>[^(]+)(| \(contains (?P<allergens>.*)\))$")

    match = re.search(r"^(?P<ingredients>[^(]+)(| \(contains (?P<allergens>.*)\))$", line)
    ingredients = match.group("ingredients").split(' ')
    allergens = set(match.group("allergens").split(', '))
    return {'ingredients': ingredients, 'allergens': allergens}

if __name__ == '__main__':
    import sys
    foods = []
    for line in sys.stdin:
        foods.append(parse_food(line.strip()))

    print(f'foods={foods}')

    ingredients = defaultdict(int)
    allergens = {}
    for f in foods:
        print(f'f={f}')
        for ingredient in f['ingredients']:
            ingredients[ingredient] += 1
        for allergen in f['allergens']:
            allergens[allergen] = allergens.get(allergen, set(f['ingredients'])) & set(f['ingredients'])

    print(f'ingredients={ingredients}')
    print(f'allergens={allergens}')

    all_allergens = set().union(*allergens.values())
    print(f'all_allergens={all_allergens}')
    print(f'sum of ingredients = {sum([ingredients[x] for x in set(ingredients).difference(all_allergens)])}')
