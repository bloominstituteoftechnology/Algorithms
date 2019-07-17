#!/usr/bin/python


# // Note to self: // is amount of times number goes into other number 


import math

def recipe_batches(recipe, ingredients):
  batches = []
  if len(recipe) == len(ingredients):
    for key in recipe:
      batches.append(ingredients[key]//recipe[key])
    return min(batches)
  else:
    return 0
  


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))