#!/usr/bin/python

import argparse

'''
finding max profits by buying first and selling later
takes in a list of numbers representing prices
the max profit is going to be max_price - low_price

if I step through the array keeping track of the lowest price I find
and subtracting it from the max price then keep track of which max prices
are the largest I should get the max profit possible


'''


def find_max_profit(prices):
  pass


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))