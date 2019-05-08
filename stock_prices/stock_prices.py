#!/usr/bin/python

import argparse

def find_max_profit(prices):
    #input: list of prices
    #output: max profit from single buy/sell
    #must buy, then sell
    #subtract x from y, with y coming before x in the list
    #edge cases:
        #empty array: 0
        #single item: -n (have to buy first, so no profit, only loss of purchase price)
        #2 items: return prices[1] - prices[0]
  pass


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))