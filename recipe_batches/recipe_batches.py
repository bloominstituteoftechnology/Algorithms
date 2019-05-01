#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  #Loop over both dictionaries
  #Compare each Key Value 
  #If Recipe > Ingredients break the search and return 0
  #Else calculate how many of each you can make.
  smallest = 1000000000000000
    recipe = list(recipe.values())
    ingredients = list(ingredients.values())
    for i in range(0, len(recipe)):
      if(recipe[i] > ingredients[i]):
        return 0
      else:
        total = ingredients[i]//recipe[i]
        if total < smallest:
          smallest = total
    return smallest



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))