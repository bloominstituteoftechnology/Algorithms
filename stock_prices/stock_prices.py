#!/usr/bin/python

import argparse

def find_max_profit(prices):
  min_price = prices[0]
  max_price = prices[1]
  profit = None
  if len(prices) < 2:
    return max_price - min_price

  profit = max_price - min_price

  for i in range(1, prices-1)
  pass


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
