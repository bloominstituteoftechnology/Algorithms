#!/usr/bin/python

import argparse


def find_max_profit(prices):
    min_price = prices[0]
    max_profit = prices[1] - min_price

    for i in range(1, len(prices)):
        price = prices[i]
        max_profit = max(price - min_price, max_profit)
        min_price = min(price, min_price)

    return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
