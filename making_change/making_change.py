#!/usr/bin/python

import sys

def making_change(amount, denominations):
  #base cases
  if amount == 0:
    return 1
  if amount < 0:
    return 0
  if len(denominations) == 0 and amount > 0:
    return 0
  else:
    return making_change(amount - denominations[-1], denominations)  + making_change(amount, denominations[:-1])


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")