#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = -1
  for k in recipe:
    if k in ingredients.keys():
      x = ingredients[k] // recipe[k]
      if batches != -1:
        if x < batches:
          batches = x
      else:
          batches = x
    else:
      batches = 0
  return batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))