#!/usr/bin/env python

import math


def recipe_batches(recipe, ingredients):
	max_batches = None
	for ingredient, requires in recipe.items():
		have = ingredients.get(ingredient, 0)
		can_make = have // requires
		if max_batches is None:
			max_batches = can_make
		if can_make < max_batches:
			max_batches = can_make

	return max_batches


if __name__ == '__main__':
	# Change the entries of these dictionaries to test
	# your implementation with different inputs
	recipe = {'milk': 10, 'butter': 5, 'flour': 5}
	ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
	print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
