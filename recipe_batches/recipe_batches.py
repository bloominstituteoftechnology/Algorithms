#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # print(len(recipe))
  # print(len(ingredients))
  # print(recipe)
  low = 0
  if len(recipe) > len(ingredients):
    # print("inside", len(recipe))
    # print("inside", len(ingredients))
    low = 0
  else:
    for i in recipe:
      # print("i", i)
      # print("recipei", recipe[i])
      for n in ingredients:
        # print("n", n)
        # print("ingredientsn", ingredients[n])
        possible = math.floor(ingredients[n]/recipe[n])
        if low == 0:
          # print("low is none", low)
          low = possible
          # print("now it's possible", low)
        elif possible < low:
          low = possible
  return low

    

# done = recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 })
# print(done)
if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }
  ingredients = { 'milk': 1288, 'flour': 9, 'sugar': 95 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))



  # if keys match, divide the value for indredients by the value for recipe
  # round down the result for the number of recipes you can make with that amount of indredient
  # if choose the lowest number
  # return