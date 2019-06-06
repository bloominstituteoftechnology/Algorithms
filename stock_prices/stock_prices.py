#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_p = None
  for i in range(len(prices) - 1):
    for j in range(i + 1, len(prices)):
      prof = prices[j] - prices[i]
      if not max_p:
        max_p = prof
      elif max_p < prof:
        max_p = prof
  return max_p


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))