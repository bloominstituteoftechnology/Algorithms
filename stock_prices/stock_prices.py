#!/usr/bin/python

import argparse
import math

def find_max_profit(prices):
  max_px = 0
  min_px = prices[0]
  for px in prices[1:]:
    min_px = min(min_px, px)
    max_px = max(px - min_px, max_px)
  return max_px




if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))