#!/usr/bin/python

import math

rec = {'milk': 100, 'butter': 50, 'flour': 5}
ing = {'milk': 940, 'butter': 910, 'flour': 101}


def recipe_batches(recipe, ingredients):
    # Grab the names of the ingredients
    recipe_ingredients = recipe.keys()

    # Set batches to 0
    batches = 0

    # Loop until function finds that their aren't enough ingredients
    while 1 == 1:
        print(f'current batches: {batches}')

        # Loop thru ingredients
        for recipe_key in recipe_ingredients:

            # Print msg if an ingredient does not exist in ingredients dictionary
            try:
                # Test if there is requiered amount of current ingredient
                if ingredients[recipe_key] >= recipe[recipe_key]:
                    print(f'avail_{recipe_key}:{ingredients[recipe_key]}, need_{recipe_key}:{recipe[recipe_key]}')

                    # Subtract required ingredient quantity from ingredients dictionary value
                    ingredients[recipe_key] -= recipe[recipe_key]
                    print(f'new avail_{recipe_key}:{ingredients[recipe_key]}')

                # Return current amount of batches if there is not enough for another batch
                else:
                    print(f'Not enough {recipe_key}')
                    print(f'batches: {batches}')
                    return batches
            # Print message if an ingredient does not exist in ingredients dictionary
            except KeyError:
                print(f'No {recipe_key} in available ingredients')
                print(f'batches: {batches}')
                return 0

        batches += 1


recipe_batches(rec, ing)

# if __name__ == '__main__':
#     # Change the entries of these dictionaries to test
#     # your implementation with different inputs
#     recipe = {'milk': 100, 'butter': 50, 'flour': 5}
#     ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
#     print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
#         batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
