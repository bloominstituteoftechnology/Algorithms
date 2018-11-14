#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # Create a temp list to hold number of batches that can be generated per recipe key
  num_batch_list = []
  # Iterate through the recipe list, calculate # of batches that can be generated per recipe key, then push the # value into num_batch_list 
  for key, value in recipe.items():
    # if a certain recipe key is not a key in ingredients, return 0 (i.e. 0 batch)
    if not key in ingredients:
      return 0
    num_batch = ingredients[key] / value
    num_batch_list.append(math.floor(num_batch) if num_batch >= 0 else 0)
  # Return the least number of batches in num_batch_list
  return int(min(num_batch_list))


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))