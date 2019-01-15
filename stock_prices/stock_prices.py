#!/usr/bin/python

import argparse

def find_max_profit(prices):
  maxProfit = 0
  for price in range(0,len(prices)):
    for nextPrice in range(prices[price+1],len(prices))
      if price < nextPrice:
        profit = nextPrice - price
        if profit > maxProfit:
          maxProfit = profit
        ##if the difference is bigger than the current maxProfit, update the maxProfit to that number.
  return maxProfit

find_max_profit([1050, 270, 1540, 3800, 2])



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))