#!/usr/bin/python

import argparse

print('westisde')

def find_max_profit(prices):
  pass


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))





  # Lambda Problem Solving Framework

  # UPER

  # U - UNDERSTAND
  # P - PLAN
  # E - EXECUTE
  # R - REFLECT

  # UNDERSTAND
  #   PROBLEM ---
  #   GET LIST OF NUMBERS EX: 4, 34, 6, 5, 574, 4
  #   the max profit is computed by subtracting some price by another
  #   price that comes before it; it can't come after it in the list of prices.

  #   GOAL
  #     GOING THRU LIST LEFT TO RIGHT, BUY AT LOW NUMBER, SELL AT HIGH NUMBER
  #     find the maximum difference between the smallest and largest prices
  #
  #
  #
  #
  #   EXPECTED RESULTS:
  #
  #     INPUT - [4, 5, 100, 10]
  #     OUTPUT - 95
  #
  #     INPUT - [90, 5, 1, 100]
  #     OUTPUT - 99

  #     INPUT - [3, 10, 5, 10]
  #     OUTPUT - 7

  #   REFLECT
  #     IS THIS EFFICIENT
  #