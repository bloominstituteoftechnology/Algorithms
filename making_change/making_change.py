#!/usr/bin/python

import sys

#only works if you use coins [1, 5, 10, 25, 50]
#if not get rid of options and use denominations instead and initialize the cache with amount + 1 0's and set cache[0] to 1
def making_change(amount, denominations):
  options = [5, 10, 25, 50]
  cache = [1] * (amount + 1)

  for coin in options:
    for higher_amount in range(coin, amount + 1):
      left_over = higher_amount - coin
      cache[higher_amount] += cache[left_over]
  
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