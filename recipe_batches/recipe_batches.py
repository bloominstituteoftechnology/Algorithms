#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
	#make temp dic to hold counter whenever ingredients value > recipe's values
	temp = {}
	#setting temp length for while loop
	boolean = True
	#iterator to create a key/value pair dic to be equal to 0 
	for i in recipe:
		temp[i] = 0
	#check first if length of recipe > length of ingredients, if not, return 0
	if len(recipe) > len(ingredients):
		return 0
	else:
		#while loop that runs as long as ingredient's value is < recipe's value
		while boolean: 
			#iterate through the recipe list with a loop
			for key in recipe:
				#checks if ingredient's value is >= recipe's value
				if ingredients[key] >= recipe[key]:
					#counts up the value of key atm by 1
					temp[key] += 1
					#sets the ingredient's value atm to be the substraction of both the ingredient's value and the recipe value
					ingredients[key] = ingredients[key] - recipe[key]
				#if ingredient's value is < than recipe's value, break out of the loop
				else:
					boolean = False
		#since we want to return the minimum value in the temp dictionary, we need to convert the dictionary to a list first, then use the min() method.
		result = list(temp.values())
		return min(result)
		
# recipe_batches({ 'milk': 100, 'butter': 50, 'flour': 5 }, { 'milk': 132, 'butter': 48, 'flour': 51 })

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))