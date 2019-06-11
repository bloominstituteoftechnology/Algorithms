#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = 0
  make = True

  while make:
    for key in recipe:
      if key in ingredients:
        if recipe[key] < ingredients[key]:
          ingredients[key] = ingredients[key] - recipe[key]
        else:
          make = False
      else:
        make = False
    if make:
      batches += 1
  return batches




if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))