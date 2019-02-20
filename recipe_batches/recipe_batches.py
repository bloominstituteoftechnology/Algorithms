#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # return min(int(ingredients.get(elem, 0) // num) for elem, num in recipe.items())
    batches = []
    if len(recipe) != len(ingredients):
        return 0
    for el in recipe:
        if recipe[el] <= ingredients[el]:
            batches.append(int(ingredients[el]//recipe[el]))
        else:
            return 0

    return min(batches)


if __name__ == '__main__':
        # Change the entries of these dictionaries to test
        # your implementation with different inputs
    recipe = {'milk': 2, 'sugar': 40, 'butter': 20}
    ingredients = {'milk': 5, 'sugar': 120, 'butter': 500}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
