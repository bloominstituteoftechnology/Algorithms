#!/usr/bin/python

import argparse

def find_max_profit(prices):
    if len(prices) > 2:
        largest = max(prices[1:])
        diff = largest - prices[0]
        return max(diff, find_max_profit(prices[1:]))
    else:
        return prices[1] - prices[0]


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
