#!/usr/bin/python

import argparse

def find_max_profit(prices):
  cache = []
  for index, price in enumerate(prices):
    current_list = prices[index:]
    if len(current_list) > 1:
      subtrahend = current_list[0]
      for minuend in current_list[1:]:
        cache.append(minuend - subtrahend)
  return max(cache)


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))