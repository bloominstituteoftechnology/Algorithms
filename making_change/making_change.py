#!/usr/bin/python

import sys

cache = {1:1}

def making_change(amount, denominations):
  
 if amount in cache: 
  return cache[amount]
   totalWays = 0 

  for d in denominations:
    if d <= amount:
      totalWays += making_change(amount-d, denominations) + making_change(amount, denominations)

      cache[amount] = totalWays
      return totalWays

      print(cache)
      print(making_change(10,[1, 5, 10, 25, 50]))
      


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")