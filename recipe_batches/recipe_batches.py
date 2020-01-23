#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batch_count = 0
  #if all values in ingredients are equal to or greater than corresponding recipe dict, increment batch count
  make = True
  if len(recipe) == len(ingredients):
    while make == True:
      for x in recipe:
        if recipe[x] <= ingredients[x]:
          ingredients[x] -= recipe[x]
        else:
          make = False
      if make == True:
        batch_count += 1

  return batch_count




if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))