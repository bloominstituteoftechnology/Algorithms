#!/usr/bin/python

import argparse

def find_max_profit(prices):

  max_profit = None

  for index_buy in range(len(prices) - 1):
    price_buy = prices[index_buy]
    index_sell = index_buy + 1

    for price_sell in prices[index_sell:]:
      profit = price_sell - price_buy

      if max_profit == None or profit > max_profit:
        max_profit = profit
  
  return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
