#!/usr/bin/python

import sys

cache = {}


def making_change(amount, denominations):
  global cache

  if amount in cache:
    return cache[amount]

  elif amount == 0:
    return 1

  elif amount < 5:
    result = making_change(amount - denominations[0], denominations)
    cache[amount] = result
    return result

  elif amount < 10 and amount >= 5 :
    result = making_change(amount - denominations[0], denominations) + making_change(amount - denominations[1], denominations)
    cache[amount] = result
    return result

  elif amount < 25 and amount >= 10 :
    result = making_change(amount - denominations[0], denominations) + making_change(amount - denominations[1], denominations) + making_change(amount - denominations[2], denominations)
    cache[amount] = result
    return result

  elif amount < 50 and amount >= 25 :
    result = making_change(amount - denominations[0], denominations) + making_change(amount - denominations[1], denominations) + making_change(amount - denominations[2], denominations) + making_change(amount - denominations[3], denominations)
    cache[amount] = result
    return result

  else:
    result = making_change(amount - denominations[0], denominations) + making_change(amount - denominations[1], denominations) + making_change(amount - denominations[2], denominations) + making_change(amount - denominations[3], denominations) + making_change(amount - denominations[4], denominations)
    cache[amount] = result
    return result

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")
