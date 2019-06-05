#!/usr/bin/python

import operator


def recipe_batches(recipe, ingredients):
    num_batches = {}  # These are the number of batches
    # each ingredient can make
    for k, v in recipe.items():
        if k not in ingredients:
            return 0

        num_batches[k] = ingredients[k] // v

    print(num_batches)
    return min(num_batches.items(), key=operator.itemgetter(1))[1]


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print(
        "{batches} batches can be made from the available ingredients: {ingredients}."
        .format(
            batches=recipe_batches(recipe, ingredients),
            ingredients=ingredients))
