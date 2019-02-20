#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    min = float('inf')
    for ingredient in recipe:
        try:
            times = ingredients[ingredient] // recipe[ingredient]
            if times < min:
                min = times
        except KeyError:
            return 0
    return min

# time complexity is O(k) where k = number of ingredients a recipe requires
# space complexity is O(1)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
