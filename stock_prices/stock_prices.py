#!/usr/bin/python

import argparse

# max profit variable start at inital index and compare 
# min price make it index independent
import math 
def find_max_profit(prices):
  max_profit = -math.inf # or float("-inf")
  min_price = math.inf
  for price in prices:
    print(f'This is the old max profit {max_profit}')
    max_profit = max(price - min_price, max_profit) # 0 0 1270 3530 3530
    print(f'This is the next max profit if I buy it at this price {price - min_price}')
    min_price = min(price, min_price) #1050 270 270 270 2
  return max_profit

# when you buy at first value and sell at the others
# def find_max_profit(prices):
#   bought = prices[0]
#   max_profit = -9999999

#   for p in prices[1:]:
#     profit = p - bought
#     if profit > max_profit:
#       max_profit = profit
  
#   print(max_profit)


# naive solution
# def find_max_profit(prices):
#   max_profit = float("-inf")
#   while prices != []:
#     bought = prices[0]
#     for p in prices[1:]:
#       profit = p - bought
#       if profit > max_profit:
#         max_profit = profit
#     prices = prices[1:] # or prices.pop(0)

#   print(max_profit)

# def find_max_profit(prices):
#   min_buy_price = prices[0]
#   max_profit = prices[1] - min_buy_price

#     for p in prices[1:]:
#       profit = p - min_buy_price
#       max_profit = max(profit, max_profit)
#       # if profit > max_profit:
#       #   max_profit = profit
#       min_buy_price = min(p, min_buy_price)
#       # if p < min_buy_price:
#       #   min_buy_price = p
#     prices = prices[1:] 

#   print(max_profit)
# for loop iterate everything after first index 
# min_buy_price is the first index
# look for a number lower than min_buy_price and subtract each index from it to see max profit

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