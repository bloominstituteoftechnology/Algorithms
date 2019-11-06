#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    if len(recipe) > len(ingredients):
        print(0)
        return 0
    else:
        final_batches = []
        for ing, amt in recipe.items():
            divided = ingredients[ing] // amt
            final_batches.append(divided)
        print(min(final_batches))
        return min(final_batches)



r_one = { 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }
i_one = {'milk': 1288, 'flour': 9, 'sugar': 95 }
r_two = {'milk': 100, 'butter': 50, 'cheese': 10 }
i_two = { 'milk': 198, 'butter': 52, 'cheese': 10 }
r_three = { 'milk': 2, 'sugar': 40, 'butter': 20 }
i_three = { 'milk': 5, 'sugar': 120, 'butter': 500 }

# recipe_batches(r_one, i_one)

# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
