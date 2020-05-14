#!/usr/bin/python

def recipe_batches(recipe, ingredients):
    max_batches = None
    for item, qty in recipe.items():
        try:
            max_batches_for_item = ingredients[item] // qty
        except KeyError:
            return 0
        
        if max_batches is None:
            max_batches = max_batches_for_item
        else:
            max_batches = min([max_batches_for_item, max_batches])
    return max_batches
            
        
        


if __name__ == '__main__':
    # Change the entries of these dictionaries to test 
    # your implementation with different inputs
    recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
    ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
    print("{batches} batches can be made from the available ingredients: "
          "'{ingredients}.".format(batches=recipe_batches(recipe, ingredients),
          ingredients=ingredients))