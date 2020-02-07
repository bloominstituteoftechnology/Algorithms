#!/usr/bin/python

import sys

total = 0
count = 0
sub_count = 1

def making_change(amount, denominations):
  
  test = [1] + [0] * (amount)

  for index in denominations:
    for place in range(index, amount + 1):
      test[place] = test[place] + test[place - index]
  return test[amount]


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")