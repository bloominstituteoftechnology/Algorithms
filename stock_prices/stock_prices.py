#!/usr/bin/python

import argparse

def find_max_profit(prices):
  #  set initial values
  smallestPrice = prices[0]
  largestProfit = prices[1] - smallestPrice

  # iterate through the prices to find the largestProfit
  for index in range(1, len(prices)):
    eachPrice = prices[index]
    largestProfit = max(eachPrice - smallestPrice, largestProfit)
    smallestPrice = min(eachPrice, smallestPrice)


  # return `largestProfit` after exiting the loop
  return largestProfit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))