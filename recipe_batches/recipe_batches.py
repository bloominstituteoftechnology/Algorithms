#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    batches = []
    for ingredient in recipe:
        if ingredient not in ingredients:
            batches.append(0)
        elif recipe[ingredient] > ingredients[ingredient]:
            batches.append(0)
        else:
            batches.append(math.floor(ingredients[ingredient]/recipe[ingredient]))
    batchesFinal = min(batches)
    return batchesFinal or 0

#check if ingredients match needed ingredients for the recipe.
#if they do remove the amount needed for the 

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))