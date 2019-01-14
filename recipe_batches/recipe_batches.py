#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  if len(ingredients) < len(recipe):
    # If our ingredients has less than the recipe, then we definitely don't have enough
    return 0

  batches = {}

  for key, ingredient in ingredients.items():
    if recipe[key]: # If the recipe has the current ingredient
      if ingredients[key] >= recipe[key]:
        # We have enough of a ingredient for the recipe
        batches[key] = int(ingredients[key] / recipe[key])
      else:
        # We don't have enough ingredients
        return 0
  return batches[min(batches, key=batches.get)]


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))