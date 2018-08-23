#!/usr/bin/python

def find_max_profit(prices):
  min_price = prices[0]
  max_profit = prices[1] - min_price

  for price in prices:
    max_profit = max(price - min_price, max_profit)
    min_price = min(price, min_price)

  return max_profit
