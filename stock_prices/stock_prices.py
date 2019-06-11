#!/usr/bin/python

import argparse

def find_max_profit(prices):
  
  min_buy = prices[0]
  max_profit = -9999999999
  i, k = 0, 0

  # Loop it
  for i in range(0, len(prices)):

    if prices[i] <= min_buy:
      min_buy = prices[i]

      for k in range(i+1, len(prices)):

        if (prices[k] - min_buy) > max_profit:
          max_profit = prices[k] - min_buy

  return max_profit



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))