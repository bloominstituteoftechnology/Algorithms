#!/usr/bin/python

import argparse

def find_max_profit(prices):
  bigDif = 0
  loss = 0
  currentDif = 0
  while len(prices) > 0:
    for num in range(len(prices)):
        currentDif = prices[num] - prices[0]
        if currentDif > bigDif:
          bigDif = currentDif
        if currentDif < bigDif:
          loss = currentDif
    del prices[0]
  if bigDif == 0:
    return loss
  return bigDif

  




print(find_max_profit([1050, 270, 1540, 3800, 2]))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))