#!/usr/bin/python

# 1. Understand the question
# keys = ingredient names
# values = ingredient amounts
# recipe-dictionary = represent amounts of each ingredient needed for 1 batch
# ingredients-dictionary = represent amounts of each ingredient available
# batch = recipe//ingredients
# Output the total number of WHOLE batches that can be made
# Function should return 0 if there is not enough of the items to make a batch

# 2. Create Plan
# set total_batches to a big number
# compare recipe to ingredients
# find how many batches can be made
# return total_batches

# 3. Implement Plan
# create variables?

# 4. Revise
# Alternatives?
import math

def recipe_batches(recipe, ingredients):
  total_batches = math.inf 

  for ingredient, amount in recipe.items():
    if ingredient not in ingredients:
      return 0
    
    batch = (ingredients[ingredient] // amount)
    if batch < total_batches:
      total_batches = batch

  return total_batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))