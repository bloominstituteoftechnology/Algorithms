#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    if recipe.keys() != ingredients.keys():
        return 0
    else:
        batch = 0
        multiple = 0
        prev_mult = None
        # I have to check the values of each ingredient
        # Each value must be at least 100% of each recipe item
        # If it is, move on
        # If not, we must return 0
        for i in recipe:
            if recipe[i] == ingredients[i]:
                batch -= 1
            elif recipe[i] >= ingredients[i]:
                batch += 0
            else:
                batch += 1
                recipe_mult = ingredients[i] // recipe[i]
                if prev_mult == None:
                    prev_mult = recipe_mult
                    multiples = recipe_mult
                else:
                    if prev_mult == recipe_mult:
                        multiples = recipe_mult
                    elif prev_mult <= recipe_mult:
                        multiples = prev_mult
                    else:
                        multiples = 0
    if batch == len(ingredients) and multiples == 0:
        return 1
    elif multiples != 0 and batch == len(ingredients):
        return multiple





if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
