#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = -1
  no_more_ingredients = False

  while no_more_ingredients == False:
    batches +=1

    for item in recipe:
      if item in ingredients.keys():
        if recipe[item] <= ingredients[item]:
          ingredients[item] -= recipe[item]
        else:
          no_more_ingredients = True
          break
      else:
          no_more_ingredients = True
          break
    # break

  return batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))