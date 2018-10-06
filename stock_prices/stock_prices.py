#!/usr/bin/python

import argparse

prices = [1050, 270, 1540, 3800, 2]


def find_max_profit(prices):
    biggestProfit = 0
    
    for i in range(len(prices)):
        if i == len(prices) - 1:
            return biggestProfit
        for j in range(len(prices)): 
            if i + j > len(prices) - 1:
                biggestProfit
            elif prices[i+j] - prices[i] > biggestProfit:
                biggestProfit = prices[i+j] - prices[i]
            elif biggestProfit == 0 and prices[i+j] - prices[i] < 0:
                biggestProfit = prices[i+j] - prices[i]
            else:
                biggestProfit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))