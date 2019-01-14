#!/usr/bin/python

import argparse

def find_max_profit(prices):
  available_buys = prices[:-1]
  cheapest_buy_index = available_buys.index(min(available_buys))
  cheapest_buy = available_buys[cheapest_buy_index]
  available_sells = prices[cheapest_buy_index+1:]
  largest_sell = available_sells[available_sells.index(max(available_sells))]

  return largest_sell - cheapest_buy

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))