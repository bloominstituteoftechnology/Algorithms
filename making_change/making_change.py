#!/usr/bin/python

import sys

# can accept following coins [1,5,10,25,50]
# initialize the cache with amount + 1 0's and set cache[0] to 1
# loop through all of the higher amounts between our coin and the amount (i.e., `for higher_amount in range(coin, amount + 1)`)
# take difference between higher amount and value of coin and start building values in cache
# perform that loop for every single coin, and then return the answer in our cache for the original amount!

def making_change(amount, denominations):
  options = [5, 10, 25, 50]
  cache = [1] * (amount + 1)

  for coin in options:
    for higherAmount in range(coin, amount + 1):
      remainder = higherAmount - coin
      cache[higherAmount] += cache[remainder]
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