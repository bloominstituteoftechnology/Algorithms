#!/usr/bin/python

import argparse

def find_max_profit(prices):
  current_price = prices[0]
  profit = prices[1] - prices[0]

  # loop over prices starting at the second item in the list
  for price in prices[1:]:
    # if price - current_price is greater than profit
    # set profit to price - current_price
    if (price - current_price) > profit:
      profit = price - current_price
    # if the price is less than the current_price 
    # set current_price equal to the next price
    if price < current_price:
      current_price = price
    

  return profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))