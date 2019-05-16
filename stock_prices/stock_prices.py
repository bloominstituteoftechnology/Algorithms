#!/usr/bin/python

import argparse

def find_max_profit(prices):
  maxProf = float("-inf")
  for i in range(0, len(prices)-1):
    for j in range(i+1, len(prices)-1):
      diff = prices[j] - prices[i]
      if diff > maxProf:
        maxProf = diff
  return maxProf


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))