#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # each ingredient value is = or > recipe value
  batches = 0
  recipe_keys = list(recipe.keys())
  ingredients_keys = list(ingredients.keys())
  recipe_vals = list(i[1] for i in recipe.items())
  ingredients_vals = list(i[1] for i in ingredients.items())
  # recipe_val = recipe.values()
  # ingredients_val = ingredients.values()
  # first check if you have all ingredients
  if(recipe_keys == ingredients_keys):
  # then check if you have enough ingredients
  # while loop to subtract and keep count
      



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
