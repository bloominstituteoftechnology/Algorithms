#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  left_over = [ingredients.get(k, 0) - v for k,v in recipe.items()]
  smallest_amount_left = min(left_over)
  if smallest_amount_left < 0:
    return 0
  else:
    amount_of_batches = 100
    for k,v in recipe.items():
      batch = ingredients.get(k) // v
      if amount_of_batches > batch:
        amount_of_batches = batch
  return amount_of_batches



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))