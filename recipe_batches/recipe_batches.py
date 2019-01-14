#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  ''' 
    make list of times
    loop over recipe
    loop over ingredients
    find number of times ingredient[i] can be subtracted by recipe[i]
    return lowest number in list

  '''
  pass 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))