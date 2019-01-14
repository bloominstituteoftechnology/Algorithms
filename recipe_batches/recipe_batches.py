#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  count = 0
  can_make_batches = True
  while can_make_batches:
	  for ingredient, amount in recipe.items():
		  try:
			  ingredients[ingredient] -= amount
			  if ingredients[ingredient] < 0:
				  can_make_batches = False
				  break
		  except KeyError:
			  return 0
	  if can_make_batches:
		  count += 1
  return count


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))