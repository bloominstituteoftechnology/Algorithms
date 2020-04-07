#!/usr/bin/python

import math

# run time: O(n)
def recipe_batches(recipe, ingredients):
    batches = []
    for item in recipe:
        if item not in ingredients:
            return 0
        batches.append(ingredients[item] // recipe[item])
    return min(batches)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = { 'milk': 100, 'butter': 50, 'cheese': 10 }
    ingredients = { 'milk': 198, 'butter': 52, 'cheese': 10 }
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

