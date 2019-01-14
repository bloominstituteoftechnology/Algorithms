#!/usr/bin/python

import argparse
# list_of_prices = [1050, 270, 1540, 3800, 2]


def find_max_profit(prices):
  sorted_prices = sorted(prices)
  highest_num = sorted_prices[-1]
  count = 0
  def find_the_low(x):
    if prices.index(highest_num) > prices.index(x):
      lowest_num = x
      return highest_num - lowest_num
    if prices.index(highest_num) < prices.index(x):
      count = count + 1
      return find_the_low(sorted_prices[count])
  return find_the_low(sorted_prices[0])
  pass


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))