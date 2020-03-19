#!/usr/bin/python

import sys

def making_change(amount, denominations):
  cache = [0 for i in range(amount + 1)]
  cache[0] = 1
  
  for d in denominations:
    for amount in range(d, amount +1): 
      cache[amount] = cache[amount] + cache[amount - d]
  
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