#!/usr/bin/python

import argparse

def find_max_profit(prices):
  if len(prices) <= 1:
    return 0

  max_price = prices[0]
  min_price = prices[0]

  for i, price in enumerate(prices):
    if price < min_price:
      max_price = 0
      min_price = price
    elif price > max_price:
      max_price = price
    print(f"Max{max_price}")
    print(f"Min{min_price}\n")

  return max_price - min_price

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))