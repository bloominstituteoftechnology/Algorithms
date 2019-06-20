#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  b = []
  for x in recipe:
    print(x)
    if x not in ingredients:
      b.append(0)
      print(b)
    elif recipe[x] > ingredients[x]:
      b.append(0)
    else:
      b.append(math.floor(ingredients[x]/recipe[x]))
  b_c = min(b)
  return b_c or 0 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))