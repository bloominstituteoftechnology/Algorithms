#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # sets number of batches and counter (to count the batches) to zero
    max_batch = 0
    counter = 0

    # checks ingredients on hand vs needed by recipe
    for i in recipe:
        try:
            # only whole numbers available
            batches = ingredients[i] // recipe[i]
        except:
            batches = 0  # if not.....
        if counter == 0 or batches <= max_batch:
            # changes max_batch to how ever many batches you could make (from earlier in the function)
            max_batch = batches
        counter += 1
    return max_batch


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
