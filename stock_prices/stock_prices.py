#!/usr/bin/python

import argparse

def find_max_profit(prices):

  largest_index = 0
  smallest_index = 0
  j = 0
  
  for i in prices:
    if prices[i] > prices[largest_index]:
      largest_index == i

  while j < largest_index:
    if prices[j] < prices[0]:
      smallest_index == j
      j += 1

  
  return prices[largest_index] - prices[smallest_index]

  pass


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))