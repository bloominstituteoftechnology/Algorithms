#!/usr/bin/python
import math

def recipe_batches(recipe, ingredients):
  '''
  descriptipn:
    function should output the maximum number of whole batches that can be made 

  pseudo:
    - write a for loop
    - check that all ingredients in the recipe are available  (if statement)
    - check if ingredients with the same key in the recipe match, exceed, or are lower than the recipe
    - find a way to count the batches
  '''
  batches = []
  for i in recipe:
    # handles if an ingredient is missing
    if i not in ingredients:
      batches.append(0)
    # handles if the ingredients are less that what's needed in the recipe
    elif recipe[i] > ingredients[i]:
      batches.append(0)
    # checks how many ingredient items there are per recipe item, adds it to an array
    else:
      batches.append(math.floor(ingredients[i]/recipe[i]))
  # min chooses the minimum ingredient batch b/c that's the only amount available to make a whole batch
  return min(batches)
  




if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))