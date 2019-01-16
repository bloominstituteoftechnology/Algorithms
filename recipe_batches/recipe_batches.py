#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    ing_batches = []
    if len(recipe) > len(ingredients):
        print(0)
        return 0
    for x in recipe:
        ing_batches.append(int(ingredients[x]/recipe[x]))
    print(min(ing_batches))
    return min(ing_batches)


if __name__ == '__main__':
        # Change the entries of these dictionaries to test
        # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
