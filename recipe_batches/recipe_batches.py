#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    recipe_needs = []
    ingredients_on_hand = []
    amount_left = []

    for key in recipe:
        if key not in ingredients:
            return 0
    else:
        recipe_needs.append(recipe[key])
        ingredients_on_hand.append(ingredients[key])

    for idx, ingredient in enumerate(ingredients_on_hand):
        quantity_left = ingredient - recipe_needs[idx]

        if quantity_left < 0:
            return 0
        else:
           amount_left.append(ingredient / recipe_needs[idx])

    return int(min(amount_left))


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))