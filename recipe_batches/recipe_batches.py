#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  max_batch = 1000
  for key, value in recipe.items():
    if key not in ingredients.keys() or value > ingredients[key]:
      return 0
    pos_batch = math.floor(ingredients[key]/value)
    if pos_batch < max_batch:
      max_batch = pos_batch
  return max_batch

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))