#!/usr/bin/python

import math

'''
UNDERSTANDING:

-Takes in 2 dictionaries = 1 dictionary is amount of ingredients needed, 1 is amount of ingredients available
- returns the amount of batch you can make

'''

def recipe_batches(dict1, dict2):
    arr = []
    if len(dict1) != len(dict2):
        return 0
      
    for i in dict1:
        for j in dict2:
            # arr.append(dict2[j] % dict1[i])
            if (i == j):
                arr.append(dict2[j] / dict1[i])
    
    max_batch = int(min(arr))       
    # for j in dict2:
    #     print(dict2[j])
    
    return max_batch


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))