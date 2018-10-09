#!/usr/bin/python

import argparse

def find_max_profit(prices):
  largest = -100
  for i, first_el in enumerate(prices):
    for j, second_el in enumerate(prices):
      if j > i and second_el - first_el > largest:
        largest = second_el - first_el
  return largest


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))