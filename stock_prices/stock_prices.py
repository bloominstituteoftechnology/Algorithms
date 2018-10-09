#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_profit = 0
  for i, buy_price in enumerate(prices):
    for j, sell_price in enumerate(prices):
      if i == 0 and j == 1:
        max_profit = sell_price - buy_price
      elif j > i and sell_price - buy_price > max_profit:
        max_profit = sell_price - buy_price
  return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))