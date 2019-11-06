#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  """
  Determine the # of whole batches can be made with given ingredients.
  """
  # edge case where there is a key in receipe that is not in ingredients
  for key in recipe.keys():
    if key not in list(ingredients.keys()):
      return 0

  # number of full batches to return
  batches = 0
  # Conditional to start while loop
  run = True
  # print(f'starting batches {recipe}, {ingredients}')
  # counter = 1

  while run == True:

    # iterate through recipe items and sub values from ingredients
    for key, value in recipe.items():
      ingredients[key] -= value
    
    # iterate through ingredients, if we have negative values then this wasn't
    # a successful run and we return the batches from previous runs
    for key, value in ingredients.items():
      if value < 0:
        return batches
      else:
        pass
    
    # successful run to reach this point so we increment batches
    batches += 1
    # print(f'{counter} loop: {recipe}, {ingredients}, batches {batches}')
    # counter += 1

  return batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))