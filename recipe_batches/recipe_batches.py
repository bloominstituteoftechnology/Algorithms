#!/usr/bin/python

import math

"""
Thoughts on solving this problem:

- Seems like a minimum of two loops will be required: one to check for ingredients available, one to check for ingredients required. Maybe a one-loop way later, not concerned about this for now.
- At its base level, this should be a straightforward problem -- simply check numbers against one another to see if enough ingredients are available to complete given recipe(s).


"""
def recipe_batches(recipe, ingredients):
  pass 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))