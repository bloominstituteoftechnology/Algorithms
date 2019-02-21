#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = []

# for every item in the recipe, check to see if it is there, if not return 0
# if it is, then devide the number of ingredients you have, by the number the recipe calls for
# and then return the number rounded down to the line above to get how many batches you would be able to make
  for i in recipe:
    if i not in ingredients:
      return 0
    else:
      batches.append(ingredients[i]//recipe[i])
      

  return min(batches)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))