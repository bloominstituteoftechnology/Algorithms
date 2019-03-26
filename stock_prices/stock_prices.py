#!/usr/bin/python

import argparse

def find_max_profit(prices):
  maximum_profit = float('-inf')

  for (i, buying_price) in enumerate(prices[:len(prices)-1]):
  #compare elements to each other except the last one
    for selling_price in prices[i+1:]:
      profit = float(selling_price - buying_price)
      if profit > maximum_profit:
        maximum_profit = profit

  return maximum_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))