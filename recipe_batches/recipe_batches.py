#!/usr/bin/python

# import math

def recipe_batches(recipe, ingredients):
  batches = 0
  lowest = 0

  if len(recipe) > len(ingredients):
    return 0
  
  lowest = min(ingredients.values())
  ingredients_list = ingredients.items()
  key = ''

  for item in ingredients_list:
    
    if item[1] == lowest:
      key = item[0]

      amount = recipe.get(key)
      batches = item[1] // amount
     
  return batches

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))