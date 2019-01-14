#!/usr/bin/python

import argparse

def find_max_profit(prices):
  L1 = prices[:-1]
  L2 = prices[0:]

  buy = min(L1)
  sell = max(L2)

  profit = sell-buy

  return profit



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))