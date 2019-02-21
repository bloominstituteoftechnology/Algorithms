#!/usr/bin/python

import math

# how many batches of a particular recipe can we make 
  # ingredients // recipe  for each value
  # min of all of the values would be how many batches there are
#recipe key values list > than ingredients return 0
#recipe and ingredients have the same keys
#ingredients.get(key, 0) would just give me a 0 if key missing
def recipe_batches(recipe, ingredients):
  batches = []
  for item in recipe: #item in list of values in recipe
    if item not in ingredients:
      batches.append(0) # appending 0 for value of items not there
    elif recipe[item] > ingredients[item]:
      batches.append(0) 
    else:
      batches.append(ingredients[item]//recipe[item]) 
  return min(batches)
  

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))