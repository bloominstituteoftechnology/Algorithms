#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  max_batch = 999999
  for k in recipe:
    if k not in ingredients:
      return 0
    elif ingredients[k] < recipe[k]:
      return 0
    else:
      batch = int(ingredients[k] / recipe[k])
      if batch < max_batch:
        max_batch = batch
  return max_batch

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 500, 'butter': 500, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))