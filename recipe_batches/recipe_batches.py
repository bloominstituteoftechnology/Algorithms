#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    # keep lowest number as max number of batches
    max_batches = 0
    ctr = 0 # to keep track ingredient count
    for each in recipe:
        # substracting each price to each one ahead
        # and keeping only if greater than "max_profit"
        try:
            # find number of batches available for each ingredient
            # mod division of available by required ingredients
            batches = ingredients.get(each) // recipe.get(each)
        # if ingredient not available, return 0 
        except:
            batches = 0
        # make "max_batches" = to "batches" on first iteration
        # or when number of "batches" is smaller than "max_batches"
        if ctr==0 or batches <= max_batches:
            max_batches = batches
        ctr += 1
    return max_batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))