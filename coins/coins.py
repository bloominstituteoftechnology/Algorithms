#!/usr/bin/python

import sys

def coin_denominations(amount, denominations):
  ways = [0] * (amount + 1)
  ways[0] = 1

  for coin in denominations:
    for higher_amount in range(coin, amount + 1):
      remainder = higher_amount - coin
      ways[higher_amount] += ways[remainder]

  return ways[amount]


if __name__ == "__main__":