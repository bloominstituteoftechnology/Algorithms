#!/usr/bin/python

import argparse

def find_max_profit(prices):
  """
  Find the maximum profit from a list of stock prices.
  Iterate left to right to find maximum difference from a series of l-r iterations.
  """
  # base case is we buy first period and sell second period
  profit = prices[1] - prices[0]
  # print(prices)

  for price in prices[:-1]:
    # iterate from 1 to the n-1 element (we have no shorting 
    # so we can only sell on the last element)
    # print(f'price {price}')

    for sell in prices[prices.index(price)+1:]:
      # iterate to end of prices
      # print(f'sell {sell}')
      # print(f'global profit: {profit}, temp profit {sell - price}')
      if (sell - price) > profit:
        profit = sell - price
  
  return profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))