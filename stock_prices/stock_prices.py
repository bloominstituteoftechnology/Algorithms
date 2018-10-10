#!/usr/bin/python

import argparse


# def find_max_profit(prices):
#     while True and len(prices) > 1:
#         max1 = max(prices)
#         min1 = min(prices)
#         if prices.index(min1) < prices.index(max1):
#             return max1-min1
#         else:
#             prices.remove(min1)
#     return 0 
def find_max_profit(prices):
  n = len(prices)
  lowest = prices[0]
  highest = prices[1] - prices[0]

  for i in range(1,n,1):
    highest = max(highest, prices[i] - lowest)

    lowest = min(lowest, prices[i])
    
  return highest 


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
