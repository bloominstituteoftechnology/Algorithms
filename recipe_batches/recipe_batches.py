#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
	temp = {}
	#setting temp length for while loop
	boolean = True

	for i in recipe:
		temp[i] = 0
	#check first if length of recipe == to length of ingredients, if not, return 0
	if len(recipe) > len(ingredients):
		return 0
	else:
	#while loop that runs as long as temp's length is equal to recipe's length
		while boolean: 
		#iterate through the recipe list with a loop
			for key in recipe:
				if ingredients[key] >= recipe[key]:
					temp[key] += 1
					ingredients[key] = ingredients[key] - recipe[key]
					print(temp)
				else:
					boolean = False
					
		result = list(temp.values())
		return min(result)


# recipe_batches({ 'milk': 100, 'butter': 50, 'flour': 5 }, { 'milk': 132, 'butter': 48, 'flour': 51 })
if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))