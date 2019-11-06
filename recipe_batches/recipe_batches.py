#!/usr/bin/python
'''
Plan:
find the smallest number of recipe that can fit in available ingredients.
return 0 if no ingredients.
'''
import math

def recipe_batches(recipe, ingredients):
  recipeKeys = recipe.keys()
  batchPass = 0
  batches = 0

  for k in recipeKeys:
    if k in ingredients:
      batchPass = ingredients[k] // recipe[k]
      if batches == 0:
        batches = batchPass
      elif batches > batchPass:
        batches = batchPass
    else:
      batches=0
      break
  

  return batches

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))