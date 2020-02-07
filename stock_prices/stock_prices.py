#!/usr/bin/python

import argparse

def find_max_profit(prices):
  if len(prices) < 2:
    return 0
  
  # set intial lowest and maxProfit values from array values
  lowest =  prices[0]
  maxProfit = prices[1] - prices[0]

  # for each item in prices
  for i in range(1, len(prices)):
    price = prices[i]
    # each new item, find out the difference from the current item and the lowest prev price 
    profitFromTrade = price - lowest
    # track the lowest price
    lowest = min(lowest, price)
    # save the max, positive difference
    maxProfit = max(profitFromTrade, maxProfit)
  # return max when finished 
  return maxProfit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))