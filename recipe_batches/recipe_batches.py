#!/usr/bin/python

import math
#MAKE SURE EACH VALUE IN THE RECIPE IS GREATER THAN OR EQUAL TO ON HAND THEN DEVIDE THE NUMBER OF INGREDIENTS BY THE NUMBER IN RECIPIE LOWSEST NUMBER WINS
# IF NOT BATCHES 0

def recipe_batches(recipe, ingredients):
  recipie_amount = []
  ingredients_amt = []
  max_batches = 0
  counter = 0
  for i in recipe.values():
    recipie_amount = i
    print(recipie_amount)
  for i in ingredients.values():
    ingredients_amt = i
    print ingredients_amt

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))