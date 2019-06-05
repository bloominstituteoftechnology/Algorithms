#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batches = []

    if recipe.keys() != ingredients.keys():
        return 0
    else:
        for key in ingredients:
            if ingredients[key] >= recipe[key]:
                batches.append(ingredients[key]//recipe[key])

            else:
                return 0
    print(min(batches))
    return min(batches)


# recipe_batches({'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5}, {
#                'milk': 1288, 'flour': 9, 'sugar': 95})  # 0

recipe_batches({'milk': 100, 'butter': 50, 'cheese': 10}, {
               'milk': 198, 'butter': 52, 'cheese': 10})  # 1
if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
