#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # 1. If we don't have an ingredient that is called for by the recipe, just return 0
  # 2. If any ingredient doesn't meet the amount called for by the recipe, return 0
  # 3. Figure out the minimum ratio (round this down to an integer) of each ingredient amount / recipe amount
  min_ratio = math.inf
  # loop through our recipe dictionary, we care about both the ingredient name as well as the necessary amount
  for ingredient, amount in recipe.items():
    # check to see if the current ingredient exists in our ingredients dict
    if ingredient not in ingredients:
      return 0
    # the ingredient exists in our ingredients list; figure out the ratio 
    # divide the amount we have available in the ingredients list by the amount called for by the recipe
    ratio = ingredients[ingredient] // amount
    # if we ever get a ratio of 0, just return 0
    if ratio == 0:
      return 0
    # see if we need to update our min_ratio variable
    if ratio < min_ratio:
      min_ratio = ratio

  return min_ratio


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))