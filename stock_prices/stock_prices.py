#!/usr/bin/python

import argparse

def find_max_profit(prices):
  maxProfit = 0
  for index, price in enumerate(prices):
    ##for all indexes after the current index, if the 2nd index value is larger, get the difference between the two
      for index, nextPrice in enumerate(prices):
        if nextPrice > price:
          profit = nextPrice - price:

      ##if the difference is bigger than the current maxProfit, update the maxProfit to that number.



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))