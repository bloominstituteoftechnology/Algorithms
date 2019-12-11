#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  max_batches = 0

  recipe = list(recipe.values())
  ingredients = list(ingredients.values())
  print(f"hello {recipe}")
  print(f"hello {ingredients}")
  pass


if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
