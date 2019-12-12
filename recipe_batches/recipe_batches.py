#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  maxBatches = 0

  return maxBatches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))





#   LAMBDA PROBLEM SOLVING FRAMEWORK

# UPER

# UNDERSTAND
#     GOAL - RETURN HOW MANY BATCHES OF RECIPE CAN BE MADE FROM INPUT OF 2 DICTIONARIES
#     {1ST RECIPES}, 2ND {CURRENT INGREDIENTS}
#       BASED ON TEST RESULTS NO NEED TO ACCOUNT FOR BAD INPUT
#
#     EX:
# INPUT
#         recipe_batches(
#   { 'milk': 100, 'butter': 50, 'flour': 5 },
#   { 'milk': 138, 'butter': 48, 'flour': 51 }
# )
# OUTPUT -- 0 -- NOT ENOUGH INGREDIENTS

#     EX:
# INPUT
#       recipe_batches(
#   { 'milk': 2, 'sugar': 40, 'butter': 20 },
#   { 'milk': 5, 'sugar': 120, 'butter': 500 }
# )
# OUTPUT -- 2 -- NOT ENOUGH INGREDIENTS


# PLAN
# INPUT(DICTIONARY1, DICTIONARY2) RETURN => MAX BATCHES(TYPE=INT)
# def recipe_batches(recipe, ingredients):
#   maxBatches = 0
#
#
#
#   return maxBatches

# EXECUTE

# REFLECT
