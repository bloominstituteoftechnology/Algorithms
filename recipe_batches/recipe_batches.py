#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # divide ingredients number by recipe number for each key
  limitingFactor = 99999
  for recipeIngredient, availableIngredient in zip(recipe.values(), ingredients.values()):
    batchSize = availableIngredient / recipeIngredient
    # if the quotient is less than the limitingFactor number, set limitingFactor to that new number
    if batchSize < limitingFactor:
      limitingFactor = batchSize
  # if limitingFactor is less than 1, set it to 0
  #return limiting factor without decimals
  if limitingFactor < 1:
    limitingFactor = 0
  print(limitingFactor)
 
recipe_batches(
  { 'milk': 100, 'butter': 50, 'flour': 5 },
  { 'milk': 138, 'butter': 48, 'flour': 51 }
)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))