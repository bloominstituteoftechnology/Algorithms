#!/usr/bin/python

recipe_requirements = {'milk': 100, 'butter': 50, 'cheese': 10}
ingredient_requirements = {'milk': 298, 'butter': 52, 'cheese': 10}

recipe_requirements2 = {'milk': 100, 'butter': 50, 'cheese': 10}
ingredient_requirements2 = {'milk': 398, 'butter': 102, 'cheese': 20}

recipe_requirements3 = {'milk': 100, 'butter': 50, 'cheese': 10, 'eggs': 3}
ingredient_requirements3 = {'milk': 98, 'butter': 102, 'cheese': 20}


def recipe_batches(recipe, ingredients):
    enough_materials = []
    for item in recipe:
        if item not in recipe or item not in ingredients:
            return 0
        if ingredients[item] / recipe[item] > 0:
            enough_materials.append((ingredients[item] / recipe[item]))
        else:
            enough_materials.append(0)

    if min(enough_materials) >= 1:
        return min(enough_materials)
    else:
        return 0
# time complexity: O(3n) or O(n)


print(recipe_batches(recipe_requirements, ingredient_requirements))
print(recipe_batches(recipe_requirements2, ingredient_requirements2))
print(recipe_batches(recipe_requirements3, ingredient_requirements3))
