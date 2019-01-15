#!/usr/bin/python

import argparse

# max profit variable start at inital index and compare 
# min price make it index independent
import math 
def find_max_profit(prices):
  max_profit = -math.inf
  min_price = math.inf
  for price in prices:
    max_profit = max(price - min_price, max_profit) # 0 0 1270 3530 3530
    min_price = min(price, min_price) #1050 270 270 270 2
  return max_profit


print(find_max_profit([1050, 270, 1540, 3800, 2]))
# current is 1050
# maxProfit = max(current - min_price, maxProfit)

print(find_max_profit([33, 350, 120, 600, 460]))
find_max_profit([100, 90, 80, 50, 20, 10]) # -10




if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))