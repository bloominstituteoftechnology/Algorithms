#!/usr/bin/python
recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
import math

def recipe_batches(recipe, ingredients):
  # rec_key_list = list(recipe.keys())
  # print(rec_key_list[0:])
  # recipe_values = list(recipe.values())
  # print(recipe_values)
  # print(recipe.get('milk'))
  evaluated_ri = {k: ingredients[k]//recipe[k] for k in recipe.keys() & ingredients}
  eval_values = evaluated_ri.values()
  sorted_values = sorted(eval_values)
  if sorted_values[0] > 0:
    return sorted_values[0]
  else:
    print("Not Enough Ingredients")

  
  pass 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 500, 'butter': 250, 'flour': 250 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))