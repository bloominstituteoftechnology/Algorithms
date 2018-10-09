#!/usr/bin/python

import sys
import math


def making_change(amount, denominations):
  ways = [0] * (amount + 1)
  # makes an array that has the same number of 0s as the amount plus an additional that holds the end value
  ways[0] = 1
  #makes the first value in the array 1
  for coin in denominations:
  # each coin in used 
        for j in range(coin, amount + 1):
          #for each number between the coin and the end of the ways array, this adds the number from the coins number back (IE if you're on nickles it starts at ways[5], and adds ways[0] to it). Pennies adds one to every item in the array. Nickles adds 1 for 6-10. Then 2 for 11-15, then 3 for 16-20. Dimes does the same thing except it takes it's values from ten back (where the nickles made it two already)
            ways[j] += ways[j - coin]
            print(j-coin)
  return ways[amount]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
