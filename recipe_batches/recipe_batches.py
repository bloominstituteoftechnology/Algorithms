#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    min_batch = None
    for ingredient in recipe:
        if ingredient in ingredients:
            # print(ingredients[ingredient], recipe[ingredient])
            batches = ingredients[ingredient] // recipe[ingredient]
            if min_batch is None:
                min_batch = batches
            else:
                min_batch = min(batches, min_batch)
        else:
            return 0
    return min_batch


recipe_batches(
    {'milk': 2, 'sugar': 40, 'butter': 20},
    {'milk': 5, 'sugar': 120, 'butter': 500}
)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
