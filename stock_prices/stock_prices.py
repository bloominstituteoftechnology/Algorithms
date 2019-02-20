#!/usr/bin/python

import argparse

def find_max_profit(prices):
  """
  iterate through list
  compare difference between them
  return highest difference
  """
  max_profit = -(prices[0] - prices[1])
  for index, price in enumerate(prices):
    for second_price in prices[index + 1:]:
      profit = -(price - second_price)
      if profit > max_profit:
        max_profit = profit
  return max_profit



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))