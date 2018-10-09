#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    batches = []
    for ingredient in recipe:
        if ingredient in ingredients:
            batches.append(ingredients.value()/ingredient.value())
    

#check if ingredients match needed ingredients for the recipe.
#if they do remove the amount needed for the 

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))