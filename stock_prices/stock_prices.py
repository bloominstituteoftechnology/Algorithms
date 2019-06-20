#!/usr/bin/python

import argparse

def find_max_profit(prices):
  minPrice = None
  maxProfit = None
  i = 0
  for buyPrice in prices:
    # Looping through all the prices but keeping the buyPrice always 1 index lower than the sell price 
    if minPrice == None:
      minPrice = buyPrice
    if minPrice > buyPrice:
      minPrice = buyPrice
    # I'm using an index based range here to keep the sell price always 1 index higher than the buyPrice
    for i in range(prices.index(buyPrice)+1, len(prices)):
      if maxProfit == None:
        maxProfit = prices[i] - minPrice
      if prices[i] - minPrice > maxProfit:
        maxProfit = prices[i] - minPrice

  return maxProfit
  

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()
  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

  #find_max_profit([10, 7, 5, 8, 11, 9])