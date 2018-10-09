#!/usr/bin/python

import sys

def making_change(amount, denominations):
  ways = [0] * (amount + 1) # amount = 10 + 1 [0,0,0,0,0,0,0,0,0,0,0]
  ways[0] = 1  # - [1,0,0,0,0,0,0,0,0,0,0]
  # if amount <= 0:
  #   return 0
  # elif 1 <= amount <= 4:
  #   return 1
  # elif 5 <= amount <= 9:
  #   return 2
  # else:
  for i in denominations:
    for j in range(i , amount + 1):# j = 1,2,3,4,5,,6,7,8,9,10,5,6,7,8,9,10,10 incrementing i = 1,5,10 cents
      ways[j] += ways[j - i]
  return ways[amount]


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")