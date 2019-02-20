#!/usr/bin/python

import math
# need to check that both dicts have the same key
# we can assume that if the length of the recipe dict is greater than the length of the ingredients dict, we cant return any batches either
# compare if the recipe value is > or < the ingredients value at that dict
# if the recipe value > ingredients value we cant make any batches, so return count
# else if the ingredients value > recipe value, subtract the recipe value from ingredients value, then call again


def recipe_batches(recipe, ingredients):
    count = 0
    flag = True

    if len(recipe) > len(ingredients):
        return 0
    else:
        copyIng = ingredients.copy()
        while flag == True:
            for index, key in enumerate(recipe.items()):
                newKey = copyIng[key[0]] - key[1]
                newDict = {key[0]: newKey}
                print(key[1])
                print(copyIng[key[0]])
                if key[1] <= copyIng[key[0]]:
                    copyIng.update(newDict)
                else:
                    flag = False
            count += 1
        if(count == 1):
            return count
        else:
            return count-1
        pass


if __name__ == '__main__':
        # Change the entries of these dictionaries to test
        # your implementation with different inputs
        # { 'milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 5, 'sugar': 120, 'butter': 500 }
    recipe = {'milk': 2, 'sugar': 40, 'butter': 20}
    ingredients = {'milk': 5, 'sugar': 120, 'butter': 500}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
