#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    difference = []
    for ingredient in recipe:
        if ingredient in ingredients:
            difference.append(ingredients[ingredient] / recipe[ingredient])
        else:
            difference = 0
            break
    if min(difference) < 1:
        return 0
    else:
        return round(max(difference) - 0.5)


if __name__ == '__main__':
        # Change the entries of these dictionaries to test
        # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
