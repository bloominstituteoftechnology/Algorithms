#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    qtyOfBatches = {}
    lowestBatch = None
    for iR in recipe:
        if iR in ingredients:
            recipeIngr = recipe.get(iR)
            ingredientsIngr = ingredients.get(iR)
            batchesPerIngr = int(ingredientsIngr / recipeIngr)
            tempBatches = batchesPerIngr
            lowestBatch = batchesPerIngr if (
                lowestBatch == None or lowestBatch > batchesPerIngr) else lowestBatch
            print(lowestBatch)
            if(batchesPerIngr == 0):
                return 0
            qtyOfBatches[iR] = batchesPerIngr
            print(f"min of batches: {lowestBatch}")
        else:
            return 0
    return lowestBatch


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 51, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
