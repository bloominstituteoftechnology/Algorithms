#!/usr/bin/python

import argparse
from math import inf

def find_max_profit(prices):
  min_price = inf
  max_profit = -inf
  for price in prices:
    profit = price - min_price
    if profit > max_profit:
      max_profit = profit
    if price < min_price:
      min_price = price
  return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))