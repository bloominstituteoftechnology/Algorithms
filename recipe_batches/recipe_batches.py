#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  numBatches = 0
  # Check if the ingredients contains all the recipe items
  while True:
    for ingredient in recipe:
      if ingredients.get(ingredient) == None:
        # We don't have all the ingredients available in the list so exit.
        return numBatches
      else:
        ingredients[ingredient] = ingredients.get(ingredient) - recipe.get(ingredient)
        if ingredients[ingredient] < 0:
          return numBatches
    numBatches += 1
    

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))