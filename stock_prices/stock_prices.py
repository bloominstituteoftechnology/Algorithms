#!/usr/bin/python
"""
bot buys and sells amazon stocks
function find_max_profit (prices)
    prices = []

return max_profit from a single buy and sell
order of trade: buy first before selling

find_max_profit([1050, 270, 1540, 3800, 2]) should return 3530

diff btw smallest and largest prices
max_profit = some price - another price that comes before it

current_min_price_so_far = 
max_profit_so_far = 

Algorithm
profit = []
iterate through stock prices
keep track of lowest price
subtract lowest price from current item(i)
append result of subttaction to profit list
find the maximum profit using max() method


"""

import argparse

def find_max_profit(prices):
  profit = []
  for i in range (0, len(prices)):
    for j in range (i + 1, len(prices)):
        price_diff = prices[j] - prices[i]
        profit.append(price_diff)

  return max(profit) 




if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))