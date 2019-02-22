#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  min=None
  for key in recipe:
    if key in ingredients:
      batches= ingredients[key]//recipe[key]
      if min==None or batches<min:
        min=batches
    else:
        min=0
  return min

print(recipe_batches({ 'milk': 2 }, { 'milk': 200}))
if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))