#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batch = 0
  cooking = True

  while cooking:
    for key, value in recipe.items():
      if key in ingredients:
        if ingredients[key] < recipe[key]:
            print('dont have enough ', key)
            cooking = False
        ingredients[key] = ingredients[key] - recipe[key]
          
      else:
        return 0

    if cooking:
      batch = batch + 1
  return batch
  # batch = 0
  # for i in recipe:
  #   print(f'{i}: {recipe[i]}')
  #   if i in ingredients and ingredients[i] > recipe[i]:
  #     ingredients[i] = ingredients[i] - recipe[i]
  #   else:
  #     return 0
  # print('batch made!') 
  # batch = batch + 1
  # return batch



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs

  #{ 'milk': 100, 'butter': 50, 'cheese': 10 }, { 'milk': 198, 'butter': 52, 'cheese': 10 }
  
  # recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  # ingredients = { 'milk': 132, 'butter': 52, 'flour': 51 }

  recipe = { 'milk': 100, 'butter': 50, 'cheese': 10 }
  ingredients = { 'milk': 198, 'butter': 52, 'cheese': 10 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))