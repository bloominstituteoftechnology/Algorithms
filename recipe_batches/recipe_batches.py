#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

  max_batches = 2 ** 100

  batches = {}
  for i in recipe:
    # print(i)
    try:
      batches[i] = ingredients[i] // recipe[i]
    except:
      print(f'{i} not in ingredients')
      return 0 
  
  for i in batches.values():
    if i < max_batches:
      max_batches = i

  return max_batches

recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
print(recipe_batches(recipe, ingredients))




if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))