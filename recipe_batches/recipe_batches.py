#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  cache = []
  if set(recipe.keys()) == set(ingredients.keys()):
    for item_re, amount_re in recipe.items():
      total_ing = ingredients.get(item_re)
      if total_ing >= amount_re:
        cache.append(math.floor(total_ing / amount_re))
      else:
        return 0
    return min(cache)
  else:
    return 0


if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 30, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 156, 'butter': 78, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))