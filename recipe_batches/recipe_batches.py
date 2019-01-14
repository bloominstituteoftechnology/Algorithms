#!/usr/bin/python

import math
# need to check that both dicts have the same key
# compare if the recipe value is > or < the ingredients value at that dict
# if the recipe value > ingredients value we cant make any batches, so return count
# else if the ingredients value > recipe value, subtract the recipe value from ingredients value, then call again


def recipe_batches(recipe, ingredients):
    pass


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
