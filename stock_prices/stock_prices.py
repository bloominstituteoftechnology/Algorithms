#!/usr/bin/python

import argparse

def find_max_profit(prices):
 import math
def find_max_profit(prices): 
  count = math.inf * -1

  for x in range(0, len(prices)): 
    for y in range(x+1, len(prices)):
        difference = prices[y] - prices[x]
        if count < difference:
          count = difference

  return count
  pass



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))