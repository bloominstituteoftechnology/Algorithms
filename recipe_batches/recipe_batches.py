#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  #check if we have enough for one batch
  #if not, just return 0
  #take the ratio of each ingredient
  #return the samllest ratio of all the ratios
  min_ratio = math.inf

  for ingredient, amount in recipe.items():
    if ingredient not in ingredients:
      return 0
    ratio = ingrdients[ingredient] // amount
    if ratio < min_ratio:
      min_ratio = ratio

  return min_ratio



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))