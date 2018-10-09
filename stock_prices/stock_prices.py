#!/usr/bin/python

import argparse

def find_max_profit(prices):
  pass


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()
  high = args.integers[0]
  low = args.integers[0]
  for price in args.integers:
    if price > high:
      high = price 
    elif price < low:
      low = price 
  profit = high - low 
  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=profit, prices=args.integers))