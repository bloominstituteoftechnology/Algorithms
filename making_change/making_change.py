#!/usr/bin/python

import sys

def making_change(amount, denominations):
  #if amount is less than 1 return 0
  #if 


  if amount <= 1:
    return amount
  
  elif amount > 1:
    coins = denominations
    for i in coins:
      if i > amount:
        tooLarge = coins.index(i, 0, len(coins))
        print(tooLarge)

    

    
    
making_change(10, denominations = [1, 5, 10, 25, 50])


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")