#!/usr/bin/python

import sys

def find_max_profit(prices):
  min_price = prices[0]
  max_profit = prices[1] - min_price

  for price in prices:
    max_profit = max(price - min_price, max_profit)
    min_price = min(price, min_price)

  return max_profit


if __name__ == "__main__":
  if len(sys.argv) > 1:
    prices = sys.argv[1]
    print("Max profit for the given list of prices is {profit}.".format(profit=find_max_profit(prices)))
  else:
    print("Usage: stock_prices.py [prices]")