#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # pull keys from each dictionary
    required_for_recipe = recipe.keys()
    avail_ingredients = ingredients.keys()

    # set num_of_batches variable to keep track of lowest number from all ingredients
    num_of_batches = float("inf")

    # make sure all keys in the recipe are in the ingredients
    if set(required_for_recipe).issubset(avail_ingredients):
        for i in required_for_recipe:
            if ingredients[i] / recipe[i] < num_of_batches:
                num_of_batches = math.floor(
                    ingredients[i] / recipe[i])
    else:
        return 0

    return num_of_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
