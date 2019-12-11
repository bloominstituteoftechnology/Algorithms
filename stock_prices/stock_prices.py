#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_diff = None
  for i in range(len(prices) - 1):
    for j in range(i + 1, len(prices)):
      diff = prices[j] - prices[i]
      if not max_diff:
        max_diff = diff
      elif max_diff < diff:
        max_diff = diff
  return max_diff


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))