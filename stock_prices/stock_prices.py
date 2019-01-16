#!/usr/bin/python
import math
import argparse


def find_max_profit(prices):
  maxNum = float("-inf")
  if len(prices) == 0:
    return 0
  while len(prices) >= 2:
    first = prices[0]
    big = max(prices[1:])
    if big - first > maxNum:
        maxNum = big - first
    prices = prices[1:]
  return maxNum


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))