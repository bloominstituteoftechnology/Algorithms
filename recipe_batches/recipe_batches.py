#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients, count=0):
  # we need to globally track how many batches we've made, and pass recursively
  # TODO: find how to do this w/o global variables
  global batches
  batches = count
  can_cook = []

  # if we do not have any necessary ingredient, return 0
  if len(recipe) > len(ingredients):
    return 0

  # we need to see if we are able to make a batch
  for item in ingredients:
    if ingredients[item] >= recipe[item]:
      can_cook.append(True)
    else:
      can_cook.append(False)

  # if we have all necessary ingredients, add a batch to count and subtract from ingredients
  if all(can_cook):
    batches += 1
    remainder = {key: ingredients[key] - recipe.get(key, 0) for key in ingredients.keys()}
    # recursion call with the remaining ingredients
    recipe_batches(recipe, remainder, batches)
    
  return batches


  ### NOTES
  # this subtracts the recipe from the ingredients and gives the remainder
  # remainder = {key: ingredients[key] - recipe.get(key, 0) for key in ingredients.keys()}


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))