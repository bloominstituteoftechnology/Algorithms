#!/usr/bin/python

import argparse

def find_max_profit(prices):
  profit = 0
  min = prices[0]
  for i in prices:
    val = i
    print(f'val: {val}')
    if val < min:
      min = val
      if val == prices[len(prices)-1] and profit == 0:
        profit = profit - min
    elif val > min and profit < val - min:
      profit = val - min
    print(f'min: {min}')
    print(f'profit: {profit}')
  return profit 

# def find_max_profit(prices):
#   min_price = prices[0]
#   max_profit = prices[1] - min_price

#   for i in range(1, len(prices)):
#     price = prices[i]
#     max_profit = max(price - min_price, max_profit)
#     min_price = min(price, min_price)

#   return max_profit
  
# find_max_profit([1050, 270, 1540, 3800, 2])

# def find_max_profit(prices):
#     # max profit variable start at initial index and compare
#     # min price make it index independent
#     max_profit = -math.inf
#     min_price = math.inf
#     for price in prices:
#         max_profit = max(price - min_price, max_profit) # -inf, -780, 1270, 3530, 3530
#         min_price = min(price, min_price) # 1050, 270...
#     return max_profit

# find_max_profit([1050, 270, 1540, 3800, 2])
# find_max_profit([100, 90, 80, 50, 20, 10])

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))