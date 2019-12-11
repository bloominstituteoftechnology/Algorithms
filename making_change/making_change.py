#!/usr/bin/python

import sys

def making_change(amount, denominations):
  o = 0
  if amount == 0:
    return 1
  for i in range(len(denominations) - 1, -1, -1):
    if amount - denominations[i] == 0:
      o += 1
    elif amount - denominations[i] > 0:
      o += making_change(amount - denominations[i], denominations[:i+1])
  return o


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")