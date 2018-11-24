#!/usr/bin/python

import sys

def making_change(amount, denominations):
  # --- method 1 start ---
  # if amount == 0:
  #   return 1 
  
  # if amount < 0:
  #   return 0

  # if len(denominations) == 0:
  #   return 0
  
  # return making_change(amount - denominations[-1], denominations) + making_change(amount, denominations[-1])
  # --- method 1 end ---
  
  ways = [0] * (amount + 1)
  
  ways[0] = 1  # ways will be an array, each element is number of ways to get to 0 cents, 1 cent, 2 cents, 3 cents, ... , amount of cents

  for coin in denominations:                       # Loop through each coin denomination 1, 5, 10, 25, 50
    for higher_amount in range(coin, amount + 1):  # Loop through each integer from current coin (denomination) to (amount + 1)
      remainder = higher_amount - coin
      ways[higher_amount] += ways[remainder]       # shorthand for ways[higher_amount] = ways[higher_amount] + ways[remainder]
      # print(f'{coin} {ways}')                      # number of ways to get to 0 cents, 1 cent, 2 cents, 3 cents, ... , amount of cents
    
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