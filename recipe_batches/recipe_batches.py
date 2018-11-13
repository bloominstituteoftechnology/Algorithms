#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    make = []
    for i in list(recipe.keys()):
        if i in ingredients and recipe[i] < ingredients[i]:
            make.append(math.floor(ingredients[i] / recipe[i]))
        elif i not in ingredients:
            return 0
    return min(make)


# print(
#     recipe_batches(
#         {"milk": 100, "flour": 4, "sugar": 10, "butter": 5},
#         {"milk": 1288, "flour": 9, "sugar": 95},
#     )
# )  # 0
# print(
#     recipe_batches(
#         {"milk": 100, "butter": 50, "cheese": 10},
#         {"milk": 198, "butter": 52, "cheese": 10},
#     )
# )  # 1
# print(
#     recipe_batches(
#         {"milk": 2, "sugar": 40, "butter": 20}, {"milk": 5, "sugar": 120, "butter": 500}
#     )
# )  # 2
# print(recipe_batches({"milk": 2}, {"milk": 200}))  # 100


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
