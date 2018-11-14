#!/usr/bin/python

import sys

# def making_change(amount, denominations):
#   # NAIVE SOLUTION
#   if amount == 0:
#     return 1

#   if amount < 0:
#     return -1

#   if len(denominations) == 0:
#     return 0

#   return making_change(amount - denominations[-1], denominations) + making_change(amount, denominations[:-1])


# VERSION 2
def making_change(amount, denominations):
  ways = [0] * (amount + 1)

  ways[0] = 1

  for coin in denominations:
    for higher_amount in range(coin, amount + 1):
      remainder = higher_amount - coin
      ways[higher_amount] += ways[remainder]
      print(f'{coin} in {ways}')
  return ways[amount]
  

  # we can initialize a cache as a list (a dictionary would work fine as well) of 0s 
  # with a length equal to the amount we're looking to make change for.
  
  # cache = [0] * amount

  # each val in cache is # of ways to make i cents
  # change for 0 is only one way

  # cache[0] = 1

  # pass 


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")