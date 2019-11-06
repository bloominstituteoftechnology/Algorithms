#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  max_number = 0
  limit = None
  for key, value in recipe.items():
    if key in ingredients:
      number = ingredients[key] //value
    else:
      max_number= 0
      break
    if limit == None:
      max_number = number
      limit = max_number
    else:
      if number< limit:
        limit = number


  return max_number


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))