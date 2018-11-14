#!/usr/bin/python

import argparse

def find_max_profit(prices):
  left = 9999999999
  right = 0
  max = []
  for price in prices:
    if price > right:
      right = price
    else:
      max.append(right - left)
      right = price
      left = price
  true_max = 0
  for price in max:
    if price > true_max:
      true_max = price
  return true_max
    


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))