#!/usr/bin/python

import argparse

def find_max_profit(prices):
  pass


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))


# NOTES
# 1 Understanding
  # given an array of prices in chronological order, this function
  # should return the largest increase possible between two indexes
  # moving from left to right

# 2 Sketch
  # what will this function do if passed the improper format method?
  # is that something we need to be concerned with?

# 3 come up with first plan

# 4 Think of how to improve

# 5 Implement improved solution