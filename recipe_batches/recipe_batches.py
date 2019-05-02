#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  multipiler = math.inf
  for key, value in recipe.items():
    if key in ingredients:  
      calc_multiplier = (ingredients[key])//value
      if calc_multiplier < multipiler:
        multipiler = calc_multiplier
      print(f'multipiler: {multipiler}, calc_multiplier: {calc_multiplier}')
    else:
      return 0
  return multipiler

# def recipe_batches(recipe, ingredients):
#   min_ratio = math.inf

#   for ingredient, amount in recipe.items():
#     if ingredient not in ingredients:
#       return 0
#     ratio = math.floor(ingredients[ingredient] / amount)
#     if ratio < min_ratio:
#       min_ratio = ratio
    
#   return min_ratio

# print(recipe_batches({ 'milk': 100, 'butter': 50, 'cheese': 10 }, { 'milk': 200, 'butter': 52 }))

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))