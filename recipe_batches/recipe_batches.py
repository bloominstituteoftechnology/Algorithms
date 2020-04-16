
import math


def recipe_batches(recipe, ingredients):
    ingredient_amount = [0] * len(recipe)
    batches = 0
    if len(recipe) > len(ingredients):
        batches = 0
    else:
        for index, value in enumerate(recipe):
            for index2, value2 in enumerate(ingredients):
                if value == value2:
                    ingredient_amount[index] = ingredients[value2] // recipe[value]

    print(ingredient_amount)
    if min(ingredient_amount) < 1:
        batches = 0
    else:
        batches = min(ingredient_amount)
    print(batches)
    return batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
