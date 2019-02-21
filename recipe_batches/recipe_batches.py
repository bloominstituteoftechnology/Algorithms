#!/usr/bin/python
import math


def recipe_batches(recipe, ingredients):
    batches = 0
    done = False
    # need to use try to catch the error from any missing keys when comparing the dictionaries
    try:
        # while done == False, run loop
        while not done:
            # set the shortage to false at the start
            shortage = False
# compare the keys of reciepes and ingredients
            for key in recipe.keys():
                # deep subtract the matching recipes from the ingredients
                ingredients[key] -= recipe[key]
# if you have none left on any of them, then we're done with 0 batches
                if ingredients[key] == 0:
                    done = True
# if the remaining ingredents are greater than 0
                elif ingredients[key] < 0:
                    done = True
                    shortage = True
            if not shortage:
                batches += 1
# the test checks for butter which isn't in one of the cases
# this keyError let's it pass without issues over mismatched keys
    except KeyError:
        print('That key does not exist bruhh')
# finally block lets it execute the try command without error
    finally:
        return batches


recipe_batches({'milk': 100, 'butter': 50, 'flour': 5},
               {'milk': 138, 'butter': 100, 'flour': 51})


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
