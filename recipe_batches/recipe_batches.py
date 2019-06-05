#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # holds amount of each ingredient/how many batches we can make with it
    batches = []

    # checks to see that we have the same ingredients as we do keys
    if recipe.keys() != ingredients.keys():
        return 0
    else:
        # we only have to loop once since we now know that we have all of the sam ingredients
        for key in ingredients:
            # if we have enough of a specific ingredient, how many batches could we make with it?
            if ingredients[key] >= recipe[key]:
                batches.append(ingredients[key]//recipe[key])
            # if the answer is 0, just return 0 now
            else:
                return 0
    # the smallest number within the batches list is the max amount of the recipe we can make
    print(min(batches))
    return min(batches)


recipe_batches({'milk': 100, 'butter': 50, 'cheese': 10}, {
               'milk': 198, 'butter': 52, 'cheese': 10})  # 1
if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
