#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_profit = 0
  for i, price in enumerate(prices):
    for j in range (i + 1, len(prices)):
      current_profit = prices[j] - price
      if max_profit == 0 or current_profit > max_profit:
          max_profit = current_profit
  return max_profit
 

print(find_max_profit([100, 450, 2500, 56, 7]))
  



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))