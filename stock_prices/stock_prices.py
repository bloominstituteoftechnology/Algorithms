#!/usr/bin/python

import argparse
import math

def find_max_profit(prices):
  result = math.inf * -1
  for buy in range(0, len(prices)):
    for sell in range(buy + 1, len(prices)):
      difference = prices[sell] - prices[buy]
      if difference > result:
        result = difference
  return result


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))