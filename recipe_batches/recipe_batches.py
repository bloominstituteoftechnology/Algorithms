#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  ing_keys =  set(ingredients.keys())
  rec_keys =  recipe.keys()
  batches = []
  for k in rec_keys:
    if k not in ing_keys:
      return 0
    batches.append(int(ingredients[k] / recipe[k]))
  return min(batches)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))