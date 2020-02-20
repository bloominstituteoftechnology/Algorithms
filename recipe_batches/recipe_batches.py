#!/usr/bin/python

import math

"""
function parameters  recipe = {}, ingredients = {}
ingredient {
  name: amount
}
recipe {
  ingredient_name: amt available
}

return max



"""

def recipe_batches(recipe, ingredients):
  for key in recipe.keys():
    if key in ingredients:
      recipe[key] = ingredients[key] // recipe[key]
      if recipe[key] == 0:
        break
    else:
      recipe[key] = 0
  return min(recipe.values())

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))