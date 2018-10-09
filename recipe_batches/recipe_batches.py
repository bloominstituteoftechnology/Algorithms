#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  recipeValue = recipe.values()
  ingredientValue = ingredients.values()

  if recipe.keys() == ingredients.keys():
    for value1 in ingredientValue:
      for value2 in recipeValue:

        return math.floor((value1 / value2))
    # return ingredients.values() / recipe.values() 
  else:
    return 0 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))