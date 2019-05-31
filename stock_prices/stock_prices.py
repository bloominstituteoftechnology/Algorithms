#!/usr/bin/python

import argparse

# if x is negative
#       find closest to 0
# if x is positive
#       find farthest from 0
#

def find_max_profit(prices):
  negative_list = []
  positive_list = []
  for index, x in enumerate(prices):
    if index <len(prices) - 1 and x >= prices[index + 1]
  pass


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))