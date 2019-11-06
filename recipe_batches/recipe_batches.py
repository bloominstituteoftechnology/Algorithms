#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batch = 0
  can_make = True

  while can_make:
    for key in recipe:
      if key in ingredients:
        if recipe[key] <= ingredients[key]:
          ingredients[key] = ingredients[key] - recipe[key]
        else:
          can_make = False
      else:
        can_make = False
    if can_make:
      batch += 1
  return batch


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))