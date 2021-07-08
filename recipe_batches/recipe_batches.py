#!/usr/bin/python

import math

#  to get item name for item in recipe 
#  to get item count do recipe[item]

def recipe_batches(recipe, ingredients):

  batchCount = 9999999

  for ingredient, quantity in recipe.items():
    if ingredient not in ingredients:
      return 0
  
    ratio = ingredients[ingredient] // quantity

    if ratio < batchCount:
      batchCount = ratio

  return batchCount
  
if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))