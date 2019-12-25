#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batch_counter = 0
  '''
    Base:
      - Create counter_tracker
    1. Keep track of recipe iterations
    2. Keep track of ingredient iterations
    3. Compare the two
      3a. Default to 0 if ingredient iteration is not greater than recipe
      3b. If ingredient[i] > recipe[i]
        + increment counter_tracker
        + ingredients[i] - recipe[i]
        + Loop back and test again
  '''
  
      


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))