#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
			
	needed_ingredients = {key: ingredients[key] for key in ingredients if key in recipe}

	if list(needed_ingredients.keys()) != list(recipe.keys()):
		return 0

	batches = 100000
	for item in needed_ingredients:
		if ingredients[item] // recipe[item] < batches:
			batches = ingredients[item] // recipe[item]
	
	return batches




if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 1, 'butter': 5, 'flour': 1}
  ingredients = { 'milk': 10, 'butter': 15, 'eggs': 100  }







  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

  recipe_batches(recipe,ingredients)