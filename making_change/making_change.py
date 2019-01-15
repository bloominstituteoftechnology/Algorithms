#!/usr/bin/python

import sys

def making_change(amount, denominations):
  if amount == 0 or amount == 1:
    return 1

  if amount not in denominations:
    denominations[amount] = (amount - 1) + (amount - 2) + (amount - 3) + (amount - 4) + (amount - 5)
  
  return denominations



if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")