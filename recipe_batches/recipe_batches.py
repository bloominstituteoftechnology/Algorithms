#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches=None
  ingredient_keys=ingredients.keys()
  for ingredient in ingredient_keys:
    enough_ingredient=ingredients[ingredient]/recipe[ingredient]
    if batches==None:
      batches=enough_ingredient
    elif enough_ingredient<batches:
      batches=enough_ingredient
  return int(batches)



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 50, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))