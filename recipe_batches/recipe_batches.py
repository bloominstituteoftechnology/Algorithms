#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  min_ratio = math.inf

  for ingredient, amount in recipe.items():
    if ingredient not in ingredients:
       return 0
    ratio = ingredients[ingredient] // amount
    if ratio < min_ratio:
       min_ratio = ratio

  return min_ratio
pass 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 10, 'butter': 500, 'flour': 45 }
  ingredients = { 'milk': 248, 'butter': 8, 'flour': 1 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))