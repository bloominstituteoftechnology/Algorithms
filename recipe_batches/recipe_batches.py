#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

  max_batches = None
  recipe_items = recipe.keys()

  for recipe_item in recipe_items:
    try:
      batches = int(ingredients[recipe_item] / recipe[recipe_item])

      if max_batches == None or batches < max_batches:
        max_batches = batches
    except: #if ingredient is not in pantry, errow will throw
      return 0
  
  return max_batches

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48}
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
