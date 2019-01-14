#!/usr/bin/python

import argparse

def find_max_profit(prices):
  """
  what do i need to do in this problem?  I need to compare the difference between each argument and the arguments that follow.  I need to return the largest positive value

  iterate over the list
  compare a & b, looking for a < b
  save all the positives in a list
  sort the list
  return last item in the list
  """
  pass


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))