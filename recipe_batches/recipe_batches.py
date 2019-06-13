#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  #base case: if the ingredients are not present in the recipe or the ingredient amount is not enough return 0
  batches = []
  for val in recipe:
    if val not in ingredients or recipe[val] > ingredients[val]:
      return 0
    #else find how many batches one can make per ingredient, add it to the list and return the smallest amount found in the list
    else:
      batches.append(math.floor(ingredients[val]/recipe[val]))
  return min(batches) 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }
  ingredients = { 'milk': 1288, 'flour': 9, 'sugar': 45 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))