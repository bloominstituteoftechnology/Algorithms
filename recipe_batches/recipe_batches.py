import math

def recipe_batches(recipe, ingredients):
  arr = []
  recipes = [i for i in recipe.values()]
  ingredients = [j for j in ingredients.values()]
  for x in range(0, len(recipes)):
    for y in range(0, len(ingredients)):
      if x == y:
        if ingredients[y] > recipes[x]:
          num = recipes[x] % ingredients[y]
          batch = int(ingredients[y] / num) 
          # print(batch)
          arr.append(batch)
        elif ingredients[y] == recipes[x]:
          arr.append(1)
        else:
          # print(ingredients[y], recipes[x])
          arr.append(0)
  if len(recipes) > len(arr):
    return 0
  else:
    return min(arr)


print(recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 }))
print(recipe_batches({ 'milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 5, 'sugar': 120, 'butter': 500 }))
# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))