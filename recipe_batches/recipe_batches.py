#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    ingredients_value_array = []
    recipe_value_array = []
    for key, value in recipe.items():
        recipe_value_array.append(value)
    for key, value in ingredients.items():
        ingredients_value_array.append(value)
    if len(recipe_value_array) != len(ingredients_value_array):
        return 0
    sum = 0
    batches = 0
    while sum >= 0:
        for i in range(0, len(recipe_value_array)):
            sum = ingredients_value_array[i] - recipe_value_array[i]
            ingredients_value_array[i] = sum
            print(ingredients_value_array[i])
            if sum < 0:
                return(batches)
            elif sum == 0:
                batches += 1
                return(batches)
        batches += 1
    return batches
if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))


"""
    
    Understand
    ___________
    
    Do the recipe and inventory dictionaries all of the same types of ingredients listed?
        No, sometimes the recipe dictionary has certain keys that the ingredient dictionary does not.
        
    Do the dictionaries ever have the same keys but in a different order?
        No, if the dictionaries have the same keys they will always be in the same order.
        Also, if one dictionary has an extra key, it will be placed at the end.
        
    Plan
    ___________
    
    create 4 arrays to store the keys and values of both dictionaries so that I am sure they are ordered. Compare the values of the
    
"""
