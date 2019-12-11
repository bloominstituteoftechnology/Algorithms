#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients, batch_count=0):
  batch_count = batch_count
  if len(recipe) > len(ingredients):
    return batch_count
  for key in ingredients.keys():
   if ingredients[key] < recipe[key]:
      return batch_count
   else:
      ingredients[key] = ingredients[key] - recipe[key]
      batch_count += 1
      newingreds = ingredients
      
      
      return recipe_batches(recipe,newingreds,batch_count)
      
  
  
if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 , 'sugar': 90}
  ingredients = { 'milk': 138, 'butter': 90, 'flour': 50 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))