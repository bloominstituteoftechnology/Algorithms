#!/usr/bin/python

import argparse

def find_max_profit(prices):
    smallest = prices[0]
    for i in range(len(prices)):
        if prices[i] < smallest and prices[i] != prices[len(prices) - 1]:
            smallest = prices[i]
    
    smallest_value_index = prices.index(smallest)
    shortened_prices = prices[smallest_value_index + 1 :]
    largest = shortened_prices[0]

    for i in range(len(shortened_prices)):
        if shortened_prices[i] > largest:
            largest = shortened_prices[i]

    return largest - smallest

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))