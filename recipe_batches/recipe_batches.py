#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  prevMax = math.inf
  ingVal = list(ingredients.values())
  for i,val in enumerate(recipe.values()):
    if ingredients.keys() != recipe.keys():
      prevMax = 0
    elif ingVal[i]/val < 1:
      prevMax = 0
    elif ingVal[i]/val < prevMax:
      prevMax = round(ingVal[i]/val)
  return prevMax
  pass 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))