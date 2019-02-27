#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  if len(recipe) != len(ingredients):
    return 0
  for itemRecipe, ammtRecipe in recipe.items():
    for itemIng, ammtIngr in ingredients.items():
      if itemRecipe == itemIng:
        if ammtIngr / ammtRecipe < 1:
          return 0
        else:
          return math.floor(ammtIngr / ammtRecipe)
       



print(recipe_batches(
  { 'milk': 100, 'butter': 50, 'flour': 10, 'cookies': 100 },
  { 'milk': 198, 'butter': 52, 'flour': 10 }
))

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))