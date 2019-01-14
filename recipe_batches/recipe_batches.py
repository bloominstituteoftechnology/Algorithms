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
  recipe_avail = 0
  for k, v in recipe.items():
    if k in ingredients.keys():
      if v > ingredients[k]:
        return 0
      else:
        ingredients[k] = ingredients[k] - v
        recipe_avail += 1
  return recipe_avail
  


recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
ingredients = { 'milk': 132, 'butter': 55, 'flour': 51 }
print(recipe_batches(recipe, ingredients))


# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))