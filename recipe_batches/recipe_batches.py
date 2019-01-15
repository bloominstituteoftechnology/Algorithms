#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  
  """
  recipe {"name" : amountOfIngredientsNeeded}
  ingredients {"name" : amountOfIngredientsAvailable}
   
  Check to see if the recipe contains the ingredients, if not, return 0 (ingredients.count < recipe.ccount)
  Check to see if amountOfIngredientsAvailable > amountOfIngredientsNeeded, if yes, return the max number of batches; if not, return 0
  """
  
#  numberOfRecipes = 0
#  
#  while True:
#    for ingredient, amountNeeded in recipe.items():
#      amountAvailable = ingredients[ingredient]
#      if amountAvailable < amountNeeded:
#        return numberOfRecipes
#      ingredients[ingredient] = amountAvailable - amountNeeded
#    numberOfRecipes += 1
    
    # three loops: while, for-in, ingredients[]
    
    
  minAmount = None
  
  for ingredient, amountNeeded in recipe.items():
    # default value is 0 for ingredient that doesn't exist
    amountAvailable = ingredients.get(ingredient, 0)
    amountPossible = amountAvailable // amountNeeded # gives back smallest whole number
    
    if minAmount != None:
      minAmount = min(minAmount, amountPossible)
    else:
      minAmount = amountPossible
      
  return minAmount
  
  # three loops: for-in, ingredients[]
    
if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))