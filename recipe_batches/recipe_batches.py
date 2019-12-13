#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batches = []
    for rec, recAmount in recipe.items():
        for ing, ingAmount in ingredients.items():
            # if recipe key and ing key are identical and their lengths are identical, proceed
            if rec == ing and len(recipe) == len(ingredients):
                # add to empty array the quotient of ing value divided by recipe value, this gives us the amount of batches for each ingredient in the recipe
                batches.append(ingAmount//recAmount)
                # if theres a 0 in the list, we know that we don't have enough of an ingredient for our recipe
                if 0 in batches:
                    return 0
                # check to see if all values in the bathes list are identical
                elif all(i == batches[0] for i in batches):
                    # if its true, we know we equal amount of ingredients for the recipe and we'll return that value
                    return batches[0]
                # if no zeros and no identical numbers exist in batches, return the lowest value in the list
                else:
                    # this lowest value is the minimun number of batches we can make
                    return min(batches)
            else:
                return 0  # if length of recipes doesn't equal length of ingredients, we can't make any batches
    return batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
