#!/usr/bin/python

import argparse

def find_max_profit(prices):
  """ profit = []
  for index in enumerate(prices):
    i = index[0]
    if i < len(prices) - 2:
      for price in prices:
        if prices.index(price) >= index + 1:
          profit.append(price - prices[index])
  profit.sort(reverse = True)
  return profit[0] """

  min_price = prices[0]
  profit = prices[1] - prices[0]
  for i in range(1, len(prices)):
    if prices[i] < min_price:
      min_price = prices[i]
    elif prices[i] - min_price > profit:
      profit = prices[i] - min_price
  return profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))