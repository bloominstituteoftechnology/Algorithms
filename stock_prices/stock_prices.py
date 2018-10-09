#!/usr/bin/python

import argparse

def find_max_profit(prices):
  cheapStock = 9999999999999999999999999999999999999999999999
  expensiveStock = 0
  cheapCount = 0
  expensiveCount = 0
  cheapestAtCount = 0
  expensiveAtCount = 0

  for price in prices:
    cheapCount += 1
    print(cheapCount)
    if cheapStock > price:
      cheapStock = price
      cheapestAtCount = cheapCount   
      print([cheapStock, cheapestAtCount])

  for price in prices:
    expensiveCount += 1
    print(expensiveCount)
    if expensiveStock < price:
      expensiveStock = price 
      expensiveAtCount = expensiveCount    
      print([expensiveStock, expensiveAtCount])

  return expensiveStock - cheapStock


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))