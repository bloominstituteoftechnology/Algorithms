#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    need = []
    have = []
    for i in recipe.keys():
        need.append(i)
    for i in ingredients.keys():
        have.append(i)
    for i in need:
        if i not in have:
            return 0
    ratios = []
    for i in recipe:
        ratio = ingredients[i] // recipe[i]
        if ratio < 1:
            return 0
        ratios.append(ratio)
    return min(ratios)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))