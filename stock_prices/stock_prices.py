#!/usr/bin/python

import argparse

def find_max_profit(prices):
  min_price = prices[0]
  max_price = prices[1]
  profit = 0
  max_profit = 0
  if len(prices) < 2:
    return max_price - min_price

  max_profit = max_price - min_price

  print(f"Max profit {max_profit}")

  for i in range(1, len(prices)-1):
    profit = prices[i] - min_price
    print(prices[i])
    if profit > max_profit:
      max_profit = profit
    # elif profit < max_profit:
    if prices[i] <= min_price:
      min_price = prices[i]
    # if prices[i] > max_price:
    #   max_price = prices[i]

  return max_profit

print(find_max_profit([100, 90, 80, 50, 20, 10]))
# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()
#
#   prices = args.integers
#   profit = find_max_profit(args.integers)
#
#
#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
