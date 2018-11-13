#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    # make lists from values of passed in dictionaries
    recipe_quantities = list(recipe.values())
    ingredients_quantities = list(ingredients.values())
    # add 0 for each left off ingredient (specifically for the first test)
    while len(recipe_quantities) != len(ingredients_quantities):
        ingredients_quantities.append(0)
    # create a new list and add the ratio of eligible batches, rounded down to an int
    minimum_case = list()
    for i in range(0, len(recipe_quantities)):
        minimum_case.append(int(ingredients_quantities[i] / recipe_quantities[i]))
    # return the minimum value (least number of batches) from the above operation
    return min(minimum_case)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
    recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
    ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
    print("{batches} batches can be made from the available ingredients:   {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
