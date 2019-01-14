#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  currMax = 0
  prevMax = 99999
  keyVals = recipe.keys()
  for key in keyVals:
    if not ingredients.get(key):
      return 0
    hold = ingredients.get(key)
    while (hold/recipe.get(key))  >= 1:
      currMax = currMax + 1
      hold = hold - recipe.get(key)
    if currMax < prevMax:
      prevMax = currMax
  return prevMax
  pass 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))