#!/usr/bin/python

def recipe_batches(recipe, ingredients):

    min_ratio = 20000

    for ingredient, amount in recipe.items():
        if ingredient not in ingredients:
            return 0
        ratio = ingredients[ingredient] // amount  # floor division
        if ratio < min_ratio:
            min_ratio = ratio

    return min_ratio


if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
