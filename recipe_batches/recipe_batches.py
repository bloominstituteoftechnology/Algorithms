#!/usr/bin/python

import math

# Output the maximum number of whole batches that can be made for the supplied
#  recipe using the ingredients in the second dictionary


# BELOW COMES WITH NO PRINT STATEMENTS
def recipe_batches(recipe, ingredients):
    l = []
    if len(recipe) != len(ingredients):
        batches = 0
    else:
        for item_r, item_i in zip(recipe, ingredients):
            item_r = (ingredients[item_i] // recipe[item_r])
            l.append(item_r)
        # l.sort()
        batches = min(l)
    return batches

# # BELOW COMES WITH MANY PRINT STATMENTS
# def recipe_batches(recipe, ingredients):
#   l = []
#   if len(recipe) != len(ingredients):
#     batches = 0
#   else:
#     for item_r, item_i in zip(recipe, ingredients):
#       item_r = (ingredients[item_i] // recipe[item_r])
#       l.append(item_r)
#       # print(f'Inside for loop {item_r}')
#     # print(f'Outside for loop {item_r}')
#     # print(item_r)
#     # print(item_i)
#     l.sort()
#     batches = l[0]
#     # print(l)
#   return batches

#
# r = { 'milk': 100, 'butter': 50, 'flour': 5 }
# i = { 'milk': 132, 'butter': 48, 'flour': 51 }
#
# r2 = { 'milk': 100, 'butter': 50, 'cheese': 10 }
# i2 = { 'milk': 198, 'butter': 52, 'cheese': 10 }
# r3 = { 'milk': 2, 'sugar': 40, 'butter': 20 }
# i3 = { 'milk': 5, 'sugar': 120, 'butter': 500 }
#
# r4 = { 'milk': 2 }
# i4 = { 'milk': 200}
#
# print(recipe_batches(r, i))
# print(recipe_batches(r2, i2))
# print(recipe_batches(r3, i3))
# print(recipe_batches(r4, i4))

# print(len(r))

#
# print(i['milk'] // r['milk'])
# print(i['butter'] // r['butter'])
# print(i['flour'] // r['flour'])

# print(r['milk'])


# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))