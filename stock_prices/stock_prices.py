#!/usr/bin/python

import argparse

def find_max_profit(prices):
  pass
  maxPrice = 1
  minPrice = 0
  for i in range (0, len(prices)):
        for j in range(0, i):
            if (prices[i]-prices[j])>(prices[maxPrice]-prices[minPrice]):
                maxPrice=i
                minPrice=j
  return prices[maxPrice]-prices[minPrice]


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))