#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = []
  for x in recipe:
    if x not in ingredients:
      batches.append(0)
    elif recipe[x] > ingredients[x]:
      batches.append(0)
    else:
      batches.append(math.floor(ingredients[x]/recipe[x]))
  batches_complete = min(batches)
  return batches_complete or 0 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))