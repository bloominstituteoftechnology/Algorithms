#!/usr/bin/python

def recipe_batches(recipe, ingredients):
    howManyTimesTracker = None
    prevHowManyTimesTracker = None
    for r in recipe:
        if r in ingredients:
            howManyTimesTracker = ingredients[r] // recipe[r]
            if prevHowManyTimesTracker == None:
                prevHowManyTimesTracker = howManyTimesTracker
            else:
                if prevHowManyTimesTracker < howManyTimesTracker:
                    howManyTimesTracker = prevHowManyTimesTracker
                elif prevHowManyTimesTracker > howManyTimesTracker:
                    prevHowManyTimesTracker = howManyTimesTracker
        else:
            return 0
    return howManyTimesTracker


"""
function foodAmounts(recipe, ingredients) {
  let howManyTimesTracker;
  let prevHowManyTimesTracker = null;

  for (r in recipe) {
    if (ingredients[r]) {
      howManyTimesTracker = Math.floor(ingredients[r] / recipe[r])

      if (prevHowManyTimesTracker === null) {
        prevHowManyTimesTracker = howManyTimesTracker
      } else {
        if (prevHowManyTimesTracker < howManyTimesTracker) {
          howManyTimesTracker = prevHowManyTimesTracker
        } else if (prevHowManyTimesTracker > howManyTimesTracker) {
          prevHowManyTimesTracker = howManyTimesTracker
        }
      }
    } else {
      return 0
    }
  }
  return howManyTimesTracker
}
"""


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
