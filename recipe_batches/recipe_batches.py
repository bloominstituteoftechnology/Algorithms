#!/usr/bin/python

import math

# FIRST PASS


def recipe_batches(recipe, ingredients):
    # lowest number of batches that can be made

    # If recipe has more ingredients than ingrdients available
    if len(recipe) > len(ingredients):
        return 0

    for i, ingredient in enumerate(recipe):
        if ingredients[ingredient] // recipe[ingredient] == 0:
            return 0

        print(recipe[0])

        if ingredients[ingredient] // recipe[ingredient] < low:
            low = ingredients[ingredient] // recipe[ingredient]

    return low


if __name__ == '__main__':
                # Change the entries of these dictionaries to test
                # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
