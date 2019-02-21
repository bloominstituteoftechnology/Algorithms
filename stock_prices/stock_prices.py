#!/usr/bin/python

import argparse
#  Your function should return the maximum profit that can be made from a single
#  buy and sell.

# For this problem, we essentially want to find the difference between the 
# smallest and largest prices in the list of prices.

def find_max_profit(prices):
  max_profit = 0

# goes through and looks at each number as a buying price and a selling price
  for i_buy in range(len(prices) - 1): 
    price_buy = prices[i_buy]
    i_sell = i_buy + 1
    
# defines all possible profit number from all comparisons, but will only return 
# the profit that is higher than the rest
    for price_sell in prices[i_sell:]:
      profit = price_sell - price_buy
      
      if max_profit == 0 or profit > max_profit:
        max_profit = profit

  print (f'{max_profit}')
  return max_profit


find_max_profit([1050, 270, 1540, 3800, 2])
if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))