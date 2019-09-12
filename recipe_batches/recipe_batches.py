#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
	max_num = 0
	for r in recipe:
		if r not in ingredients:
			return 0
		batch = (ingredients[r] // recipe[r])
		if max_num is 0:
			max_num = batch
	return max_num


if __name__ == '__main__':
	# Change the entries of these dictionaries to test
	# your implementation with different inputs
	recipe = {'milk': 100, 'butter': 50, 'flour': 5}
	ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
	print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
		batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
