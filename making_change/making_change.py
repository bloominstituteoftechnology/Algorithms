#!/usr/bin/python

import sys
# 1 * 0 + 5 * 0 = 0
# [1, 5]
#   making_change(100, [1, 5]):
#     making_change(100 -1,[1, 5])
#       making_change(100,[5])
def making_change(amount, denominations):
  # amount cents 
  # demoniations lists of different coins
  # iterate through demonination  
  # return number of combinations
  # storage_list to keep track of all of the ways 
  # storage amount + 1
  if amount == 0:
    return 1 # 0 pennies and nickels etc
  if amount < 0:
    return 0
  # if len(denominations) == 0:
  #   return 0
  if len(denominations) == 1:
    return 1
  return making_change(amount - denominations[-1], denominations) + making_change(amount, denominations[:-1])


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]      
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")