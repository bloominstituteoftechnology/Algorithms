#!/usr/bin/python

import math

def recipe_batches(recipe, inventory):
  # function takes in 2 dictionaries, one representing a recepie and the other how much ingrededients we have
  # compare recipe to ingredients
  # find how many batches of the recipe we can make given what the recipe calls and what we have

  # batch available for ONE ingredient: 
  # needed (20) what we have (40), QUOTIENT = 40 / 20

  # FIND THE LARGEST QUOTIENT AND OUTPUT IT
    # If there are ANY quotients less than 1 then output 0
  
  # inputs:
  # 2 dictionaries each with POSSIBLE keys: 
    # milk, butter, flour, cheese, sugar

  # RECIPE =    { 'milk': 100, 'butter': 50, 'flour': 5 }
  # INVENTORY = { 'milk': 138, 'butter': 48, 'flour': 51 }

  ## ---------------------- FIND THE SMALLEST BATCH POSSIBLE

  ## loop through recipe dictionary get the quotient of inventory item divided 
  ## by recipe amount, while also recording the smallest batch possible, which is what
  # will be returned. if there are any missing keys from the inventory dict recipe dict has, return 0.
  smallest_batch = 999999999999

  # first check if the length of the inventory equal or greater, if it's smaller
  # then we don't have all the ingredients
  if len(recipe) > len(inventory):
    return 0

  # loop through the recipie and check the inventory dict for matching key
  for ingredient_key in recipe:
    if ingredient_key in inventory:
      # found matching ingredient, calculate how many batches it can make
      batch_amount = inventory[ingredient_key] // recipe[ingredient_key]
      if batch_amount < 1: # not enough ingredients for one batch, recipe not possible
        return 0
      else:
        # at least one batch is possible, check if it's the smallest, if it is, save it
        if batch_amount < smallest_batch:
          smallest_batch = batch_amount
  
  # at the end of the loop we should have the smallest batch possible
  return smallest_batch

# print(recipe_batches({ 'milk': 2 }, { 'milk': 200}))

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))