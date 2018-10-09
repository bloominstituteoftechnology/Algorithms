#!/usr/bin/python

import sys


def making_change(amount, denominations):
    cache = {x: 0 for x in range(amount + 1)}
    cache[0] = 1

    for coin in denominations:
        # essentially allows us to iterate through cache and update the values based on the difference
        # when coin = 1, everything gets initialized to 1
        # when coin = 5, now we take into account the diff, which allows us to increment accordingly
        # e.g. 5-9 should be 2, because the diff remains at 0-4, but when it hits 10, we take into
        # account of cache[5], which will be 2, which leads to an updated cache[10] of 3
        # follows this logic throughout, until we iterate through the valid coins and can return cache[amount]
        for higher_amount in range(coin, amount + 1):
            diff = higher_amount - coin
            cache[higher_amount] += cache[diff]

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