#!/usr/bin/python
import math


def recipe_batches(recipe, ingredients):
    batches = 0
    done = False
    try:
        while not done:
            shortage = False
            for key in recipe.keys():
                ingredients[key] -= recipe[key]
                if ingredients[key] == 0:
                    done = True
                elif ingredients[key] < 0:
                    done = True
                    shortage = True
            if not shortage:
                batches += 1
    except KeyError:
        print('That key does not exist bruhh')
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
