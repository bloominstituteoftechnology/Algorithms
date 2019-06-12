#!/usr/bin/python

import argparse

def find_max_profit(prices):
  pass
  maxPrice = 0
  minPrice = 0
  count = 1
  while count < 2:
    for i in range(0, len(prices) -1):
      if prices[i] < prices[minPrice] :
        minPrice = i 
      if prices[i] > prices[maxPrice] and i>maxPrice :
        maxPrice = i
    count +=1
  return prices[maxPrice] - prices[minPrice]


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))