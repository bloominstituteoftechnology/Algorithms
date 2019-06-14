#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_profit = prices[1]-prices[0]
  for x in range(len(prices)-1):
    for y in range(x+1, len(prices)):
      if prices[y] - prices[x] > max_profit:
        max_profit = prices[y] - prices[x]
  return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))