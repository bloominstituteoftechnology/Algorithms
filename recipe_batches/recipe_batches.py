#!/usr/bin/python

# recipie function receives dictionary of recipie and another dictionary of ingredients
# key is ingredient's name , values are the amounts
# case of recipie, amount needed, case of ingredients, amount available
# recipie_batches outputs max number of whole batches that can be made
# edge case, if recipie has ing that ingredients do not
# edge case, if recipie has ing amount that ingredients do not
#

import math

recipe = {'milk': 100, 'butter': 50, 'flour': 5, }
ingredients = {'milk': 138, 'flour': 51, 'butter': 52, "sugar": 20}


def recipe_batches(recipe, ingredients):
    batches = []
    # return 0 if recipie has more ingredients than in the ingredients dict
    if not all(key in ingredients for key in recipe):
        return 0
    # find key values in recipie and ingredients
    # for key1 in recipe.keys():
    #     print(f"key: {key1}, value: {recipe.get(key1)}")
    # for key2 in ingredients.keys():
    #     print(f"key: {key2}, value: {ingredients.get(key2)}")
    # for key in recipe:
    #     print(key)
    #     print(ingredients[key])
    #     print(recipe[key])
    for key in recipe:
        batches.append(math.floor(ingredients[key]/recipe[key]))
        print(batches)

    return min(batches)


batches = recipe_batches(recipe, ingredients)
print(batches)

# if __name__ == '__main__':
#     # Change the entries of these dictionaries to test
#     # your implementation with different inputs
#     recipe = {'milk': 100, 'butter': 50, 'flour': 5}
#     ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
#     print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
#         batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
