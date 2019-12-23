#!/usr/bin/python

import argparse

def find_max_profit(prices):
  profits = []
  for i in enumerate(prices):
    index = i[0]
    if index < len(prices)-2:
      for price in prices:
        if prices.index(price) >= index+1:
          profits.append(price - prices[index])

  profits.sort(reverse = True)
  return profits[0]


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
