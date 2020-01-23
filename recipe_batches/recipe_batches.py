#!/usr/bin/python

from math import inf, floor

def recipe_batches(recipe, ingredients):
  max_batches = inf

  for ingredient, amount in recipe.items():
    if ingredient not in ingredients:
      return 0

    batches = floor(ingredients[ingredient] / amount)
    if batches < max_batches:
       max_batches = batches

  return max_batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 420, 'butter': 150, 'flour': 50 }
  ingredients = { 'milk': 1132, 'butter': 348, 'flour': 751 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))