#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    m = None
    for k in recipe.keys():
        if k not in ingredients.keys():
            return 0
        if ingredients[k] // recipe[k] < m if m != None else True:
            m = ingredients[k] // recipe[k]
    return m if m != None else 0
        
        


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
