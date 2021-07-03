#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # set price to the first elem in list
  price = prices[0]

  # define the max profit with index b - index a
  max_profit = prices[1] - prices[0]

  # loop in range of 1 (skipping the first elem(price) and loop through the entire list)
  for i in range(1, len(prices)):
      # if less than price, set the price = to the elem
      # else, set max_profit equal to prices[index] - price
      if prices[i] < price:
          price = prices[i]
      elif prices[i] - price > max_profit:
          max_profit = prices[i] - price
  return max_profit



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))