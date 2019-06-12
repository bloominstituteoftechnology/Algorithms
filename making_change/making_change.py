#!/usr/bin/python

import sys

def calculate(amount, denominations, cache):
  if amount < 0:
    return 0
  elif amount == 0:
    return 1
  elif len(denominations) == 1:
    return 1
  else:
    try:
      if cache[f'{amount}-{denominations}'] > 0:
        return cache[f'{amount}-{denominations}']
    except KeyError:
      pass
    permutations = 0
    while denominations[-1] > amount:
      denominations.pop()
    for i in range(amount//denominations[-1] + 1):
      permutations += calculate(amount - (i * denominations[-1]), denominations[:-1], cache)
    cache[f'{amount}-{denominations}'] = permutations
    return permutations

def making_change(amount, denominations):
  if amount is 0 or amount is 1:
    return 1
  else:
    return calculate(amount, list(denominations), {})


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")