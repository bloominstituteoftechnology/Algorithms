#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    # Get ingredients
    recipe_ingredients = [key for key, value in recipe.items()]
    stock_ingredients = [key for key, value in ingredients.items()]
    
    # Check that we have all the ingredients
    for entry in recipe_ingredients:
        if entry not in stock_ingredients:
            return 0
        else:
            pass
        
    # Get possible batch sizes for each
    possible_batch_sizes = []
    
    for key, value in recipe.items():
        batch_size = ingredients[key] // value
        possible_batch_sizes.append(batch_size)
        
    return min(possible_batch_sizes)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))