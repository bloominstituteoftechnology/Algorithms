#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients): 
  for key in recipe: # milk flour sugar butter
    if key in ingredients:
      ingredientValue[count] // recipeValue[count]
      # do your logic thang
    else:
      # the key doesn't exist in ingredients
      # therefore, return 0
  
  # `milk` `flour` `butter`
  # if recipeKeys == ingredientKeys :
  #   while True:
  #     print(recipeKeys, ingredientKeys)
  #     count+=1
  #     print (ingredientValue[count] // recipeValue[count])
  #     if ingredientValue[count] // recipeValue[count] <= 0:
  #       print("Not Enough")
  #       return 0
  #     elif count >= len(ingredientValue):
  #       print("exited")
  #       return ingredientValue[count] // recipeValue[count]
  # else:
  #   return 0 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))