#!/usr/bin/python

import argparse

def find_max_profit(prices):
  smallest = 0
  smallestIdx = 0
  biggest = 0
  biggestIdx = 0

  for index, value in enumerate(prices):
    if index == 0:
      smallest = value
      smallestIdx = index
    if value < smallest and biggestIdx == False or not index > biggestIdx:
      smallest = value
      smallestIdx = index
    if smallestIdx < index and value > smallest and value > biggest:
      biggest = value
      biggestIdx = index
  print(biggest - smallest)
  return biggest - smallest


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))