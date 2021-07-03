#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # set a new list of ingredients
  ingred = []

  # loop through the recipe list with the key
  for key in recipe:

      # if the ingredients key is not none, append the ingredient
      # key // recipe key, else, append a 0
      if ingredients.get(key) is not None:
          ingred.append(ingredients[key]//recipe[key])
      else:
          ingred.append(0)

  # return the min amount of ingredients
  return min(ingred)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))