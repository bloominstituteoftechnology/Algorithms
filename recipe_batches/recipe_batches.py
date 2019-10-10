#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches =  []
  quantity = None
  try:
    for i in  recipe:
      if(ingredients[i]):
        quantity = int(ingredients[i]/ recipe[i])
        batches.append(quantity)
      maxBatches = min(batches)
    return maxBatches
  except:
    maxBatches = 0
    return maxBatches



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 },
  ingredients = { 'milk': 1288, 'flour': 9, 'sugar': 95 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))