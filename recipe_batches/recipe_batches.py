#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  keys = list(recipe.keys())
  tuples = [(recipe[key], ingredients.get(key, 0)) for key in keys]
  batches = sorted([i[1] // i[0] for i in tuples])
  return batches[0]



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

# initial thoughts
# for each ingredient create a tuple.
  #   need    have
  #   (5,      15)
  
  # overall would look like [(5,15),(2,10),(10, 10)]
  # integer divide // from this into new list [3,2,1]
  # sort list [1,2,3]
  # return 0 index

##############
# SOLUTION 1 #
##############

# recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
# ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }

# def solution_1(recipe, ingredients):
#   keys = list(recipe.keys())
#   tuples = [(recipe[key], ingredients.get(key, 0)) for key in keys]
#   division = sorted([i[1] // i[0] for i in tuples])
#   return division[0]

# print(solution_1(recipe, ingredients)) # 0 !YAAY

# after a little research this method definately worked.

# did refactor a little
# division = [i[1] // i[0] for i in tuples]
# division.sort()
# Became
# division = sorted([i[1] // i[0] for i in tuples])

# Currently failing tests. Going to paste them here so I can inspect a little

# print(recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 })) # 0
# 22 steps
# print(recipe_batches({ 'milk': 100, 'butter': 50, 'cheese': 10 }, { 'milk': 198, 'butter': 52, 'cheese': 10 })) # 1
# 20 steps
# print(recipe_batches({ 'milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 5, 'sugar': 120, 'butter': 500 })) # 2
# 20 steps
# print(recipe_batches({ 'milk': 2 }, { 'milk': 200})) # 100
# 16 steps

# I see it, was forgetting to return just the first index of batches
# return batches
# changed to
# return batches[0]

# and tests pass!!!

# Interesting note, the number of on hand ingredients
# or the number of keys in the second dictionary do not
# add any more steps

# Grabbing data from the longest test case and reducing
# necessary ingredients to see if I can spot the trend

# Recipe Ingredients    Steps
# 1                     16
# 2                     18
# 3                     20
# 4                     22
# 5                     24

# Think we are looking at O(n)