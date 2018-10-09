#!/usr/bin/python

import math

#How many times does the each available value divide into recipe value for all key:values. 
def recipe_batches(recipe, ingredients):#this function is O(n^2) and memory is O(n), because var r grows with input growth. 
  r = []
  for k, v in ingredients.items(): 
    for j, t in recipe.items():
      if j not in ingredients:
        return 0
      else:  
        r.append(v/recipe[k])

  return int(min(r))


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))