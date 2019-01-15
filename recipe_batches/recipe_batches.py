#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  max_batches = 1000000
  for item in recipe.keys():
    if item not in ingredients.keys():
      return 0
    current_batches = ingredients[item] // recipe[item]
    if current_batches < max_batches:
      max_batches = current_batches

  return max_batches 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))