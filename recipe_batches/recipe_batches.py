#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batch_size = None
  for recipe_ing, recipe_cnt in recipe.items():
    if recipe_ing in ingredients:
      ingredient_cnt = ingredients[recipe_ing]
      maximum = int(ingredient_cnt / recipe_cnt)
      if batch_size == None or maximum < batch_size:
        batch_size = maximum
    else: 
      return 0

  return batch_size or 0 
    


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))