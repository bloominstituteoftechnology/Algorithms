#!/usr/bin/python

import argparse

def find_max_profit(prices):

  
  min_price = prices[0]
  max_profit = prices[1] - min_price
  
  for i in range(len(prices)):
    for j in range(1 + i, len(prices)):
      if prices[j] - prices[i] > max_profit:
        max_profit = prices[j] - prices[i]
  print(max_profit)
  return max_profit

  
find_max_profit([10, 7, 5, 8, 11, 9])

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))