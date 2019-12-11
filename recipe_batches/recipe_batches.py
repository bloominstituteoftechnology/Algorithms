#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  max_batch = None
  for k in recipe:
    if k not in ingredients:
      return 0
    else:
      b = ingredients[k] // recipe[k]
      if not max_batch:
        max_batch = b
      elif max_batch > b:
        max_batch = b
  return max_batch


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))