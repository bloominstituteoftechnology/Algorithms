#!/usr/bin/python

import math

recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }

print(ingredients['milk']/recipe['milk'])
print(ingredients['butter']/recipe['butter'])
print(ingredients['flour']/recipe['flour'])

# if any ratio is less than 1, no batches can be made
# the number of batches will be equivalent to the smallest ratio of ingredient items available to recipe items needed

# def recipe_batches(recipe, ingredients):
#   ratios = []
#   for i in ingredients:
#     for j in recipe:
#       ratios.append(ingredients[i]/recipe[j])
#   return ratios
#   pass 

def recipe_batches(recipe, ingredients):
  a = []
  b = []
  ratios = []
  min_ratio = 0
  limit = 0
  for i in ingredients:
    a.append(ingredients[i])
  for i in recipe:
    b.append(recipe[i])
  ratios = [x/y for x, y in zip(a,b)]
  min_ratio = min(ratios)
  if min_ratio > 1:
    limit = math.floor(min_ratio)
  else:
    print("Cannot make any batches")
  return limit

recipe_batches(recipe,ingredients)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 52, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))