#!/usr/bin/python

import argparse

def find_max_profit(prices):
  low = prices[0]
  high = prices[0]
  max_profit = 0
  for i in range(0, len(prices) - 1):
    if prices[i] < low:
      low = prices[i]
      if i == 1 and high > low:
        max_profit = low - high
    elif prices[i] - low > max_profit:
        high = prices[i]
        max_profit = high - low
  return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))