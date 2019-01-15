#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  remaining_ingredients = ingredients
  check_ingredients = True
  batches = 0

  while check_ingredients:
    has_complete_batch = True
    for item in recipe.keys(): # For each item in recipe, check if there are enough items in ingredients
      if item in remaining_ingredients and remaining_ingredients[item] >= recipe[item]:
        remaining_ingredients[item] -= recipe[item] # If yes then subtract recipe items from ingredients
      else: # If there are not enough items, then return number of batches
        has_complete_batch = False
        break

    if has_complete_batch:
      batches += 1
    else:
      check_ingredients = False

  return batches

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))