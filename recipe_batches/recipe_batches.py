#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  max_batches = 0

  recipe_keys = set(recipe.keys())
  ingredients_keys = set(ingredients.keys())
  ingredients_keys_list = list(ingredients.keys())

  print(f"hello {recipe_keys}")
  print(f"hello {ingredients}")

  common_ingredients = set(recipe_keys).intersection(set(ingredients_keys))
  print(len(common_ingredients))
# first thing we want to check is if we even have the ingredients for the recipe in the first place.
  if len(common_ingredients) != len(ingredients_keys_list):
    return 0



if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5, 'dooper': 10 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
