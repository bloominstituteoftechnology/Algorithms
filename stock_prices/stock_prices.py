#!/usr/bin/python

"""
input --> list of stock prices
output -->  max-profit = single buy, single sell (but first buying before selling)

For example, `find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530, which is the maximum profit that can be made from a single buy and then sell of these stock prices. 

We get this by subtracting 3800 - 270  = 3530


HINTS:
maximum difference between smallest and largest prices

we also have to make sure that the max profit is computed by subtracting some price by another price that comes _before_ it; it can't come after it in the list of prices. 

Because you bought at 3800 and sold at 2

What matters is if you buy a stock at i of 1, you can only sell it at i > 1


"""

import argparse




def find_max_profit(prices):
    # find the max number and isolate it
    # max_num = sort(prices)


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

find_max_profit([1050, 270, 1540, 3800, 2])