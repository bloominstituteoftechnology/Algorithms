#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  min_ingridients = None
  for i, amount_required in recipe.items():
    #assign 0 for ingridients that are not there
    amount_we_have = ingredients.get(i, 0)
    amount_can_have = amount_we_have // amount_required
    if min_ingridients != None:
      min_ingridients = min(min_ingridients, amount_can_have)
    else:
      min_ingridients = amount_can_have
  return min_ingridients        
  

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))