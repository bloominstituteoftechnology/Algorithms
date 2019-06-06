#!/usr/bin/python

import math
"""
Took me another 2 hours
"""

def recipe_batches(recipe, ingredients):
  batches = [] #create an empty list
  loop = 1e1000 # create a big min number which can be replaced
  for k,v in recipe.items(): #for key value pair in dict
#     print(k,v)
#     total_ingredient_amt = ingredients[k] #[k] is an index which ouputs value for each key
      if k in ingredients: # like i in a list
        batch_per_ingredient = ingredients[k]//recipe[k] #create a list of floor division for whole batches
        batches.append(batch_per_ingredient) #append it to the empty list
      else:
        batches.append(0) #if the lists have discrepency then append 0
  # we find the minimum from the list we created
  # this comes from the first problem   
  for i in range(0, len(batches)):
    if batches[i] < loop:
      loop = batches[i]
  return loop
  


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))