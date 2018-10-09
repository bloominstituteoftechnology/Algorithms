#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  total = math.inf
  
  if(len(recipe) != len(ingredients)):
    return 0
  else: 
    for r_key, r_value in recipe.items():
      for i_key, i_value in ingredients.items():
        if i_key == r_key:
          dishes = i_value // r_value
          print(dishes, "dishes")
          if dishes <= 0: 
            total = 0
          elif dishes < total: 
            print(total, "total")
            total = dishes
      
  return total      
     
  pass 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))