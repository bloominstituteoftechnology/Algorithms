#!/usr/bin/python

import argparse

def find_max_profit(prices):
  min_price = min(prices[0], prices[1])
  profit = prices[1] - prices[0]

  if len(prices) > 2:
    for i in range(2, len(prices)):
      if prices[i] - min_price > profit:
        profit = prices[i] - min_price
      if prices[i] < min_price:
        min_price = prices[i]
  return profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()








  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))