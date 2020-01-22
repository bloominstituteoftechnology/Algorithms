#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
	# BASE CASES
	if len(ingredients) != len(recipe):
		return 0
	# we need a counter to keep a track of how many batches can be done
	batches = 0

	# we need to iterate to access key/value for both recipe and ingredients
	for ingredient in recipe:
		# as long as we have enough ingredients, keep going!
		while ingredients[ingredient] >= recipe[ingredient]:
			# we check if ingredients current value is greater than recipe current value
			if(ingredients[ingredient] >= recipe[ingredient]):
				# if it is, we subtract ingredients value and the recipe value and increase counter by 1.
				ingredients[ingredient] -= recipe[ingredient]
				batches += 1
			# we check if the number of batches is equal/greater than the length of the recipe, if it is we divide by the length of the recipe
			if(batches >= len(recipe)):
				batches //= len(recipe)
	return batches
  


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))