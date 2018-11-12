#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max = prices[1]-prices[0]
  # print ('max:', max)
  for index_buy in range(len(prices)):
    # print ('price[index: ]', prices[index_buy:])
    for sold in prices[index_buy+1:]:
      if sold-prices[index_buy] > max:
        max = sold-prices[index_buy]
  return max

# print ( find_max_profit([10, 7, 5, 8, 11, 9]) )
# print (find_max_profit([100, 90, 80, 50, 20, 10]))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))