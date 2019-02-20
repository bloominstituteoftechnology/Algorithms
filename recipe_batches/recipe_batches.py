#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  """
  --  Fuction will receive receipe need as well as ingredients available
  --  Function should output the maximum number of whole batches that can be made for the supplied recipe 
      using the ingredients available
      Approach  : -
      1. Find keys in receipe and in gredients dict
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
    #as checking keys.. can use dict[key] instead of dict.get(key)
    #The get() method returns a default value if the key is missing.
    #if the key is not found dict[key], KeyError exception is raised
    for key in recipe:
        batches.append(ingredients[key] // recipe[key])
        return min(batches)
      
  else:
      return 0 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))