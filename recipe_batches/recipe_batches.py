#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  divs = []
  for item in recipe:
    ing = ingredients.get(item)
    rec = recipe.get(item)
    if ing==None or rec==None:
      return 0
    divs.append(int(ing/rec))
  min = 9999999999
  for div in divs:
    if div < min:
      min = div
  return min


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5, 'salt':1 }
  ingredients = { 'milk': 132, 'butter': 50, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))