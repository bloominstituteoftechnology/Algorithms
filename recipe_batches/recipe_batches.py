#!/usr/bin/python

import math

# def recipe_batches(recipe, ingredients):
#   maxBatches = 0
#
#   return maxBatches
#
#
# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
#
#



#   LAMBDA PROBLEM SOLVING FRAMEWORK

# UPER

# UNDERSTAND
#     GOAL - RETURN HOW MANY BATCHES OF RECIPE CAN BE MADE FROM INPUT OF 2 DICTIONARIES
#     {1ST RECIPES}, 2ND {CURRENT INGREDIENTS}
#       BASED ON TEST RESULTS NO NEED TO ACCOUNT FOR BAD INPUT
#     - ACCOUNT FOR HAVING NO INGREDIENTS IN STORED
#     EX:
# INPUT
#         recipe_batches(
#   { 'milk': 100, 'butter': 50, 'flour': 5 },
#   { 'milk': 138, 'butter': 48, 'flour': 51 }
# )
# OUTPUT -- 0 -- NOT ENOUGH INGREDIENTS

#     EX:
# INPUT
#       recipe_batches(
#   { 'milk': 2, 'sugar': 40, 'butter': 20 },
#   { 'milk': 5, 'sugar': 120, 'butter': 500 }
# )
# OUTPUT -- 2 -- NOT ENOUGH INGREDIENTS

print('PROGRAM START')
# PLAN
# INPUT(DICTIONARY1, DICTIONARY2) RETURN => MAX BATCHES(TYPE=INT)
def recipe_batches(recipe, ingredients):
  max_batches = 0

  for recipe_ingredient in recipe:
    if recipe_ingredient not in ingredients:
      return 0

      current_max = ingredients[recipe_ingredient] // recipe[recipe_ingredient]

      if current_max <= 0:
        return 0
      elif max_batches == None or current_max < max_batches:
        max_batches = current_max
    return max_batches








      # if max_batches == 0:
      #   max_batches = current_batches
      # elif max_batches > current_batches:
      #   max_batches = current_batches
      # print('current_batches')
      # print(current_batches)
      # recipes_values = recipe.items()
      # print('recipe.values')
      # print(recipe.values)
      # ingredients_values = ingredients.items()
      # print('ingredients.values')
      # print(ingredients.values)
      # # FOR EACH VALUE IN THE FIRST DICTIONARY,
      # for i in recipe_ingredient:
      #   print('I IN RECIPE')
      #   print(i)
      #  # if value1 is lessor than value2 return value1 / value2
      #   recipesCount = i
      #   print('recipesCount')
      #   print(recipesCount)
      #   for i2 in ingredients_values:
      #     print('I2 IN RECIPE')
      #     print(i2)
      #     ingredientsCount = i2
      #     print('ingredientsCount')
      #     print(ingredientsCount)
      #     if recipesCount < ingredientsCount:
      #
      #       z = recipesCount / ingredientsCount
      #       print('if')
      #       print(z)
      #       return z
      #     else:
      #       z = ingredientsCount / ingredientsCount
      #       print('else')
      #       print(z)
      #       return z
          # elif:
          #   return 0
          #
      # COMPARE TO EACH VALUE IN 2ND DICTIONARY
      # IF
      # RETURN WHOLE NUMBER IF GREATOR THAN 1, ELSE RETURN 0

    #   print('FUNCTION RAN')
    #   print(max_batches)
    #   return max_batches
    #
    # print(max_batches)
    # return max_batches

# EXECUTE
recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 })
print('PROGRAM END')
# REFLECT

if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
