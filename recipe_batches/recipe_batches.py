#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    if set(recipe.keys()) == set(ingredients.keys()):
        list_of_batches_ingred = []
        for key in recipe.keys():
            list_of_batches_ingred.append(math.floor(ingredients[key] / recipe[key]))
        if min(list_of_batches_ingred) == 0:
            return None
        else:
            return min(list_of_batches_ingred)
    else:
        return None


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
