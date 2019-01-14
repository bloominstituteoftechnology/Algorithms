#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  """
  --  Fuction will receive receipe need as well as ingredients available
  --  Function should output the maximum number of whole batches that can be made for the supplied recipe 
      using the ingredients available
      Approach  : -
      1. Find keys inreceipe and ingredients dict
      2. Check for the equality.. i.e. all ingredients available for receipe
              - if yes then go ahead
              - else can't make that receipe. Not all ingredients available
      3. If all ingredients are available for receipe
              - access value using key and check ingredient amount is greater than receipe needed
                  --  if yes count multiple and return receipe batch
                  --  Insufficient ingredients available

  """
  batches = []
  if recipe.keys() == ingredients.keys():
    for key in recipe:
        #print(key)
        #print(ingredients[key])
        #print(recipe[key])
        enough_ingredient = int(ingredients[key] / recipe[key])
        #print("for key {} :  {}".format(key , enough_ingredient))
        batches.append(enough_ingredient)
            
        if 0 in batches:
            return 0 
        else:
            return min(batches)
            
  else:
      return 0 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))