#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batches = float("inf")
    for recipe_ingredient in recipe.keys():
        try:
            recipe_amount = recipe[recipe_ingredient]
            ingredient_amount = ingredients[recipe_ingredient]
            temp_batch = ingredient_amount // recipe_amount
            if temp_batch < batches:
                batches = temp_batch
        except:
            return 0

    return batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
