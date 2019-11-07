#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  max_batch = 0
  counter = 0
  for i in recipe:
    try:
      # floor division for values
      # both versions ".get(i)" and "[i]" work
      # batches = ingredients.get(i) // recipe.get(i)
      batches = ingredients[i] // recipe[i]
    except:
      # if dictionary keys don't align
      batches = 0
    if counter == 0 or batches <= max_batch:
      max_batch = batches
    counter += 1
  return max_batch


  # batches = 0
  # for key in recipe.keys():
  #   if key not in ingredients.keys():
  #     return 0
  #   else:
  #     batches = ingredients[key] // recipe[key]
  # return batches


  # common = recipe.keys() & ingredients.keys()
  # return min({k: ingredients[k] / recipe[k] for k in ingredients.keys() & recipe})
  # if set(recipe) == set(ingredients) is False:
  #   return "Sorry, the ingredients and recipe do not match"
  # # else:
  # return min({key: ingredients[key] // recipe[key] for key in ingredients})

  # batches = 0
  # canMake = True
  # while canMake:
  #   for key in recipe:
  #     for key in ingredients:
  #       if recipe[key] < ingredients[key]:
  #         ingredients[key] = ingredients[key] - recipe[key]
  #       else:
  #         canMake = False
  #     else:
  #       canMake = False
  #   if canMake:
  #     batches += 1
  # return batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))