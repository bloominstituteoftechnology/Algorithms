#!/usr/bin/python

import argparse

"""
Thoughts on solving this problem:

We can do this using a quicksort-style algorithm. To determine the highest profit, we need to find the largest difference between any two numbers. 
- Set initial index to the first value
- For each following value in the list, compare difference. Store the difference.
- Move the initial index to the next value and repeat until the gratest difference between any two numbers is found.

"""
def find_max_profit(prices):
  # commented out two-loop code
  pass


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))