#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_profit = 0
  stored_value = prices[0]
  max_profit = prices[1]-prices[0]
  index = 2
  while True:
    if index > len(prices):
      break
    for price in prices[index-1:]:
      if price - stored_value > max_profit:
        max_profit = price - stored_value
    stored_value=prices[index-1]
    index += 1
  return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))