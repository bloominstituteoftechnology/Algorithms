#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # Confirm we have the ingredients needed
    # for recipe
    if set(recipe) == set(ingredients):
        batches = []
        for i in recipe:
            # Find how many batches can be made out
            # of available ingredients
            if ingredients[i] >= recipe[i]:
                used = ingredients[i] // recipe[i]
                batches.append(used)
        # Find the smallest number of batches in the list
        return min(batches)
    else:
        # Return 0 if we don't have the needed ingredients
        return 0


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
