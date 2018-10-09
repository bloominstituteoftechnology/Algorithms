#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = []
  for ingredient in recipe:
    # print(ingredient) # `milk` `butter` `flour` `sugar`
    if ingredient not in ingredients:
      return 0
    else:
      # divide # of ingredient from ingredients by # of ingredient from recipe
      whole = math.floor(ingredients[ingredient] / recipe[ingredient])
      if whole >= 1:
        batches.append(whole)
      else:
        return 0
  print('batches:', batches)
  return min(batches)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))