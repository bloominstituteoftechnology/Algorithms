#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # Store the highest and lowest prices from our array
  high = 0
  low = 0
  # Search are array for the Highest Price
  for i in range(0 , len(prices)):
    if prices[i] > high:
      high = prices[i]
      low = prices[i]
  # Store the high and eliminate any remaining elements past them in the array
  high_i = prices.index(high)-1
  # find the lowest number in the remaining array
  for i in range(0, high_i):
    if  prices[i] < low:
      low = prices[i]
  # return the high minus this number
  return high - low



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))