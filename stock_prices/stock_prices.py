#!/usr/bin/python

import argparse
"""
Problem:
Find the maximum profits in a stock price pick

Understand the problem:
----------------------
You can sell only in future
you can not reverse back in transcation (can't go back in time)
integers only
you want to maximize the profits

anlayze:
--------
"""

def find_max_profit(prices):
  #profit
  max_value = 0
  max_value_location = 0
  min_value = 1e1000
  # get the max value even the last element matters
  for i in range(1, len(prices)):
    if prices[i] > max_value:
      max_value = prices[i]
      max_value_location = i   
  # get the min value when buying the stock
  # the last element wouldn't matter because we wouldn't be able to sell it
  for j in range(0, max_value_location):
    if min_value > prices[j]:
      min_value = prices[j] 
  return max_value-min_value

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))