#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # get all the keys in each dictionary
  r_keys = recipe.keys()
  i_keys = ingredients.keys()

  results = []
  min = None
  
  # want to loop through each of they keys inside recipe
  for i, key in enumerate(r_keys):
    value = None
    # integer divide each recipe key with the corresponding key in ingredients
    if key in i_keys:
      value = ingredients[key] // recipe[key]
    else:
      value = 0
    
  # initialize the value on first run and if the new value is lower than the current min update it
    if min == None or min > value:
      min = value
  return min

print(recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 }))

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))