#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    max_batches = None
    for key in recipe:
        if not key in ingredients:
            # if you don't have any of one ingredient,
            # then you can't make any
            return 0
        local_max = math.floor(ingredients[key] / recipe[key])
        if max_batches is None or local_max < max_batches:
            max_batches = local_max
    return max_batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
