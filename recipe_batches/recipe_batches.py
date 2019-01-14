#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    recipe_dict = {}
    ingredients_dict = {}
    for k, v in recipe.items():
        recipe_dict[k] = v
    for k, v in ingredients.items():
        ingredients_dict[k] = v
    return ingredients_dict


if __name__ == '__main__':
        # Change the entries of these dictionaries to test
        # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
