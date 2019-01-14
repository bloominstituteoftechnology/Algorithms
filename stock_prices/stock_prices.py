#!/usr/bin/python

import argparse

def find_max_profit(prices):
  ''' 
    define variable for highest in list
    define variable for lowest in list
    loop through list
    put highest number in highest variable
    put lowest in lowest
    loop through range to highest
    if lowest equals num return true
    else remove lowest and recurse
    return highest - lowest
  '''
  pass


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))