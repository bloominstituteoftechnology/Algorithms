#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    enough = []
    for key in recipe:
        if ingredients.get(key) is not None:
            enough.append(ingredients[key]//recipe[key])
        else:
            enough.append(0)
    return min(enough)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
