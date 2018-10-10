#!/usr/bin/python

import sys

def make_change(amount, denominations):
    cache = [0] * (amount + 1)
    cache[0] = 1 

    #loop over the denominations list 
    for coin in denominations:
        for higher_amount in range(coin, amount+1):
            remainder = higher_amount - coin
            cache[higher_amount] += cache[remainder]
            #remainder will be some value we have seen already. 
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