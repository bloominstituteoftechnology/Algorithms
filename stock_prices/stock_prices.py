#!/usr/bin/python

import argparse

def find_max_profit(prices):
  curr_max = prices[1] - prices[0]
  for j in range(len(prices)-1):
    for i in range(1, len(prices)-1):
      if (i > j):
        if (curr_max < prices[i] - prices[j]):
          curr_max = prices[i] - prices[j] 
  return curr_max


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))