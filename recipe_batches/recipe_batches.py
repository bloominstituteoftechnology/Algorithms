#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    recipe_dictionary = recipe
    ingredient_dictionary = ingredients

    total_batches = None

    for key in recipe_dictionary.keys():
        #Check if this key exist in ingredient_dictionary
        # if not, then batches -> 0 and return from here
        if key not in ingredient_dictionary:
            return 0
        batches = ingredient_dictionary[key]//recipe_dictionary[key]
        if batches ==0:
            return 0

        # print(total_batches, batches)
        if not total_batches:
            total_batches = batches
        else:
            total_batches = min(total_batches, batches)

    # print (total_batches)
    return total_batches

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 332, 'butter': 108, 'flour': 51 }
  recipe_batches(recipe, ingredients)
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))