#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

  flag = False # flag to help set baseline batch count
  batches = 0 # lowest common denom for ingredient batches

  for key in recipe.items():

    # if recipe ingredient exists
    if key in ingredients.keys():
      # batches per ingredient amt floored
      cur_batch = ingredients[key] // recipe[key]

      # flag for if baseline batch hasn't been set
      if flag == False:
        flag = True
        batches = cur_batch # 1st iteration will set the baseline

      # if batch is less than min and flag has been set,
      elif cur_batch < batches and flag:
        batches = cur_batch # set new min

    # if recipe ingredient is not present, no batches can be made
    else:
      return 0

  return batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
