#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    difference = []
    for recipe_ingredient in recipe:
        if recipe_ingredient in ingredients:
            difference.append(
                ingredients[recipe_ingredient] / recipe[recipe_ingredient])
        else:
            difference = [0]
            break
    if min(difference) < 1:
        return 0
    else:
        return round(min(difference) - 0.4)


if __name__ == '__main__':
        # Change the entries of these dictionaries to test
        # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'cheese': 10}
    ingredients = {'milk': 198, 'butter': 52, 'cheese': 10}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
