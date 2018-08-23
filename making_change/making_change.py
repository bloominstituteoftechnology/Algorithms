#!/usr/bin/python

import sys

def coin_denominations(amount, denominations):
  if amount == 0:
    return 1
  if amount < 0:
    return 0
  if len(denominations) <= 0 and amount > 0:
    return 0
  else:
    return coin_denominations(amount - denominations[-1], denominations) + coin_denominations(amount, denominations[:-1])


# def coin_denominations(amount, denominations):
#   ways = [0] * (amount + 1)
#   ways[0] = 1

#   for coin in denominations:
#     for higher_amount in range(coin, amount + 1):
#       remainder = higher_amount - coin
#       ways[higher_amount] += ways[remainder]

#   return ways[amount]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 100]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=coin_denominations(amount, denominations), amount=amount))
  else:
    print("Usage: coins.py [amount]")