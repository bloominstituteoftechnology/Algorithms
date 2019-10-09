#!/usr/bin/python

import argparse

def find_max_profit(prices):
  maxPrice = max(prices)
  maxPriceIndex = prices.index(maxPrice)
  profits =[]
  for i in prices:
    if(maxPriceIndex < prices.index(i)):
      profits.append(i - maxPrice)
    else:
      profits.append(maxPrice - i)
  profits.remove(profits[maxPriceIndex])
  print(profits)
  maxProfit= max(profits)
  return maxProfit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))