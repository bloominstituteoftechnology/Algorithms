#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    min_batches = float('inf') # sets to infinity so that any number that comes up is less than it. 
    something_missing = False 
    for item in recipe:
        if something_missing:# edge case as soon as its discovered something is missing no need to check other values. 
            break
        try:# if the item is missing it will throw an error
            if recipe[item] <= ingredients[item]:
                if int(ingredients[item] / recipe[item]) < min_batches:
                    min_batches = int(ingredients[item] / recipe[item])
                    # the item with the least amount is the number we can do. 
        except:
            something_missing = True 
        
    if something_missing:
        return 0
    else:
        return min_batches 
# The time complexity of this solution is O(n) space complexity is O(1)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))