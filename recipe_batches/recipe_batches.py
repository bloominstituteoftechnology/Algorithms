#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    cake_batches = 0
    for key, value in recipe.items():
        if key not in ingredients or ingredients[key] < value:
            cake_batches = 0
            break
        something = ingredients[key] // value
        if cake_batches > 0 and something > cake_batches:
            continue
        cake_batches = something
    return cake_batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
