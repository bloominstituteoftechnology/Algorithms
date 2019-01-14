#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batches = []
    if len(recipe) == len(ingredients):
        for k in ingredients:
            batches.append(ingredients[k] // recipe[k])

    return batches


recipe = {"milk": 2, "sugar": 40, "butter": 20}
ingredients = {"milk": 5, "sugar": 120, "butter": 500}
print(recipe_batches(recipe, ingredients))

if __name__ == "__main__":
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {"milk": 100, "butter": 50, "flour": 5}
    ingredients = {"milk": 132, "butter": 48, "flour": 51}
    print(
        "{batches} batches can be made from the available ingredients: {ingredients}.".format(
            batches=recipe_batches(recipe, ingredients), ingredients=ingredients
        )
    )

