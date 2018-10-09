#!/usr/bin/python

import argparse
import math

def find_max_profit(prices):
  maxVal = prices[0]
  minVal = prices[0]

  for i in range(0, len(prices), 1)
    maxVal = prices[0]
    minVal = prices[0]
    profit = None

  for i in range(0, len(prices)):
    max_value = max(maxVal, prices[i])
    min_value = min(minVal, prices[i])
    profit = max_value - min_value
  
  return profit




if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))