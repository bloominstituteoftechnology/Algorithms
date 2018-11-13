#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batch_counter = 0
  for i in recipe:
    print(recipe[i])
    for j in ingredients:      
      if ingredients[j] < recipe[i]:
        return 0
      else:
        batch_counter += 1
        ingredients[j] - recipe[i]
  print(batch_counter)
  
      


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))