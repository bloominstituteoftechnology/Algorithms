#!/usr/bin/python
"""
UNDERSTANDING THE PROBLEM:
Given a list of numbers, check which is the highest in the list, store the index,
and based on that check from the first index to that index for the lowest value and store the index in a variable as well
Then, you want to subtract the highest by the lowest and return the result of that operation
"""

import argparse

def find_max_profit(prices):
  #
  pass


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))