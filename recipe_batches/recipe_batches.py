#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    recipe_arr = list(recipe.values())
    ingredient_arr = list(ingredients.values())
    how_much = []
    if len(recipe_arr) > len(ingredient_arr):
        return 0
    if len(recipe_arr) == 1:
        return math.floor(ingredient_arr[0] / recipe_arr[0])
    #  Above if statement is because the for loop wouldn't even start if range was (0, 0) just a minor bug
    #  I'll fix it if I get the chance
    for i in range(0, len(recipe_arr)-1):
        how_much.append(ingredient_arr[i] / recipe_arr[i])
    return math.floor(min(how_much))


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
    ingredients = { 'milk': 132, 'butter': 40, 'flour': 51 }
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))