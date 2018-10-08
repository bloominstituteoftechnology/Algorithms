#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    min_batches = None
    for i in recipe:
        if i in ingredients:
            batches = math.floor(ingredients[i] / recipe[i])
        else:
            batches = 0
        min_batches =  batches if min_batches is None or batches < min_batches else min_batches
    return min_batches



if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
