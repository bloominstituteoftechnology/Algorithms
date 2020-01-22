#!/usr/bin/env python3

import math


def recipe_batches(recipe, ingredients):
    maxBatches = float("inf")
    if len(recipe) < 1:
        return 0
    for ingredient in recipe:
        requiredAmount = recipe[ingredient]
        availableAmount = ingredients.get(ingredient, 0)
        if availableAmount < requiredAmount:
            return 0
        ingredientBatchesAvailable = availableAmount // requiredAmount
        maxBatches = min(ingredientBatchesAvailable, maxBatches)

    return maxBatches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
