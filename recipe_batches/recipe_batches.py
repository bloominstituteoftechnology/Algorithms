#!/usr/bin/python


def recipe_batches(recipe, ingredients):
    enough_materials = []
    for item in recipe:
        if item not in ingredients:
            return 0
        if ingredients[item] / recipe[item] > 0:
            enough_materials.append((ingredients[item] / recipe[item]))
        else:
            enough_materials.append(0)
    if min(enough_materials) >= 1:
        return int(min(enough_materials))
    else:
        return 0


recipe_batches({'milk': 2, 'sugar': 40, 'butter': 20}, {'milk': 5, 'sugar': 120, 'butter': 500})
