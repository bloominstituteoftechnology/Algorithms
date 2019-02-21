#!/usr/bin/python

import argparse

def find_max_profit(prices):
  """
  Finds the max profit in a list of buy / sell points

  NOTE: The last price point is never going to be the buy point as it would indicate no profit every time
  because there is no sell point after the buy point, therefore we ignore the last point for a potential buy

  This function finds the cheapest possible buy and the largest sell point (which is only available after the buy)
  and returns the largest sell point minus the cheapest available buy point
  """
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