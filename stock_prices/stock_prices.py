#!/usr/bin/python

import argparse
import math

def find_max_profit(prices):
  # highest = -max(prices)
  highest = float("-inf")
  for i, c in enumerate(prices[:-1]):
    if max(prices[i+1:]) - c >= highest:
      highest = max(prices[i+1:]) - c
  print(highest)
  return highest

# [10, 7, 5, 8, 11, 9]

  

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))