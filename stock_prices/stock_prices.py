#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # keep track of the min price we've seen (this has to come before the max in our list of prices)
  # keep track of the max profit we've seen so far
  # iterate through our prices list and update these two variables
  # return our max profit we've seen so far
  #  min_price = prices[0]
  #  max_profit = prices[1] - min_price

  #  for i in range(1, len(prices)):
  #    price = prices[i]
  #    max_profit = max(price - min_price, max_profit)
  #    min_price = min(price, min_price)
  
  #  return max_profit
  max_price = max(prices)
  min_price = min(prices)
  max_price_index = prices.index(max_price)
  min_price_index = prices.index(min_price)

  if min_price_index > max_price_index and prices.index(max_price) != 0:
    new_list = list(prices[:prices.index(max_price)])
    new_lowest_price = min(new_list)
    return max_price - new_lowest_price
  
  # while prices.index(max_price) == 0:
  #   prices.pop(0)
  #   max_price = max(prices)
  #   min_price = min(prices)
  #   if len(prices) == 2:
  #     return min_price - max_price

  # return max_price - min_price
  # def rec(index):
  #   if (prices.index(max_price) == 0):
  #     prices.pop(index)
  #     max_price = max(prices)
  #     min_price = min(prices)
  #     print('asdf')
  #     if len(prices) == 2:
  #       return min_price - max_price
  #   return rec(0)

  return max_price - min_price

      
      

if __name__ == '__main__':
  # This is just some code to input accepting inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))