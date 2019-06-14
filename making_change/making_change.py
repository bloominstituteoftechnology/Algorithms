#!/usr/bin/python

import sys

def making_change(amount, denominations):
  #base cases
  if amount < 5 and amount >=0:
    return 1

  elif amount < 0:
    return 0

  # recursive case - not handling all cases correctly
  else:
    count = 0
    for c in denominations:
      count += making_change(amount - c, denominations)
    # return making_change(amount - 1, coin) + making_change(amount - 5, coin) + making_change(amount - 10, coin) + making_change(amount - 25, coin) + making_change(amount - 50, coin)
    return count

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")

    #penny = n - 1
    # nickle = n - 5
    # dime = n - 10
    # quarter = n - 25
    # 1/2 dollar = n - 50
    # n = 0 return 0
    # n = 1 return 1