#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    max = 500000
    for i in recipe:
        try:
            max = min(max, ingredients[i] // recipe[i])
        except:
            return 0
    return max


if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
