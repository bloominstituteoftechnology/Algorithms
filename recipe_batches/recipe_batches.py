#!/usr/bin/python


# check if all keys from recipe are present in ingredients
# if so, check value of each key from recipe and see if it's greater than that value from the ingredients
# 

import math

def recipe_batches(recipe, ingredients):
  a = list(recipe.keys())
  b = list(ingredients.keys())
  i = list(recipe.values())
  r = list(ingredients.values())
  if a == b:
    divided = [int(r) / int(i) for i,r in zip(i, r)]
    # print(divided)
    #checks that there's at least enough for one batch
    if all(i >= 1 for i in divided) == True:
      # print('true')
      print(int(min(divided)))
    else:
      print(0)
  else:
    print(0)
  pass 

recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 })
               
# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
