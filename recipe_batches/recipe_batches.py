#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  make = []
  for i in list(recipe.keys()):
        if i in ingredients and recipe[i] < ingredients[i]:
            make.append(math.floor(ingredients[i] / recipe[i]))
        elif i not in ingredients:
            return 0
  return min(make) 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))