#!/usr/bin/python

import argparse

def find_max_profit(prices):
  profit = prices[1] - prices[0]
  cost = prices[0]

  #for each price starting at the second item in the list
  for price in prices[1:]:
    # if the price - the cost is greater than profit set profit equal to price minus cost
    if (price - cost) > profit:
      profit = price - cost
    # if the price is less than the cost set cost equal to the new price
    if price < cost:
      cost = price
    

  return profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))