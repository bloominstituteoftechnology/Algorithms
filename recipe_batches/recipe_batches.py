#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  cache = []
  #check that both dictionaries have the same keys
  if set(recipe.keys()) == set(ingredients.keys()):
    #for each entry, check ingredients.item >= recipe.item
    #total ingredients divided by amount for recipe; add to cache
    for item_re, amount_re in recipe.items():
      total_ing = ingredients.get(item_re)
      if total_ing >= amount_re:
        cache.append(math.floor(total_ing / amount_re))
      else:
        return 0
    #check for the smallest amount, return that
    return min(cache)
  else:
    return 0


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 2 }
  ingredients = { 'milk': 200}
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

