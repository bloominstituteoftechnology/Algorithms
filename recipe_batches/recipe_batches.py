#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = []
  for i in recipe:
    if i in ingredients:
      batches.append(ingredients[i] // recipe[i])
    else:
      batches = 0
      return batches

  return min(batches)




  


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 2, 'butter': 40, 'flour': 5 }
  ingredients = { 'milk': 5, 'butter': 120, 'flour': 50}
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))