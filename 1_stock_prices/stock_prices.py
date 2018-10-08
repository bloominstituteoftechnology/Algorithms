#!/usr/bin/python

import math
import argparse

# References
# https://medium.com/@antash/six-ways-to-find-max-value-of-a-list-in-python-b7d7ccfabc0d


# How can I turn a list into an object?
# How can I iterate over an object?

def find_max_profit(prices):
  max = 0
  prices = [int(x) for x in prices]
  for price in prices:
    if price > max:
      max = price
  return max

# recursive version

# def find_max_profit(prices):
#   if len(prices) == 1:
#     return prices[0]
#   v1 = prices[0]
#   v2 = find_max_profit(prices[1:])
#   if v1 > v2:
#     return v1
#   else:
#     return v2

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))