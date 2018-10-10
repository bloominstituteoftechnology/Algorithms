#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  v1=list(recipe.values())
  v2=list(ingredients.values())
  batch=[]

  l1=len(v1)

  if len(v1)!=len(v2):
    return(0)

  for i in range(0, l1):
    if v2[i] < v1[i]:
      return(0)
    else:
      if abs(v2[i]/v1[i]) > 0:
        diff=int(abs(v2[i]/v1[i]))
        batch.append(diff)
    
    
  batch.sort()
  return (batch[0])        


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
