#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  """
  i need to look at my recipes and make sure I have enough to make something from my recipe book based on the ingredients i have available

  iterate through ingredient list looking for ingedient
  when i find an ingredient i need to check the amount that i have available vs what i need
  if i have enough of the ingredient continue to check the list
  if i dont have enough finish seaching and return false 
  """
  min_avail = []
  for k, v in recipe.items():
    if k in ingredients.keys():
      recipe[k] = math.floor(ingredients[k] / v)
      min_avail.append(recipe[k])
    else:
      return 0
  return sorted(min_avail)[0]


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))