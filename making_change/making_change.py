#!/usr/bin/python

import sys
from math import ceil

def remains(amount, denom):
  return [ amount - i * denom for i in range(amount // denom + 1) ]

def making_change(amount, denominations, caches = None):
  """ Note: this assumes the denominations are pre-sorted.

      This is also not very efficient.
      If an expression for an explicit formula can be worked out,
      it could be made very, very fast; but I don't think
      numpy can maintain the accuracy for accurate answers.
  """

  if len(denominations) == 2:
    return amount // denominations[1] + 1

  if caches == None:
    caches = { i: [None] * (amount + 1) for i in denominations }

  if caches[denominations[-1]][amount] == None:
      caches[denominations[-1]][amount] =\
        sum([ making_change(a, denominations[:-1])
              for a in remains(amount, denominations[-1]) ])
      return caches[denominations[-1]][amount]
  else:
      return caches[denominations[-1]][amount]

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")