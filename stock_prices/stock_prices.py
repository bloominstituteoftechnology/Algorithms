#!/usr/bin/python

import argparse

def find_max_profit(prices):
    differentials = []
    cursor = 1
    for pricepoint in prices:
        for next_pricepoint in prices[cursor:]:
            differentials.append(next_pricepoint - pricepoint)
        cursor += 1
    return max(differentials)





if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))