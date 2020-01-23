#!/usr/bin/python

import sys
cache = {}
sys.setrecursionlimit(1500)

def making_change(amount, denominations):
  if amount == 0 or amount == 1:
     return 1

  different_ways = [1] + [0] * amount
  for coins in denominations:
    for higher in range(coins, amount + 1):
        different_ways[higher] += different_ways[higher - coins]
  return different_ways[amount]
  pass



if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")