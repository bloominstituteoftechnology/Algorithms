#!/usr/bin/python

import math
# synopsis :
# Your function should output the maximum number of whole batches that can be made for the supplied recipe using the ingredients available to you, 
# as indicated by the second dictionary.

def recipe_batches(recipe, ingredients):
  # had a read over this for general dictionary stuff : http://www.pythonlearn.com/html-009/book010.html
  # also to address a minimalistic approach 
  # this one feels like it should be fairly straight forward. looking up a few builtins
  
  # initial thoughts were to use a min on the ingredients against an element vs 0 and use a single for loop to make sure i am only looping on a low factor
  # but it seems that using a division i may need to fix up the return maybe floor or int()
  return min(ingredients.get(elem, 0) / num for elem, num in recipe.items()) # FIXME: possibly cast to int?


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))