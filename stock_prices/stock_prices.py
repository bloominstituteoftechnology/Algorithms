#!/usr/bin/python

import argparse

def find_max_profit(prices):
  largest = 0
  smallest = 0
  iteration = 0
  for price in prices:
    if price > largest:
      largest = price
  for price in prices:
    if iteration == 0:
      smallest = price
      iteration += 1
    elif price < smallest:
      smallest = price
  return largest - smallest


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))