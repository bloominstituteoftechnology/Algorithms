#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    batches = 0
    min_batch = 100 # Start with a high number then work down
    for k1,v1 in recipe.items():
        for k2,v2 in ingredients.items():
            if k1 not in ingredients.keys():
                batches = 0
            elif k1 == k2:
                batches = v2 // v1 
            if min_batch > batches:
                min_batch, batches = batches, min_batch

    return min_batch

if __name__ == '__main__':
    # Change the entries of these dictionaries to test 
    # your implementation with different inputs
    recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
    ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
    print("{batches} batches can be made from the available ingredients: {ingredients}."
          .format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))