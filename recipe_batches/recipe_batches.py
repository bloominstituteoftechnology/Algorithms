#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # For each ingredient in the recipe
    #   check that we have enough of that ingredient to make one
    #   If we don't, return zero
    #   Otherwise check how many batches with ingredients
    batches = None
    for ingredient in recipe.keys():

        if ingredient not in ingredients.keys():
            return 0

        if recipe[ingredient] > ingredients[ingredient]:
            return 0

        if batches is None:
            batches = ingredients[ingredient] // recipe[ingredient]

        if batches > (ingredients[ingredient] // recipe[ingredient]):
            batches = ingredients[ingredient] // recipe[ingredient]

    return batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 232, 'butter': 150, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
