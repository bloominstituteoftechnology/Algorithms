#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # Check to make sure the names of the ingredients 
  # are in both dictionaries
  if (set(recipe) == set(ingredients)):
    batches = [] # Create an empty list to fill later
    for i in recipe:
      # Loop through teh ingredients in recipe
      if (ingredients[i] >= recipe[i]): # If there's enough of that ingredient
        num = ingredients[i]//recipe[i] # See how many batches we could make with that one ingredient
        batches.append(num) # Add to empty list
      else:
        return 0
    return min(batches) # Return the min value in list of batches
  else:
    return 0


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))