#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_profit_so_far = 0

  for i in range(0, len(prices)):
    cur_min_price = i
    for j in range(i+1, len(prices)):
      profit = prices[j] - prices[i]
      if max_profit_so_far == 0:
        max_profit_so_far = profit
      elif profit > max_profit_so_far:
          profit, max_profit_so_far = max_profit_so_far, profit
  return max_profit_so_far

print(find_max_profit([1050, 270, 1540, 3800, 2]))