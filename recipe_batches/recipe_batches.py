#!/usr/bin/python

import math

"""
Thoughts on solving this problem:

- Seems like a minimum of two loops will be required: one to check for ingredients available, one to check for ingredients required. Maybe a one-loop way later, not concerned about this for now.
- At its base level, this should be a straightforward problem -- simply check numbers against one another to see if enough ingredients are available to complete given recipe(s).


"""
def recipe_batches(recipe, ingredients):
  count = []
  # test for appropriate lengths
  if len(recipe) != len(ingredients):
    return 0
  
  recipeSort = sorted(recipe)
  ingredSort = sorted(ingredients)

  for i in range(len(recipeSort)):
    ingredOne = ingredSort[i]
    recOne = recipeSort[i]
    # test the above variables
    print(ingredOne, recOne)
    if recOne == ingredOne:
      if recipe[recOne] <= ingredients[ingredOne]:
        count.append(int(ingredients[ingredOne]/recipe[recOne]))
      else:
        return 0
    else:
      return 0
  return min(counter)
  pass 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))