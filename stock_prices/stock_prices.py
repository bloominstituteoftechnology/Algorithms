#!/usr/bin/python

import argparse

def find_max_profit(prices):
   # keep track of the min price we've seen (this has to come before the max in our list of prices)
   # keep track of the max profit we've seen so far
   # iterate through our prices list and update these two variables
   # return our max profit we've seen so far
   min_price = prices[0]
   max_profit = prices[1] - min_price

   for i in range(1, len(prices)):
     price = prices[i]
     max_profit = max(price - min_price, max_profit)
     min_price = min(price, min_price)
  
   return max_profit

max_price = max(prices)
  lowest_price = min(prices)
  prices_and_indexs = [[price, prices.index(price)] for price in prices]
  for price_and_index in prices_and_indexs:
    for price in prices:
      if max_price == price and price_and_index[1] < prices.index(price):
        #print(price_and_index[1], prices.index(price))
        return price - lowest_price

        else:
      prices.remove(max_price)
      new_max_price = max(prices)
      return new_max_price - max_price


if __name__ == '__main__':
  # This is just some code to input accepting inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))