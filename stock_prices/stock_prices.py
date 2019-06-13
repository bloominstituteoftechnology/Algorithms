#!/usr/bin/python

import argparse

#recieves and list of amazon stock prices
def find_max_profit(prices):
  #base case
  if len(prices) <= 1:
    return 0
  else: 
  #max profit is computed by subtracting some price by another price that comes before it
    max_profit = prices[len(prices)-1] - prices[len(prices)-2]
    for x in range(1, len(prices)):
      for y in range(x+1, len(prices)):
        profit = prices[y] - prices[x]
        if profit > max_profit:
          max_profit = profit
  return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))