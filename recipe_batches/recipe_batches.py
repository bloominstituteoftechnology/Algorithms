#!/usr/bin/python
import sys


def recipe_batches(recipe, ingredients):
    batches = sys.maxsize

    for key in recipe:
        if key in ingredients:
            if batches > ingredients[key] // recipe[key]:
                batches = ingredients[key] // recipe[key]
        else:
            return 0
    return batches


# def recipe_batches(recipe, ingredients):
#     batches = []

#     for key in recipe:
#         if key in ingredients:
#             batches.append(ingredients[key] // recipe[key])
#         else:
#             return 0
#     return min(batches)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test 
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 50}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))