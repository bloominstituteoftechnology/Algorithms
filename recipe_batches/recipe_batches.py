#!/usr/bin/python

import math

# I'm looking for the integer quotient k of 2 integers a and b such that a = bk + r

def recipe_batches(recipe, ingredients):
  if recipe.keys() != ingredients.keys():
    print('Missing ingredient')
    return 0
  else:
    quotients = []
    for i in ingredients:
      quotient = ingredients[i] // recipe[i]
      quotients.append(quotient)
    print('quotients: ', quotients)
    print('max batches: ', min(quotients))
    return min(quotients)
      


recipe_batches(
  { 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, 
  { 'milk': 1288, 'flour': 9, 'sugar': 95 }
)

recipe_batches(
  { 'milk': 100, 'butter': 50, 'cheese': 10 }, 
  { 'milk': 198, 'butter': 52, 'cheese': 10 }
)

# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))