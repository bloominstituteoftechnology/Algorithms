#!/usr/bin/python

import random
import time
import argparse
import math



start = time.time()

def recipe_batches(recipe, ingredients):
  
  max_recipe_for_each_ingredient = []

  for row in recipe.items():
      if row[0] not in ingredients:
        return 0
      elif row[1] > ingredients[row[0]]:
        return 0
      max_recipe_for_each_ingredient.append(int(ingredients[row[0]]/row[1]))
  
  return min(max_recipe_for_each_ingredient)

print(recipe_batches({ 'milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 5, 'sugar': 120, 'butter': 500 }))

end_time = time.time()

ben_total_time = end_time - start


print('ben time:', ben_total_time)

start = time.time()

def recipe_batches1(recipe, ingredients):
  rcp = None
  for key in recipe.keys():
    ingredients.setdefault(key, 0)
    number_for_ingredient = ingredients[key] // recipe[key]
    if rcp is None or number_for_ingredient < rcp:
      rcp = number_for_ingredient
  return rcp

print(recipe_batches({ 'milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 5, 'sugar': 120, 'butter': 500 }))

end_time = time.time()

sergey_total_time = end_time - start


print('sergey time:', sergey_total_time)

start = time.time()

def recipe_batches2(recipe, ingredients):
  rArray = []
  iArray = []
  result = []
  for k, v in recipe.items():
    rArray.append(v)
  for k, v in ingredients.items():
    iArray.append(v)
  for i in range(0, len(rArray)):
    result.append(iArray[i]//rArray[i])
  return min(result)

print(recipe_batches({ 'milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 5, 'sugar': 120, 'butter': 500 }))

end_time = time.time()


ivan_total_time = end_time - start

print('Ivan time:', ivan_total_time)
if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))