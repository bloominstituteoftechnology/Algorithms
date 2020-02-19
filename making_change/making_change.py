#!/usr/bin/python

import sys

def making_change(amount, denominations):
  cache = [0 for i in range(amount+1)]
  cache[0] = 1
  print(cache)
  # check all coins
  for coin in denominations:
    # set combinations for all values from value of coin till amount + 1
    for i in range(coin, amount + 1):
      # add number of combinations to value in cache
      cache[i] = cache[i] + cache[i-coin]
    print(cache)
  return cache[amount]


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")