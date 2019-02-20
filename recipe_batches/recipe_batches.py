#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  max_batch = 0
  for i, key in enumerate(recipe):
    # first check if ingredient is in both lists
    if key in ingredients:
      #matches key of ing to recipe
      curr_batch = int(ingredients[key]/recipe[key]) # should math.floor this
      if curr_batch < max_batch or i == 0:
        max_batch = curr_batch
    else:
      return 0
  return max_batch


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

  