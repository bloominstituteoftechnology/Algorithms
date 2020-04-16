#!/usr/bin/python

## whats the question asking: how many batches of a recipe can we make from th input of 2 dictionaries dic1(recipes), dic2(ingreidents)
## with this in mind we need to input both dictionaries and return the maxium batches possible may be //
## https://www.w3schools.com/python/python_sets.asp
##https://www.w3schools.com/python/ref_func_min.asp

import math

def recipe_batches(recipe, ingredients):
    if set(recipe) == set(ingredients): ## check to see if we have the correct ammount of ingredients to make a single or multiple bacthes
      batches =[]
      for i in recipe:  ## check how many if any ammount of batches can be made from what we have avaible 
          if ingredients[i] >= recipe[i]:
            consumed = ingredients[i] // recipe[i]
            batches.append(consumed)
      return min(batches) ## this will show us what is the minium ammount of batches we can make 
      ## we need to make a case senario for when there is not enough to make any batches using else and have the return be zero
    else:
      return 0 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))