#!/usr/bin/python

import argparse
import math

def find_max_profit(prices):
  ''' 
    [x] define variable for highest in list
    [x] define variable for lowest in list
    [x] loop through list
    [x] put highest number in highest variable
    [x] put lowest in lowest
    [x] loop through range to highest
    [] if lowest equals num return true
    [] else remove lowest and recurse
    [] return highest - lowest
  '''

  difference = -math.inf

  for i, stock in enumerate(prices):
      for j, stock2 in enumerate(prices):
          if j > i:
              if stock2 - stock > difference:
                  difference = stock2 - stock
            
            
  return difference


find_max_profit([100, 90, 80, 50, 20, 10])

find_max_profit([1050, 270, 1540, 3800, 2])


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))