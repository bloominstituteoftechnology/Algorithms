#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients, batches=0):
  batch = batches
  pendingBatch = []
  for ingredient in recipe:
    if ingredient in ingredients: #check if it has ingredient at all
      if recipe.get(ingredient) <= ingredients.get(ingredient): #check if it has enough ingredient
        pendingBatch.append(1) #if so, add a tally to pending
        ingredients[ingredient] -= recipe.get(ingredient) #decrement from ingredients
        if len(pendingBatch) == len(recipe): #check if the pending batch is finished
          batch += 1 #if it is, increment batch
          pendingBatch = [] #and reset pending
          recipe_batches(recipe, ingredients, batch) #try again to make another batch
        else:
          continue #otherwise keep going until a full batch is made
      else: #if you can't keep going, return how many batches were made thus far
        print ("not enough!")
        print (batch)
        return batch
    else:
      return 0
print(recipe_batches({ 'milk': 100, 'butter': 50, 'cheese': 10 }, { 'milk': 198, 'butter': 52, 'cheese': 10 }))

# if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  # recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  # ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  # print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))