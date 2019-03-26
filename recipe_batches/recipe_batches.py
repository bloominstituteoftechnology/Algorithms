#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

  count = 0

  for name in recipe.keys():
    if name not in ingredients:
      return 0
    tempCount = int(ingredients[name] / recipe[name])
    if count == 0 or tempCount < count:
      count = tempCount

  return count

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 2}
  ingredients = { 'milk': 200 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))