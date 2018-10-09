#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  current_item = ""
  sequence = []
  batches = 0
  # for each item in recipe[0,1,2]
  for item in ingredients:
  # find it in ingredient, if equal to or higher, subtract from itself
    if item in recipe and values(recipe[item]) >= values(ingredients[item]):
      sequence.append(values(recipe[item]) - values(ingredients[item])

      return sequence
    else:
      break
  # otherwise break
  # if all of keys in recipe are true

  if lens(batch) == lens(recipe)
  batches + 1
  # add 1 to batch


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))