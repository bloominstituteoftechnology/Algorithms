#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    batch_qty = []
    try:
        for ing_r in recipe:
            batches = ingredients[ing_r]//recipe[ing_r]
            batch_qty.append(batches)
    except KeyError as ke:
        return 0

    return min(batch_qty)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))