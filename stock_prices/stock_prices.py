#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_profit = 0
  for i in range(len(prices)-1, 1, -1):
    for j in range(0,i):
      profit = prices[i] - prices[j]
      if profit > max_profit:
        max_profit = profit
  return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))