#!/usr/bin/python

import math

# Pseudo
# DO a while loop
# Compare values of each and if they pass then subtract rec and ing
# Do batch++
# New value of ingredients compare to recipe again, if lower then break loop and return batch
# if equal or higher batch++ and subtract recipe and ingredients
# Rinse and repeat


# def recipe_batches(recipe, ingredients):
#     ing_milk = ingredients["milk"]
#     ing_butter = ingredients["butter"]
#     ing_flour = ingredients["flour"]
#     rec_milk = recipe["milk"]
#     rec_butter = recipe["butter"]
#     rec_flour = recipe["flour"]
#     batch = 0

#     if (ing_milk < rec_milk or
#         ing_butter < rec_butter or
#             ing_flour < rec_flour):
#         return batch
#     else:

#         while(ing_milk >= rec_milk and
#               ing_butter >= rec_butter and
#               ing_flour >= rec_flour):
#             batch += 1
#             ing_milk -= rec_milk
#             ing_butter -= rec_butter
#             ing_flour -= rec_flour

#     return batch


# Compare if they have same keys. If dont then batch = 0
# While values in ingredients are equal or greater than recipe subtract and repeate loop and batch++


# Couldnt get while loop to work so checked to see if each of them had the same keys
# If same keys then iterate through the  keys
# If ingredients < recipe then return 0
# If not then divide ingred/recipe and append that into batch array
# Then call "min" function to return the lowest number meaning lowest batch
def recipe_batches(recipe, ingredients):
    batch = []

    if recipe.keys() == ingredients.keys():
        for key in recipe:
            if ingredients[key] < recipe[key]:
                return 0
            else:
                batch.append(ingredients[key] // recipe[key])

    else:
        return 0

    return min(batch)

    # First dic is recpie = How much we need to make
    # Second dic is ingredients = How much we have currently
    # If dont have enough then returns zero, else returns how much you can make(1,2,3, etc)
# print(recipe_batches(
#     {'milk': 100, 'butter': 50, 'flour': 5},
#     {'milk': 301, 'butter': 50, 'flour': 0}
# )
print(recipe_batches(
    {'milk': 2, 'sugar': 40, 'butter': 20},
    {'milk': 5, 'sugar': 120, 'butter': 500}
))


# if __name__ == '__main__':
#     # Change the entries of these dictionaries to test
#     # your implementation with different inputs
#     recipe = {'milk': 100, 'butter': 50, 'flour': 5}
#     ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
#     print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
#         batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
