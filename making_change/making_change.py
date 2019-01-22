#!/usr/bin/python

import sys

def making_change(amount, denominations):
  """
  The function needs to take an amount and find out how many permutations of the 
  denominations given it would take to reach that amount. Trying to find a pattern
  within the solutions right now.
  """
  if amount < 5:
    return 1
  if amount <= 9:
    return 2


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")