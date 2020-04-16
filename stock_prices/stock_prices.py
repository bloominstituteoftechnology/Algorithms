#!/usr/bin/python

import argparse

def find_max_profit(prices):
  cur_min = prices[0]
  cur_max_profit = prices[1] - prices[0]
  for i, x in enumerate(prices[:-1]):
    if cur_min > x:
      cur_min = x
      for y in prices[i+1:]:
        profit = y - cur_min
        if profit > cur_max_profit:
          cur_max_profit = profit
  return cur_max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))