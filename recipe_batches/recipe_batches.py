#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # print(ingredients)
    howMany = 0
    for r in recipe:
        if recipe[r] - ingredients[r] >= 0:
            howMany = 0
        else:
            total = ingredients[r] / recipe[r]
            howMany = total
    print(howMany)


recipe_batches({'milk': 100, 'butter': 50, 'flour': 5},
               {'milk': 138, 'butter': 100, 'flour': 51})


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
