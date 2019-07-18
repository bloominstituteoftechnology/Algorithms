#!/usr/bin/python

import argparse

def find_max_profit(prices):
    max = 0
    length = len(prices)
    for i in range(1, length):
      for j in range(i + 1, length):
        p = prices[j] - prices[i]
        if not max:
          max = p
        elif max < p:
          max = p
    return max


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
