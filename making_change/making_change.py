#!/usr/bin/python

import sys

denominations = [1, 5, 10, 25, 50]
# def making_change(amount, denominations):
#   obj = {
#     4: 1,
#     5: 2, 
#     10: 4
#   }
#   if amount <= obj[amount]:
#     return obj[amount]




# pennies, nickels, dimes, quarters, and half-dollars:

#  1. We can make change for 10 cents using 10 pennies
#  2. We can use 5 pennies and a nickel
#  3. We can use 2 nickels
#  4. We can use a single dime

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")