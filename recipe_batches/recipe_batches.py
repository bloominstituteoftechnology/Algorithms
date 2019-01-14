#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  count = 0
  flag = True

  if len(recipe) > len(ingredients):
    return 0
  ingredients_copy = ingredients.copy()
  while flag == True:
    for i, key in enumerate(recipe.items()):
      if key[1] <= ingredients_copy[key[0]]:
        ingredients_copy.update({key[0]: ingredients_copy[key[0]] - key[1]})
      else:
        flag = False
    count += 1
  if count == 1:
    return count
  else:
    return count - 1

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))