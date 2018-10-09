#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches=None
  recipe_keys=recipe.keys()
  for ingredient in recipe_keys:
    try:
      min_ingredient=int(ingredients[ingredient]/recipe[ingredient])
      if batches==None:
        batches=min_ingredient
      elif min_ingredient<batches:
        batches=min_ingredient
    except:
      return 0
  return batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 30, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 156, 'butter': 78, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))