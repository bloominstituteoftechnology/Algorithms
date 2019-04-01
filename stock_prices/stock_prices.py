#!/usr/bin/python

import argparse

def find_max_profit(prices):
  maxprof = -10000000000
  for p in range(len(prices)-1):
    for j in range(p+1,len(prices)-1): 
      prof = prices[j] - prices[p]
      if maxprof <= prof:
        maxprof = prof
  return maxprof



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))