#!/usr/bin/python

import argparse

def find_max_profit(prices):
  maxProfit = 0
  assigned = False
  for bp in range(0,len(prices)):
    if(bp < len(prices)-1):
      for sp in range(bp+1,len(prices)):
        profit = -prices[bp]+prices[sp]
        if profit > maxProfit or assigned == False:
          maxProfit = profit
          assigned = True
  return maxProfit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))