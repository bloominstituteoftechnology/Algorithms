#!/usr/bin/python

import argparse

def find_max_profit(prices):
  
  max = prices[0]
  min = prices[0]
  profit = prices[1] - prices[0]


  for price in prices:
    if price < min:
      min = price
      max = price
    if price > max:
      max = price
      if profit < max - min:
        profit = max - min

  return profit;

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))