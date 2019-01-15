#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # First implementation
    """
    count = 0
    while True:
        for item in recipe:
            if item not in ingredients:
                return count
            elif ingredients[item] < recipe[item]:
                return count
            else:
                ingredients[item] -= recipe[item]
        # If each item in recipe gets to the else statement
        count += 1
    """
    
    # Time efficiency optimization - O(n)
    batches = []
    for item in recipe:
        if item not in ingredients:
            return 0
        else:
            batches.append(ingredients[item] // recipe[item])
    return min(batches)


print(recipe_batches(
    {'milk': 100, 'butter': 50, 'flour': 5},
    {'milk': 138, 'butter': 51, 'flour': 51}
))

if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
