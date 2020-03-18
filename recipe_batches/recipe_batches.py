#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # start
  new_ingredients_for_item = [0]*len(recipe)
  counter = 0 
  #base
  for i in recipe:
    if i in ingredients:
      new_ingredients_for_item[counter] = int(ingredients[i]/recipe[i])
      counter += 1
  return min(new_ingredients_for_item)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))