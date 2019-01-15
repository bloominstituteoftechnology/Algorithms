#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  ''' 
    make list of times
    loop over recipe
    loop over ingredients
    find number of times ingredient[i] can be subtracted by recipe[i]
    return lowest number in list

  '''
  times = []

  for key, value in recipe.items():
    for key2, value2 in ingredients.items():
      if key == key2:
        times.append(int(value2/value))
      elif key not in ingredients or key2 not in recipe:
        times.append(0)
  times.sort()
  return times[0]
    



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))