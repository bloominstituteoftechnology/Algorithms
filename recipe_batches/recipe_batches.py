#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    count = []
    batch_count = 0

    if len(recipe) != len(ingredients):
        return batch_count
    for ingredient in recipe:
        count.append(ingredients[ingredient]//recipe[ingredient])
    batch_count = min(count)
    return batch_count


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
