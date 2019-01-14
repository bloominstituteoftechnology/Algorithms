#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    countList = []

    if len(recipe) != len(ingredients):
        return 0

    for rec in recipe:  # O(n)
        if rec in ingredients:
            if recipe[rec] <= ingredients[rec]:
                countList.append(int(ingredients[rec]/recipe[rec]))
            else:
                return 0
        else:
            return 0
    return min(countList)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("""{batches} batches can be made from the available ingredients:
  {ingredients}.""".format(batches=recipe_batches(recipe, ingredients),
                           ingredients=ingredients))
