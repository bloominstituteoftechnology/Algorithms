#!/usr/bin/python

import argparse

#  0 - 100 + 90 = p
def find_max_profit(prices):
  pass

  # I honestly don't know what to do
  # Not sure how to approach or even
  # solve the problem to begin with so transcribing
  # the problem into code, I just don't understand





if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))