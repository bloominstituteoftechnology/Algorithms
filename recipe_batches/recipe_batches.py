#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  for i in recipe:
    for x in ingredients:
      if ingredients[x] - recipe[i] <= 0:
        print(ingredients[x], recipe[i])
        return 0
  else:
    return min(float(ingredients[x] / recipe[x]))


# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

#   print(recipe_batches(
#   { 'milk': 100, 'butter': 50, 'flour': 5 },
#   { 'milk': 138, 'butter': 48, 'flour': 51 }
# ))


print(recipe_batches(
  { 'milk': 100, 'butter': 50, 'flour': 5 },
  { 'milk': 200, 'butter': 500, 'flour': 25 }
))