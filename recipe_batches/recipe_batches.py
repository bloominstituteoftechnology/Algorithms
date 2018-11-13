#!/usr/bin/python

import math
import sys

def recipe_batches(recipe, pantry):
	num_batches = sys.maxsize
	for ingredient, amount in recipe.items():
		if ingredient in pantry:
			pantry_amount = pantry[ingredient]
			multiplier = pantry_amount/amount
			if multiplier < num_batches:
				num_batches = multiplier
		else:
			return 0  
	return int(num_batches)



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'sugar': 10, 'flour': 5 }
  ingredients = { 'milk': 232, 'butter': 100, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
