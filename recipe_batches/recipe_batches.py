#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  firstkey = (list(recipe.keys())[0])
  batches = ingredients[firstkey]/recipe[firstkey]

  for key in recipe:
    if ingredients[key]/recipe[key] < batches:
      batches = ingredients[key]/recipe[key]
    
 
  return int(batches)
  
  


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 40, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))