#!/usr/bin/python

import argparse
import math

def find_max_profit(prices):

  max_profit = float("-inf")

  while prices != []:
    bought = prices[0]
  
    for price in prices[1:]:
      profit = price - bought
      if profit > max_profit:
        max_profit = profit
    prices.pop(0)

  print(max_profit)

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))