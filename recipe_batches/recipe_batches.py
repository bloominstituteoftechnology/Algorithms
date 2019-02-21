#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batches = []
    for item in recipe:
        if item not in ingredients:
            batches.append(0)
        elif recipe[item] > ingredients[item]:
            batches.append(0)
        else:
            batches.append(ingredients[item]//recipe[item])
    return min(batches)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

    # Need to compare keys in dictionary that are the same. Divide the recipe by the ingredients to ensure
    # that the number is a whole integer. If not, round down. And then check if the integers from those ops are the same.
    # if not take the smallest integer and return
    # that as the number of batches.
